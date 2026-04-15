# Software v0.3

`v0.3` is a promotion lane marker for the first flood-capable runtime.

## Sign-off sentence

**v0.3** means: flood-node observations normalized through canonical ingest,
flood conditions reflected in parcel-state — without claiming response logic,
sump monitoring, or intervention surfaces.

## Software scope

| Surface | Status | Acceptance test |
|---------|--------|----------------|
| Ingest: flood observation normalization | Implemented | AC-1 |
| Inference: flood condition derivation | Implemented | AC-3 |
| Node registry: three-node binding | Docs-only | AC-2 |
| Parcel view: flood condition display | Planned | AC-4 |
| All v0.2 software surfaces | v0.2 target | AC-6 (regression) |

## Blockers (from gap register)

| ID | Gap | Status |
|----|-----|--------|
| V03-G1 | Flood observation normalization | **Resolved** — ingest handler implemented |
| V03-G2 | Flood condition derivation in inference | **Resolved** — water depth, rise rate, calibration consumed |
| V03-G3 | Node registry three-node support | Partial — schema supports `low_point_flood`; not exercised |
| V03-G4 | Parcel view flood evidence display | Planned |

## Key acceptance criteria

- **AC-1**: Flood packet normalization — water_depth_cm, rise_rate_cm_per_hr, calibration_state preserved
- **AC-3**: Flood condition in parcel-state — flood-relevant conditions derived with evidence_mode
- **AC-2**: Three-node registry — indoor + outdoor + flood bound to one parcel

## Contract boundary changes (v0.2 → v0.3)

- Ingest accepts `oesis.flood-node.v1` schema lineage
- Node registry supports `node_class: "low_point_flood"`
- Parcel-state includes flood-derived condition fields (additive)

## Non-goals

- Sump pump monitoring or equipment-state (v1.5)
- Flood intervention or response verification (v1.5)
- Weather-PM or thermal observation families
- Trust scoring or governance enforcement

## How to use this lane

- Inherit baseline software docs from `../v0.1/`.
- Add files here only if a `v0.3`-specific software delta is explicitly accepted.

## Related

- `../v0.2/README.md`
- `../../release/v0.3/README.md`
- `../../release/v0.3/v0.3-implementation-status.md`
- `../inference-engine/architecture.md`
