# LUMEN interoperability challenge: scope binding

**Vector:** `SCOPE-BINDING-NEGATIVE-001`  
**Expected verdict:** `FAIL`  
**Evidence class:** self-authored negative vector; independent reproduction not yet obtained

## Claim under test

Content integrity is not authorization. A Decision Passport can have a correct canonical content digest while still executing a tool-and-arguments pair outside the exact approved scope.

The fixture `examples/interop/lumen-v0.1.scope-binding-mismatch.json` is deliberately constructed so that:

1. the passport content digest is valid;
2. the policy decision is `ask`;
3. the approval status is `approved`;
4. execution is recorded as `completed`;
5. the approval `scope_digest` does not match the canonical commitment to the executed tool and argument digest.

A conforming verifier MUST reject the passport. A verifier that checks only content integrity and approval status will falsely accept it.

## Canonical scope commitment

For this v0.1 interoperability profile, compute SHA-256 over the UTF-8 encoding of this canonical JSON object using sorted keys and separators `(',', ':')`:

```json
{"arguments_sha256":"<execution.arguments_sha256>","tool":"<execution.tool>"}
```

The resulting hex digest MUST equal `governance.approval.scope_digest` before an `ask` decision may record `execution.status = completed`.

## Reproduction

```bash
python3 reference/lumen_verify.py \
  examples/interop/lumen-v0.1.scope-binding-mismatch.json
```

Expected output contains:

```text
FAIL: approval scope mismatch
```

## Independence boundary

This vector and the reference verifier are produced by CognOS. Passing the bundled test is not independent validation, certification, or endorsement. The purpose of publishing the vector is to invite a separate implementation to reproduce, challenge, or falsify the expected verdict against a commit-pinned artifact.
