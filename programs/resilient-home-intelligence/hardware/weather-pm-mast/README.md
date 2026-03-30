# Weather + PM Mast

## What it is

A more complete parcel mast that adds particulate sensing and local weather mechanics.

## Standalone value

This subsystem should be buildable and useful even if the full neighborhood platform does not exist yet.

## Scope for current version

- SPS30
- wind speed
- wind direction
- rainfall
- mast hardware

## Intended outputs

- PM1/2.5/4/10
- wind
- rain
- environmental context for smoke and storm logic

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

- field stability testing
- maintenance plan
- integration with parcel inference
