# mast-lite

## One-line summary

Sheltered-outdoor reference sensor node; extends the `oesis.bench-air.v1` packet lineage from indoor to sheltered outdoor. The second node in the v0.2 integrated parcel kit. Architecturally in scope today; hardware build spec and field-hardening evidence are the v0.2 promotion blockers.

## Deployment posture

Values cited from canonical sources; do not edit here if upstream changes.

- **Deployment class:** `sheltered` — per [`../node-taxonomy.md`](../node-taxonomy.md) next-promotion table and [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node".
- **Power tier:** `12V-DC` from an outdoor-rated adapter, or USB routed from indoor through a cable gland — per [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) Deployment-class standards (sheltered row).
- **IP tier:** `IP44` minimum — per ladder sheltered row.
- **Transport tier:** `serial` floor, `Wi-Fi` permitted where coverage is reliable — per ladder sheltered row.
- **Protective fixtures:** radiation shield required — passive or fan-aspirated. Pre-verification readings inadmissible per [`../calibration-program.md`](../calibration-program.md) §C item 7.
- **Sensor variants:**
  - Temperature + humidity: SHT45 with **sintered-filter outdoor-rated variant** per [`../sensor-placement-and-representativeness-guide.md`](../sensor-placement-and-representativeness-guide.md) Sensor variant selection principles — sheltered envelope requires sintered cap for condensation tolerance.
  - Gas resistance: BME680 — same as bench-air; humidity sensitivity in sheltered environment is a known interpretation caveat.

## Version evolution

| Build version | Status | Spec path | Notes |
|---|---|---|---|
| `v0-1` (planned) | **not yet drafted** | `oesis-builds/specs/mast-lite/v0-1.md` — **does not exist** | Tracked as **G12**. Skeleton proposal at [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) Skeleton 1. |

## Calibration posture

Governed by [`../calibration-program.md`](../calibration-program.md) (physical-sensor program).

- **Deployment-maturity target:** `v1.0` — required for v0.2 promotion per [`../../current/pre-1.0-version-progression.md`](../../current/pre-1.0-version-progression.md) item 5.
- **Reference instruments:** not yet populated — sheltered-class temperature / humidity reference required per §A minimum coverage table. Tracked as **G13**.
- **Burn-in:** 48 h for BME680 per §B; applies here same as to bench-air.
- **Protective fixture verification:** radiation shield thermal-loading acceptance test required — not yet authored. Pre-shield readings inadmissible per §C item 7.
- **Admissibility status:** no readings admissible today (no build spec, no reference instruments, no shield verification).
- **§F build-spec metadata block:** planned — skeleton provided in the proposal cited above.

## Role in each program-phase

| Phase | Role | Notes |
|---|---|---|
| `v0.1` | **not in scope** | v0.1 is bench-air-only indoor slice. |
| `v0.2` | **sheltered-outdoor half of the two-node kit** (first promotion target) | Paired with bench-air. Milestone 2 in [`../../current/milestone-roadmap.md`](../../current/milestone-roadmap.md). Decision 2026-04-19: write the build spec (option A) rather than scope heat to bridge-path. |
| `v0.3` | unchanged from v0.2 | Flood-node lands alongside; mast-lite unchanged. |
| `v0.4` | sheltered node within multi-node registry | Registry lifecycle. |
| `v0.5` | unchanged from v0.4 | Governance-gated shared-layer contribution. |
| `v1.0` (pre-1.0 ladder) | fleet-wide deployment-maturity `v1.0` | Full calibration-program §G v1.0 posture attested. |
| `v1.5` (capability-stage bridge) | **may graduate to `weather-pm-mast`** | Richer outdoor evidence via weather-pm-mast becomes second-wave outdoor lane; mast-lite may step aside per [`../phase-roadmap.md`](../phase-roadmap.md) node-family maturity map. |

## Cross-repo link map

| Concern | Location |
|---|---|
| Architecture posture row | [`../node-taxonomy.md`](../node-taxonomy.md) next-promotion; [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) Tier 2 + "Deployment posture per node" |
| Hardware design | [oesis-hardware/mast-lite/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/mast-lite) |
| Build spec | **missing** — tracked as G12; skeleton in [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) |
| Build procedures | not yet authored |
| Runtime normalizer | Shared with bench-air via `oesis.bench-air.v1` lineage; `location_mode: "sheltered"` distinguishes mast-lite packets |
| Packet schema | Inherits `oesis.bench-air.v1` from [oesis-contracts/v0.1/](https://github.com/lumenaut-llc/oesis-contracts/tree/main/v0.1) |
| Gap register entries | **G12** (build spec missing — primary blocker), **G13** (reference instruments), **G14** (burn-in gate applies), **G17** (admissibility facts in schema) |

## Known gotchas

- **Build spec does not exist.** This is the central issue. Everything else derives from it. Milestone 2 promotion is blocked until the spec, calibration procedure, and radiation-shield design exist in `oesis-builds/`.
- **Radiation shield non-optional.** Bare SHT45 outdoor readings are corrupted by solar loading (often 2–4 °C bias). Pre-shield readings are inadmissible per calibration-program §C item 7 — not advisory.
- **Transport / power coordination.** USB from indoor through cable gland is permitted for sheltered class but requires weatherproof cable path, drip loop, and polyfuse per [oesis-hardware/parcel-kit/power-source-guide.md](https://github.com/lumenaut-llc/oesis-hardware/blob/main/parcel-kit/power-source-guide.md).
- **Indoor vs sheltered vs outdoor confusion.** "Sheltered" ≠ "outdoor". A covered porch / breezeway / eave-protected wall is sheltered. An open mast is outdoor. Mast-lite targets sheltered. Outdoor-exposed siting requires weather-pm-mast or similar.

## Related

- [`../node-taxonomy.md`](../node-taxonomy.md) next-promotion table
- [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) sheltered-class row
- [`../calibration-program.md`](../calibration-program.md) §C protective-fixture rule
- [`../architectural-choices-by-stage.md`](../architectural-choices-by-stage.md) row v0.2
- [`bench-air-node.md`](bench-air-node.md) — indoor sibling
- [`weather-pm-mast.md`](weather-pm-mast.md) — outdoor successor
