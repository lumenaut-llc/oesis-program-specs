# ADR 0004: Use Condition-Estimate Terminology Instead of Safety Determinations

- Status: Accepted
- Date: 2026-03-30
- Owners: program maintainers
- Related workstreams: inference engine, parcel platform, claims governance, docs

## Context

Early terminology such as `stay_safe`, `enter_safe`, and `escape_safe` can sound like emergency instructions or certified safety determinations. That language creates reliance risk and overstates what parcel sensing plus public context can responsibly support, especially under sparse evidence, stale inputs, or partial adoption.

The system still needs homeowner-readable outputs, but they should not sound like guarantees or official authorization.

## Decision

The project uses condition-estimate terminology rather than safety-determination terminology in user-facing concepts and core data contracts.

Current parcel-state fields are:
- `shelter_status`
- `reentry_status`
- `egress_status`
- `asset_risk_status`

Product language should frame these as estimates, indicators, or risk signals rather than commands or certifications.

## Consequences

Positive:
- reduces claim and reliance risk
- better matches uncertainty-aware inference behavior
- aligns schemas, docs, and UI copy with conservative product posture

Costs:
- terms may feel less marketable or dramatic
- some future contributors may try to reintroduce stronger language for simplicity or appeal

## Alternatives considered

- keep safety wording and rely on disclaimers
  Rejected because disclaimers alone do not undo the force of directive labels.
- remove parcel status outputs entirely
  Rejected because homeowners still need understandable synthesized outputs.

## Follow-up work

- keep notification text aligned with estimate language
- prevent marketing or pilot materials from drifting back into directive safety wording
- validate that UI copy preserves uncertainty and provenance context
