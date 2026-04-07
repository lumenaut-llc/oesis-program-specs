# Neighborhood Signal Transformation Overview

## Purpose

Describe the high-level method for turning private home-level observations and parcel states into privacy-scoped neighborhood intelligence.

This document is intentionally architectural and non-enabling.
It exists to clarify product direction and design rules, not to publish detailed algorithms, thresholds, or implementation values.

## Problem

A block or neighborhood can become much more informative than a single parcel, but raw household telemetry should not be treated as the default shared product.

The project therefore needs a transformation layer that:

- preserves immediate value for a participating home
- creates useful shared neighborhood intelligence
- limits unnecessary exposure of parcel-linked household data
- makes uncertainty explicit

## Inputs

The transformation layer may draw from:

- private parcel-state outputs
- bounded hazard-support signals
- sensor-health summaries
- public context
- route and topology context
- optional community-defined sharing rules

It should not assume that all raw household observations are shareable.

## Outputs

The transformation layer should produce neighborhood-safe derived objects such as:

- shared neighborhood signals
- block condition summaries
- microcell trend summaries
- route-segment readiness states
- hotspot or low-point markers
- neighborhood confidence summaries

## Design goals

### Preserve household control

Households should remain the primary owners of raw local observations.

### Share only what the block needs

The default transformation should favor:

- category labels
- trends
- bounded ranges
- confidence classes
- freshness classes

over precise parcel-linked telemetry.

### Avoid false precision

Shared outputs should not imply more local certainty than the inputs justify.

### Make disagreement visible

Mixed or conflicting neighborhood signals should remain visible in the resulting shared layer.

## Conceptual transformation stages

### 1. Local qualification

The system first determines whether a local source is fit to influence a shared layer for a given hazard.

Examples of qualifiers:

- indoor versus outdoor suitability
- source freshness
- sensor-health status
- hazard observability fit
- installation quality

### 2. Shared-signal extraction

The system converts a private parcel state or local signal into a bounded shared object.

Examples:

- not "house at 123 Main has PM2.5 of X"
- but "shared signal suggests worsening smoke burden in this microzone"

### 3. Spatial grouping

Signals are associated with nearby microcells, low points, corridors, or route segments.

These groupings should reflect likely real-world variation patterns, such as:

- drainage pathways
- street canyons
- slope
- prevailing wind corridors
- parcel adjacency

### 4. Neighborhood synthesis

Grouped signals are combined into shared neighborhood outputs such as:

- worsening
- improving
- hotspot
- mixed
- insufficient coverage

### 5. Confidence and uncertainty annotation

The system annotates each shared output with:

- freshness
- signal density
- representativeness
- known blind spots
- disagreement level

### 6. Audience-specific delivery

Different users may receive different versions of shared outputs:

- a private household participant
- a block member
- a neighborhood operator
- a public or institution-facing aggregate view later

## Hazard-specific transformation patterns

### Smoke

Best shared forms:

- directional worsening
- microcell burden class
- route smoke burden
- trend change

Avoid by default:

- exact parcel-linked sensor exposure

### Flood and runoff

Best shared forms:

- low-point trouble markers
- street-segment passability concerns
- worsening runoff classes

Avoid by default:

- parcel-specific raw water readings tied to a household identity

### Heat

Best shared forms:

- block heat-persistence trend
- nighttime recovery weakness
- shaded versus exposed microzone pattern

Avoid by default:

- private indoor readings exposed as neighborhood truth

### Outage and shelter stress

Best shared forms:

- localized utility degradation
- shelter readiness stress clusters
- route and access degradation

Avoid by default:

- detailed household occupancy or private hardship exposure

## Privacy posture

The transformation layer should default to:

- derived signals before raw values
- coarse spatial grouping before parcel identification
- revocable sharing
- bounded visibility windows
- explicit participant understanding of what is contributed

## Product implications

The project should treat this transformation layer as a first-class product capability, not just a backend detail.

Why it matters:

- it creates the neighborhood moat
- it determines whether block intelligence feels helpful or invasive
- it shapes trust more than many visible UI features

## What this document intentionally does not specify

To stay within current release and legal boundaries, this document does not specify:

- exact transformation formulas
- thresholds
- weighting rules
- aggregation minima
- timing and batching logic
- conflict-resolution details

Those details belong in later internal design and legal-review materials.

## Evaluation questions

- Does the shared output help block members make better local sense of conditions?
- Would a participant be surprised by what was shared?
- Does the shared layer reveal disagreement and blind spots?
- Is the shared signal more useful than a public-only map?
- Does the product still work when only a few homes contribute?
