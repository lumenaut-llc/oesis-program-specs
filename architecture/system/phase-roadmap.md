# Phase Roadmap

## Lane

This document is the `system/` lane version of this topic.

Use it for cross-version stage framing, program execution sequencing, and the
relationship between capability stages and deployment maturity.

If you need the debated target-lane roadmap wording, use
`../v1.0/phase-roadmap.md`.

## Purpose

Translate the long-term vision into staged execution from the current parcel-sensing baseline to a more serious parcel-first adaptation system.

## Planning rules

- every phase must deliver standalone value
- network effects should improve the product, not unlock the entire product
- new phases should preserve parcel stewardship and private-by-default defaults
- new phases should preserve decentralized and democratic governance aims rather than drifting into household surveillance
- claims should stay behind proven technical capability
- each phase should narrow the hardware, software, and governance surface enough to ship
- keep control permission separate from data-sharing permission

## Canonical version map

- `current v1` = Stage A = parcel sensing and inference
- `v1.5` = Stage B = measurement-to-intervention foundation
- `v2` = Stage C = bounded adaptation guidance
- `v2.5` = Stage D = bounded controls and compatibility mapping
- `v3` = Stage E = parcel adaptation engine
- `v4` = Stage F = parcel + route + block resilience

Use `architecture-gaps-by-stage.md` as the companion document for deciding which
missing operational surfaces belong in capability stages and deployment maturity,
without confusing those axes with public release labels such as `v0.1`.

For **promotion discipline** (current truth vs next promotion vs later stages) and the **node taxonomy**, use:

- `version-and-promotion-matrix.md`
- `node-taxonomy.md`

## Deployment maturity overlay

The program also uses a separate deployment maturity ladder.
It should be read as a hardware and operational overlay, not as a renumbering of the capability stages above.

- `deployment maturity v0.1`
  bench prototype and first bring-up
- `deployment maturity v1.0`
  first field-hardened parcel kit
- `deployment maturity v1.5`
  trust, calibration, maintenance, and device-operations hardening
- `deployment maturity v2.0`
  decision-policy and adaptation support on top of a hardened evidence path

This means a node family can be architecturally in scope for `current v1` while still being only `deployment maturity v0.1` or an early `deployment maturity v1.0` target.

## Stage A — Current v1 baseline

### Goal

Establish a credible parcel-first sensing and inference product that is useful with one home, honest under sparse evidence, and compatible with partial adoption.

### Outcomes

- canonical parcel-state model and evidence-mode language
- basic ingest, normalization, and reference inference pipeline
- confidence, freshness, and explanation posture
- privacy, consent, export, and revocation baseline
- hazard-specific claim boundaries for smoke, pluvial flooding/runoff, and heat
- explicit distinction between bench-grade hardware and the first field-hardened parcel kit

### Must-have work

- finalize home, parcel, observation, and parcel-state data contracts
- document what current node classes can and cannot support
- document the shared field-hardening bundle required before any node is called deployed or field-ready
- align dwelling-facing language with claims-and-safety rules
- keep `unknown` and low-confidence outcomes honest
- define recommendation-language boundaries before shipping action prompts
- preserve the current parcel-state contract through this stage

### Exit criteria

- synthetic reference pipeline runs end to end
- example payloads validate
- core docs agree on terminology and claim posture
- current `v1` is clearly framed as parcel sensing and inference, not full parcel adaptation or automation
- the repo can say which hardware lanes are `deployment maturity v0.1`, early `deployment maturity v1.0`, or still below a deployable threshold

## Stage B — v1.5 measurement-to-intervention foundation

### Goal

Add the minimum new data needed so the platform can evolve from parcel sensing into parcel adaptation without pretending that the adaptation engine already exists.

### Core rule

Collect the minimum data needed to model the relationship between outdoor hazards, house operating state, available interventions, and resulting outcomes.

### Key additions

- `indoor-response-node` for indoor PM2.5, indoor temperature, and indoor RH
- `power-outage-node` for mains status and backup-power state
- `equipment-state-adapter` for HVAC mode, fan state, recirculation/fresh-air state, purifier state, window or shade state where relevant, and sump/drain equipment state where relevant
- building and site metadata such as orientation, roof type or color, shading, tree canopy, impervious area, low points, drainage paths, vent locations, filter path, filter size, and higher-MERV support
- intervention and response records such as `action-log`, `outcome-log`, and before/after response windows
- **read-side** equipment-state and coarse capability hints (what exists / what is observed), without requiring a full **controls-compatibility inventory** — that inventory (interface classes, integration tiers, policy versioning) is primarily **Stage D / `v2.5`**

### Design rule

Keep parcel-state mostly stable in this stage.
Store the new `v1.5` data in separate support objects rather than overloading the current state contract.

### Core success test

Can the platform begin measuring response curves such as outdoor PM versus indoor PM, outdoor heat versus indoor heat response, rainfall versus low-point/access degradation, and action timestamp versus improvement?

### What this stage proves

This stage proves that the product can model response, not just exposure.

It should start to answer:

- how outdoor PM translates to indoor PM in this house
- how outdoor heat translates to indoor heat burden in this house
- what happens when HVAC switches to recirculate
- what happens when a purifier runs
- what happens to usability and access when water depth rises at a low point
- whether a given action actually helped

### Exit criteria

The minimum bar is one honest closed-loop chain of:

`hazard -> house state -> action -> measured outcome`

with evidence-quality limits carried into the outcome interpretation and without implying that all controls are automated.

## Stage C — v2 bounded adaptation guidance

### Goal

Turn parcel sensing plus `v1.5` support data into serious engineering guidance without implying autonomous control.

### Core capabilities

- condition model
- building response model
- intervention model
- operational recommendations
- material implementation recommendations
- ranked intervention reasoning based on effect size, cost, reversibility, time to implement, confidence, and multi-hazard benefit

### Exit criteria

- the platform can recommend which bounded action is most likely to help a parcel and explain why
- recommendation outputs remain clearly separate from hazard certainty
- the product is still advisory-first

## Stage D — v2.5 bounded controls and compatibility mapping

### Goal

Prepare the system to interact with real homes through bounded, low-risk control surfaces and compatibility mapping.

### Core capabilities

- controls inventory per parcel
- compatibility surfaces for local API, Matter, Home Assistant, cloud-only, BACnet, or none
- local-controller availability and override rules
- three-tier integration model:
  - advisory only
  - soft integration
  - harder building integration later

### First automation targets

- HVAC recirculation during smoke
- continuous fan mode during smoke
- purifier activation
- smart shade lowering during high solar load
- runoff threshold crossing alerts or bounded relay flows later

### Exit criteria

- every first automation target is reversible, bounded, low-risk, and verifiable
- failed-control logging and manual override are first-class behaviors

## Stage E — v3 parcel adaptation engine

### Goal

Move from current-state guidance into a real parcel adaptation engine.

### Core capabilities

- time-to-threshold outputs
- compound hazard logic
- action-effect memory
- household capacity modeling
- repeated-event learning for outdoor-to-indoor response, intervention effectiveness, and parcel-specific degradation/recovery

## Stage F — v4 parcel + route + block resilience

### Goal

Extend beyond the house to route, egress, and shared neighborhood infrastructure resilience while preserving private-by-default household data handling.

### Core capabilities

- parcel layer
- route and egress layer
- block and neighborhood weak-point layer
- community intervention ranking
- shared infrastructure and refuge planning surfaces

## Cross-phase enablers

These workstreams should advance continuously across phases:

- deployment maturity and field-hardening discipline
- recommendation engine posture
- privacy and consent tooling
- sensor-health scoring
- observability and provenance
- calibration and deployment guidance
- shared terminology and claims discipline
- local-first and degraded-connectivity behavior
- partnership and governance models
- house-state and response-curve quality
- parcel operator override and bounded control governance

## Suggested sequencing bets

### Highest-confidence first bets

- smoke and indoor air
- heat burden
- flooding and runoff
- outage readiness
- smoke protection as the first closed loop

### Strong second-wave bets

- freeze and winter storm
- windstorm exposure
- route readiness
- chronic environmental burden

### Longer-horizon bets

- community investment ranking
- resilience hubs
- community evidence and advocacy products
- broader federation layers
