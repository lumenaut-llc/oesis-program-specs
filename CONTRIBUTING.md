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
- identify whether the change affects claims language, sharing defaults, or data release posture

## Governance-sensitive changes

The following changes need extra care and should reference the relevant governance docs:
- changes to parcel-state wording, notifications, or action-oriented copy
- changes to privacy defaults, sharing modes, or data export/deletion behavior
- changes to schemas carrying parcel-linked or shared data
- additions of external datasets or example datasets

See:
- `programs/resilient-home-intelligence/docs/privacy-governance/`
- `programs/resilient-home-intelligence/legal/`

## Commit style

Use clear scoped commits, for example:
- `hardware(bench-air-node): add sensor wiring diagram`
- `software(parcel-platform): add parcel state type`
- `docs(calibration): add rain gauge test procedure`
