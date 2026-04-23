# ADR 0008: Mast-Lite Build Spec as Milestone 2 Gate (Option A)

- Status: Accepted
- Date: 2026-04-19
- Owners: Open Environmental Sensing and Inference System (hardware + technical)
- Related workstreams:
  - oesis-hardware/v0.1/mast-lite
  - oesis-builds/specs/mast-lite (planned)
  - architecture/current/milestone-roadmap
  - release/v.0.1 (gap-register G12)

## Context

Mast-lite is the sheltered-outdoor sensor node that completes the v0.2 two-node parcel kit (bench-air + mast-lite) per [`../../architecture/current/pre-1.0-version-progression.md`](../../architecture/current/pre-1.0-version-progression.md). It is architecturally required for program-phase v0.2 promotion.

However:
- No build spec exists at `oesis-builds/specs/mast-lite/` (gap G12).
- No calibration procedure exists.
- No radiation-shield design or thermal-loading acceptance test is documented.
- Hardware build-guide exists at `oesis-hardware/v0.1/mast-lite/` but has not been independently reproduced.
- The v1 hazard formula's primary heat path (per ADR 0007) assumes outdoor temperature from mast-lite.

Two options presented:

- **Option A.** Write the mast-lite build spec, calibration procedure, and radiation-shield design as a Milestone 2 acceptance gate. Primary heat path targets mast-lite outdoor temperature.
- **Option B.** Scope heat formula to indoor-bridge-only (bench-air indoor SHT45 with 0.4× coefficient discount). Defer mast-lite. Primary outdoor heat path lands at Milestone 4 with weather-pm-mast or mast-lite maturity.

## Decision

**Option A is chosen.** Mast-lite build spec, calibration procedure, and radiation-shield design become Milestone 2 acceptance gates. The v1 hazard formula's primary heat path is mast-lite outdoor temperature, not indoor-bridge-only.

Concretely, Milestone 2 acceptance per [`../../architecture/current/milestone-roadmap.md`](../../architecture/current/milestone-roadmap.md) requires:
- `oesis-builds/specs/mast-lite/v0-1.md` with BOM, wiring, firmware pin-out, reproducible build
- `oesis-builds/procedures/mast-lite/calibration.md` with a characterized reference instrument
- Radiation-shield design inside the build spec with thermal-loading acceptance test
- Build independently reproduced once before Milestone 2 promotion
- All node families in the v0.2 kit (bench-air + mast-lite) at `deployment maturity v1.0` calibration posture per calibration-program §G (see ADR 0009)

## Consequences

Positive:
- Primary heat path is sensor-backed outdoor temperature, not an indoor proxy with 0.4× discount. Preserves sensor-primacy architectural claim (ADR 0007) for both hazards, not just smoke.
- v0.2 promotion produces a credible two-node parcel kit rather than a one-node plus a degraded bridge.
- Per-node part sheet [`../../architecture/system/parts/mast-lite.md`](../../architecture/system/parts/mast-lite.md) becomes the aggregator as the work progresses.

Negative:
- Adds real hardware-spec-writing work to Milestone 2. G12 is now a primary blocker; G13 (reference instruments) and G14 (burn-in gate) bite in parallel.
- Milestone 2 promotion cannot happen purely via runtime changes; hardware work is on the critical path.
- If mast-lite hardware owner is under-resourced, v0.2 blocks indefinitely.

## Alternatives considered

**Option B (indoor-bridge-only heat).**
Rejected because the indoor-bridge path cannot physically represent parcel-wide outdoor heat. Parcel-state outputs at v0.2 would be making claims their sensor can't back. The formal v0.2 promotion bar ("first indoor + sheltered outdoor kit") implies an outdoor source; degrading to indoor-only would make v0.2 structurally narrower than its own definition.

## Follow-up work

- Build-vault agent to apply proposal [`../proposals/oesis-builds-node-skeletons.md`](../proposals/oesis-builds-node-skeletons.md) Skeleton 1 (mast-lite §F block).
- Author radiation-shield thermal-loading acceptance test under `oesis-builds/specs/mast-lite/`.
- Populate reference instrument for sheltered-class temperature/humidity under `oesis-builds/procedures/mast-lite/references/` (closes part of G13).
- Independent build reproduction required before Milestone 2 promotion.
- Update part sheet as work lands.
