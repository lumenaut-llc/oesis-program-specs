# Revised architecture blueprint

**Canonical incorporation:** Layer ↔ object mapping → [`architecture/current/architecture-object-map.md`](../../architecture/current/architecture-object-map.md) and [`architecture/current/reference-stack.md`](../../architecture/current/reference-stack.md); near-term posture → [`architecture/current/implementation-posture.md`](../../architecture/current/implementation-posture.md). This file keeps the full seven-layer blueprint.

## Versioning cleanup

How these names map to the repo’s accepted slices, capability stages, and
runtime lanes is spelled out in [`00-version-labels-and-lanes.md`](00-version-labels-and-lanes.md)
and the canonical matrix at [`architecture/system/version-and-promotion-matrix.md`](../../architecture/system/version-and-promotion-matrix.md).
In short:

- `v0.1` = narrow accepted reference slice
- `v0.2` = next accepted two-node parcel-kit promotion
- runtime `v1.0` lane = optional additive asset lane, not the same thing as `v0.2`
- capability `v1.5` = measurement-to-intervention bridge

Keep these labels separate:

- `v0.1` = narrow executable reference slice
- `v0.2` = next accepted parcel-kit promotion
- `v1.0` = first materially broader system than the first narrow slice
- `v1.5` = measurement-to-intervention bridge

Do not collapse these into one label. The project is strongest when the executable slice, the architecture target, and the later bridge stage are spoken about distinctly.

## Revised layered architecture

### 1. Sensing and capture layer

Purpose: capture direct observations and preserve raw evidence.

Objects:
- sensor node
- node packet
- raw packet archive
- device clock / `observed_at`
- device health snapshot

Near-term posture:
- bench-air first
- mast-lite second
- flood optional
- thermal deferred
- weather + PM later

### 2. Ingest and temporal integrity layer

Purpose: turn raw packets into trustworthy normalized observations.

Objects:
- ingest receipt
- normalized observation
- packet lineage
- `measured_at` / `received_at` / `processed_at`
- freshness window
- replay / dedupe state
- buffering state

This should be treated as core architecture, not implementation detail. Timing integrity, buffering, and stale-data handling are part of the truth model.

### 3. Context and trust layer

Purpose: hold the slow-changing context that makes point observations meaningful.

Objects:
- parcel
- parcel context
- node registry
- parcel priors
- installation metadata
- deployment-quality metadata
- calibration state
- trust penalties

Route and access context should first appear here as parcel-adjacent context rather than as a full route engine.

### 4. State estimation layer

Purpose: fuse evidence into the current best estimate, with uncertainty.

Objects:
- local evidence
- shared evidence
- external public context
- divergence record
- parcel-prior application
- public-only foil path
- contrastive explanation
- fused hazard state
- confidence
- evidence mode
- provenance summary

This should remain rules-first and evidence-first in the near term.

It should also remain parcel-first in a specific technical sense:

- local-versus-public mismatch is a primary signal, not just a trust penalty
- parcel metadata should shape explicit priors before fusion
- fused outputs should carry a fact-versus-foil explanation surface for audit

### 5. Impact and functional state layer

Purpose: translate hazard state into operationally meaningful conditions.

Objects:
- shelter viability
- reentry viability
- egress viability
- asset risk
- route/access degradation
- utility dependency flags
- functional state summary

This layer should be made explicit. It is the bridge from environmental state to operational meaning.

### 6. Governance and sharing layer

Purpose: enforce owner control, scoped sharing, and visibility rules.

Objects:
- sharing settings
- consent record
- rights request
- export bundle
- retention policy state
- access log
- shared neighborhood signal

This layer should exist even if some surfaces remain partial in the current implementation.

### 7. Presentation and operations layer

Purpose: render parcel truth, evidence, and system health to users and operators.

Objects:
- parcel view
- evidence summary
- homeowner dashboard
- operator review surface
- neighborhood/shared map
- alert/event timeline later

## Most important conceptual split

The system should explicitly split three ideas that are currently too compressed inside parcel state:

### Hazard state
What the environment is believed to be doing.

### Functional state
What that means for shelter, egress, reentry, access, utility dependence, and asset exposure.

### Response state
What actions are available, taken, or verified, and whether they changed outcomes.

That split keeps the baseline simple while creating a clean bridge to later response and adaptation logic.

## Minimal object map by stage

### `v0.1`
- parcel
- packet
- normalized observation
- parcel context
- parcel state
- parcel view
- evidence summary

The current parcel-state lane may already include additive audit fields for:

- parcel-prior application
- divergence records
- public-only counterfactuals
- contrastive explanations

### `v1.0`
- all of the above
- node registry
- installation metadata
- trust / deployment-quality flags
- shared neighborhood signal
- functional state
- event history

### `v1.5`
- all of the above
- house state
- indoor-response and outage evidence
- coarse house capability / equipment-state support
- intervention event
- verification outcome
- building-and-site response metadata
- node health
- deployment metadata object
- device event history
- response-window and verification support

Full control compatibility and bounded-controls inventory should be treated as a
later stage rather than part of the minimum bridge.

## One-line stage definitions

- `v0.1`: Can we honestly produce a parcel view from one observation path?
- `v1.0`: Can we produce a more trustworthy parcel state from a real parcel kit and limited shared evidence?
- `v1.5`: Can we produce one honest `hazard -> house state -> action -> measured outcome` loop?

## Functional state and response (dedicated note)

The bridge from hazard → operational meaning → verified response is spelled out in [`functional-state-and-response-model.md`](functional-state-and-response-model.md). It complements:
- sensing and ingest layers above
- parcel inference and evidence modes
- [`07-information-layer-and-functional-recovery.md`](07-information-layer-and-functional-recovery.md) for the information-layer target
- [`09-phasing-v0.1-v1.0-v1.5.md`](09-phasing-v0.1-v1.0-v1.5.md) for when objects enter each phase
