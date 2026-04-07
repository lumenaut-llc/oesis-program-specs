# Sensor Placement and Representativeness Guide

## Purpose

Define how sensor placement affects truthfulness, confidence, and hazard observability so the product does not over-interpret poorly placed devices.

## Why placement matters

Most errors in a home resilience system will not come only from bad models.
They will also come from:

- sensors in the wrong place
- sensors in overly local micro-environments
- users assuming all sensors represent the whole parcel equally

Placement is therefore part of the inference system.

## Core principle

The product should never assume that a sensor is fully representative just because it is functioning.

Every placement should be interpreted along two dimensions:

- what it can observe well
- how representative it is of the home, parcel, or shared neighborhood layer

## Placement categories

### Indoor

Typical examples:

- bedroom
- living room
- office
- hallway

Strengths:

- good for indoor air burden
- good for indoor heat and cold burden
- useful for shelter readiness

Weaknesses:

- weak proxy for parcel-wide outdoor conditions
- weak for flood unless tied to specific intrusion detection
- weak for shared neighborhood intelligence by default

### Sheltered

Typical examples:

- covered porch
- garage-adjacent sheltered space
- breezeway
- eave-protected exterior wall

Strengths:

- can provide some local outdoor-like context
- often useful for transition conditions

Weaknesses:

- may be biased by walls, roofs, radiant surfaces, and enclosure effects
- should not be treated as fully outdoor truth

### Outdoor

Typical examples:

- open yard mount
- mast
- roofline with appropriate exposure
- dedicated low-point installation for flooding

Strengths:

- best candidate for parcel outdoor context
- most useful for shared block intelligence if siting is good

Weaknesses:

- can still be distorted by sun, walls, pavement, or direct runoff peculiarities
- requires better calibration and siting discipline

## Representativeness classes

The product should classify placement representativeness explicitly.

### Class A: Broadly representative for intended hazard

Example:

- well-sited outdoor air sensor for local smoke trend

### Class B: Partially representative

Example:

- sheltered porch sensor that gives useful but biased outdoor cues

### Class C: Highly localized

Example:

- indoor bedroom sensor near a window or vent

### Class D: Unsupported or misleading for the target interpretation

Example:

- indoor temperature sensor treated as parcel-wide outdoor heat truth

## Hazard-specific placement guidance

### Smoke and air

Best placements:

- dedicated outdoor air-quality sensing for parcel and shared context
- indoor sensing for shelter and indoor burden

Watchouts:

- indoor PM is not the same as outdoor smoke burden
- sheltered outdoor placement may lag or dampen plume behavior

### Heat

Best placements:

- indoor living-space measurements for shelter burden
- properly exposed outdoor measurements for parcel heat context

Watchouts:

- direct sun, attic heat, garage heat, and wall exposure can create false heat severity

### Flood and runoff

Best placements:

- documented low-point sensors
- known runoff pathways
- sump and intrusion sensors for home-specific conditions

Watchouts:

- one dry point on a parcel does not clear the whole parcel
- one wet point may reflect an intended drainage concentration rather than generalized flooding

### Freeze

Best placements:

- exposed pipe-adjacent or cold-zone sensors for freeze risk
- indoor living-space sensors for cold burden

Watchouts:

- central indoor readings can hide freeze-prone edge conditions

### Wind

Best placements:

- elevated outdoor siting with known exposure

Watchouts:

- yard fences, buildings, and tree cover can distort readings dramatically

## Day-one product posture

The phase-1 product should likely assume:

- indoor sensors are highly valuable for home readiness
- indoor sensors are weak for shared neighborhood hazard truth
- outdoor-capable shared intelligence requires more disciplined siting

## Setup requirements

The setup flow should capture at minimum:

- indoor, sheltered, or outdoor mode
- placement type
- approximate height class
- obvious nearby bias factors if known

Examples of bias factors:

- near window
- near HVAC vent
- near pavement
- under eave
- low-point drain area
- against sun-facing wall

## Product behavior implications

### Confidence

Confidence should degrade when:

- placement is weak for the target hazard
- placement is highly localized
- placement quality is unknown

### Recommendation scope

Recommendations should become more general when representativeness is weak.

### Shared-layer eligibility

Not every sensor should contribute equally to neighborhood intelligence.

Shared-layer participation should depend partly on:

- hazard fit
- placement quality
- freshness
- health

## Pilot guidance

During pilots, the team should document:

- where each sensor was placed
- what it was expected to represent
- what it actually appeared to represent during events

## Failure modes to avoid

- treating all connected sensors as equally trustworthy
- silently upgrading indoor readings into parcel truth
- letting poor siting create false neighborhood gradients

## Open questions

- Which placement fields most improve interpretive quality?
- When should the product ask a user to move a sensor rather than simply degrade confidence?
