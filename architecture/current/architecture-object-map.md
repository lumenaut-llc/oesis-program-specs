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

## Relationship to layered blueprint (`05`)

The seven layers in `../../program/operating-packet/05-revised-architecture-blueprint.md` map onto this
object map as follows (this file is the **enumerated** model; `05` names the
**canonical layer titles**):

| `05` layer | Objects in this map |
| ---------- | ------------------- |
| 1. Sensing and capture | **1** Sensor node, **2** Packet / raw evidence (plus device time and health as node/packet concerns) |
| 2. Ingest and temporal integrity | **3** Collection / ingest boundary, **4** Normalized observation (receipt, lineage, timing, replay, dedupe, buffering as part of the truth model) |
| 3. Context and trust | **5** Parcel context, **6** Node registry, **7** Public context; route/access context stays parcel-adjacent, not a full route engine |
| 4. State estimation | **9** Parcel state (fused hazard-oriented estimate, confidence, evidence mode, provenance) |
| 5. Impact and functional state | **9** Parcel state (shelter, reentry, egress, asset risk and related fields as **functional** interpretation—see note under **§9**) |
| 6. Governance and sharing | **8** Shared neighborhood signal, **11** Rights / sharing / export / audit |
| 7. Presentation and operations | **10** Parcel view / evidence summary; optional shared-map presentation is policy-gated via **§8** surfaces |

**Program-phase minimal objects (`05`):** the narrow **`v0.1`** list in `05` (parcel,
packet, normalized observation, parcel context, parcel state, parcel view,
evidence summary) matches the **core** of **§1–5, 9–10** here (sensing through
context, plus parcel state and presentation). **`v1.0`**
adds explicit emphasis on **registry**, installation/trust metadata, **shared**
signal maturity, **functional state** as a clearer split, and history—consistent
with statuses here (**§6** `docs-only`, **§8** `partial`, and matrix rows).
**`v1.5`** response and verification objects are planned in
`../../program/operating-packet/functional-state-and-response-model.md` and `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`,
not first-class rows in this `v0.1` map.

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
- `../../contracts/node-registry-schema.md`

### 2. Packet / raw evidence

Status: `implemented`

Role:
- transport and contract object emitted by hardware or raw external feeds
- preserves raw evidence before normalization

Current `v0.1` use:
- packet contracts exist and are validated
- the current live software path most concretely supports `oesis.bench-air.v1`

Main sources:
- `../../contracts/node-observation-schema.md`
- `../../software/ingest-service/interfaces.md`
- `../../hardware/bench-air-node/serial-json-contract.md`

### 3. Collection path / home-platform ingest boundary

Status: `implemented`

Role:
- move node data from the device into the trusted ingest surface
- preserve receipt truth, delivery visibility, and transport freshness
- separate evidence availability from later inference and parcel conclusion logic
- carry **ingest receipt**, **packet lineage**, and transport-side **buffering /
  replay / dedupe** posture as part of the truth model (`05` §2), not as optional
  plumbing

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
- anchor **temporal integrity**: `measured_at` / `received_at` / `processed_at`,
  freshness windows, and stale-data handling as architecture, not polish (`05` §2)

Current `v0.1` use:
- normalization is implemented for the current bench-air lineage
- this is one of the strongest current boundaries in the stack

Main sources:
- `../../contracts/v0.1/README.md`
- `../../contracts/v0.1/examples/normalized-observation.example.json`
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
- `../../contracts/parcel-context-schema.md`
- `reference-stack.md`
- `../../architecture/system/integrated-parcel-system-spec.md`

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
- `../../contracts/node-registry-schema.md`
- `../../architecture/system/integrated-parcel-system-spec.md`
- `../../release/v.0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v.0.1/`)

### 7. Public context

Status: `implemented`

Role:
- external regional or coarse context that may influence parcel conclusions
- supports operation under partial local coverage

Current `v0.1` use:
- public weather and smoke adapters are part of the reference pipeline
- public context is already a live inference input, not just a future concept

Main sources:
- `../../contracts/public-context-schema.md`
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
- `../../contracts/shared-neighborhood-signal-schema.md`
- `../../software/shared-map/architecture.md`
- `../../release/v.0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v.0.1/`)

### 9. Parcel state

Status: `implemented`

Role:
- primary decision object
- parcel-level condition estimate output
- carries confidence, evidence mode, freshness, hazards, and explanation payload

**Hazard vs functional vs response (`05`):** the parcel-state contract **compresses**
what the blueprint separates as **hazard-oriented** estimates and **functional**
meaning (shelter, reentry, egress, asset risk, access/utility framing). **Response
state**—actions taken, verification, controllability—is **out of scope** for the
narrow **`v0.1`** slice; see `../../program/operating-packet/functional-state-and-response-model.md` and
program-phase **`v1.5`** in `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`.

Current `v0.1` use:
- parcel-state generation is central to the current reference path
- this is the core output where the current architecture lands conclusions

Main sources:
- `../../contracts/parcel-state-schema.md`
- `technical-philosophy.md`
- `reference-stack.md`

### 10. Parcel view / evidence summary

Status: `implemented`

Role:
- presentation objects for dwelling-facing and operator-safe interpretation
- separates product-safe summaries from lower-level parcel-state internals

Current `v0.1` use:
- parcel view and evidence summary are part of the reference stack and current
  local checks

Main sources:
- `../../software/parcel-platform/architecture.md`
- `../../contracts/explanation-payload-schema.md`
- `../../contracts/evidence-summary-schema.md`

### 11. Rights / sharing / export / audit objects

Status: `partial`

Role:
- governance-operational objects for sharing settings, consent, rights,
  export, access logging, and retention cleanup

Current `v0.1` use:
- several schemas and reference utilities exist
- important product surfaces are still partial or docs-only

Main sources:
- `../../contracts/v0.1/schemas/`
- `../../release/v.0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v.0.1/`)
- `../../software/parcel-platform/README.md`

## Layered view

The grouping below is the **object-map** shorthand for navigation. **Canonical
layer names and purposes** are in `../../program/operating-packet/05-revised-architecture-blueprint.md`
(see Relationship table above).

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

### Response and verification layer (capability-stage `v1.5` bridge)

These objects are **not** part of the `v0.1` decision layer. They belong to
capability-stage `v1.5` and exist here for architectural completeness. JSON
schemas and examples are present in `contracts/v0.1/schemas/` for structural
validation, but their design authority lives in `contracts/v1.5/` and
`../../architecture/v1.5/house-state-and-verification-model.md`.

- house state — indoor response and power-state snapshot (`planned`)
- intervention event — action taken during a hazard event (`planned`)
- verification outcome — measured before/after result (`planned`)
- equipment-state observation — read-side HVAC/fan/purifier signals (`planned`)
- source provenance record — per-signal freshness and audit trail (`planned`)
- house capability — coarse physical equipment inventory (`planned`)

### Controls layer (capability-stage `v2.5`)

- control compatibility — endpoint inventory with integration class (`planned`)

See `../../architecture/system/node-taxonomy.md` for capability-stage placement
and `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` for phasing.

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

- `../../release/v.0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v.0.1/`)

Do not let architecture prose imply that a `partial`, `docs-only`, or `planned`
object is already a complete product/runtime surface.

## Blueprint and phasing references

- `../../program/operating-packet/05-revised-architecture-blueprint.md` — seven-layer model and hazard /
  functional / response split
- `../../program/operating-packet/functional-state-and-response-model.md` — bridge toward response and
  verification objects
- `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` — when objects mature by program phase
