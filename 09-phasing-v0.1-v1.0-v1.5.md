# Phasing: v0.1, v1.0, v1.5

**Canonical incorporation:** Phase summary → [`program/README.md`](program/README.md); milestones ↔ phases → [`architecture/current/milestone-roadmap.md`](architecture/current/milestone-roadmap.md); reading order → [`architecture/current/README.md`](architecture/current/README.md). This file keeps the detailed phasing narrative.

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

## `v1.5` — measurement-to-intervention bridge

### Core goal

Prevent the system from dead-ending into a parcel-status dashboard by adding the minimum extra objects needed to model response, intervention, and verification.

### Why this phase

The source bundle is explicit that **`v1.5`** is the first minimum bridge into **house-state, intervention, controllability, and verification** data, and that **node health**, **deployment metadata**, and **device event history** should become **separate support surfaces** here rather than overloading or silently changing the **core parcel-state contract**. See [`functional-state-and-response-model.md`](functional-state-and-response-model.md).

### What gets added

#### House-state objects
- indoor PM
- indoor temperature / RH
- HVAC mode
- fan / recirculation state
- purifier state
- backup power state
- window/shade state where available

#### Intervention objects
- intervention event
- manual action log
- bounded recommendation log
- action timestamp
- action target

#### Verification objects
- before/after outcome window
- response curve
- verification result
- effect-size estimate
- confidence ceiling from evidence quality

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

### Outputs

- parcel condition
- parcel functional state
- intervention candidate
- verification result
- response history summary

### What still stays out

- full automation platform
- full route/block resilience engine
- broad neighborhood planning suite
- full civic infrastructure dashboard

### Success question

Can we model what the house did, what could be done, and whether it helped?

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
