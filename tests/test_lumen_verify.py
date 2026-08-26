import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "reference"))

from lumen_verify import ZERO_DIGEST, canonical_digest, verify  # noqa: E402


class LumenVerifierTests(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "examples" / "lumen-decision-passport-v0.1.example.json"
        self.passport = json.loads(self.path.read_text(encoding="utf-8"))

    def test_example_is_structurally_valid(self):
        self.assertEqual([], verify(self.passport, allow_zero_digest=True))

    def test_digest_detects_mutation(self):
        signed = copy.deepcopy(self.passport)
        signed["integrity"]["content_sha256"] = canonical_digest(signed)
        self.assertEqual([], verify(signed))
        signed["truth_claim"]["statement"] = "mutated"
        self.assertTrue(any("digest mismatch" in error for error in verify(signed)))

    def test_ask_cannot_complete_without_approval(self):
        invalid = copy.deepcopy(self.passport)
        invalid["execution"]["status"] = "completed"
        errors = verify(invalid, allow_zero_digest=True)
        self.assertTrue(any("requires approved scope" in error for error in errors))

    def test_weight_and_tier_are_recomputed(self):
        invalid = copy.deepcopy(self.passport)
        invalid["imprint"]["weight"] = 0.9
        errors = verify(invalid, allow_zero_digest=True)
        self.assertTrue(any("weight mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
