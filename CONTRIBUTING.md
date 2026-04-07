# Contributing

This repository is organized around modular, documented subsystems.

## Split working rules

- treat this repository as the canonical specs, release, and governance home during the repo split
- treat `../oesis-runtime` as the canonical runtime repository
- treat `../oesis-public-site` as the canonical public-site repository
- treat local `oesis/` and `sites/public-preview/` paths as migration pointers only
- do not add new runtime dependencies on `docs/`, `technical-architecture/`, `hardware/`, `software/`, `legal/`, `media/`, `shared/`, `meta/`, or `sites/`
- use contracts, public-content, and runtime-evidence bundle boundaries instead of new cross-tree relative-path reads
- use `scripts/repo_split.py` and the `repo-split-*` make targets when refreshing split artifacts or sibling repos

## Contribution priorities

- clarity over cleverness
- reproducibility over speed
- privacy-safe defaults
- explicit provenance for data and assumptions
- standalone utility for each subsystem

## Before opening a PR

- update the relevant subsystem README
- update any affected docs in `docs/`
- update `technical-architecture/` when the current or target architecture version changes
- add or revise diagrams if the change alters architecture
- note whether the change affects privacy, governance, or calibration
- add unresolved questions to the subsystem `open-questions.md`
- identify whether the change affects claims language, sharing defaults, or data release posture
- state whether the change belongs to the specs repo, the runtime repo, or the site repo

## Governance-sensitive changes

The following changes need extra care and should reference the relevant governance docs:

- changes to parcel-state wording, notifications, or action-oriented copy
- changes to privacy defaults, sharing modes, or data export/deletion behavior
- changes to schemas carrying parcel-linked or shared data
- additions of external datasets or example datasets

See:

- `docs/privacy-governance/`
- `legal/`

## Commit style

Use clear scoped commits, for example:

- `hardware(bench-air-node): add sensor wiring diagram`
- `software(parcel-platform): add parcel state type`
- `docs(calibration): add rain gauge test procedure`
