# Bench Air Node

## What it is

The smallest possible starter node for learning the sensing, firmware, and data pipeline.

## Standalone value

This subsystem should be buildable and useful even if the full neighborhood platform does not exist yet.

## Scope for current version

- ESP32-S3
- SHT45
- BME688
- USB power
- Indoor or sheltered testing

## Intended outputs

- temperature
- humidity
- pressure
- VOC/gas trend
- basic health telemetry

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

- publish JSON packets
- add logging
- turn into outdoor mast-lite
