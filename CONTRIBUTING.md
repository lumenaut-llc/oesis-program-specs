# Contributing

This repository is organized around modular, documented subsystems.

## Contribution priorities

- clarity over cleverness
- reproducibility over speed
- privacy-safe defaults
- explicit provenance for data and assumptions
- standalone utility for each subsystem

## Before opening a PR

- update the relevant subsystem README
- update any affected docs in `docs/`
- add or revise diagrams if the change alters architecture
- note whether the change affects privacy, governance, or calibration
- add unresolved questions to the subsystem `open-questions.md`

## Commit style

Use clear scoped commits, for example:
- `hardware(bench-air-node): add sensor wiring diagram`
- `software(parcel-platform): add parcel state type`
- `docs(calibration): add rain gauge test procedure`
