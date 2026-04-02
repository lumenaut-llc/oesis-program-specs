# Integrated Parcel Kit BOM

## Purpose

Translate the integrated parcel system design into a practical first bill of materials by deployment tier.

Companion checklist:

- `parcel-kit-procurement-checklist.md`
- `parcel-installation-checklist.md`

## Governing rule

The parcel kit is one system, but not one physical box.
Use specialized nodes where placement requirements differ, then unify them through one parcel identity, one node registry, and one software path.

## Shared non-hardware system parts

Every tier assumes these system parts exist:

- one `parcel_id`
- one parcel-context record
- one node-registry record
- one sharing-settings record
- one ingest endpoint path
- one local validation path through `make rhi-check`

## Tier 1: Fastest useful parcel kit

### Goal

Deliver useful single-home value on the shortest timeline.

### Hardware BOM

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | `bench-air-node` build | indoor or sheltered reference node |
| 1 | ESP32-S3 development board | inside bench-air-node |
| 1 | SHT45 breakout | primary temperature and humidity |
| 1 | BME680 breakout | pressure and gas-trend support |
| 1 | USB power supply and cable | simplest first power path |

### Software and ops BOM

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | ingest service path | serial validation first, HTTPS push later |
| 1 | inference engine path | uses local plus public evidence |
| 1 | parcel-platform view | one homeowner-facing parcel surface |

### When to choose it

- fastest pilot
- indoor smoke and heat focus
- minimal hardware risk

## Tier 2: First integrated parcel kit

### Goal

Add outdoor parcel context without waiting for the richer mast build.

### Additional hardware BOM

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | `mast-lite` build | sheltered outdoor reference node |
| 1 | second ESP32-S3 development board | separate outdoor controller |
| 1 | second SHT45 breakout | outdoor primary temperature and humidity |
| 1 | second BME680 breakout | outdoor pressure and gas-trend support |
| 1 | vented enclosure and shield hardware | preserve airflow and survivability |
| 1 | basic mount or eave hardware | stabilize sheltered outdoor placement |

### Integration requirements

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | parcel-scoped node registry | binds indoor and outdoor nodes to one parcel |
| 2 | stable node IDs | one per controller |
| 1 | shared transport posture | recommended `https_push` for both nodes |

### When to choose it

- first full homeowner pilot
- need indoor versus outdoor distinction
- want one coherent parcel kit without PM mast complexity

## Optional hazard module: Flood

### Add only when

- the parcel has a meaningful runoff low point
- flood and drainage are an actual target use case

### Additional hardware BOM

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | `flood-node` build | low-point runoff evidence module |
| 1 | ESP32-S3 development board | separate flood controller |
| 1 | MB7389 ultrasonic range sensor | low-point depth evidence |
| 1 | weather-resistant enclosure | splash-aware housing |
| 1 | fixed mounting bracket | must preserve repeatable geometry |

### Additional integration requirements

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | runoff low-point install record | part of parcel context and registry meaning |
| 1 | dry-reference measurement | required before stronger interpretation |
| 1 | conservative flood observation family | keep point evidence distinct from parcel-wide claims |

## Tier 3: Rich outdoor upgrade

### Goal

Promote the outdoor leg from `mast-lite` to `weather-pm-mast` after the simpler kit is stable.

### Additional hardware BOM

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | `weather-pm-mast` build | richer outdoor evidence path |
| 1 | SPS30 | particulate sensing |
| 1 | mast hardware and enclosure upgrades | exposure-ready mounting |
| optional | wind and rain components | only after PM-first stability |

### Replacement rule

Treat `weather-pm-mast` as an upgrade to the outdoor reference lane, not a requirement before the first integrated pilot.

## Separate R&D lane: Thermal

### Keep separate because

- controller class differs
- privacy review differs
- observation family differs

### Hardware BOM

| Quantity | Item | Notes |
| --- | --- | --- |
| 1 | `thermal-pod` build | fixed-scene thermal system |
| 1 | Raspberry Pi 5 | current controller |
| 1 | MLX90640 | thermal array |
| 1 | hooded enclosure | must control scene and self-heating |

### Product rule

Do not fold the thermal pod into the default integrated parcel kit until the derived-only contract and usefulness case are stronger.

## Node-to-system map

| Node | Parcel role | Normalized family target | Default status |
| --- | --- | --- | --- |
| `bench-air-node` | indoor reference | `air.node.snapshot` | required |
| `mast-lite` | outdoor reference | `air.node.snapshot` | recommended |
| `flood-node` | runoff low point | `flood.low_point.snapshot` | optional |
| `weather-pm-mast` | richer outdoor upgrade | `air.pm_weather.snapshot` | second wave |
| `thermal-pod` | scene-level thermal R&D | `thermal.scene.snapshot` | separate lane |

## Recommended first integrated pilot bundle

- 1 `bench-air-node`
- 1 `mast-lite`
- 1 parcel node-registry record
- 1 shared `https_push` transport posture
- optional `flood-node` only on the right parcels

That is the best balance between singular system design, truthful hazard coverage, and timeline pressure.
