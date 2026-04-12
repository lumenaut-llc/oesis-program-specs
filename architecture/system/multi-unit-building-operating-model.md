# Multi-Unit Building Operating Model

## Purpose

Define how Open Environmental Sensing and Inference System should extend from
single-home deployments into apartments, condos, and other shared-building
environments.

## Why multi-unit matters

Many residents do not live in detached homes.
If the project only fits single-parcel parcel operators, it leaves out:

- renters
- apartment residents
- condo communities
- mixed-use buildings
- senior and assisted-living contexts later

Multi-unit environments also create distinctive resilience problems:

- shared HVAC effects
- floor-by-floor heat differences
- elevator dependence
- common-area outages
- hallway, stairwell, and egress constraints

## Core model

A multi-unit deployment should preserve the same principles as the single-home model:

- private by default
- useful to one household
- shared by choice
- honest about uncertainty

But it must add a building layer between the household and block.

## Building layers

### Unit layer

Private household conditions within a single apartment or condo.

Typical outputs:

- shelter readiness
- air quality readiness
- heat readiness
- outage readiness

### Building shared layer

Derived building-level intelligence based on common-area conditions, shared-system context, and optionally aggregated unit signals.

Typical outputs:

- building readiness summary
- elevator or access degradation
- corridor and common-area heat or smoke stress
- shared-system outage status

### Neighborhood layer

Building-safe contributions into the wider block or neighborhood shared layer.

## Key design questions

1. What belongs to the private unit view?
2. What can be shared safely at the building level?
3. What can leave the building boundary into neighborhood intelligence?
4. Who, if anyone, can act as a building operator?

## Unit-level use cases

- indoor air burden
- smoke intrusion
- heat and cold burden
- outage readiness
- elevator or access awareness for affected residents

## Building-level use cases

- shared-system failures
- hallway or stairwell smoke burden
- whole-building outage clustering
- uneven floor or wing conditions
- cooling-failure patterns

## Neighborhood contribution posture

A multi-unit building should not default to exposing unit-level conditions externally.

Preferred building-to-neighborhood contributions:

- building-level readiness summary
- route and access degradation signals
- aggregate or bounded shared conditions
- known uncertainty and coverage limitations

## Operator roles

Possible roles:

- resident participant
- building steward or operator
- neighborhood operator later

Any building operator role should have limited visibility and should not imply unrestricted access to private unit conditions by default.

## Special accessibility considerations

Multi-unit environments raise extra issues for:

- mobility-limited residents
- elevator dependence
- stairwell access during outages
- common-area air quality

These should be treated as first-class resilience concerns, not edge cases.

## Risks to avoid

- turning building participation into landlord surveillance
- exposing unit-level hardship to building management by default
- assuming common-area signals represent all units equally

## Open questions

- What is the right default boundary between unit, building, and neighborhood outputs?
- How should renter rights and landlord visibility be handled?
