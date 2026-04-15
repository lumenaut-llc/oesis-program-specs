# Software v0.4

`v0.4` is a promotion lane marker for multi-node registry and evidence composition.

## Sign-off sentence

**v0.4** means: mature node lifecycle, installation metadata, evidence
composition weighting, and deployment-quality flags — without claiming trust
scoring as a product surface, governance enforcement, or intervention logic.

## Software scope

| Surface | Status | Acceptance test |
|---------|--------|----------------|
| Node registry lifecycle (register/bind/disable/replace/retire) | Partial | AC-1 |
| Installation metadata capture | Docs-only | AC-2 |
| Evidence composition weighting | Planned | AC-3 |
| Deployment-quality flags | Planned | AC-4 |
| Node replacement continuity | Planned | AC-5 |
| All v0.3 software surfaces | v0.3 target | AC-6 (regression) |

## Blockers (from gap register)

| ID | Gap | Status |
|----|-----|--------|
| V04-G1 | Node registry lifecycle: full end-to-end flow | Partial — schema supports CRUD; not exercised |
| V04-G2 | Installation metadata capture surface | Docs-only — contract formalized; no capture path |
| V04-G3 | Evidence composition weighting by source class and quality | Planned |
| V04-G4 | Deployment-quality flags in registry and parcel view | Planned |
| V04-G5 | Node replacement continuity scenario | Planned — no reference implementation |
| V04-G6 | Evidence composition explanation: weighting rationale | Planned |

## Key acceptance criteria

- **AC-1**: Node lifecycle — register, bind, disable, replace, retire; inference uses only enabled nodes
- **AC-2**: Installation metadata — operator submits deployment metadata as `deployment-metadata` record
- **AC-3**: Evidence composition — fresh indoor weighted higher than stale outdoor; deployment grade in provenance
- **AC-5**: Node replacement — retired node history preserved; new node contributes to current inference

## Contract boundary changes (v0.3 → v0.4)

- Node registry adds lifecycle state (active, disabled, retired) and `deployment_grade` (bench_grade, field_ready)
- Deployment-metadata contract integrated as evidence composition input
- Parcel-state provenance includes source weighting rationale

## Non-goals

- Full trust scoring as composed product surface (v1.0)
- Governance enforcement or sharing controls (v0.5)
- House-state, equipment-state, or intervention surfaces (v1.5)

## How to use this lane

- Inherit baseline software docs from `../v0.1/`.
- Add files here only if a `v0.4`-specific software delta is explicitly accepted.

## Related

- `../v0.3/README.md`
- `../../release/v0.4/README.md`
- `../../release/v0.4/v0.4-implementation-status.md`
- `../../contracts/v1.0/deployment-metadata-schema.md`
