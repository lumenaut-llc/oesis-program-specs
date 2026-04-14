# Parcel Platform Interfaces v1.5

## Purpose

Describe the bridge-stage parcel-facing APIs once response support surfaces are
treated as first-class product objects.

## Primary parcel-facing surfaces

- parcel state
- evidence summary
- house state
- interventions
- verification outcomes

## Priority bridge surfaces

The platform should emphasize these bridge surfaces before full control
compatibility becomes a required product promise:

- `house_state`
- `interventions`
- `verification_outcomes`

## Controls note

`control_compatibility` may exist in draft form later, but it should not be
treated as the main near-term product surface.

The main near-term product shift is:

- indoor response sensing
- power and outage sensing
- equipment-state visibility
- action logging
- outcome verification

Full compatibility inventory remains a `v2.5` concern.

## Design rule

The parcel platform should present non-node support surfaces as product objects,
not as hidden metadata attached to parcel-state.

## First serious proof path

The first parcel-facing closed-loop proof should let an operator inspect:

1. current outdoor and parcel condition
2. indoor response condition
3. observed equipment posture
4. recorded household action
5. measured verification result

## Guardrails

- do not overread draft compatibility data as operational controls readiness
- do not hide verification and action records behind a generic timeline label
- do not make the bridge stage read like a weather-dashboard expansion only
