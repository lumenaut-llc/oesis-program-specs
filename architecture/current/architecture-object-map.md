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
- circuit-monitor is a planned v1.5 node family for non-invasive CT clamp
  current-draw monitoring of HVAC and sump circuits; see
  `../../architecture/system/node-taxonomy.md`

Main sources:
- [`bench-air-node/README.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/bench-air-node/README.md)
- [`mast-lite/README.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/mast-lite/README.md)
- [`node-registry-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/node-registry-schema.md)

### 2. Packet / raw evidence

Status: `implemented`

Role:
- transport and contract object emitted by hardware or raw external feeds
- preserves raw evidence before normalization

Current `v0.1` use:
- packet contracts exist and are validated
- the current live software path most concretely supports `oesis.bench-air.v1`

Main sources:
- [`node-observation-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/node-observation-schema.md)
- `../../software/ingest-service/interfaces.md`
- [`bench-air-node/serial-json-contract.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/bench-air-node/serial-json-contract.md)

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
- [`v0.1/README.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/README.md)
- [`v0.1/examples/normalized-observation.example.json`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/examples/normalized-observation.example.json)
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
- [`parcel-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-context-schema.md)
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
- [`node-registry-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/node-registry-schema.md)
- `../../architecture/system/integrated-parcel-system-spec.md`
- `../../release/v0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v0.1/`)

### 7. Public context

Status: `implemented`

Role:
- external regional or coarse context that may influence parcel conclusions
- supports operation under partial local coverage

Current `v0.1` use:
- public weather and smoke adapters are part of the reference pipeline
- public context is already a live inference input, not just a future concept

Main sources:
- [`public-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/public-context-schema.md)
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
- [`shared-neighborhood-signal-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/shared-neighborhood-signal-schema.md)
- `../../software/shared-map/architecture.md`
- `../../release/v0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v0.1/`)

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
- [`parcel-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-state-schema.md)
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
- [`explanation-payload-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/explanation-payload-schema.md)
- [`evidence-summary-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/evidence-summary-schema.md)

### 11. Rights / sharing / export / audit objects

Status: `partial`

Role:
- governance-operational objects for sharing settings, consent, rights,
  export, access logging, and retention cleanup

Current `v0.1` use:
- several schemas and reference utilities exist
- important product surfaces are still partial or docs-only

Main sources:
- [`v0.1/schemas/`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/schemas/)
- `../../release/v0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v0.1/`)
- `../../software/parcel-platform/README.md`

### 12. Calibration session / reference instrument

Status: `docs-only`

Role:
- per-device record of a calibration session against a characterized reference instrument
- authoritative source for a node's current calibration state (the field already referenced in §1 and §6)
- produced under `oesis-builds/procedures/<node>/calibration.md` per `../system/calibration-program.md` §E

Current `v0.1` use:
- placeholder `references/TBD.md` file exists under bench-air procedures; no populated reference instrument yet (tracked as v0.1 gap register G13)
- calibration session log format defined in calibration-program §E; no sessions logged yet

Main sources:
- `../system/calibration-program.md`
- per-node calibration procedures under [`oesis-builds/procedures/`](https://github.com/lumenaut-llc/oesis-builds/tree/main/procedures)

### 13. Admissibility fact

Status: `planned`

Role:
- runtime-computed decision per normalized observation
- carries `admissible_to_calibration_dataset: bool` plus reason codes
- filters which readings can train hazard-formula coefficients or shape parcel-state claims
- derived from schema facts carried on the canonical observation (tracked as v0.1 gap register G17)

Current `v0.1` use:
- not yet implemented in ingest or inference (tracked as v0.1 gap register G15)
- facts the decision depends on are not yet in the observation schema (tracked as G17)

Main sources:
- `../system/calibration-program.md` §C
- `../system/adapter-trust-program.md` §C

### 14. Adapter source authority

Status: `planned`

Role:
- declared origin for Tier 1 passive inference methods and Tier 2 cloud-API adapter data
- carries pinned API contract version, authentication model, cross-check posture
- analogous to reference instrument for physical sensors — the anchor against which adapter data is trusted

Current `v0.1` use:
- no adapters exist in v0.2 scope; this object becomes load-bearing at capability stage v1.5 (tracked as v0.1 gap register G18)
- policy defined in `../system/adapter-trust-program.md`

Main sources:
- `../system/adapter-trust-program.md` §A
- `../system/node-taxonomy.md` tiered acquisition model (Tier 1 / 2 / 3)

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

### Trust and admissibility layer

- calibration session / reference instrument
- admissibility fact
- adapter source authority (capability-stage `v1.5` bridge)

### Response and verification layer (capability-stage `v1.5` bridge)

These objects are **not** part of the `v0.1` decision layer. They belong to
capability-stage `v1.5` and exist here for architectural completeness. JSON
schemas and examples are present in [`v0.1/schemas/`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/schemas/) for structural
validation, but their design authority lives in [`v1.5/`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/) and
`../../architecture/v1.5/house-state-and-verification-model.md`.

Full contract triples (narrative doc + JSON schema + example) for all six objects
are in [`v1.5/`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/). See [`v1.5/README.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/README.md) for the
complete listing. Parcel-platform API endpoints for these objects are documented
in `../../software/parcel-platform/interfaces.md` with `Status: planned`
annotations.

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

- `../../release/v0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v0.1/`)

Do not let architecture prose imply that a `partial`, `docs-only`, or `planned`
object is already a complete product/runtime surface.

## Blueprint and phasing references

- `../../program/operating-packet/05-revised-architecture-blueprint.md` — seven-layer model and hazard /
  functional / response split
- `../../program/operating-packet/functional-state-and-response-model.md` — bridge toward response and
  verification objects
- `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` — when objects mature by program phase
