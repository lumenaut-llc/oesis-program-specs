# flood-node

## One-line summary

Low-point runoff depth and rise-rate sensor; introduces outdoor deployment class and dedicated `flood.low_point.snapshot` observation family. Geography-gated module — included only for parcels where runoff or pooling is operationally meaningful. Runtime normalization implemented; hardware build spec still open.

## Deployment posture

- **Deployment class:** `outdoor` — per [`../node-taxonomy.md`](../node-taxonomy.md) geography-gated table and [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node".
- **Power tier:** `battery + solar` with documented runtime floor, or `hardened mains` — per [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) outdoor-class row.
- **IP tier:** `IP65` — flood-node installations see standing water; upgraded from IP54 passive default.
- **Transport tier:** `serial` floor → `LoRa` permitted (low-point mounts often beyond reliable Wi-Fi).
- **Protective fixtures:**
  - Rigid mount at a documented low-point.
  - Zero-reference tied to a physical staff gauge (depth readings are only interpretable against documented geometry).
- **Sensor variants:**
  - Water depth: ultrasonic rangefinder, outdoor-rated (e.g., MaxBotix MB7389 or equivalent) — variant TBD per [`../sensor-placement-and-representativeness-guide.md`](../sensor-placement-and-representativeness-guide.md) Sensor variant selection principles.
  - Rise rate: derived from depth time-series; not a separate sensor.

## Version evolution

| Build version | Status | Spec path | Notes |
|---|---|---|---|
| `v0-1` (planned) | not yet drafted | `oesis-builds/specs/flood-node/v0-1.md` — **does not exist** | Skeleton proposal at [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) Skeleton 2. |

Build guide exists at [oesis-hardware/flood-node/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/flood-node) with provisional calibration only; independent reproduction not confirmed.

## Calibration posture

Governed by [`../calibration-program.md`](../calibration-program.md) (physical-sensor program).

- **Deployment-maturity target:** `v1.0` (first fielded kit).
- **Reference instruments:** flood-node reference = staff gauge + manual depth measurement; not yet populated under `oesis-builds/procedures/flood-node/references/`. Tracked as **G13**.
- **Burn-in:** not required — ultrasonic sensors do not require conditioning.
- **Protective fixture verification:** rigid mount + zero-reference + staff gauge acceptance tests to be authored. Without documented geometry, depth numbers are decoration (inadmissible per §C).
- **Admissibility status:** no readings admissible today (no build spec, no populated reference, no documented geometry acceptance).
- **§F build-spec metadata block:** planned — skeleton in the proposal cited above.

## Role in each program-phase

| Phase | Role | Notes |
|---|---|---|
| `v0.1` / `v0.2` | **not in scope** | v0.1 is indoor-only; v0.2 is indoor + sheltered. |
| `v0.3` | **first flood-capable slice** (first outdoor-class node enters) | Dedicated `flood.low_point.snapshot` observation family. Milestone 3 in [`../../current/milestone-roadmap.md`](../../current/milestone-roadmap.md). |
| `v0.4` | low-point node within multi-node registry | Registry + evidence composition. |
| `v0.5` | unchanged from v0.4 | Governance-gated shared-layer eligibility. |
| `v1.0` (pre-1.0 ladder) | fleet-wide deployment-maturity `v1.0` | §F / §G compliance attested. |
| `v1.5` | unchanged | Flood loop (hazard → house-state → action → outcome) partially authored in [`../../v1.5/house-state-and-verification-model.md`](../../v1.5/house-state-and-verification-model.md) "Second closed loop: flood protection". |

## Cross-repo link map

| Concern | Location |
|---|---|
| Architecture posture row | [`../node-taxonomy.md`](../node-taxonomy.md) geography-gated; [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node" |
| Hardware design | [oesis-hardware/flood-node/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/flood-node) |
| Build spec | **missing** — skeleton in [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) |
| Runtime normalizer | `oesis.ingest.v0_3.normalize_flood_packet` |
| Packet schema | `oesis.flood-node.v1` → `flood.low_point.snapshot` — [oesis-contracts/v0.3/](https://github.com/lumenaut-llc/oesis-contracts/tree/main/v0.3) |
| Gap register entries | **G10** (PRD hazard claims vs bench-air-only sensing includes flood), **G13** (reference instruments), **G17** (admissibility facts in schema) |

## Known gotchas

- **Geometry discipline is non-optional.** One dry point on a parcel does not clear the whole parcel. One wet point may reflect intended drainage concentration, not generalized flooding. See [`../sensor-placement-and-representativeness-guide.md`](../sensor-placement-and-representativeness-guide.md) flood placement guidance.
- **Provisional calibration only** as of 2026-04-15 (per [`../../current/implementation-posture.md`](../../current/implementation-posture.md)). Promotion to `deployment maturity v1.0` blocked on characterized reference + geometry discipline.
- **Power runtime floor** — outdoor-class requires 72 h runtime floor under worst-case solar per deployment-maturity-ladder. Undersized solar is a common bring-up mistake.

## Related

- [`../node-taxonomy.md`](../node-taxonomy.md) geography-gated section
- [`../calibration-program.md`](../calibration-program.md) §C protective-fixture rule
- [`../architectural-choices-by-stage.md`](../architectural-choices-by-stage.md) row v0.3
- [`../../v1.5/house-state-and-verification-model.md`](../../v1.5/house-state-and-verification-model.md) "Second closed loop: flood protection"
- [`mast-lite.md`](mast-lite.md) — sheltered-class sibling
