# Block-Level Operating Model

## Purpose

Define how Open Environmental Sensing and Inference System should behave once
multiple nearby households participate in a shared block-scale network.

## Why the block matters

The block is the first scale where network effects become visible to ordinary participants.

One home can understand itself.
Several nearby homes can understand:

- whether conditions are isolated or shared
- whether conditions are moving in a direction
- whether one street, low point, or corridor is degrading faster than another
- whether a public feed is missing a meaningful local difference

The block layer should create better local awareness without requiring households to expose raw telemetry by default.

## Core block-level outcomes

The block layer should help answer:

1. What seems to be changing around me nearby?
2. Is my home an outlier or part of a local pattern?
3. Which nearby segments look worse, better, or uncertain?
4. How much should I trust the block signal?
5. What, if anything, should the block consider doing together?

## Canonical block objects

### Participating home

A household that contributes some level of local sensing and receives private home-level outputs.

### Shared neighborhood signal

A privacy-scoped derived signal produced from one or more participating homes for limited shared use.

### Microcell

A small derived spatial unit, such as:

- one side of a block
- a low-point corridor
- a short street segment
- a courtyard cluster

Microcells should be chosen to reflect how conditions actually vary, not just arbitrary map tiles.

### Block condition summary

A derived overview that describes:

- dominant hazards
- trend direction
- confidence
- freshness
- known uncertainty

### Route segment

A directional local path element whose readiness can be estimated from nearby conditions.

## Design rules

### Private by default

Raw household data should remain private unless a participant explicitly chooses a more open mode.

### Shared intelligence first

The default block product should rely on:

- bounded summaries
- trend indicators
- confidence and freshness
- hotspot or low-point flags
- route segment states

not unrestricted household telemetry.

### Participation should improve but not dominate

The block layer should improve a household's interpretation, not replace private home-level reasoning.

### Confidence must reflect representativeness

A block signal should not be treated as strong simply because many signals exist.
It must also reflect:

- placement quality
- indoor versus outdoor suitability
- sensor health
- spatial coverage gaps
- agreement or disagreement between contributors

### Social design is part of the product

Block intelligence is not only a data problem.
It also requires:

- understandable sharing controls
- community trust
- mutual-aid norms
- clear boundaries on visibility

## Participation model

### Participation tiers

The system should support multiple participation tiers.

#### Tier 1: Private home only

- receives private home outputs
- contributes nothing to shared block intelligence

#### Tier 2: Derived block contribution

- shares bounded derived signals only
- participates in block condition and route intelligence

#### Tier 3: Expanded trusted-sharing mode

- shares richer but still scoped signals within explicit community rules
- suitable only for narrowly governed pilots or trusted groups

The default should be Tier 1 or Tier 2 depending on the product posture and consent design.

## Block-scale product surfaces

### Shared condition layer

A participant should be able to see a local shared layer that includes:

- block condition summary
- current dominant concerns
- likely worsening or improving direction
- hotspot and low-point markers
- route-segment readiness

### Neighbor agreement and disagreement

The product should distinguish:

- broad local agreement
- partial agreement
- isolated anomalies
- insufficient coverage

This is important because disagreement is often informative.

### Trend surface

The block layer should emphasize change over time:

- worsening
- improving
- stable
- mixed

### Confidence surface

Every block output should include:

- signal freshness
- participation density
- representativeness quality
- unresolved uncertainty

## Example block use cases

### Smoke plume movement

- one side of a block sees smoke rise first
- nearby homes indicate plume direction and timing
- route segments downgrade where smoke burden worsens

### Runoff and low-point flooding

- several parcels near the same low point show worsening water conditions
- one street segment becomes the obvious trouble spot
- a household uphill can see that its own parcel is still relatively better

### Night heat persistence

- shaded parcels cool earlier
- exposed parcels remain hot
- block trend shows a nighttime heat island pattern

### Outage clustering

- a few nearby homes lose power
- block summary shows localized utility degradation
- households can distinguish isolated home failure from block-level outage

## Operating logic

### Step 1: Validate local sources

Before any block inference, the system should assess:

- source freshness
- sensor health
- installation mode
- hazard observability fit

### Step 2: Convert local outputs into shared neighborhood signals

Contributors should produce bounded derived signals suitable for shared use.

### Step 3: Group signals into microcells and route segments

Signals should be associated with spatial units that reflect likely condition variation.

### Step 4: Compute block summaries

The system should derive:

- dominant hazard state
- trend direction
- hotspot or low-point flags
- route readiness
- confidence and unresolved uncertainty

### Step 5: Return private plus shared views

Participants should see:

- their private home state
- the shared block layer
- explanations of where those differ

## Governance requirements

### Minimum governance concepts

- who can contribute
- what is shared
- who can see what
- how to revoke sharing
- how long shared signals persist
- who can act as a community operator, if anyone

### Community operator role

Later pilots may allow a trusted community operator to:

- monitor block-level health
- coordinate mutual aid
- review incident summaries

This role should never imply unrestricted household access by default.

## Success metrics

- participants report that nearby participation improves local understanding
- block outputs reveal meaningful local differences that public feeds miss
- privacy controls are understandable
- disagreement and uncertainty are visible rather than hidden
- participants do not feel surveilled

## Failure modes to avoid

- exposing raw household telemetry as the default block product
- overstating confidence from dense but low-quality signals
- pretending every parcel on a block behaves the same
- encouraging social pressure to overshare
- turning the block layer into a generalized neighborhood surveillance tool

## Dependencies

- neighborhood signal transformation methods
- route readiness modeling
- privacy and consent controls
- community governance patterns
- recommendation-engine boundaries for shared alerts
