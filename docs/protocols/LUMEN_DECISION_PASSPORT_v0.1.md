# LUMEN Decision Passport v0.1

LUMEN is the CognOS Sovereign Proof-of-Agency protocol. It proves why an action was permitted and whether the observed execution remained within the human-approved contract.

## Normative flow

```text
human intent
  -> typed contract
  -> provenance-bound context
  -> entropic imprint
  -> DENY | ASK | ALLOW
  -> scoped approval when required
  -> bound execution
  -> evidence receipt
  -> Decision Passport
```

## Conformance

A conforming producer MUST:

1. issue a globally unique `decision_id`;
2. preserve the original intent without treating it as executable authority;
3. calculate the entropic imprint using `ENTROPIC-IMPRINT-002`;
4. bind approvals to the exact scope and tool-argument digest;
5. record evidence by reference and SHA-256 commitment;
6. distinguish policy decision from execution outcome;
7. produce a content digest over the canonical passport payload;
8. avoid secrets, raw credentials, and private reasoning traces;
9. fail closed when a required field cannot be established;
10. link corrections through `supersedes` rather than rewriting history.

## Canonicalization and digest

For v0.1, the digest input is the full JSON object with `integrity.content_sha256` set to 64 ASCII zeroes. Producers serialize with UTF-8, sorted object keys, no insignificant whitespace, and JSON separators `(',', ':')`. The SHA-256 hex digest of those bytes becomes `integrity.content_sha256`.

This digest detects mutation; it is not an identity signature. Implementations requiring non-repudiation SHOULD additionally sign the digest with an approved asymmetric signature profile and keep key identity outside the passport.

## Truth status

`truth_claim.status` is one of:

- `raw_signal`
- `hypothesis`
- `provisional`
- `verified`
- `superseded`
- `rejected`

`verified` means justified under the recorded context and evidence. It does not mean metaphysically absolute or permanently immune to correction.

## Policy decisions

- `deny`: execution is prohibited;
- `ask`: execution requires a matching valid human approval;
- `allow`: policy permits execution without a new approval at this tier.

An implementation MUST NOT convert `deny` into `allow` at runtime. For `ask`, a missing, expired, revoked, or mismatched approval blocks execution.

## Reference artifacts

- Schema: `schemas/lumen-decision-passport-v0.1.schema.json`
- Example: `examples/lumen-decision-passport-v0.1.example.json`
- Verifier: `reference/lumen_verify.py`
- Foundational doctrine: `docs/constitutional/TRUTH_CENTER_DOCTRINE_v0.1.md`

