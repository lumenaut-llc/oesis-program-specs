# Phase Roadmap

## Purpose

Translate the long-term vision into staged execution from homeowner utility to block-level network effects to city-scale federation.

## Planning rules

- every phase must deliver standalone value
- network effects should improve the product, not unlock the entire product
- new phases should preserve homeowner ownership and private-by-default defaults
- claims should stay behind proven technical capability
- each phase should narrow the hardware, software, and governance surface enough to ship

## Phase 0: Foundation and truthfulness

### Goal

Establish the minimum architecture, language, and safety posture required for a credible resilience product.

### Outcomes

- canonical parcel-state model
- evidence-mode language
- confidence and freshness posture
- basic ingest, normalization, and reference inference pipeline
- privacy and consent baseline
- hazard-specific claim boundaries

### Must-have work

- finalize home, parcel, observation, and parcel-state data contracts
- document what current node classes can and cannot support
- align homeowner-facing language with claims-and-safety rules
- keep `unknown` and low-confidence outcomes honest
- define recommendation-language boundaries before shipping action prompts

### Exit criteria

- synthetic reference pipeline runs end to end
- example payloads validate
- core docs agree on terminology and claim posture
- MVP hazards are defined conservatively enough for pilots

## Phase 1: Home resilience assistant

### Goal

Ship a homeowner product that is useful with one home and no neighborhood participation.

### Primary jobs to be done

- tell me what is happening at my home right now
- tell me how serious it seems
- tell me why the system thinks that
- tell me what reasonable next steps to consider

### Initial hazard focus

- wildfire smoke and indoor air burden
- extreme heat and indoor heat burden
- flooding and runoff at the parcel edge or low point
- outage and shelter readiness

### Core user-facing features

- current readiness states
- confidence and freshness
- reasons and evidence summaries
- recommendation cards with conservative language
- event timeline and change detection
- alerting for meaningful worsening
- setup flow for parcel and home context

### Core technical capabilities

- one or more home sensors
- parcel and structure context capture
- hazard-specific rules with explicit observability limits
- safe alert thresholds
- local-plus-public context fusion
- homeowner-facing parcel view

### Non-goals

- dense neighborhood inference
- multi-home coordination
- city-scale outputs
- aggressive predictive claims

### Exit criteria

- a single participating home gets recurring value outside major disasters
- recommendation language is understandable and trustworthy
- alert volume is manageable
- users can explain why the system produced the current state

## Phase 2: Block intelligence

### Goal

Use nearby participation to materially improve local awareness, timeliness, and spatial resolution.

### Primary jobs to be done

- tell me whether nearby conditions are worsening before mine do
- tell me whether my home is an outlier or part of a block-level pattern
- show me what nearby streets or low points look worse
- help the block coordinate without exposing everyone’s raw data

### Core user-facing features

- shared block condition layer
- street-segment and microcell readiness summaries
- block trend direction and rate-of-change signals
- neighborhood anomaly detection
- participation-aware confidence uplift
- voluntary mutual-aid flags and check-in workflows later

### Core technical capabilities

- privacy-scoped neighborhood signal transformation
- neighbor-consensus and disagreement handling
- microcell or street-segment inference
- sensor-health and representativeness scoring
- outdoor-versus-indoor source weighting
- route and hotspot inference

### Candidate pilot scenarios

- smoke plume movement across several blocks
- repeated runoff trouble spots on one street
- nighttime urban heat pockets
- outage clusters during a storm

### Non-goals

- raw household telemetry exposure by default
- citywide institutional dashboards as the primary product
- exact disaster-front tracking claims

### Exit criteria

- block participation produces measurable improvement over single-home + public-only context
- privacy defaults remain intelligible and trusted
- users perceive clear added value from neighbor participation

## Phase 3: Neighborhood resilience network

### Goal

Federate many blocks into neighborhood-scale resilience intelligence and coordination.

### Primary jobs to be done

- show how conditions vary across several blocks
- identify recurring neighborhood stress patterns
- coordinate local adaptation and mutual aid
- support resilience hubs and trusted community spaces

### Core user-facing features

- neighborhood snapshots
- corridor and route condition views
- resilience-hub readiness overlays
- neighborhood trend history
- voluntary shared incident boards

### Core technical capabilities

- neighborhood aggregation logic
- governance controls for community operators
- escalation paths for shared alerts
- resilience-hub and shared-space participation models

### Example expansion targets

- schools
- churches
- libraries
- community centers
- apartment complexes

### Exit criteria

- multiple blocks can participate under a common governance model
- neighborhood insights are useful without becoming household surveillance

## Phase 4: Citizen-built smart city federation

### Goal

Allow neighborhoods to contribute consented aggregate intelligence into a city-scale civic layer without surrendering resident ownership.

### Primary jobs to be done

- show citywide resilience patterns from bottom-up signals
- support planning, adaptation, and infrastructure accountability
- share consented aggregate intelligence with institutions when communities approve

### Core user-facing features

- federated neighborhood summaries
- city-scale trend and burden maps
- infrastructure stress reports
- resident-owned evidence products for advocacy and planning

### Core technical capabilities

- cross-neighborhood federation
- common aggregation and privacy standards
- partner-facing exports and APIs
- auditability and governance reporting

### Non-goals

- institution-owned raw household data lakes
- replacing emergency management systems
- indiscriminate public disclosure of parcel-linked conditions

### Exit criteria

- city-scale aggregation remains community-trusted
- institutions can consume useful outputs without controlling household data

## Cross-phase enablers

These workstreams should advance continuously across phases:

- recommendation engine posture
- privacy and consent tooling
- sensor-health scoring
- observability and provenance
- calibration and deployment guidance
- shared terminology and claims discipline
- local-first and degraded-connectivity behavior
- partnership and governance models

## Suggested sequencing bets

### Highest-confidence first bets

- smoke and indoor air
- heat burden
- flooding and runoff
- outage readiness

### Strong second-wave bets

- freeze and winter storm
- windstorm exposure
- route readiness
- chronic environmental burden

### Longer-horizon bets

- landslide and debris flow
- multi-unit building intelligence
- resilience hubs
- community evidence and advocacy products
- city-scale federation

## Open questions

- Which phase-1 features create the strongest everyday retention?
- Which block-level signals are best shared as aggregates versus bounded raw values?
- What microcell resolution is technically defensible for each hazard?
- Which future phases require new hardware classes rather than new inference only?
