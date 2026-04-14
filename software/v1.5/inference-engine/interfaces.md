# Inference Engine Interfaces v1.5

## Purpose

Describe the bridge-stage inference inputs and outputs once response surfaces are
first-class support objects.

## Primary input groups

- normalized local observations
- parcel context
- public context
- optional shared neighborhood signals
- indoor-response observations
- power-state observations
- equipment-state snapshots
- action-log entries
- verification-outcome records

## Priority order for bridge inputs

The minimum next bridge inputs should be treated in this order:

1. indoor response observations
2. power and outage observations
3. equipment-state snapshots
4. action-log entries
5. verification-outcome records

That ordering reflects product importance, not only implementation convenience.

## Primary output groups

- parcel-state snapshot
- explanation payload
- response-window comparison outputs
- later recommendation outputs
- later verification summaries

## Contract rule

`parcel-state` remains the parcel-facing status contract.

Bridge-stage records should influence future reasoning without silently
expanding the meaning of parcel-state into a giant mixed object.

## First serious closed loop

Smoke should be the first serious end-to-end loop:

- outdoor evidence at trigger time
- indoor PM / temperature / RH response
- equipment-state posture
- bounded action record
- measured verification over roughly a 30 to 90 minute window

## Stage note

- `v1.5`: bridge inputs become first-class
- `v2`: recommendation outputs strengthen
- `v2.5`: full compatibility inventory and bounded control behavior mature later
