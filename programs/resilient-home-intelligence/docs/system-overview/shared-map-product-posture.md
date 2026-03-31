# Shared Map Product Posture

## Purpose

Define what the shared map is for, what it should and should not show, and how it should differ from both private home views and generic public hazard maps.

## Core idea

The shared map is not the whole product.
It is one surface for neighborhood intelligence.

Its job is to help participants understand shared local conditions and trends without collapsing the project into:

- a generic map dashboard
- a public parcel-level exposure tool
- a surveillance interface

## Primary role of the shared map

The shared map should help a participant answer:

- what nearby conditions appear worse or better
- which local corridors, low points, or microzones look stressed
- where conditions are changing fastest
- how much local agreement or uncertainty exists

## What the shared map is not

It is not primarily:

- a replacement for the private home view
- a parcel-by-parcel public risk display
- a platform for inspecting individual households
- an official emergency management map

## Design posture

### Derived over raw

The shared map should prioritize:

- summaries
- trends
- confidence
- route segments
- hotspot or low-point indicators

over raw household measurements.

### Microzones over exact households

Where possible, the map should show:

- street segments
- low points
- corridor conditions
- microcell summaries

instead of household-identified sensor points.

### Uncertainty should be visible

Map surfaces should explicitly show:

- insufficient coverage
- mixed signals
- stale areas
- low-confidence areas

### Change matters more than static color

The shared map should emphasize:

- worsening
- improving
- stable
- mixed

not only static hazard coloring.

## Candidate shared-map layers

### Block condition layer

- dominant concern by microzone
- trend direction
- confidence class

### Route-readiness layer

- degraded segments
- uncertain segments
- relative route preference under uncertainty

### Low-point and hotspot layer

- runoff trouble spots
- persistent heat pockets
- smoke burden corridors

### Network-health layer

- coverage density
- stale areas
- low-representativeness areas

This layer may be more suitable for advanced or operator views.

## Audience variants

### Participant view

Should show:

- nearby shared conditions
- route and trend intelligence
- confidence and freshness

Should not default to:

- inspecting other households

### Operator view

May additionally show:

- aggregate participation health
- map-health and coverage issues
- incident summaries

Still should not default to:

- unrestricted raw household browsing

### Public or partner view later

If a public or institution-facing map exists later, it should be:

- more aggregated
- more delayed where needed
- more explicitly governed

## Privacy and safety constraints

The shared map should avoid default behaviors that:

- reveal exact parcel-linked private conditions
- expose vulnerable households
- encourage emergency overconfidence from sparse data
- convert resilience infrastructure into neighborhood surveillance

## Good map questions

- Which nearby segment seems most degraded?
- Where is the block most uncertain?
- Is a low-point trouble spot recurring?
- Does the shared map disagree with the public regional picture?

## Bad map questions

- Which house is causing this signal?
- Which neighbor is in the worst condition?
- Exactly which household has the strongest indoor burden?

## Product success criteria

- participants understand how the map differs from their private home view
- the map reveals local patterns that public feeds miss
- the map does not feel invasive
- uncertainty and sparse coverage are easy to read

## Open questions

- Which layers belong in the default participant map versus advanced views?
- What is the right balance between simplicity and richness for stressful events?
- Should some hazards avoid map-first presentation altogether and remain card-first?
