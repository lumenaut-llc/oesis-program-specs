# Software v0.2

`v0.2` is a promotion lane marker for the first widened parcel kit.

## Sign-off sentence

**v0.2** means: bench-air + mast-lite bound to one parcel, both streams
normalized and combined, parcel view explains source mix — without claiming
field-hardened deployment, governance enforcement, or flood/thermal coverage.

## Software scope

| Surface | Status | Acceptance test |
|---------|--------|----------------|
| Ingest: bench-air normalization | Implemented (v0.1) | AC-6 (regression) |
| Ingest: mast-lite normalization | Partial | AC-1 |
| Inference: two-source combination | Planned | AC-3 |
| Parcel view: source-mix explanation | Planned | AC-4 |
| Node registry: two-node binding | Partial | AC-2 |
| v0.1 regression suite | Implemented | AC-6 |

## Blockers (from gap register)

| ID | Gap | Status |
|----|-----|--------|
| V02-G1 | Mast-lite normalization: outdoor metadata extraction in shared lineage | Partial |
| V02-G2 | Node registry lifecycle: two-node binding with enable/disable | Partial |
| V02-G3 | Parcel view source-mix: indoor vs sheltered outdoor attribution | Planned |
| V02-G4 | Inference two-source combination with appropriate confidence | Planned |

## Key acceptance criteria

- **AC-1**: Mast-lite packet → normalized with outdoor metadata preserved
- **AC-2**: Two nodes registered to one parcel → registry returns both with correct classes
- **AC-3**: Two-source inference → parcel-state reflects multi-source input with provenance
- **AC-4**: Parcel view attributes evidence to indoor vs sheltered outdoor nodes

## Contract boundary changes (v0.1 → v0.2)

- Node registry supports `node_class: "outdoor_reference"` alongside `"indoor_air"`
- Parcel-state provenance distinguishes indoor and outdoor local sources
- No schema breaking changes — v0.2 is additive

## Non-goals

- Trust scoring or deployment-quality flags (v1.0)
- Sharing/consent enforcement (v0.5)
- Flood, thermal, or equipment-state observation families
- Shared-map or neighborhood signals

## How to use this lane

- Inherit baseline software docs from `../v0.1/`.
- Add files here only if a `v0.2`-specific software delta is explicitly accepted.

## Related

- `../v0.1/README.md`
- `../../release/v0.2/README.md`
- `../../release/v0.2/v0.2-implementation-status.md`
- `../../architecture/current/pre-1.0-version-progression.md`
