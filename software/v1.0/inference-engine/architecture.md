# Inference Engine Architecture v1.0

## Purpose

Describe the stronger target-lane inference role once OESIS moves from parcel
sensing into response measurement.

## Core stance

The inference engine should not evolve into "more hazard scoring plus more
weather inputs."

It should evolve into an engine that can reason across:

- outdoor hazard evidence
- indoor response evidence
- household operating state
- action records
- measured outcome windows

## Product consequence

The next important software shift is:

hazard -> house state -> action -> verified outcome

## Core objects

- normalized observation
- parcel context
- house-state support object
- equipment-state support object
- intervention event
- verification outcome
- parcel-state snapshot
- explanation payload

## Design rule

Keep the parcel-state contract stable where practical. Bridge-stage response
objects should sit beside parcel-state rather than being hidden inside it.

## First serious closed-loop target

Smoke protection should be the first serious end-to-end proof because it offers
a bounded, measurable loop:

- outdoor smoke evidence
- indoor PM / temperature / RH response
- recirculation / fan / purifier posture
- action timestamp
- indoor improvement over a defined response window

## Guardrails

- do not treat sparse indoor evidence as permission to overclaim certainty
- do not mix hazard certainty with intervention confidence
- do not add control logic before outcome verification exists
- do not treat support objects as optional extras once the product claims
  response measurement

## Stage split

- `v1.5`: house state, action, and verification become first-class support
  records
- `v2`: recommendation logic becomes stronger
- `v2.5`: compatibility mapping and bounded controls mature later
