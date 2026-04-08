# Milestone Roadmap v0.1

## Purpose

Define the practical delivery sequence implied by the current truthful
reference architecture.

This file translates the current `v0.1` architecture into milestones that can
be used for planning, acceptance, and scope control without pretending later
surfaces are already implemented.

## Status

Current implementation-aligned milestone roadmap.

## Planning rules

- start with one useful parcel before requiring neighborhood participation
- keep one parcel identity, one ingest path, one inference layer, and one
  parcel-facing view
- add new hardware families only when they preserve the same system contract
- do not let milestone language outrun the current
  `implemented` / `partial` / `docs-only` / `planned` posture
- keep privacy, provenance, confidence, and claims boundaries inside every
  milestone definition

## Milestone 1: one parcel, one node

### Goal

Prove the minimum functioning `v0.1` slice on a single parcel using one local
evidence node.

### Scope

- `bench-air-node`
- one versioned packet lineage
- one ingest acceptance and normalization path
- one parcel inference path
- one homeowner-facing parcel view
- public weather and smoke context through the current software lane

### Build requirements

- repeatable `bench-air-node` bring-up
- packet validation and normalization for the current bench-air lineage
- parcel context sufficient for honest interpretation
- parcel-state and parcel-view outputs with confidence, freshness, evidence
  mode, and reasons

### Acceptance criteria

- `bench-air-node` emits valid packets repeatedly
- the packet validates and normalizes through the ingest boundary
- inference combines local evidence with parcel context and current public
  context
- parcel platform renders a homeowner-readable parcel answer with explanation
- one parcel receives useful output without neighborhood participation

### Current posture

- hardware path: `implemented`
- reference packet-to-parcel software path: `implemented`
- privacy and sharing product surface: minimum boundary only

## Milestone 2: first integrated parcel kit

### Goal

Treat the parcel as one coherent indoor-plus-outdoor system rather than as two
disconnected devices.

### Scope

- keep `bench-air-node`
- add `mast-lite`
- bind both nodes through one parcel-scoped node registry
- extend parcel evidence summaries so source mix is understandable

### Build requirements

- stable indoor reference node installation
- stable sheltered outdoor reference node installation
- one registry model that binds both nodes to one `parcel_id`
- install metadata and calibration state that operators and inference can trust

### Acceptance criteria

- `bench-air-node` and `mast-lite` both emit valid packets
- both nodes are bound to one parcel through the registry path
- ingest and inference remain singular rather than splitting by node family
- parcel outputs clearly explain indoor versus sheltered outdoor evidence
- `mast-lite` survives sheltered outdoor validation without frequent resets or
  disappearing devices

### Current posture

- `bench-air-node`: `implemented`
- `mast-lite` hardware and shared packet lineage: `partial`
- stronger registry-driven lifecycle: not yet complete

## Milestone 3: hazard-module expansion

### Goal

Add parcel-specific hazard modules only where they create real value and still
fit the singular parcel-system contract.

### Scope

- `flood-node` only for parcels where runoff or pooling is operationally
  meaningful
- flood observation family support
- flood-aware parcel explanation and conservative interpretation

### Build requirements

- explicit `flood.low_point.snapshot` normalization path
- install and geometry metadata that anchor low-point meaning
- inference that keeps flood evidence low-point scoped instead of silently
  generalizing it to the whole parcel

### Acceptance criteria

- flood packets normalize into a dedicated observation family
- parcel outputs preserve the difference between low-point evidence and broader
  parcel conclusions
- adding flood support does not fork the product into a separate architecture

### Current posture

- `flood-node` hardware lane: `partial`
- flood observation family in the canonical software path: `planned`

## Milestone 4: richer outdoor sensing

### Goal

Improve parcel-edge evidence quality after the simpler sheltered outdoor lane is
stable.

### Scope

- graduate from `mast-lite` toward `weather-pm-mast`
- add particulate and richer outdoor sensing only after the shared outdoor
  packet and install posture is stable
- preserve one parcel-first software path

### Build requirements

- `air.pm_weather.snapshot` normalization support
- richer outdoor calibration and maintenance assumptions
- parcel explanation that preserves provenance and observability limits

### Acceptance criteria

- richer outdoor packets normalize cleanly into a dedicated observation family
- parcel inference improves with the new evidence without turning into a black
  box
- outdoor expansion does not require redesigning ingest, inference, or parcel
  presentation

### Current posture

- `weather-pm-mast` hardware lane: `partial`
- PM/weather observation family in software: `planned`

## Milestone 5: shared neighborhood surface

### Goal

Expose shared value downstream of parcel-private reasoning without turning the
system into parcel surveillance.

### Scope

- shared-map aggregation
- sharing controls and revocation posture
- retention, export, and access-log flows
- hard private-versus-shared boundary enforcement

### Build requirements

- thresholded and policy-gated aggregate publication
- revocation and retention behavior that is technically enforceable
- user and operator surfaces that match sharing-policy claims

### Acceptance criteria

- shared outputs are coarse and policy-gated
- parcel-private evidence never becomes parcel-resolution public output
- revocation and retention behavior are verifiable, not only documented
- shared surfaces remain downstream of parcel-private reasoning

### Current posture

- shared-map aggregate API: `partial`
- richer sharing, consent, and revocation product surfaces: `docs-only` or
  `partial`

## Separate research lane

### `thermal-pod`

`thermal-pod` should remain outside the critical path for the first parcel kit.

Use it as a separate research lane until:

- privacy posture is stronger
- retention posture is clearer
- usefulness is demonstrated for the parcel-facing product
- the thermal observation family is normalized in the canonical software path

## Recommended near-term order

1. `bench-air-node`
2. packet validation and normalization
3. parcel inference and parcel view
4. parcel-scoped registry and install metadata hardening
5. `mast-lite`
6. optional flood expansion where parcel conditions justify it
7. richer outdoor PM and weather sensing
8. mature shared-map and sharing controls

## Alignment references

- `README.md`
- `technical-philosophy.md`
- `reference-stack.md`
- `minimum-functioning-v0.1.md`
- `implementation-posture.md`
- `component-boundaries.md`
- `../../architecture/system/integrated-parcel-system-spec.md`
- `../../release/2026-04-14/implementation-status-matrix.md`
