# CognOS Constitutional Engineering Framework

> A governance framework for policy-driven, auditable and reversible AI-assisted software engineering.

## Purpose

The CognOS Constitutional Engineering Framework defines the operating rules used to evolve software systems with human oversight, explicit policy, persistent evidence and controlled autonomy.

It is designed for engineering environments where AI agents, developers and decision-makers collaborate across long-running projects without losing traceability, architectural intent or rollback capability.

## Core model

```text
Intent
  ↓
Policy
  ↓
Plan
  ↓
Atomic change
  ↓
Tests and evidence
  ↓
Human approval
  ↓
Reversible commit
  ↓
Receipt and handover
```

## Principles

- **Observe before change** — inspect repository, runtime and dependencies before modifying anything.
- **Evidence over assumption** — source control, tests, configuration and runtime state prevail over memory or narrative.
- **Fail-closed scope** — every unplanned expansion requires an explicit stop and approval.
- **Atomic delivery** — changes are decomposed into small, independently verifiable and reversible tranches.
- **Human-governed autonomy** — autonomy grows only together with policy, tests, observability and recovery mechanisms.
- **Persistent decisions** — architectural decisions are recorded as ADRs rather than left in transient conversations.
- **Receipts and handovers** — every completed task leaves a durable operational record.
- **Secrets by design** — credentials and sensitive runtime data remain outside version control and reports.
- **No blind rewrite** — modernization is incremental and preserves working capabilities.

## Reference control plane

Projects adopting the framework may use a lightweight documentation control plane:

```text
reports/
├── HANDOVER.md
├── README.md
├── current/
│   ├── status.md
│   ├── next-step.md
│   ├── backlog.md
│   └── risks.md
├── master/
│   ├── master-plan.md
│   ├── roadmap.md
│   └── architecture.md
├── milestones/
├── receipts/
├── audits/
├── decisions/
└── history/
```

The structure is adapted to each repository. It is not intended as documentation bureaucracy: every artifact must support governance, recovery, auditability or decision quality.

## Autonomy maturity model

1. **Observe** — inspect and report.
2. **Recommend** — propose decisions and diffs.
3. **Execute with approval** — apply explicitly authorized changes.
4. **Policy-governed autonomy** — operate within machine-readable constraints.
5. **Closed-loop optimization** — improve based on measured outcomes while preserving audit and rollback.

## Intended applications

- AI-assisted software delivery
- agentic engineering workflows
- architecture modernization
- decision-intelligence platforms
- regulated or high-accountability systems
- multi-device and interruption-prone development environments
- long-lived projects requiring reliable knowledge transfer

## Relationship to CognOS

This repository is the governance layer for the broader CognOS ecosystem. CognOS projects use these principles to coordinate architecture, implementation, testing, operational evidence and human approval.

The framework is intentionally model-agnostic and tool-agnostic. Its objective is not to prescribe a specific AI provider, but to ensure that any automation remains explainable, bounded and recoverable.

## Status

The framework is under active definition. Public documents describe principles and governance patterns; implementation templates and reusable policies will be added incrementally after validation in active CognOS projects.

## Author

Created by **Ennio Princi** — AI Systems Architect, Agile Coach and designer of explainable Decision Intelligence systems.

## Truth Center and LUMEN v0.1

The first executable constitutional profile implements the authorial principle:

> «La verità sta al centro.» — Ennio Princi

It connects proportional governance to the entropic imprint of an action and crystallizes verified actions as portable Decision Passports.

- [Truth Center Doctrine v0.1](docs/constitutional/TRUTH_CENTER_DOCTRINE_v0.1.md)
- [LUMEN Decision Passport protocol v0.1](docs/protocols/LUMEN_DECISION_PASSPORT_v0.1.md)
- [Decision Passport JSON Schema](schemas/lumen-decision-passport-v0.1.schema.json)
- [Reference Decision Passport](examples/lumen-decision-passport-v0.1.example.json)
- [Dependency-free verifier](reference/lumen_verify.py)
- [Verifier tests](tests/test_lumen_verify.py)

Run the reference checks with:

```bash
python3 -m unittest discover -s tests -v
python3 reference/lumen_verify.py examples/lumen-decision-passport-v0.1.example.json --allow-zero-digest
```

