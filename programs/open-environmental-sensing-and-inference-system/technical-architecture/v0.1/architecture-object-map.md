# Architecture Object Map v0.1

## Purpose

Define the first-class objects and layers of the current `v0.1` architecture so
the system is not described as parcel-only or runtime-only.

## Status

Current reference architecture map.

Use this file to explain what the system reasons about, what each object is for,
and how implemented each object is in the current reference stack.

If you need the narrower answer to "what must work for a functioning first
version," read `minimum-functioning-v0.1.md` alongside this file.

## Object model

### 1. Sensor node

Status: `implemented`

Role:
- primary direct observation object
- device health, uptime, and calibration state
- install role and physical placement context

Current `v0.1` use:
- bench-air-node is the most concrete current observation source
- mast-lite is partially supported through the current shared packet lineage
- other node families exist in architecture and hardware docs but are not all
  implemented in the current reference software path

Main sources:
- `../../hardware/bench-air-node/README.md`
- `../../hardware/mast-lite/README.md`
- `../../docs/data-model/node-registry-schema.md`

### 2. Packet / raw evidence

Status: `implemented`

Role:
- transport and contract object emitted by hardware or raw external feeds
- preserves raw evidence before normalization

Current `v0.1` use:
- packet contracts exist and are validated
- the current live software path most concretely supports `oesis.bench-air.v1`

Main sources:
- `../../docs/data-model/node-observation-schema.md`
- `../../software/ingest-service/interfaces.md`
- `../../hardware/bench-air-node/serial-json-contract.md`

### 3. Collection path / home-platform ingest boundary

Status: `implemented`

Role:
- move node data from the device into the trusted ingest surface
- preserve receipt truth, delivery visibility, and transport freshness
- separate evidence availability from later inference and parcel conclusion logic

Current `v0.1` use:
- node-to-home/platform collection is already real in the current reference path
- the first network meaning in `v0.1` is evidence collection, not neighborhood
  intelligence
- this layer is what makes packet delivery and ingest trust part of the
  architecture rather than hidden plumbing

Main sources:
- `../../software/ingest-service/architecture.md`
- `../../software/operator-quickstart.md`
- `reference-stack.md`

### 4. Normalized observation

Status: `implemented`

Role:
- canonical evidence object after ingest
- stable downstream input to inference
- primary bridge between packet contracts and parcel-state derivation

Current `v0.1` use:
- normalization is implemented for the current bench-air lineage
- this is one of the strongest current boundaries in the stack

Main sources:
- `../../docs/data-model/README.md`
- `../../docs/data-model/examples/normalized-observation.example.json`
- `../../software/ingest-service/architecture.md`

### 5. Parcel context

Status: `implemented`

Role:
- parcel-specific priors and interpretation context
- site and installation information needed for honest inference

Current `v0.1` use:
- parcel context participates in the current reference pipeline
- it exists more strongly as a contract and reference input than as a mature
  end-user product surface

Main sources:
- `../../docs/data-model/parcel-context-schema.md`
- `reference-stack.md`
- `../../docs/system-overview/integrated-parcel-system-spec.md`

### 6. Node registry

Status: `docs-only`

Role:
- binds nodes to one parcel
- carries install role, location mode, hardware family, and schema lineage
- prevents node identity from being confused with parcel truth

Current `v0.1` use:
- the registry contract is clearly defined
- the full registry-driven operational path is not yet a complete product/runtime
  surface

Main sources:
- `../../docs/data-model/node-registry-schema.md`
- `../../docs/system-overview/integrated-parcel-system-spec.md`
- `../../docs/release/2026-04-14/implementation-status-matrix.md`

### 7. Public context

Status: `implemented`

Role:
- external regional or coarse context that may influence parcel conclusions
- supports operation under partial local coverage

Current `v0.1` use:
- public weather and smoke adapters are part of the reference pipeline
- public context is already a live inference input, not just a future concept

Main sources:
- `../../docs/data-model/public-context-schema.md`
- `../../software/ingest-service/public-weather-adapter.md`
- `../../software/ingest-service/public-smoke-adapter.md`

### 8. Shared neighborhood signal

Status: `partial`

Role:
- privacy-scoped shared inference object
- supports neighborhood-aware reasoning without exposing exact parcel truth

Current `v0.1` use:
- contract exists
- aggregation path exists
- still not a fully mature first-class product surface

Main sources:
- `../../docs/data-model/shared-neighborhood-signal-schema.md`
- `../../software/shared-map/architecture.md`
- `../../docs/release/2026-04-14/implementation-status-matrix.md`

### 9. Parcel state

Status: `implemented`

Role:
- primary decision object
- parcel-level condition estimate output
- carries confidence, evidence mode, freshness, hazards, and explanation payload

Current `v0.1` use:
- parcel-state generation is central to the current reference path
- this is the core output where the current architecture lands conclusions

Main sources:
- `../../docs/data-model/parcel-state-schema.md`
- `technical-philosophy.md`
- `reference-stack.md`

### 10. Parcel view / evidence summary

Status: `implemented`

Role:
- presentation objects for homeowner-facing and operator-safe interpretation
- separates product-safe summaries from lower-level parcel-state internals

Current `v0.1` use:
- parcel view and evidence summary are part of the reference stack and current
  local checks

Main sources:
- `../../software/parcel-platform/architecture.md`
- `../../docs/data-model/explanation-payload-schema.md`
- `../../docs/data-model/evidence-summary-schema.md`

### 11. Rights / sharing / export / audit objects

Status: `partial`

Role:
- governance-operational objects for sharing settings, consent, rights,
  export, access logging, and retention cleanup

Current `v0.1` use:
- several schemas and reference utilities exist
- important product surfaces are still partial or docs-only

Main sources:
- `../../docs/data-model/schemas/`
- `../../docs/release/2026-04-14/implementation-status-matrix.md`
- `../../software/parcel-platform/README.md`

## Layered view

### Observation layer

- sensor node
- packet / raw evidence

### Collection and ingest layer

- collection path / home-platform ingest boundary
- normalized observation

### Context layer

- parcel context
- node registry
- public context
- shared neighborhood signal

### Decision layer

- parcel state

### Presentation layer

- parcel view
- evidence summary

### Governance-operational layer

- sharing settings
- consent records
- rights requests
- export bundles
- operator access events
- retention cleanup reports

## `v0.1` rule of interpretation

The parcel is the primary decision object, but not the only architecture object.

`v0.1` should be read as:
- parcel-first for decisions
- sensor-first for direct observation
- collection-first for evidence availability
- context-aware for inference
- provenance-first for explanation and trust

This does not yet imply that every multi-scale doctrine idea is fully
implemented in the current stack.

## Status discipline

This object map uses the same status vocabulary as:

- `../../docs/release/2026-04-14/implementation-status-matrix.md`

Do not let architecture prose imply that a `partial`, `docs-only`, or `planned`
object is already a complete product/runtime surface.
