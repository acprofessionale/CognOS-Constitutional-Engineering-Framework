# Public Capability Projection Governance v1

Status: PROPOSED FOUNDATION
Scope: engineering governance for public projection of CognOS capability state

## Purpose

Define how authoritative CognOS state may be projected into a public-facing trust/capability portal without turning the portal into a control plane, policy engine, evidence authority or secret store.

## Core rule

The public portal is a **projection**, never the source of truth.

Authoritative state remains in CognOS canonical contracts, registries, runtime policy/evidence systems and ratified governance artifacts.

## Allowed public projection

A sanitized public record MAY include:

- capability name/ID;
- vertical consumer;
- external provider name;
- lifecycle status;
- verification status;
- whether explicit human approval is required;
- whether external/public side effects exist;
- latest verified timestamp;
- high-level purpose;
- high-level limits/disclaimers;
- public change history where safe.

## Prohibited public projection

The portal MUST NOT expose:

- client secrets;
- access/refresh tokens;
- raw OAuth material;
- exact internal policy logic where disclosure increases attackability;
- exploitable infrastructure details;
- private user/account identifiers not intended for publication;
- raw evidence bundles containing Confidential/Restricted data;
- internal incident details before approved disclosure;
- credentials, environment files or secret-bearing logs.

## Authority semantics

The portal MUST NOT:

- approve capability execution;
- promote a capability to VERIFIED;
- change R0–R4 or A0–A4 semantics;
- admit a provider;
- override a deny;
- grant runtime scopes;
- act as human approval authority merely because an authenticated administrator edits WordPress.

A WordPress content edit is a presentation change, not a CognOS policy decision.

## Verification semantics

Public states must distinguish at least:

- PROPOSED
- DESIGNED
- IMPLEMENTED
- VERIFIED
- BLOCKED
- NOT_VERIFIED
- DEPRECATED

No model-generated statement, marketing copy, provider documentation or UI configuration alone may promote a capability to VERIFIED.

## Publication pipeline

Target architecture:

```text
Canonical CognOS State
  -> projection policy
  -> redaction/sanitization
  -> signed/versioned public projection artifact or API
  -> WordPress renderer
```

WordPress should ideally consume a prepared safe projection rather than query internal control-plane data directly.

## WordPress boundary

WordPress MAY own:

- public pages;
- navigation;
- presentation templates;
- public documentation;
- legal/public transparency content;
- rendering of safe capability projection data.

WordPress MUST NOT automatically own:

- OAuth token exchange;
- token persistence;
- CognOS secret storage;
- policy evaluation;
- evidence authority;
- provider admission;
- execution approval.

Any exception requires explicit architecture/security review.

## Required public sections

The first portal should support:

- `/` overview;
- `/capabilities/` safe capability projection;
- `/governance/` human authority and execution principles;
- `/tiktok/` provider/vertical transparency;
- `/transparency/` AI and automation disclosure;
- `/security/` high-level security model and reporting contact;
- `/privacy/` privacy policy;
- `/terms/` terms of service;
- `/about/` identity/project context;
- `/contact/` operator contact.

## Change governance

Before a public capability/status change:

1. identify authoritative source/evidence;
2. verify freshness;
3. classify disclosure sensitivity;
4. generate sanitized projection;
5. review for overclaim/misrepresentation;
6. publish via controlled change;
7. preserve rollback/version history;
8. record public-change evidence.

## Misrepresentation gate

Publication must fail closed if it would:

- represent EXECUTED as VERIFIED;
- represent DESIGNED as IMPLEMENTED;
- hide a known blocker materially relevant to the public claim;
- imply provider endorsement without evidence;
- claim security/compliance certification not actually held;
- expose personal or secret data;
- imply autonomous authority that CognOS has not ratified.

## Legal/content governance

Privacy/Terms drafts may include technical facts already evidenced. Unknown legal/operator facts must remain `OWNER_INPUT_REQUIRED` until supplied and ratified.

Do not fabricate legal entity, VAT data, jurisdiction, DPO, processor list, transfer basis, retention periods or contact details.

## Initial portal acceptance criteria

- portal is explicitly non-authoritative;
- public capability status is traceable to canonical evidence;
- secret-bearing data cannot enter normal content workflows;
- TikTok is presented as external provider, not CognOS authority;
- human sovereignty and fail-closed semantics are visible;
- WordPress can be replaced without changing CognOS governance semantics;
- all public claims are reversible, versioned and attributable.
