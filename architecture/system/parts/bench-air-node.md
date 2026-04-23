# bench-air-node

## One-line summary

Indoor air sensor node for parcel-operator-local smoke and heat evidence; the reference lineage for the `oesis.bench-air.v1` packet family. Current-truth hardware; the only node family proven end-to-end through the software stack today.

## Deployment posture

Values cited from canonical sources; do not edit here if upstream changes.

- **Deployment class:** `indoor` — per [`../node-taxonomy.md`](../node-taxonomy.md) current-truth table and [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node" row.
- **Power tier:** `USB` — per [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) Deployment-class standards (indoor row).
- **IP tier:** `IP20` (none required) — per ladder indoor row.
- **Transport tier:** `serial` (v0.1 floor per gap G3); Wi-Fi permitted in later lanes.
- **Protective fixtures:** none required (indoor-only).
- **Sensor variants:**
  - Temperature + humidity: SHT45 per [`../sensor-placement-and-representativeness-guide.md`](../sensor-placement-and-representativeness-guide.md) Sensor variant selection principles; unfiltered variant acceptable for indoor placement.
  - Gas resistance: BME680 per decision [`oesis-builds/decisions/bench-air-node/2026-04-bme680-authoritative.md`](https://github.com/lumenaut-llc/oesis-builds/blob/main/decisions/bench-air-node/2026-04-bme680-authoritative.md).

## Version evolution

| Build version | Status | Spec path | Notes |
|---|---|---|---|
| `v0-1` | shipped (v0.1 reference) | [`oesis-builds/specs/bench-air-node/v0-1.md`](https://github.com/lumenaut-llc/oesis-builds/blob/main/specs/bench-air-node/v0-1.md) | §F front-matter block missing — tracked as G16; proposal at [`../../../meta/proposals/oesis-builds-calibration-program-integration.md`](../../../meta/proposals/oesis-builds-calibration-program-integration.md) Edit 4 |
| `v0-2` (planned) | not yet drafted | tbd | Forward version to carry any schema / wiring / firmware changes that arise from v0.2 promotion work |

## Calibration posture

Governed by [`../calibration-program.md`](../calibration-program.md) (physical-sensor program).

- **Deployment-maturity target:** `v1.0` (first fielded kit) — required by v0.2 promotion bar per [`../../current/pre-1.0-version-progression.md`](../../current/pre-1.0-version-progression.md) item 5, with retroactivity rule: v0.1 sign-off is not reopened, but bench-air must reach v1.0 posture as part of v0.2.
- **Reference instruments:** not yet populated under `oesis-builds/procedures/bench-air-node/references/` — placeholder only. Tracked as **G13**.
- **Burn-in:** 48 h required for BME680 per calibration-program §B. Not yet enforced in bring-up acceptance. Tracked as **G14**.
- **Admissibility status:** v0.1 readings are **not admissible** to calibration-dataset coefficient fitting per §C. Admissibility becomes possible after v1.0 posture is reached (§F block populated, reference instruments present, burn-in gate enforced, protective-fixture requirements satisfied — all n/a for indoor).
- **§F build-spec metadata block:** planned — proposal at [`../../../meta/proposals/oesis-builds-calibration-program-integration.md`](../../../meta/proposals/oesis-builds-calibration-program-integration.md) Edit 4.

## Role in each program-phase

| Phase | Role | Notes |
|---|---|---|
| `v0.1` | sole node; one parcel, one pipeline, one view | Frozen reference slice per [`../../current/minimum-functioning-v0.1.md`](../../current/minimum-functioning-v0.1.md). Deployment-maturity `v0.1` acceptable. Serial-only transport. |
| `v0.2` | indoor half of the two-node kit | Paired with mast-lite for sheltered outdoor. Must reach deployment-maturity `v1.0` per promotion bar (retroactivity rule applies). |
| `v0.3` | unchanged from v0.2 | Flood-node lands alongside; bench-air role unchanged. |
| `v0.4` | indoor node within multi-node registry | Stronger registry-driven lifecycle per [`../../current/milestone-roadmap.md`](../../current/milestone-roadmap.md) Milestone 4 context. |
| `v0.5` | unchanged from v0.4 | Governance-gated shared-layer contribution possible per gap G22. |
| `v1.0` (pre-1.0 ladder) | same role; now at fleet-wide deployment-maturity `v1.0` | §F, §A, §B, §C, §E all complete per calibration-program §G. |
| `v1.5` (capability-stage bridge) | unchanged physical role; indoor-response-node may complement it | indoor-response-node adds indoor PM2.5 / T / RH; bench-air remains the primary indoor air source for smoke/heat. |

## Cross-repo link map

| Concern | Location |
|---|---|
| Architecture posture row | [`../node-taxonomy.md`](../node-taxonomy.md) current-truth; [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node" |
| Hardware design | [oesis-hardware/bench-air-node/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/bench-air-node) (build-guide, wiring, serial-json-contract, firmware) |
| Build spec (pinned) | [oesis-builds/specs/bench-air-node/v0-1.md](https://github.com/lumenaut-llc/oesis-builds/blob/main/specs/bench-air-node/v0-1.md) |
| Build procedures | [oesis-builds/procedures/bench-air-node/](https://github.com/lumenaut-llc/oesis-builds/tree/main/procedures/bench-air-node) (bring-up, calibration, cross-check, stress-test) |
| Build guide (practical) | [oesis-builds/GUIDE.md](https://github.com/lumenaut-llc/oesis-builds/blob/main/GUIDE.md) |
| Runtime normalizer | [oesis-runtime: `oesis.ingest.normalize_packet`](https://github.com/lumenaut-llc/oesis-runtime) |
| Packet schema | `oesis.bench-air.v1` — [oesis-contracts/v0.1/node-observation-schema.md](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/node-observation-schema.md) |
| Gap register entries | **G13** (reference instruments), **G14** (burn-in gate), **G16** (§F block), **G23** (config provenance) |

## Known gotchas

- **BME680 vs BME688** — BOM CSV defect resolved via decision [`oesis-builds/decisions/bench-air-node/2026-04-bme680-authoritative.md`](https://github.com/lumenaut-llc/oesis-builds/blob/main/decisions/bench-air-node/2026-04-bme680-authoritative.md).
- **48h burn-in** — BME680 gas-resistance readings are unstable for the first 24–48 h. Ingest tagging via `burn_in_complete: false` is planned (G14) but not yet wired.
- **Thermal-bleed between BME680 and SHT45** — spec requires ≥ 2 cm separation; slipping this contaminates the gas-resistance rolling baseline by the temperature sensor's self-heating.
- **Wikipedia-style entity reference:** [oesis-wiki BME680 entity page](https://github.com/lumenaut-llc/oesis-wiki/blob/main/wiki/entities/bme680.md), [oesis-wiki SHT45 entity page](https://github.com/lumenaut-llc/oesis-wiki/blob/main/wiki/entities/sht45.md).

## Related

- [`../node-taxonomy.md`](../node-taxonomy.md)
- [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md)
- [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md)
- [`../calibration-program.md`](../calibration-program.md)
- [`../architectural-choices-by-stage.md`](../architectural-choices-by-stage.md) row v0.1
- [`mast-lite.md`](mast-lite.md) — sibling node that lands at v0.2
