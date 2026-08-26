#!/usr/bin/env python3
"""Minimal dependency-free verifier for CognOS LUMEN Decision Passport v0.1."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
from typing import Any

ZERO_DIGEST = "0" * 64
REQUIRED = {
    "schema_version", "decision_id", "recorded_at", "intent", "truth_claim",
    "imprint", "evidence", "governance", "execution", "integrity",
}


def canonical_digest(passport: dict[str, Any]) -> str:
    payload = copy.deepcopy(passport)
    payload.setdefault("integrity", {})["content_sha256"] = ZERO_DIGEST
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def expected_tier(weight: float) -> str:
    if weight < 0.05:
        return "clay"
    if weight < 0.20:
        return "rough"
    if weight < 0.50:
        return "cut"
    return "diamond"


def verify(passport: dict[str, Any], allow_zero_digest: bool = False) -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED - passport.keys())
    if missing:
        return [f"missing required field: {name}" for name in missing]
    if passport["schema_version"] != "cognos.lumen.decision-passport.v0.1":
        errors.append("unsupported schema_version")

    imprint = passport["imprint"]
    factors = [imprint.get(name) for name in ("scope", "impact", "irreversibility", "entropy")]
    if not all(isinstance(value, (int, float)) and 0 <= value <= 1 for value in factors):
        errors.append("imprint factors must be numbers in [0,1]")
    else:
        computed = round(math.prod(factors), 6)
        declared = imprint.get("weight")
        if not isinstance(declared, (int, float)) or abs(declared - computed) > 0.000001:
            errors.append(f"imprint weight mismatch: declared={declared!r}, computed={computed}")
        elif imprint.get("tier") != expected_tier(computed):
            errors.append(f"imprint tier mismatch: declared={imprint.get('tier')!r}, expected={expected_tier(computed)!r}")

    governance = passport["governance"]
    approval = governance.get("approval", {})
    execution = passport["execution"]
    if governance.get("decision") == "deny" and execution.get("status") not in {"not_started", "blocked"}:
        errors.append("constitutional deny cannot have an executed status")
    if governance.get("decision") == "ask" and execution.get("status") == "completed" and approval.get("status") != "approved":
        errors.append("completed ASK decision requires approved scope")

    declared_digest = passport["integrity"].get("content_sha256")
    computed_digest = canonical_digest(passport)
    if declared_digest == ZERO_DIGEST and allow_zero_digest:
        pass
    elif declared_digest != computed_digest:
        errors.append(f"content digest mismatch: declared={declared_digest!r}, computed={computed_digest}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("passport", type=Path)
    parser.add_argument("--allow-zero-digest", action="store_true", help="accept an unsigned example fixture")
    parser.add_argument("--print-digest", action="store_true", help="print the canonical digest")
    args = parser.parse_args()
    passport = json.loads(args.passport.read_text(encoding="utf-8"))
    if args.print_digest:
        print(canonical_digest(passport))
    errors = verify(passport, allow_zero_digest=args.allow_zero_digest)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {passport['decision_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
