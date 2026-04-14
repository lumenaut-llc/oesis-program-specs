# Equipment State Observation Schema (`v1.5`)

## Purpose

Capture read-side operating posture for bridge-stage response loops while
keeping `house-state` compact and stable.

## Why this belongs in `v1.5`

`v1.5` is where OESIS needs enough measured operating-state evidence to connect:

`hazard -> house state -> action -> measured outcome`

without pretending controls automation is complete.

## Minimum fields

- `parcel_id`
- `captured_at`
- `confidence_band`
- `source`
- `signals`

## Bridge-stage signal targets

- HVAC mode
- fan state
- recirculation versus fresh-air posture
- purifier state
- sump or pump state

## Guardrails

- Read-side state first; do not imply guaranteed actuation.
- Preserve source kind and freshness metadata for every snapshot.
- Keep this object private by default unless explicit sharing policy applies.

## Related

- `house-state-schema.md`
- `intervention-event-schema.md`
- `verification-outcome-schema.md`
- `../../../hardware/v1.5/equipment-state-adapter.md`
