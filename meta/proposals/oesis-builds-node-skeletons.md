# Proposal — Skeleton build specs for five node families in oesis-builds

## Status

Proposal. Drafted 2026-04-19. To be applied by the user via the oesis-builds build-vault agent, per the vault-scope rule in `oesis-builds/CLAUDE.md` ("Writes allowed ONLY under oesis-builds/").

Companion to [`oesis-builds-calibration-program-integration.md`](oesis-builds-calibration-program-integration.md), which covers bench-air-node specifically. This proposal covers the five remaining node families: mast-lite, flood-node, weather-pm-mast, thermal-pod, circuit-monitor.

## Why this is a proposal, not an edit

`oesis-builds/CLAUDE.md` scopes that vault's writes to itself. External agents (including this session) must respect the symmetric implication — the vault owns its own content. This doc captures skeletons for the build-vault agent to apply.

## Why these skeletons are needed

Per [`oesis-program-specs/architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §F, every node family in scope requires a `oesis-builds/specs/<node>/v0-X.md` file with a YAML front-matter metadata block. Today, only `bench-air-node` has a spec (and its §F block is covered in the companion proposal as Edit 4).

Five node families have no spec at all in `oesis-builds/specs/` today:
- `mast-lite` — blocker for v0.2 promotion (gap G12)
- `flood-node` — v0.3 lane
- `weather-pm-mast` — v1.0 lane
- `thermal-pod` — research-gated
- `circuit-monitor` — v1.5 bridge (Tier 3 direct measurement)

Each skeleton below can be filled in as hardware arrives; landing the §F block now means v0.2 promotion review has a structural contract to verify against.

## Schema revision

All skeletons below target `calibration_program_revision: "2026-04-19"`. If [`calibration-program.md`](../../architecture/system/calibration-program.md) §F changes before these skeletons are applied, re-stamp the revision date and verify the field set.

## Proposed skeletons

### Skeleton 1 — `oesis-builds/specs/mast-lite/v0-1.md`

Closes gap G12 (mast-lite spec missing). Deployment class: **sheltered**. Maturity target: **v1.0** (required for v0.2 promotion).

```yaml
---
node_family: mast-lite
build_version: v0-1
deployment_class: sheltered
deployment_maturity_target: v1.0
measurands:
  - name: temperature_c
    sensor_variant: sht45-sintered-filter-outdoor-rated  # variant TBD; placement guide requires sintered cap or equivalent for sheltered/outdoor
    accuracy_statement: "±0.1 °C, 0–60 °C (Sensirion datasheet); radiation-shield verification required per calibration-program §C"
    reference_instrument_ref: references/TBD.md  # tracked as G13
  - name: relative_humidity_pct
    sensor_variant: sht45-sintered-filter-outdoor-rated
    accuracy_statement: "±1.0 %RH, 0–100 %RH"
    reference_instrument_ref: references/TBD.md  # tracked as G13
  - name: gas_resistance_ohm
    sensor_variant: bme680-breakout-adafruit-3660
    accuracy_statement: "no absolute accuracy floor; repeatability-gated by burn-in; ambient humidity-sensitive in sheltered siting"
    reference_instrument_ref: null
burn_in:
  required: true
  window_hours: 48  # BME680 platform default per calibration-program §B
protective_fixtures:
  - name: passive radiation shield
    acceptance_test_ref: specs/mast-lite/radiation-shield-thermal-loading-test.md  # to author
    rationale: "Bare SHT45 outdoor readings are corrupted by solar loading; pre-shield readings inadmissible per calibration-program §C item 7"
transport:
  primary: serial
  permitted_fallbacks: [wifi]
power:
  source: dc_12v  # or USB routed from indoor, per deployment-maturity-ladder sheltered-class defaults
  protection:
    - "surge protection on entry"
    - "fused input"
    - "strain relief on cable path"
    - "24 h minimum buffering where ingest loss is consequential"
calibration_program_revision: "2026-04-19"
---
```

### Skeleton 2 — `oesis-builds/specs/flood-node/v0-1.md`

v0.3 lane. Deployment class: **outdoor**. Critical fixtures: rigid mount, zero-reference, staff gauge for water-depth calibration.

```yaml
---
node_family: flood-node
build_version: v0-1
deployment_class: outdoor
deployment_maturity_target: v1.0
measurands:
  - name: water_depth_cm
    sensor_variant: ultrasonic-rangefinder-outdoor-rated  # e.g. MaxBotix MB7389 or equivalent
    accuracy_statement: "±1 cm typical; geometry-dependent; zero-reference required"
    reference_instrument_ref: references/TBD.md  # tracked as G13; flood-node reference = staff gauge + manual depth measurement
  - name: rise_rate_cm_per_hr
    sensor_variant: derived  # computed from depth time-series, not a separate sensor
    accuracy_statement: "derived metric; inherits depth accuracy; rate threshold requires documented calibration window"
    reference_instrument_ref: null
burn_in:
  required: false  # ultrasonic sensors do not require conditioning
  window_hours: null
protective_fixtures:
  - name: rigid mount at documented low-point
    acceptance_test_ref: specs/flood-node/low-point-geometry-test.md  # to author
    rationale: "Flood-node readings are only interpretable against a documented geometry; without it, depth numbers are decoration"
  - name: zero-reference + staff gauge
    acceptance_test_ref: specs/flood-node/zero-reference-calibration.md  # to author
    rationale: "Without a zero-reference tied to a physical staff gauge, depth calibration is not traceable per calibration-program §A"
transport:
  primary: serial
  permitted_fallbacks: [lora, wifi]
power:
  source: battery_solar
  protection:
    - "surge + transient + weather protection on entry"
    - "fused; sealed connectors"
    - "72 h runtime floor under worst-case solar"
    - "retention of last observations through power events"
calibration_program_revision: "2026-04-19"
---
```

### Skeleton 3 — `oesis-builds/specs/weather-pm-mast/v0-1.md`

v1.0 lane (second-wave outdoor). Deployment class: **outdoor**. Adds PM2.5 measurand — first node to do so.

```yaml
---
node_family: weather-pm-mast
build_version: v0-1
deployment_class: outdoor
deployment_maturity_target: v1.5  # richer outdoor lane; higher maturity target per deployment-maturity-ladder node-family maturity map
measurands:
  - name: pm2_5_ug_m3
    sensor_variant: sps30-or-equivalent-laser-scattering-sensor  # variant TBD
    accuracy_statement: "±10 μg/m³ or ±10 % (whichever greater) per EPA AQS; EPA AirNow cross-check required at onboarding"
    reference_instrument_ref: references/TBD.md  # tracked as G13; PM reference = collocated EPA AQS reference monitor or equivalent
  - name: temperature_c
    sensor_variant: sht45-sintered-filter-outdoor-rated
    accuracy_statement: "±0.1 °C, 0–60 °C; radiation-shield verification required"
    reference_instrument_ref: references/TBD.md
  - name: relative_humidity_pct
    sensor_variant: sht45-sintered-filter-outdoor-rated
    accuracy_statement: "±1.0 %RH"
    reference_instrument_ref: references/TBD.md
  - name: pressure_hpa
    sensor_variant: bme280-or-equivalent  # TBD
    accuracy_statement: "±1 hPa"
    reference_instrument_ref: references/TBD.md
  - name: wind_speed_m_s
    sensor_variant: cup-anemometer-or-ultrasonic  # TBD
    accuracy_statement: "TBD"
    reference_instrument_ref: references/TBD.md
burn_in:
  required: true
  window_hours: 48  # PM sensor conditioning + airflow stabilization
protective_fixtures:
  - name: radiation shield + PM airflow module
    acceptance_test_ref: specs/weather-pm-mast/airflow-acceptance-test.md  # to author
    rationale: "PM readings distorted without proper airflow; temperature readings distorted without radiation shield"
transport:
  primary: wifi
  permitted_fallbacks: [lora, cellular]
power:
  source: mains_outdoor_psu
  protection:
    - "outdoor-rated PSU routed through conduit"
    - "surge + transient + weather protection on entry"
    - "sealed connectors; corrosion-aware hardware"
    - "72 h runtime floor via UPS where mains reliability warrants"
calibration_program_revision: "2026-04-19"
---
```

### Skeleton 4 — `oesis-builds/specs/thermal-pod/v0-1.md`

Research-gated lane. Deployment-maturity target deliberately below `v1.0` until scene + privacy posture clears; marked `research_gated: true` so admissibility tooling can reject readings from this family for production coefficient fits.

```yaml
---
node_family: thermal-pod
build_version: v0-1
deployment_class: outdoor  # fixed scene; research-gated
deployment_maturity_target: v0.1  # intentionally kept at bench prototype until contract + privacy posture clears
research_gated: true  # flag: readings from research-gated families are inadmissible to production calibration datasets per calibration-program §C
measurands:
  - name: scene_thermal_c_grid
    sensor_variant: mlx90640-or-equivalent-32x24-thermal-array  # TBD
    accuracy_statement: "±1–2 °C absolute; relative resolution sufficient for scene gradient detection; emissivity-dependent"
    reference_instrument_ref: references/TBD.md  # thermal-scene reference = co-located hand-held IR thermometer + emissivity documentation
burn_in:
  required: true
  window_hours: 24  # thermal arrays require post-power-on warmup for stable offset
protective_fixtures:
  - name: hooded enclosure with documented field-of-view
    acceptance_test_ref: specs/thermal-pod/fov-privacy-review.md  # to author; privacy review required
    rationale: "Privacy-reviewed field-of-view is a prerequisite for any reading to be admissible; uncontrolled FOV risks surveillance drift per vision-and-use-cases.md"
transport:
  primary: wifi
  permitted_fallbacks: []
power:
  source: mains_outdoor_psu
  protection:
    - "Raspberry Pi with durable local storage"
    - "clean shutdown posture"
calibration_program_revision: "2026-04-19"
---
```

### Skeleton 5 — `oesis-builds/specs/adapters/circuit-monitor/v0-1.md`

**Note:** circuit-monitor is an **adapter** (Tier 3 direct measurement per [`node-taxonomy.md`](../../architecture/system/node-taxonomy.md) tiered acquisition model) — not a parcel-sensing hardware node. Its spec should land under `oesis-builds/specs/adapters/circuit-monitor/v0-1.md`, and it is governed by [`adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md) §F rather than calibration-program §F.

Flag for the build-vault agent: the `specs/adapters/` subtree may not exist yet. Create it if needed; it will become the home for every future adapter spec.

```yaml
---
adapter_family: circuit-monitor
build_version: v0-1
tier: tier_3_direct  # direct measurement of current draw via CT clamps
source_authority_ref: procedures/adapters/circuit-monitor/source.md  # to author; source = PZEM-004T/016 module reading CT clamp current at configured panel circuit
pinned_contract_version: pzem-004t-v3-serial  # pinned firmware + protocol version
measurands:
  - name: hvac_mode
    source_field: derived_from_current_draw_pattern
    expected_type: enum  # off | fan_only | cool | heat | recirc (where distinguishable)
    uncertainty_bound: "HIGH confidence for on/off; MEDIUM for mode distinction"
    tier_3_cross_check_ref: null  # self is tier 3; no higher tier available
  - name: sump_state
    source_field: derived_from_current_draw_pattern
    expected_type: enum  # off | running
    uncertainty_bound: "HIGH confidence for on/off"
    tier_3_cross_check_ref: null
  - name: equipment_running
    source_field: boolean_from_current_above_threshold
    expected_type: bool
    uncertainty_bound: "HIGH confidence"
    tier_3_cross_check_ref: null
  - name: power_draw_w
    source_field: pzem_power_w
    expected_type: number
    uncertainty_bound: "±1 % per PZEM-004T datasheet"
    tier_3_cross_check_ref: null
onboarding_requirements:
  cross_check_against_tier_3: false  # this IS tier 3
  initial_verification_window_hours: 24
credential_model:
  type: none  # direct serial; no cloud auth required
  scope: "local serial port"
  refresh_cadence_hours: null
deployment_maturity_target: v1.5  # v1.5 bridge hardware
# Physical posture (even though this is an adapter, the CT clamp device has physical posture):
physical_posture:
  deployment_class: indoor  # mains-adjacent, inside electrical panel or near it
  power_source: low_power_from_measured_circuit
  ip_tier: electrical_enclosure_ip20
  transport: wifi
  protective_fixtures:
    - name: electrical-code-compliant CT clamp installation
      acceptance_test_ref: specs/adapters/circuit-monitor/installation-code-compliance.md  # to author
      rationale: "Installation on live mains circuits requires licensed electrician in many jurisdictions; code compliance is a prerequisite for deployment"
adapter_trust_program_revision: "2026-04-19"
---
```

## Application via build-vault agent

```bash
cd oesis-builds
claude
> Apply the five skeletons in ../oesis-program-specs/meta/proposals/oesis-builds-node-skeletons.md.
> For each skeleton: create the target file (specs/<node>/v0-1.md or specs/adapters/<adapter>/v0-1.md), paste the YAML front-matter block exactly as written, add minimum body content (Overview, BOM-as-specified, Wiring, Firmware, Procedures, Acceptance tests, Linked decisions sections as per the _templates/spec.md skeleton), and record a decision entry under decisions/<node>/ noting the forward-looking §F declaration.
> Flag for circuit-monitor specifically: ensure specs/adapters/ subtree exists; circuit-monitor is governed by adapter-trust-program.md not calibration-program.md.
```

The build-vault agent will respect the frozen-specs / append-only rules. Each skeleton's missing acceptance-test references (`acceptance_test_ref`) become TODOs under `specs/<node>/` that the agent can either author inline or mark as pending.

## Status after application

- **G12** (mast-lite spec missing) → addressed by Skeleton 1 at structural level; full resolution requires hardware bring-up + reference instrument population + radiation-shield test authoring.
- **New structural presence** for flood-node, weather-pm-mast, thermal-pod, circuit-monitor in `oesis-builds/specs/` (or `specs/adapters/` for circuit-monitor) — each declares deployment posture in a machine-greppable form.
- **G13** (reference instruments) — unchanged; every skeleton's `reference_instrument_ref: references/TBD.md` makes the dependency explicit per family.
- **G14** (burn-in) — enforced structurally for BME680-bearing nodes (mast-lite, weather-pm-mast) and for thermal arrays (thermal-pod).
- **Per-family posture declarations** match the defaults in [`deployment-maturity-ladder.md`](../../architecture/system/deployment-maturity-ladder.md) "Deployment-class standards" and the summary table in [`integrated-parcel-system-spec.md`](../../architecture/system/integrated-parcel-system-spec.md) "Deployment posture per node".

## Related

- [`oesis-builds-calibration-program-integration.md`](oesis-builds-calibration-program-integration.md) — companion proposal for bench-air-node and vault-level integration
- [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §F schema
- [`../../architecture/system/adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md) §F schema (for circuit-monitor)
- [`../../architecture/system/deployment-maturity-ladder.md`](../../architecture/system/deployment-maturity-ladder.md) — class / power / IP / transport defaults
- [`../../architecture/system/integrated-parcel-system-spec.md`](../../architecture/system/integrated-parcel-system-spec.md) — hardware role map + deployment posture summary
- [`../../release/v.0.1/v0.1-gap-register.md`](../../release/v.0.1/v0.1-gap-register.md) — G12, G13, G14, G18
- `oesis-builds/CLAUDE.md` — vault-scope rules
