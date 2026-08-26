# CognOS Truth Center Doctrine v0.1

Status: ratified by Ennio Princi on 2026-08-26  
Normative identifiers: `TRUTH-CENTER-001`, `ENTROPIC-IMPRINT-002`, `SINCERITY-003`

## Authorial declaration

> «La verità sta al centro.» — Ennio Princi

The center is not an average between opinions, political neutrality, or a convenient compromise. It is the most stable claim remaining after observations, context, interests, interpretations, counter-evidence, and uncertainty have been made explicit.

CognOS does not claim possession of absolute truth. It governs the process through which a claim earns a declared level of trust.

## TRUTH-CENTER-001 — Truth at the center

A truth claim MUST remain distinct from the observations, interpretations, and decisions that support it. Every crystallized claim MUST retain:

- its author or accountable actor;
- the context in which it was asserted;
- evidence provenance and integrity commitments;
- known uncertainty and counter-evidence;
- the policy and approval basis for consequential action;
- an immutable link to any later correction or superseding claim.

A new fact MUST NOT silently rewrite an earlier crystallization. It creates a successor linked to the previous record.

## ENTROPIC-IMPRINT-002 — Governance follows the imprint

The constitutional weight of an action is proportional to its scope, impact, irreversibility, and observed uncertainty:

```text
Wg = S × I × R × H(Δ)
```

Where every normalized factor is in `[0,1]`:

- `S`: scope of people, systems, data, or resources affected;
- `I`: potential impact;
- `R`: irreversibility;
- `H(Δ)`: entropy of the unresolved signal or noise;
- `Wg`: minimum governance weight.

Implementations MUST round the computed result to six decimal places. A declared weight MUST equal the computed weight within `0.000001`.

The default control tiers are:

| Weight | Tier | Minimum response |
|---:|---|---|
| `0.000000–0.049999` | Clay | Record provenance; reversible exploration allowed |
| `0.050000–0.199999` | Rough | Corroboration and explicit uncertainty required |
| `0.200000–0.499999` | Cut | Human review and bounded execution required |
| `0.500000–1.000000` | Diamond | Explicit scoped approval, strong evidence, audit receipt, and recovery plan required |

Policy MAY impose a higher tier. It MUST NOT silently lower the computed tier.

## SINCERITY-003 — Verifiable coherence

Sincerity is operational coherence among declared intent, available evidence, authorized decision, and executed action.

```text
sincerity = 1 − normalized_distance(intent, claim, authorization, action)
```

Implementations MUST NOT fabricate precision when the distance cannot be measured. In that case they MUST report `not_measured` and retain the reason.

Uncertainty is not a defect to conceal. A system that declares uncertainty faithfully is more sincere than one that presents unsupported confidence.

## Carbon-to-diamond lifecycle

```text
Possibility space
  -> observed signal
  -> provenance-bound datum
  -> contextualized evidence
  -> falsifiable claim
  -> proportional governance
  -> authorized execution
  -> crystallized Decision Passport
```

Before authorization, artifacts are clay: editable, explicitly provisional, and unsuitable as authority. After validation and execution, the resulting Decision Passport is a diamond: immutable as a historical receipt, but supersedable by linked new evidence.

## Mystery Box daily register

A daily Mystery Box is an epistemic inventory, not a quality contest. Entries use one of five classes:

- `diamond`: verified and provenance-complete;
- `rough_diamond`: promising but still provisional;
- `suspended_fragment`: insufficient context;
- `pebble`: low-value or weak signal retained for possible future correlation;
- `false_brilliance`: contradicted, manipulated, or provenance-deficient.

Classification changes MUST be versioned and justified. No item becomes a diamond solely because it is persuasive, repeated, or produced by a high-confidence model.

## Safety invariants

- Natural language is never executable authority.
- Missing provenance, policy, identity, scope, freshness, or approval fails closed.
- Sensitive evidence stays local; shared records use hashes or redaction commitments.
- Private chain-of-thought MUST NOT be requested or stored.
- Approval is bound to exact scope and arguments, expires, and is revocable.
- A crystallized record is append-only; correction occurs through explicit supersession.

