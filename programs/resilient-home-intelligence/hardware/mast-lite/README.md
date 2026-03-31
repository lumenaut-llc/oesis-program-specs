# Mast-Lite Outdoor Node

## What it is

A simple outdoor parcel node focused on stable environmental readings, basic weatherproofing, and first sheltered outdoor deployment.

## Why it matters

This node is the natural outdoor follow-on to the bench air node. It lets the project validate:
- outdoor sensor siting
- radiation shielding and enclosure bias
- versioned packet continuity across indoor and outdoor nodes
- longer cable and mounting realities
- first parcel-edge evidence from sheltered outdoor conditions

## Standalone value

Even without neighborhood sharing, this node gives a single parcel owner useful local conditions:
- sheltered outdoor microclimate trend
- pressure and humidity trend context for smoke, heat, and storm interpretation
- a repeatable outdoor reference platform before the full weather mast is built
- early enclosure and maintenance lessons for later nodes

## Scope for current version

- ESP32-S3 development board
- SHT45 in radiation shield
- BME680
- optional UV
- vented outdoor enclosure
- basic mast or eave mounting
- shared I2C bus
- JSON packet output over serial and/or Wi-Fi

## Inputs

- ambient sheltered outdoor air near the install location
- local time or monotonic uptime from firmware
- device identity and firmware version
- optional Wi-Fi credentials if packets are forwarded upstream or used for time sync

## Outputs

- temperature
- humidity
- pressure
- VOC/gas trend
- optional UV
- node health
- packet freshness timestamp
- device and sensor status flags

## Risks and constraints

- The BME680 gas resistance value is useful for trend detection, not as a direct pollutant concentration.
- Outdoor siting errors can dominate sensor quality even when wiring and firmware are correct.
- Direct sun, reflected heat, wet surfaces, and wall radiation can bias temperature badly without shielding and spacing.
- A vented enclosure improves survivability but can still trap heat or moisture if airflow is poor.
- This node should publish evidence with uncertainty, not parcel hazard claims.

## Dependencies

- shared glossary
- procurement and BOM
- documentation templates
- basic ingest path on the software side
- sheltered outdoor mounting assumptions
- serial JSON contract for first-build bring-up

## Next milestones

- validate the sheltered outdoor build against the bench air node packet contract
- add UV only after the base environmental stack is stable
- improve enclosure and cable routing
- promote the validated outdoor sensing stack into `weather-pm-mast`

## Open questions

See `open-questions.md` for unresolved decisions on enclosure venting, UV inclusion, and how aggressively outdoor filtering should happen on-node.

## Key docs

- `build-guide.md`
- `wiring.md`
- `firmware-notes.md`
- `serial-json-contract.md`
- `operator-runbook.md`
- `firmware/README.md`
