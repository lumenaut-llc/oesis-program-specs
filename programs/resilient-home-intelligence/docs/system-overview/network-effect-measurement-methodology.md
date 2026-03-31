# Network-Effect Measurement Methodology

## Purpose

Define how to evaluate whether nearby participation actually improves the product in measurable ways.

## Why this matters

The project's long-term thesis depends on a real claim:

more participating homes should create better local intelligence than a single home plus public context alone.

That claim should be measured, not assumed.

## Core network-effect question

For a given hazard and area, does adding nearby participants improve:

- timeliness
- local resolution
- confidence
- usefulness
- action relevance

without unacceptable privacy or trust costs?

## Comparison modes

The methodology should compare at least these modes:

### Mode A: Home only

- local home observations
- no public context
- no neighborhood inputs

### Mode B: Home plus public

- local home observations
- public context
- no neighborhood inputs

### Mode C: Home plus public plus neighborhood

- local home observations
- public context
- privacy-scoped neighborhood signals

The key question is whether Mode C is materially better than Mode B.

## Improvement categories

### 1. Earlier awareness

Does the shared layer reveal meaningful local worsening before the private home view or public context alone would?

Possible measures:

- minutes to first useful local warning
- time between nearby degradation and private parcel degradation

### 2. Better local discrimination

Does the shared layer help distinguish:

- one side of a block from another
- uphill from low-point conditions
- one corridor from another

Possible measures:

- number of meaningful local differences surfaced
- user-rated value of local differentiation

### 3. Better route interpretation

Does nearby participation help identify:

- degraded segments
- more viable alternatives
- growing uncertainty in specific corridors

### 4. Better confidence calibration

Does nearby participation appropriately increase confidence when signals agree and decrease confidence when they conflict?

Possible measures:

- confidence changes with participation density
- user comprehension of why confidence changed

### 5. Better recommendations

Do shared signals make recommendation cards:

- more timely
- more specific
- more believable

## Candidate quantitative measures

- time-to-awareness improvement
- number of block-level anomaly detections
- number of route-state changes attributable to shared inputs
- confidence uplift with justified agreement
- disagreement detection rate
- coverage density by microzone

## Candidate qualitative measures

- user-reported "this told me something public feeds did not"
- user-reported earlier preparation because nearby conditions worsened first
- user-reported understanding of why block participation mattered

## Hazard-specific examples

### Smoke

Potential network-effect measures:

- earlier notice that nearby smoke is worsening before the private parcel worsens
- better corridor-level plume direction interpretation

### Flood and runoff

Potential network-effect measures:

- better identification of the real low-point trouble segment
- clearer distinction between isolated parcel wetness and shared street-level problem

### Heat

Potential network-effect measures:

- better nighttime heat-persistence mapping
- clearer differentiation between exposed and shaded microzones

### Outage

Potential network-effect measures:

- earlier recognition that a failure is block-level rather than home-specific

## Experimental patterns

### Sequential activation

Start with private home views, then enable shared block intelligence and compare changes.

### Parallel cohorts

Some participants receive shared block intelligence while others remain home-plus-public only.

### Retrospective replay

Use historical event data and simulate outputs with and without neighborhood inputs.

## Important caveats

- more data is not always better if the added data is poorly placed or weakly representative
- a real network effect should improve local interpretation, not merely add map complexity
- privacy and governance costs must be counted alongside technical gains

## Success standard

A meaningful network effect likely exists when:

- participants consistently report better local understanding from shared inputs
- logs show earlier or more locally differentiated awareness in real events
- the shared layer improves confidence in the right cases without masking uncertainty
- the privacy burden remains acceptable

## Failure standard

The network-effect hypothesis is weak if:

- shared inputs rarely change interpretation meaningfully
- users cannot tell why nearby participation matters
- added block intelligence mostly duplicates public feeds
- trust drops faster than usefulness rises

## Open questions

- What minimum participant density is needed before each hazard shows measurable lift?
- Which hazards show the strongest network effect earliest?
- What is the right shared-signal granularity to maximize usefulness without oversharing?
