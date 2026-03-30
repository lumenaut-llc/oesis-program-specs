# Mast-Lite Outdoor Node

## What it is

A simple outdoor parcel node focused on stable environmental readings and first weatherproofing.

## Standalone value

This subsystem should be buildable and useful even if the full neighborhood platform does not exist yet.

## Scope for current version

- SHT45 in radiation shield
- BME688
- optional UV
- outdoor enclosure
- basic mounting

## Intended outputs

- temperature
- humidity
- pressure
- VOC/gas trend
- optional UV
- node health

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

- add PM
- improve enclosure
- validate outdoor siting
