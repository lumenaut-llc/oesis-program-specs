# weather-pm-mast

## One-line summary

Second-wave outdoor sensor node: PM2.5 plus weather (temperature, humidity, pressure, wind). First node in the stack to measure particulate matter. Targets a richer outdoor evidence path once sheltered mast-lite posture is stable. Runtime normalization implemented; hardware build spec not yet authored.

## Deployment posture

- **Deployment class:** `outdoor` — per [`../node-taxonomy.md`](../node-taxonomy.md) geography-gated table and [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) "Deployment posture per node".
- **Power tier:** `mains` with outdoor-rated PSU routed through conduit — per [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) outdoor row; higher-draw sensors (PM airflow module, active heating in some variants) bias toward mains vs battery+solar.
- **IP tier:** `IP65` for exposed mast installations.
- **Transport tier:** `Wi-Fi` primary; LoRa or cellular permitted for parcels beyond Wi-Fi reach.
- **Protective fixtures:**
  - Radiation shield for SHT45 temperature/humidity.
  - PM airflow module — flow path for particulate sensing.
- **Sensor variants:**
  - PM2.5: laser-scattering sensor (e.g., Sensirion SPS30 or equivalent) — variant TBD.
  - Temperature + humidity: SHT45 with sintered-filter outdoor-rated variant.
  - Pressure: BME280 or equivalent.
  - Wind: cup anemometer or ultrasonic.

## Version evolution

| Build version | Status | Spec path | Notes |
|---|---|---|---|
| `v0-1` (planned) | not yet drafted | `oesis-builds/specs/weather-pm-mast/v0-1.md` — **does not exist** | Skeleton proposal at [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) Skeleton 3. |

Hardware documented at [oesis-hardware/v0.1/weather-pm-mast/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/v0.1/weather-pm-mast); not independently built.

## Calibration posture

Governed by [`../calibration-program.md`](../calibration-program.md) (physical-sensor program).

- **Deployment-maturity target:** `v1.5` (trust hardening) — higher maturity than v1.0 per [`../deployment-maturity-ladder.md`](../deployment-maturity-ladder.md) node-family maturity map, because the PM mast raises the bar for power design, airflow, maintenance, local buffering, and serviceability.
- **Reference instruments:**
  - PM2.5 reference: collocated EPA AQS reference monitor or equivalent — ambitious; tracked as **G13**.
  - Temperature / humidity: outdoor-rated psychrometer — tracked as G13.
  - Pressure: barometer — tracked as G13.
- **Burn-in:** 48 h platform default for BME-family + PM sensor conditioning + airflow stabilization.
- **Protective fixture verification:** airflow acceptance test + radiation-shield thermal-loading test — both to be authored.
- **Admissibility status:** no readings admissible today (no build spec, no populated references, no fixture verifications).
- **§F build-spec metadata block:** planned — skeleton in proposal.

## Role in each program-phase

| Phase | Role | Notes |
|---|---|---|
| `v0.1` → `v0.3` | **not in scope** | No outdoor PM evidence required at these phases. |
| `v0.4` → `v0.5` | available as optional geography-gated module | Not default. |
| `v1.0` (pre-1.0 ladder) | **second-wave outdoor lane** | May graduate from mast-lite once simpler sheltered outdoor is stable per [`../phase-roadmap.md`](../phase-roadmap.md) node-family maturity map. Maturity target `v1.5`. |
| `v1.5` (capability-stage bridge) | unchanged role; feeds outdoor PM signal into smoke closed-loop | Smoke loop uses outdoor PM (weather-pm-mast) + indoor PM (indoor-response-node) + HVAC state (equipment-state-adapter) to verify filtration response. |

## Cross-repo link map

| Concern | Location |
|---|---|
| Architecture posture row | [`../node-taxonomy.md`](../node-taxonomy.md) geography-gated; [`../integrated-parcel-system-spec.md`](../integrated-parcel-system-spec.md) Tier 3 + "Deployment posture per node" |
| Hardware design | [oesis-hardware/v0.1/weather-pm-mast/](https://github.com/lumenaut-llc/oesis-hardware/tree/main/v0.1/weather-pm-mast) |
| Build spec | **missing** — skeleton in [`../../../meta/proposals/oesis-builds-node-skeletons.md`](../../../meta/proposals/oesis-builds-node-skeletons.md) |
| Runtime normalizer | `oesis.ingest.v1_0.normalize_weather_pm_packet` |
| Packet schema | `oesis.weather-pm-mast.v1` → `air.pm.snapshot` — [oesis-contracts/v1.0/](https://github.com/lumenaut-llc/oesis-contracts/tree/main/v1.0) |
| Gap register entries | **G13** (reference instruments — PM reference is the hardest to source), **G17** (admissibility facts in schema) |

## Known gotchas

- **PM reference is operationally hard.** EPA AQS-grade collocation is expensive and often not available near pilot parcels. Practical references may use AirNow collocation or PurpleAir cross-check with documented accuracy statements.
- **Airflow module not a passive shield.** PM readings depend on stable airflow path through the sensor inlet. If the module is plugged, iced, or birdsnested, readings go wrong in ways that don't match temperature/humidity failure modes.
- **Power draw makes battery+solar marginal.** Active-flow PM sensors consume more than passive T/RH/P setups; mains preferred.
- **Relative humidity PM correction.** Outdoor PM2.5 readings distort under high RH; Barkjohn formula or equivalent correction is applied in `oesis.inference.divergence_rules_v0.json` — PM sensor choice must support it.

## Related

- [`../node-taxonomy.md`](../node-taxonomy.md) geography-gated section
- [`../calibration-program.md`](../calibration-program.md) §A minimum coverage table (PM2.5 row)
- [`../architectural-choices-by-stage.md`](../architectural-choices-by-stage.md) row v1.0 / v1.5
- [`mast-lite.md`](mast-lite.md) — sheltered predecessor
- [`flood-node.md`](flood-node.md) — outdoor-class sibling
