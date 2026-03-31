# Route-Readiness Model Overview

## Purpose

Define the conceptual model for estimating whether local routes, exits, and nearby movement paths appear usable, degraded, or uncertain during disruptive conditions.

## Why route readiness matters

People do not only need to know whether their home is stressed.
They also need to know whether leaving, reentering, or moving nearby appears easier, harder, or more uncertain.

Route readiness is especially relevant for:

- smoke events
- flooding and runoff
- windstorm debris
- outage-related access problems
- heat exposure during travel
- winter icing

## Important boundary

Route readiness is not the same thing as authoritative route safety.

The system should present route readiness as:

- a local condition estimate
- a confidence-scoped decision-support signal

It should not casually imply:

- guaranteed passability
- official closure authority
- evacuation direction orders

## Core route questions

1. Does local evidence suggest that a nearby path is becoming harder to use?
2. Is there a nearby alternative that appears less degraded?
3. How sure is the system?
4. What evidence is missing?

## Route object model

### Route segment

A small local movement unit such as:

- one side of a street
- a driveway exit
- a short block corridor
- a sidewalk connection
- a local path to a neighborhood anchor

### Route readiness state

Suggested conceptual states:

- normal
- degraded
- strongly degraded
- unknown

These should later be aligned with the broader parcel-state vocabulary.

### Route evidence summary

The route layer should explain whether a route estimate is driven by:

- nearby smoke burden
- flood or runoff concerns
- wind or debris indications
- heat exposure
- public closures or incident context
- sparse or stale data

## Inputs

Potential inputs include:

- local parcel-state outputs
- neighborhood shared signals
- microcell trend summaries
- topography and drainage context
- public incident and closure context
- structure and access posture
- weather and wind context

## Hazard-specific route patterns

### Smoke

Useful route questions:

- which nearby path appears less smoke-burdened?
- is smoke worsening faster in one corridor?

Best route outputs:

- route smoke burden class
- relative route preference under uncertainty

### Flood and runoff

Useful route questions:

- which low points or curb segments appear to be collecting water?
- is the primary route degrading faster than an alternate?

Best route outputs:

- low-point warning
- likely runoff-obstructed segment
- uncertain route segment where direct evidence is missing

### Wind and debris

Useful route questions:

- which corridor appears most exposed?
- are tree-fall or obstruction signals increasing nearby?

### Heat

Useful route questions:

- which route is more exposed to dangerous heat load?
- are shaded alternatives available?

### Winter icing

Useful route questions:

- which route is likely to have the worst icing or refreeze risk?

## Model posture

### Relative over absolute

The first route model should often prefer relative statements such as:

- route A appears more degraded than route B

rather than strong absolute claims.

### Confidence-aware by design

Route states should degrade to `unknown` quickly when:

- evidence is stale
- coverage is sparse
- public context conflicts with local signals
- a hazard is poorly observed

### Multi-source synthesis

The route layer should fuse:

- private home context
- shared neighborhood context
- public context

without collapsing them into a false single certainty.

## User-facing outputs

The product should be able to show:

- primary local route readiness
- alternate route suggestion under uncertainty
- why the route appears degraded
- confidence and freshness
- prompt to review official information when relevant

## Example outputs

- "Primary street exit appears degraded by worsening runoff near the block low point."
- "The westbound walking corridor appears less smoke-burdened than the main road, but confidence is limited."
- "Route conditions are uncertain because local evidence is sparse and public context is changing."

## Major risks

- overclaiming route passability
- hiding uncertainty when coverage is weak
- producing false precision from sparse neighborhood data
- implying official route guidance authority

## Dependencies

- block-level operating model
- neighborhood signal transformation
- parcel and route context
- recommendation-engine language rules

## Open questions

- What is the minimum defensible route-segment granularity?
- Which route outputs should remain private versus shared?
- When should the product prefer not to compare routes at all because uncertainty is too high?
