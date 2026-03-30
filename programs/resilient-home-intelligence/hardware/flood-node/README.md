# Flood Node

## What it is

A dedicated low-point node that measures surface distance and water depth where runoff matters operationally.

## Standalone value

This subsystem should be buildable and useful even if the full neighborhood platform does not exist yet.

## Scope for current version

- MB7389
- small enclosure
- dedicated MCU
- mounting at true low point

## Intended outputs

- surface distance
- water depth
- rise rate
- flood-node health

## Dependencies

- shared glossary
- procurement and BOM
- documentation templates
- basic ingest path on the software side

## Build docs to create

- `build-guide.md`
- `wiring.md`
- `firmware-notes.md`
- `calibration.md`
- `open-questions.md`

## Next milestones

- calibration procedure
- rain-event testing
- drainage topology integration
