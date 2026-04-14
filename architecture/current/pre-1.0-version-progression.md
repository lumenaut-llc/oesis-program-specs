# Pre-1.0 Version Progression

## Purpose

Define how pre-`1.0` versions should advance without turning every incremental
addition into a new architecture lane.

## Core rule

Use a new `v0.x` only when the accepted runnable reference slice changes in a
way that materially expands what the system is and does.

Do not create a new `v0.x` for:

- every added node or hardware element
- every schema or example addition
- every partial implementation step
- every milestone status change

Use milestones and implementation-status labels for that narrower growth.

## Recommended progression

- `v0.1`
  One parcel, one bench-air node, one accepted ingest-to-parcel-view path.
- `v0.2`
  First widened parcel-kit slice with stable indoor-plus-sheltered-outdoor
  operation.
- `v0.3`
  First accepted flood-capable runtime slice with a dedicated flood observation
  family.
- `v0.4`
  First accepted multi-node parcel slice with stronger registry and evidence
  composition posture.
- `v0.5`
  First accepted operational sharing/governance slice with real revocation,
  retention, export, and boundary enforcement evidence.
- `v1.0`
  First materially broader system that is no longer just the narrow first
  working reference slice.

## Promotion bar for the next slice

Before promoting a new pre-`1.0` version such as `v0.2`, require:

1. explicit architecture scope
2. explicit contract and runtime boundary changes
3. explicit acceptance commands or check updates
4. explicit implementation-status evidence showing what changed

If those conditions are not met, keep the work inside the current accepted lane
and track it through milestones and status posture.

## Related docs

- `../system/version-and-promotion-matrix.md` — how accepted slices relate to capability stages and deployment maturity
- `../system/node-taxonomy.md` — hardware and v1.5 bridge surfaces referenced by widening slices
- `../system/integrated-parcel-system-spec.md` — tiered parcel kit design
