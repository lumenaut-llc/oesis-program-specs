# Proposed Architecture v1.0

## Purpose

Capture the target architecture shape once the project is ready to debate it in
more concrete terms.

## Status

Debate draft.

## Initial framing

`v1.0` should answer questions such as:

- what changes materially from the `v0.1` reference stack
- which architectural boundaries remain fixed
- which new subsystem responsibilities or contracts are required
- what operational, governance, and product surfaces must become first-class

## Proposed doctrine

The target architecture should remain parcel-first without becoming
parcel-bounded.

The parcel should stay the primary:

- decision object
- ownership and permission surface
- homeowner-facing explanation surface

But the system should reason across multiple scales underneath parcel
conclusions.

The target rule is:

- parcel-first for decisions
- sensor-first for direct observation
- field-aware for hazard reasoning
- route-aware for movement and access
- provenance-first for trust

## Multi-scale architecture stance

### Parcel

The parcel remains the main decision and ownership object.

### Sensor node

The sensor node remains the direct observation object, not the parcel truth
object.

### Shared neighborhood signal

Neighborhood-scale signals become a more explicit inference object rather than a
downstream extra.

### Route and infrastructure segment

Route and infrastructure context should become first-class operational objects
for escape, access, drainage, and utility-aware reasoning.

### Hazard field

Smoke, runoff, and heat should increasingly be modeled at their natural
operational scale before being reduced into parcel consequences.

### Derived parcel state

The parcel state remains the final product-facing answer, but should more
explicitly show how parcel, neighborhood, route, and public context contributed.

## Non-negotiable target rules

- do not treat parcel boundaries as physical hazard boundaries
- do not make inferred parcel outputs look identical to directly observed local
  results
- keep privacy parcel-first even when inference becomes more multi-scale
- preserve confidence, evidence mode, freshness, and explanation as required
  product outputs

## Implementation implications

Relative to `v0.1`, the target architecture implies:

- richer first-class context objects beyond the parcel itself
- stronger distinction between observation objects and decision objects
- more explicit neighborhood and route-aware reasoning surfaces
- stronger product treatment of inferred-neighbor and inferred-regional support
- clearer contracts for how shared and public evidence affect parcel outputs
