# Household Recommendation Catalog

## Purpose

Collect the main categories of household recommendations the product may issue, grouped by hazard and readiness scenario.

## Why this matters

A resilience product becomes real when it can turn sensed conditions into useful household actions.

This catalog is not a final rules engine.
It is a design inventory for:

- product scope
- UI planning
- recommendation-language discipline
- future policy review

## Recommendation categories

### Smoke and indoor air

Candidate recommendations:

- close windows
- switch HVAC to recirculate if available
- run air filtration
- move to the cleanest room
- reduce outdoor activity
- ventilate only during a safer outdoor window
- review replacement-filter readiness

### Heat

Candidate recommendations:

- move activity to the coolest room
- close blinds or shades in exposed rooms
- pre-cool before forecast heat where possible
- reduce exertion
- hydrate and monitor sensitive household members
- prepare backup cooling if available

### Flood and runoff

Candidate recommendations:

- inspect drains and known low points if safe
- move vulnerable items away from water-prone areas
- review alternate local routes
- prepare existing barriers or pumps
- avoid entering water-affected areas

### Freeze and winter storm

Candidate recommendations:

- protect exposed pipes
- maintain minimum indoor temperature
- prepare cold-weather supplies
- reduce unnecessary travel if route readiness worsens

### Outage and utility stress

Candidate recommendations:

- check backup power status
- preserve battery and device charge
- reduce nonessential electrical loads
- prepare for communications disruption
- review food, water, and medication readiness

### Shelter and habitability

Candidate recommendations:

- remain in the current room or move to a better room
- protect indoor air
- protect thermal comfort
- prepare an alternate shelter option
- review local official information

### Route and access

Candidate recommendations:

- avoid the most degraded nearby segment
- consider a less burdened alternative route
- review official closures or alerts
- delay movement if conditions are uncertain and worsening

## Recommendation metadata

Each recommendation should later have:

- hazard category
- triggering conditions
- minimum confidence posture
- evidence mode constraints
- allowed language tier
- contraindications or caveats

## Design rules

- recommendations should stay practical and household-appropriate
- recommendations should degrade gracefully under weak evidence
- recommendations should not imply authority the system does not have
- recommendations should reflect available household context where known

## Open questions

- Which recommendations create the most value in ordinary use, not only crisis use?
- Which recommendations require extra home-context fields before they can be shown well?
