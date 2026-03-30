# 2D Thermal Pod

## What it is

A scene-level sensing pod that produces derived thermal metrics rather than only point measurements.

## Standalone value

This subsystem should be buildable and useful even if the full neighborhood platform does not exist yet.

## Scope for current version

- Raspberry Pi 5
- MLX90640
- hooded enclosure
- derived thermal outputs

## Intended outputs

- scene max
- scene mean
- hot fraction
- thermal trend context

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

- privacy-safe derived metrics
- outdoor mounting tests
- possible future depth pod
