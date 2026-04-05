# Product Requirements: Current v1 Home Resilience Assistant

## Purpose

Define the current `v1` homeowner product that delivers immediate value with one participating home and no neighborhood dependency.

## Product statement

The current `v1` product helps a homeowner understand current home and parcel conditions, why those conditions matter, and what actions to consider during environmental disruption.

## Primary product promise

Useful alone on day one.
More informative when public context is available.
Honest about uncertainty.
Not yet a full parcel adaptation or automation system.

## Version boundary

`current v1` is the parcel sensing and inference baseline.

It should prove:
- local sensing
- parcel-state inference
- confidence, freshness, and provenance
- private-by-default data handling
- partial-adoption usefulness

It should not yet claim:
- intervention verification as a product guarantee
- ranked retrofit optimization
- automation compatibility as a core UX promise
- autonomous protective house behavior

## Target user

Primary user:

- a homeowner or renter who wants home-specific resilience guidance during smoke, heat, flood, freeze, or outage conditions

Secondary users:

- caregivers
- highly weather-exposed households
- households with poor public-data fit due to microclimate or drainage variation

## Core jobs to be done

- tell me what is happening at my home right now
- tell me if the situation is getting worse
- tell me what the system is basing that on
- tell me what reasonable actions I should consider now
- help me prepare before conditions become severe

## In-scope hazards for current v1

- smoke and indoor air burden
- heat burden
- flooding and runoff where local sensing is available
- freeze and cold burden where supported
- outage and shelter readiness

## User-facing objects

### Readiness cards

The home screen should present a small set of readiness states:

- shelter readiness
- air quality readiness
- heat readiness
- flood readiness
- power readiness
- route readiness

Each state should include:

- current label
- confidence
- freshness
- short why-this-status explanation
- recommended next steps

### Event timeline

The user should be able to see:

- what changed
- when it changed
- whether the situation is improving, stable, or worsening

### Evidence view

The product should let the user inspect:

- local observations
- public context used
- missing evidence
- stale evidence

## Functional requirements

### FR1: Current parcel-state generation

The system shall generate current readiness states from:

- local sensor observations
- parcel and home context
- optional public context
- explicit freshness and confidence logic

### FR2: Conservative recommendation engine

The system shall provide homeowner-readable next-step recommendations tied to current state and evidence mode.

Recommendations should:

- be specific enough to be useful
- avoid pretending to be official emergency instructions
- degrade to generic preparedness language when evidence is weak

### FR3: Hazard-specific trend detection

The system shall identify when conditions are:

- worsening
- improving
- stable
- stale or unknown

### FR4: Alerting

The system shall notify the user when:

- a readiness state worsens materially
- confidence drops enough to affect interpretation
- a key sensor goes stale or unhealthy
- public context indicates newly elevated concern

### FR5: Sensor-health awareness

The system shall expose whether conclusions are limited by:

- sensor location
- stale readings
- connectivity loss
- read failures
- unsupported hazard observability

### FR6: Setup and context capture

The product shall capture enough home and parcel context to improve interpretation, such as:

- indoor, sheltered, or outdoor installation mode
- basic parcel characteristics
- relevant structure characteristics
- optional user-specified sensitivities or priorities later

### FR7: Honest stage boundary

The system shall not imply that later-stage adaptation features already exist in the current product.

Examples:
- recommendations may mention recirculation or filtration if available, but the product should not imply that HVAC state is already being monitored unless that data path actually exists
- the product may reference future support for intervention verification, but it should not present verification claims as current `v1` functionality

## Non-functional requirements

### NFR1: Truthfulness

The product shall prefer `unknown` or low-confidence outcomes instead of stronger but weakly supported claims.

### NFR2: Privacy

The product shall default to private household data handling and make any sharing decision explicit and reversible.

### NFR3: Explainability

Every major state shall be accompanied by enough explanation for a user to understand the result.

### NFR4: Graceful degradation

The product shall remain usable when:

- public context is unavailable
- sensors are partially stale
- connectivity is degraded

### NFR5: Low operational burden

The product shall avoid overwhelming the user with noisy alerts or complex setup steps.

### NFR6: Democratic and homeowner-controlled posture

The product shall preserve homeowner ownership, private-by-default handling, and voluntary participation so the network can grow without becoming a centralized household surveillance system.

## Candidate current-v1 recommendations

### Smoke and air

- close windows
- switch HVAC to recirculate if available
- run filtration
- move to the cleanest room
- delay outdoor activity
- ventilate only during a safer outdoor window

### Heat

- move activity to the coolest room
- pre-cool before forecast heat if possible
- close blinds or shade exposed rooms
- start backup cooling plan
- hydrate and reduce exertion

### Flood and runoff

- inspect drains and low points
- move vulnerable items
- avoid specific routes if route confidence is low
- prepare barriers or pumps if already owned

### Freeze

- protect exposed pipes
- maintain minimum indoor temperature
- drip pipes if appropriate for the user’s locale and setup

### Outage

- check backup power status
- reduce nonessential loads
- preserve device charging
- prepare shelter-in-place resources

## Current-v1 data requirements

- local sensor observations
- sensor health metadata
- parcel identifier and basic context
- home installation context
- public smoke and weather context where available
- event history for trend detection

## Minimum bridge after current v1

The next stage after this product is `v1.5`, not a jump directly to automation.

`v1.5` adds:
- indoor PM2.5
- indoor temperature and RH
- HVAC mode, fan state, and recirculation/fresh-air state
- purifier state
- backup-power state
- building and site metadata for orientation, shading, drainage, and filter-path constraints
- intervention and outcome logging
- control compatibility inventory

These additions should land as separate support objects instead of breaking the current parcel-state shape.

## Phase-1 success metrics

- a user can explain the current home state in plain language
- recommendation cards are opened and acted on during meaningful events
- alert precision is acceptable to pilot users
- users report value during both routine and elevated conditions
- the product remains useful even without neighbor participation

## Explicit non-goals

- neighborhood mutual-aid coordination
- raw shared block maps
- city dashboards
- exact wildfire-front or evacuation prediction
- medical diagnosis
- authoritative emergency command language
- bounded automation or device control
- verified adaptation-performance scoring
- parcel-specific retrofit ranking

## Risks and watchouts

- overclaiming on hazards the current hardware cannot directly observe
- confusing indoor microclimate readings with parcel-wide outdoor truth
- alert fatigue
- legal exposure from recommendation language
- weak setup information leading to misinterpretation

## Dependencies for later phases

- recommendation engine policy
- neighborhood signal transformation methods
- additional hardware classes for flood, wind, and other hazards
- block-level governance and sharing controls
- `v1.5` support objects for house state, capability, compatibility, intervention, and verification
