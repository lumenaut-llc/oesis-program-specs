# `v1.5` house-state and verification model

**Canonical incorporation:** stage framing → [`../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`](../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md); capability roadmap → [`../system/phase-roadmap.md`](../system/phase-roadmap.md); object taxonomy → [`../system/node-taxonomy.md`](../system/node-taxonomy.md); hazard / functional / response split → [`../../program/operating-packet/functional-state-and-response-model.md`](../../program/operating-packet/functional-state-and-response-model.md).

## Purpose

Define the minimum bridge from parcel sensing into house-state, intervention,
and measured-outcome reasoning.

This is the stage where the product stops being only about:

- what is happening at the parcel

and starts being able to ask:

- what did the house do
- what operating state was the house in
- did that response actually help

## Core rule

Collect the minimum data needed to model the relationship between outdoor
hazards, house operating state, available interventions, and resulting
outcomes.

That is stronger than merely adding more local environmental sensing.
The point of `v1.5` is to build the minimum response model needed for parcel
adaptation later.

## Closed-loop shape

The minimum loop is:

`hazard -> house state -> action -> measured outcome`

Examples:

- outdoor smoke burden -> indoor PM2.5 / HVAC recirculate posture -> purifier run -> indoor PM2.5 improves over 45 minutes
- outdoor heat load -> indoor temperature / shading posture -> blinds closed + fan mode change -> indoor heat burden growth slows
- rainfall / runoff rise -> low-point accessibility and sump state -> drain clearing or pump activation -> standing water or access degradation stabilizes

## First-class `v1.5` surfaces

### `indoor-response-node`

Minimum measurements:

- indoor PM2.5
- indoor temperature
- indoor RH

Why it belongs this early:

Without indoor response, the system can describe outdoor hazard but cannot tell
whether the house is actually buffering occupants from that hazard.

### `power-outage-node`

Minimum measurements:

- mains status
- backup-power state

Richer battery, generator, and transfer posture can come later, but continuity
and outage readiness belong in the bridge stage because household function
during disruption is part of resilience, not an optional add-on.

### `equipment-state-adapter`

Minimum read-side signals where relevant:

- HVAC mode
- fan state
- recirculation versus fresh-air state
- purifier state
- window state
- shade state
- sump / drain equipment state

This is an observation surface, not yet a controls platform.
The point is to learn which operating surfaces exist at a parcel and what state
they were in when outcomes changed.

### `action-log`

Minimum fields:

- action type
- actor (`household`, `operator`, `system-suggested`, or similar)
- started at / ended at
- target surface
- reason or trigger

This records what was actually done in response to conditions.
Without it, the product cannot distinguish passive house behavior from active
intervention.

### `outcome-log` / response-verification surface

Minimum fields:

- before window
- after window
- target metric
- observed change
- verification assessment
- evidence-quality ceiling

This turns a recommendation or action into an evaluable event.
It is the first serious bridge from descriptive intelligence to parcel-specific
learning.

### Building-and-site metadata surface

Minimum metadata should include:

- orientation
- roof type or color
- shading condition
- tree canopy
- impervious area
- low points
- drainage paths
- vent locations
- filter path
- filter size
- higher-MERV support

These are not decorative context fields.
They shape whether an outdoor condition actually becomes indoor burden or parcel
stress.

## What `v1.5` is proving

`v1.5` proves that the product can model response, not just exposure.

It should start to answer questions like:

- how does outdoor PM translate to indoor PM in this house
- how does outdoor heat translate to indoor heat burden in this house
- what happens when HVAC switches to recirculate
- what happens when a purifier runs
- what happens to usability and access when water depth rises at a low point
- did a given action actually help or not

## Data discipline

### Keep parcel-state honest

The bridge should not silently overload the core parcel-state contract.
House-state, action, verification, node-health, and deployment-trust records
should remain separate support objects or extensions documented against parcel
state.

### Do not confuse response with certainty

Outcome language must inherit the quality ceiling of the underlying evidence.
An intervention can appear promising while still being low-confidence if the
measurement path is weak, stale, sparse, or poorly installed.

### Do not pretend automation exists

`v1.5` is not:

- a mature adaptation engine
- a full controls-compatibility inventory
- a general automation platform
- a guarantee of bounded control execution

Full compatibility mapping by interface class and bounded controls posture
belongs primarily in `v2.5`.

## Minimum parcel record set for one useful loop

One practical `v1.5` loop should have at least:

- hazard snapshot or hazard window
- house-state snapshot or short rolling house-state window
- building/site metadata sufficient to interpret the parcel
- observed equipment state where relevant
- action record
- before/after outcome window
- verification result with evidence-quality limit

## Exit criteria

The stage counts as successful when the system can capture the minimum
house-state and intervention surfaces needed for before/after reasoning.

At minimum, the product should be able to produce one honest closed loop of:

`hazard -> house state -> action -> measured outcome`

without pretending that all controls are automated or that the platform has
already become a mature adaptation engine.

## Recommended first closed loop

Smoke protection is the best first proof path:

- outdoor PM signal
- indoor PM response
- HVAC recirculation / fan / purifier posture
- action log
- bounded verification window for indoor PM improvement

This is narrow enough to ship honestly and strong enough to prove that the
product is learning from parcel-specific response.
