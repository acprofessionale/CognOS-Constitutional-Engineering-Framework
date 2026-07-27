claude -p "$(cat <<'PROMPT'
# CognOS Constitutional Engineering Framework
## Foundation Design Phase

You are the Founding Engineering Architect of the CognOS Constitutional Engineering Framework.

The Human Project Owner, Ennio Princi, has explicitly approved the creation of CCEF as an independent repository of the CognOS ecosystem.

CCEF is not:

- a software runtime;
- an application;
- a business Vertical Module;
- an implementation repository.

CCEF is the single authoritative source for shared engineering governance across the CognOS ecosystem.

Its purpose is to govern how human contributors and AI agents design, review, document, approve and evolve CognOS repositories.

## Existing ecosystem context

CognOS currently contains three distinct responsibility domains:

1. CognOS-Core
   - cognitive runtime;
   - runtime safety;
   - execution control;
   - R0-R4 risk classification;
   - A0-A4 autonomy classification;
   - constitutional runtime invariants.

2. CCEF
   - shared engineering governance;
   - repository standards;
   - Operational Governance Procedures;
   - reusable ADR and review models;
   - cross-repository governance;
   - AI-agent engineering rules.

3. Vertical Modules
   - domain-specific applications;
   - CognOS-Eisman is the first Vertical Module.

CCEF must not duplicate or redefine CognOS-Core runtime safety taxonomies.

## Constitutional principles

Enforce:

- Knowledge Before Code
- Governance Before Automation
- Architecture Before Implementation
- Documentation as a First-Class Artifact
- Human Accountability
- Evidence Before Confidence
- Model Agnostic
- Modular by Default
- Every Decision Must Be Explainable
- Separation of Constitutional Concerns

Governance Before Automation means:

No automation may alter a governance baseline unless the change is explicitly requested, scoped, reviewable, auditable and approved by the Human Project Owner.

## Current task

Do not create files yet.

Do not modify the repository.

Do not write implementation code.

Produce only a complete architectural proposal for the CCEF repository.

The proposal must define:

1. Purpose
2. Scope
3. Non-goals
4. Constitutional authority
5. Relationship with CognOS-Core
6. Relationship with Vertical Modules
7. Layer model
8. Repository boundaries
9. Proposed directory structure
10. Document classification model
11. Authority hierarchy
12. Dependency rules
13. Allowed and forbidden cross-repository dependencies
14. Protected artifacts
15. Human authority model
16. AI-agent authority model
17. ADR lifecycle
18. OGP lifecycle
19. Foundation Review lifecycle
20. Cross-repository validation model
21. Versioning strategy
22. Adoption model
23. Compatibility model
24. Supersession rules
25. Deprecation model
26. Evidence requirements
27. Audit requirements
28. Security-governance boundary
29. Evolution strategy
30. CCEF v1.0 Foundation exit criteria

## OGP roadmap

Include the proposed scope, but do not write the procedures:

- OGP-001 ADR Ratification Workflow
- OGP-002 Foundation Review Workflow
- OGP-003 Architecture Change Workflow
- OGP-004 Cross-Repository Validation
- OGP-005 Release Governance
- OGP-006 Emergency Governance Procedure

Define the standard OGP structure:

- Purpose
- Scope
- Authority
- Preconditions
- Inputs
- Execution Steps
- Safety Rules
- Validation
- Exit Criteria
- Evidence Required
- Rollback
- References
- Revision History

## Decision quality

For every major decision include:

- rationale;
- consequences;
- trade-offs;
- rejected alternatives;
- future evolution.

Every statement about existing repositories must cite repository-relative file:line evidence when available.

If evidence is unavailable, mark it explicitly as an assumption.

## Output

Return only:

1. Executive Summary
2. Proposed CCEF Architecture
3. Repository Structure
4. Authority Model
5. Dependency Model
6. Governance Lifecycle
7. OGP Framework
8. Versioning and Adoption
9. Risks and Trade-offs
10. Open Human Decisions
11. CCEF v1.0 Exit Criteria
12. Recommendation

Do not create files.

Wait for explicit Human Project Owner approval.
PROMPT
)"
