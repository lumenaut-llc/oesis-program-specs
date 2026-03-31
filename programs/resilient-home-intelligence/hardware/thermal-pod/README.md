# 2D Thermal Pod

## What it is

A scene-level sensing pod that uses a thermal array and publishes derived thermal metrics instead of raw frames.

## Why it matters

This node is the project’s first step into area-based sensing rather than single-point measurements. It lets the project validate:
- privacy-safe derived thermal telemetry
- hooded outdoor or semi-outdoor thermal siting
- a Raspberry Pi based node path
- scene-level trend detection without storing identifiable imagery
- how much thermal context is actually useful before adding more complex sensing

## Standalone value

Even without the full neighborhood platform, this subsystem can provide:
- scene temperature spread and trend context
- hot-fraction tracking for sun load or abnormal heat sources
- early-warning thermal drift around a fixed view
- a privacy-conscious way to test scene sensing on a parcel

## Scope for current version

- Raspberry Pi 5
- MLX90640 thermal array
- hooded enclosure
- fixed field of view
- derived metrics only, no raw thermal frame persistence
- JSON line output over stdout or local log

## Inputs

- low-resolution thermal frame from the MLX90640
- fixed install geometry and field of view
- local system time on the Raspberry Pi
- device identity and firmware version
- optional local config for thresholds and masking

## Intended outputs

- scene max temperature
- scene mean temperature
- scene min temperature
- hot fraction
- scene spread
- thermal trend context
- node health

## Risks and constraints

- This node must stay privacy-safe by default and avoid storing raw frames in the normal first-build path.
- Thermal readings are highly sensitive to sun angle, enclosure self-heating, and background composition.
- A scene-level metric can be useful without proving parcel-wide hazard truth.
- Mounting drift or an overly broad field of view can make trends harder to interpret than point sensors.

## Dependencies

- shared glossary
- procurement and BOM
- documentation templates
- basic ingest path on the software side
- privacy-governance alignment for derived-only telemetry
- a fixed-view installation plan

## Next milestones

- prove the derived-metrics-only first build
- validate the hooded enclosure against self-heating and splash
- define scene masking and hot-fraction thresholds
- decide whether any future frame snapshots are ever justified

## Open questions

See `open-questions.md` for unresolved decisions on masking, retention, and what derived thermal fields are worth keeping.

## Key docs

- `build-guide.md`
- `wiring.md`
- `firmware-notes.md`
- `serial-json-contract.md`
- `operator-runbook.md`
- `firmware/README.md`
