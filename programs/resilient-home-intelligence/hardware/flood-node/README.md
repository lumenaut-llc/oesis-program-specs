# Flood Node

## What it is

A dedicated low-point parcel node that measures surface distance and inferred water depth where runoff matters operationally.

## Why it matters

This node is the flood-specific complement to the other environmental builds. It lets the project validate:
- documented low-point installation discipline
- depth-oriented evidence instead of general weather context
- calibration against a real drainage geometry
- rise-rate detection during runoff events
- the difference between point runoff evidence and parcel-wide flood claims

## Standalone value

Even without the full neighborhood platform, this subsystem gives a parcel owner useful local information:
- low-point standing-water depth trend
- runoff rise and recession timing
- a repeatable way to compare storms at the same location
- early evidence for whether a chosen low point is operationally meaningful

## Scope for current version

- ESP32-S3 development board
- MB7389 ultrasonic range sensor
- weather-resistant enclosure with sensor opening or standoff
- fixed mounting bracket at a documented runoff low point
- analog-read bring-up path with install-specific calibration constants
- JSON packet output over serial and/or Wi-Fi

## Inputs

- measured sensor-to-surface distance at the runoff low point
- install-specific dry reference distance
- local time or monotonic uptime from firmware
- device identity and firmware version
- optional Wi-Fi credentials if packets are forwarded upstream or used for time sync

## Outputs

- raw analog signal health
- inferred surface distance
- inferred water depth
- rise rate
- node health
- packet freshness timestamp
- calibration status flags

## Risks and constraints

- Flood-node evidence is only meaningful if the install point is a real runoff low point.
- Ultrasonic distance can be biased by splashing, foam, irregular surfaces, wind, and bad mounting angles.
- First-build depth numbers should be treated as provisional until dry reference and on-site checks are complete.
- This node produces point evidence, not a parcel-wide flood truth claim by itself.
- Cable routing, condensation, and enclosure splash management matter more here than in the simpler air nodes.

## Dependencies

- shared glossary
- procurement and BOM
- documentation templates
- basic ingest path on the software side
- parcel context documenting the runoff low point
- serial JSON contract for first-build bring-up

## Next milestones

- prove a stable dry-reference installation
- validate depth deltas with manual ruler checks
- observe at least one real runoff event
- connect the low-point evidence to parcel flood inference conservatively

## Open questions

See `open-questions.md` for unresolved decisions on sensor interface choice, mount geometry, and how much of the depth calibration should live in firmware versus parcel context.

## Key docs

- `build-guide.md`
- `wiring.md`
- `firmware-notes.md`
- `serial-json-contract.md`
- `operator-runbook.md`
- `firmware/README.md`
