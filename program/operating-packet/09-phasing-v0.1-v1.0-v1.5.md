# Phasing: v0.1, v1.0, v1.5

**Canonical incorporation:** Phase summary → [`program/v0.1/README.md`](../README.md); milestones ↔ phases → [`architecture/current/milestone-roadmap.md`](../../architecture/current/milestone-roadmap.md); reading order → [`architecture/current/README.md`](../../architecture/current/README.md). This file keeps the detailed phasing narrative.

## Why the phasing matters

The ambition in the project is survivable when the phase boundaries are defended.

The core risk is not ambition by itself. The real risk is letting the future architecture lane leak into the executable lane.

**Runtime vs program vocabulary** (including why this repo does not use a `v0.2` lane name): see [`00-version-labels-and-lanes.md`](00-version-labels-and-lanes.md).

This means the project should always distinguish between:
- the narrow reference slice
- the first broader fielded parcel-intelligence lane
- the measurement-to-intervention bridge

## `v0.1` — narrow executable reference slice

### Core goal

One parcel, one bench-air lineage, one ingest path, one inference path, one parcel view.

### What belongs here

- valid packet capture
- temporal integrity basics
- packet normalization
- parcel binding
- parcel-state generation
- confidence + evidence mode
- provenance summary
- private-by-default visibility
- minimal export/logging surfaces where already partially real

### Objects

- parcel
- node packet
- normalized observation
- parcel context
- parcel priors
- local evidence
- external public context
- parcel state
- parcel view
- evidence summary
- minimum sharing boundary

### What does not belong here

- full route engine
- block or neighborhood weak-point logic
- flood observation family as a core lane
- weather + PM as a core lane
- thermal scene as a core lane
- recommendation engine beyond reason strings
- full end-user governance UX
- intervention logic
- functional recovery modeling

### Success question

Can we honestly produce a parcel view from one observation path?

### Required deployment posture

- **Deployment-maturity tier:** `v0.1` (bench prototype) per [`../../architecture/system/deployment-maturity-ladder.md`](../../architecture/system/deployment-maturity-ladder.md).
- **Deployment class set:** indoor only.
- **Power tier:** USB.
- **IP tier:** none / IP20.
- **Transport tier:** serial-only (v0.1 floor per gap register G3).
- **Calibration rigor:** provisional per [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §G at the `v0.1` tier; characterized references not required; readings not admissible to calibration dataset.

## `v1.0` — first broader fielded parcel-intelligence lane

### Core goal

Move from a narrow reference slice to a real parcel kit and a more trustworthy parcel state without pretending to be a full adaptation system.

### Why this phase

Program milestones already describe the next hardware step as **indoor plus sheltered outdoor** (bench-air plus mast-lite), while **deferring** flood as default, heavy multi-node requirements, and fully mature governance enforcement. The public **open-release v1.0** packet also treats trend/history, evidence view, setup, and privacy/governance surfaces as **partial** rather than fully shipped. **`v1.0` in this packet** is the right place to **widen the parcel product**—trust, history, limited shared signal, clearer functional translation—**without** jumping ahead to adaptation, full route engines, or complete revocation product behavior.

### What gets added

- mast-lite as first sheltered outdoor reference node
- stronger node registry use
- installation metadata as required input
- deployment-quality flags
- trust penalties tied to freshness, health, and install quality
- append-only observation/state history
- parcel state with stronger functional translation
- limited neighborhood/shared signal ingestion
- user-facing evidence view
- basic sharing settings UI
- basic export and access visibility
- route/access as parcel-adjacent context, not full route logic

### What still stays out

- bounded controls
- intervention ranking
- house-state response curves
- full route/block resilience engine
- public parcel-resolution map
- full revocation guarantees
- flood as a central default lane
- thermal as a general-purpose lane

### Success question

Can we produce a more trustworthy parcel state from a real parcel kit and limited shared evidence?

### Required deployment posture

- **Deployment-maturity tier:** `v1.0` (first fielded kit) per [`../../architecture/system/deployment-maturity-ladder.md`](../../architecture/system/deployment-maturity-ladder.md). Promotion bar item 5 in [`../../architecture/current/pre-1.0-version-progression.md`](../../architecture/current/pre-1.0-version-progression.md) requires calibration-program §G compliance at this tier for every shipped node family.
- **Deployment class set:** indoor + sheltered (adds `mast-lite`); outdoor class enters through flood-node (`v0.3`) and later weather-pm-mast.
- **Power tier:** USB for indoor; 12V-DC or USB routed from indoor for sheltered; battery+solar or hardened mains for outdoor.
- **IP tier:** IP20 indoor / IP44 sheltered / IP65 outdoor.
- **Transport tier:** serial as floor; Wi-Fi permitted for sheltered and outdoor; LoRa / cellular permitted for outdoor beyond Wi-Fi reach. All transports preserve the `oesis.bench-air.v1` lineage; transport choice does not alter schema.
- **Protective fixtures:** radiation shield required for any outdoor temperature reading (mast-lite, weather-pm-mast); rigid mount + zero reference + staff gauge for flood-node. Pre-verification readings excluded from calibration dataset per calibration-program §C.
- **Calibration rigor:** characterized reference instruments populated per measurand per deployment class (gap G13); burn-in gate enforced for BME680-bearing nodes (gap G14); §F build-spec metadata block present for every node family (gap G16 for bench-air, G12 for mast-lite).

## `v1.5` — measurement-to-intervention bridge (capability stage, not a promoted runnable slice)

This is a **capability stage** in the `version-and-promotion-matrix.md` sense,
not a separately promoted program phase like `v0.1` or `v0.2`. It describes a
class of product behavior (house-state, intervention, verification) that may be
delivered within program-phase `v1.0` or later, depending on promotion timing.

### Core goal

Prevent the system from dead-ending into a parcel-status dashboard by adding the minimum extra surfaces needed to model the relationship between outdoor hazards, house operating state, interventions, and measured outcomes.

### Core rule

Collect the minimum data needed to model the relationship between outdoor hazards, house operating state, available interventions, and resulting outcomes.

### Why this phase

The source bundle is explicit that **`v1.5`** is the first minimum bridge into **house-state, intervention, controllability, and verification** data, and that **node health**, **deployment metadata**, and **device event history** should become **separate support surfaces** here rather than overloading or silently changing the **core parcel-state contract**. See [`functional-state-and-response-model.md`](functional-state-and-response-model.md).

### What gets added

#### House-state and bridge surfaces
- `indoor-response-node` for indoor PM2.5, indoor temperature, and indoor RH
- `power-outage-node` for mains status and backup-power state
- `equipment-state-adapter` for HVAC mode, fan state, recirculation versus fresh-air state, purifier state, and window/shade or sump/drain equipment state where relevant
- building-and-site metadata surface for orientation, roof type or color, shading condition, tree canopy, impervious area, low points, drainage paths, vent locations, filter path, filter size, and higher-MERV support

#### Intervention surfaces
- `action-log` for what the household, building, or bounded recommendation path actually did
- action target, action timestamp, actor, and intended reason
- bounded recommendation log where the product suggested, but did not necessarily execute, a response

#### Verification surfaces
- `outcome-log` / response-verification surface for before/after windows
- measured outcome summaries tied to the action window
- response curves such as outdoor PM to indoor PM or outdoor heat to indoor heat burden
- verification result, effect-size estimate, and confidence ceiling from evidence quality

#### Trust support objects
- node health object
- deployment metadata object
- device event history
- calibration version
- maintenance-informed trust penalties

#### Compatibility objects
- control-compatibility record
- integration class
- local / cloud / manual-only flag

In this stage, compatibility objects should stay coarse and descriptive. A full controls-compatibility inventory still belongs later.

### Outputs

- parcel condition
- parcel functional state
- intervention candidate
- verification result
- response history summary

### What this phase is proving

This phase proves that the product can model response, not only exposure.

It should be able to begin answering:
- how outdoor PM translates to indoor PM in this house
- how outdoor heat translates to indoor heat burden in this house
- what happens when HVAC switches to recirculate
- what happens when a purifier runs
- what happens to usability and access when water depth rises at a low point
- whether a given action actually helped

### Minimum closed loop

At least one product path should support:

`hazard -> house state -> action -> measured outcome`

without pretending that every action is automated or that the system already has a mature adaptation engine.

### Required deployment posture

- **Deployment-maturity tier:** `v1.5` (trust hardening) per [`../../architecture/system/deployment-maturity-ladder.md`](../../architecture/system/deployment-maturity-ladder.md); versioned calibration state, drift-aware offsets, maintenance-informed trust penalties expected.
- **Deployment class set:** adds indoor bridge surfaces. `indoor-response-node` (indoor / USB / IP20 / Wi-Fi); `power-outage-node` (indoor / **battery-backed** — intrinsic to use case); `circuit-monitor` (mains-adjacent / low-power from measured circuit / electrical-enclosure IP20 / Wi-Fi).
- **Adapter-derived data enters first-class:** Tier 1 passive inference (e.g., thermal-slope), Tier 2 cloud-API adapters (Ecobee, Nest, Sensibo, etc.), Tier 3 direct measurement (circuit-monitor). Governed by [`../../architecture/system/adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md) — parallel program to calibration-program for adapters. Every adapter declares source authority, pinned API contract version, onboarding gate, cross-check posture.
- **Calibration rigor:** physical-sensor nodes at calibration-program §G `v1.5` tier (versioned offsets); adapter-derived data at adapter-trust §G `v1.5` tier (verification logs versioned, schema-drift detection active).

### What still stays out

- full automation platform
- mature adaptation engine
- full route/block resilience engine
- broad neighborhood planning suite
- full civic infrastructure dashboard
- full controls-compatibility inventory and bounded-controls execution semantics

### Exit criteria

The stage counts as successful when the system can capture the minimum house-state and intervention surfaces needed for before/after reasoning.

At minimum, it should be able to produce one honest closed-loop chain of:

`hazard -> house state -> action -> measured outcome`

with evidence-quality limits carried through to the outcome interpretation.

## Operational rule for all phases

The project stays credible when later-stage ideas are described as later-stage ideas.

The system becomes fragile when:
- route logic is described as if already operational in `v0.1`
- adaptation logic is described as if already supported before `v1.5`
- governance execution is described as complete while still mostly partial or docs-only

## Practical summary

- `v0.1` proves the truth of the parcel view.
- `v1.0` proves the trustworthiness of the parcel kit.
- `v1.5` proves the bridge from sensing to response and verification.
