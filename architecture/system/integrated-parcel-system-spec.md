# Integrated Parcel System Spec

## Lane

This document is the `system/` lane version of this topic.

Use it for the current integrated parcel-kit architecture, promotion logic, and
cross-version implementation framing.

If you need the debated target-lane parcel-system shape, use
`../v1.0/integrated-parcel-system-spec.md`.

## Purpose

Define the single parcel-level system design that connects the current hardware families into one coherent implementation path across hardware, ingest, inference, parcel UX, and later shared-map outputs.

## Timeline posture

This spec is optimized for a strong timeline and a phase-1 single-parcel release.

- keep one canonical Python implementation tree
- keep runtime entrypoints centralized in `oesis-runtime`
- treat the parcel kit as a coordinated system of nodes, not one all-in-one enclosure
- avoid requiring every hardware family before the first credible pilot

Supporting specs:

- `../current/README.md`
- `../../contracts/node-registry-schema.md`
- `../../hardware/parcel-kit/integrated-parcel-kit-bom.md`
- `../../hardware/parcel-kit/parcel-kit-procurement-checklist.md`
- `../../hardware/parcel-kit/parcel-installation-checklist.md`
- `deployment-maturity-ladder.md`
- `node-taxonomy.md`
- `version-and-promotion-matrix.md`

## Core design rule

A parcel may have multiple purpose-built nodes, but it should still behave as one system with:

- one parcel identity
- one node registry
- one ingest path
- one inference engine
- one dwelling-facing parcel view
- one privacy and sharing policy surface

This is the singular design.
It is not a requirement to physically merge every sensor into one chassis.
In fact, the current hardware rules explicitly argue against that when placement requirements differ.

## Truth, promotion, and staging

This spec uses three different truths on purpose:

- **Current truth** — what the reference implementation and accepted program-phase slice treat as proven today (see `version-and-promotion-matrix.md`).
- **Next promotion** — the next **accepted runnable** boundary, primarily program-phase **`v0.2`**: indoor + sheltered outdoor with explicit promotion criteria in `../current/pre-1.0-version-progression.md`. **`mast-lite` is not fully proven reference hardware until that bar is met**; it remains **partial** in runtime until family normalization and field evidence catch up.
- **Later staged additions** — capability-stage **`v1.5`** bridge objects (indoor response, outage, equipment-state, action/outcome logs, richer metadata) that support an honest **`hazard -> house state -> action -> measured outcome`** loop, then **`v2` / `v2.5`** guidance and full controls-compatibility inventory, then **`v4`** route/community surfaces. Names and roles live in `node-taxonomy.md`.

**Taxonomy is not shipment:** listing a node family in architecture does not imply field-hardened deployment or normalized observation families in Python yet.

## Recommended integrated parcel kit

## Capability stage versus deployment maturity

This spec follows the current capability roadmap, but it also uses the deployment maturity overlay.

- capability stages describe what the parcel platform can do
- deployment maturity describes whether a node family is still a bench prototype, a first field-hardened kit, or a later trust-hardened lane

When this spec uses `v0.1`, `v1.0`, `v1.5`, or `v2.0` below, it refers to deployment maturity unless it explicitly says capability stage.

### Tier 1: fastest useful parcel kit

- `bench-air-node` as the required indoor evidence node
- public weather and smoke context through the existing software path

This is the fastest end-to-end parcel operator slice.
It is primarily a **deployment-maturity `v0.1`** slice (bench-proven, not field-hardened) operating at **capability-stage `current v1`** (parcel sensing and inference baseline).

### Tier 2: first full home-and-parcel kit (next promotion target)

- `bench-air-node` for indoor conditions
- `mast-lite` for sheltered outdoor reference conditions
- optional `flood-node` only on parcels where runoff is operationally relevant

This tier is the **intended default integrated design** for the first field-credible parcel kit and aligns with program-phase **`v0.2`** once promoted. It is the first honest **deployment-maturity `v1.0`** target for the **kit as a whole** (still at **capability-stage `current v1`**), because it introduces the field-hardening bundle in `../../hardware/parcel-kit/field-hardening-checklist.md` needed to call the parcel kit deployed rather than merely buildable.

Until **`v0.2` promotion** criteria are satisfied, treat Tier 2 as **next promotion**, not as “already proven in the reference runtime.” `mast-lite` share of the bench-air packet lineage is still **partially implemented** (see observation family map below).

### Tier 3: richer outdoor parcel kit

- replace or graduate `mast-lite` into `weather-pm-mast`
- keep `bench-air-node`
- keep `flood-node` as an optional hazard module

This is the better second-wave parcel kit after the simpler outdoor node is stable.
It is better treated as a **deployment-maturity `v1.5`** target (still at **capability-stage `current v1`** unless paired with v1.5 bridge surfaces), because the PM mast raises the bar for power design, airflow, maintenance, local buffering, and serviceability.

### Separate R&D lane

- `thermal-pod`

The thermal pod should remain a separate research and privacy-reviewed lane until its contract, usefulness, and retention posture are clearer.
It should not inherit a deployability claim from the rest of the parcel kit.

## Hardware role map

| Node class | Current hardware | Placement | Primary role | Reference / promotion status |
| --- | --- | --- | --- | --- |
| Indoor air node | `bench-air-node` | indoor or sheltered | parcel operator-local smoke and heat evidence | **Current truth** — proven reference lineage end-to-end |
| Outdoor reference node | `mast-lite` | sheltered outdoor | parcel-edge weather and air context | **Next promotion (`v0.2` kit)** — architecturally required; runtime normalization **partial** until promoted |
| Rich outdoor mast | `weather-pm-mast` | outdoor mast | PM and fuller outdoor mechanics | **Later / second wave** — not default first outdoor lane |
| Low-point flood node | `flood-node` | runoff low point | depth and rise-rate evidence | **Geography-gated** optional module |
| Fixed-scene thermal node | `thermal-pod` | fixed outdoor or semi-outdoor scene | derived thermal context | **Research-gated** — not default pilot |
| Indoor response (planned) | `indoor-response-node` | indoor critical zones | indoor PM2.5, T, RH for exposure and closed-loop verification | **Capability `v1.5` bridge** — taxonomy only until built |
| Power / outage (planned) | `power-outage-node` | service / utility entry | mains and backup posture for continuity | **Capability `v1.5` bridge** — taxonomy only until built |
| Freeze (planned) | `freeze-node` | crawlspace, garage, pipe-risk zones | cold-climate hazard evidence | **Geography-gated** — taxonomy only until built |

## Singular system topology

### Parcel identity layer

- one `parcel_id`
- one parcel-context record
- one sharing-settings record
- one rights-request path

### Node registry layer

Each device should bind to the parcel through a node-registry record instead of forcing parcel metadata into every packet.

Minimum registry fields:

- `node_id`
- `parcel_id`
- `node_class`
- `location_mode`
- `install_role`
- `hardware_family`
- `schema_version`
- `transport_mode`
- `power_mode`
- `calibration_state`
- `installed_at`
- `last_seen_at`

The registry is also where the repo should eventually attach deployment-maturity facts such as enclosure revision, service posture, storage class, and replacement history rather than quietly leaving those decisions out of the architecture.

### Evidence transport layer

For timeline compression, the recommended MVP transport decision is:

- serial JSON for bring-up and troubleshooting
- HTTPS push into the ingest API for live operation

That keeps bring-up simple while converging all live nodes onto one operational path.

For `deployment maturity v1.0` and above, the transport layer also needs a documented answer for:

- local buffering or durable local storage
- replay and dedupe semantics
- field identity labels and service posture
- basic power and enclosure protection expectations

### Software path

1. node emits versioned packet
2. ingest binds packet to parcel and normalizes it
3. inference combines node evidence with parcel context and public context
4. parcel platform renders dwelling-facing condition estimates
5. shared-map publication remains optional and policy-gated

For the current parcel-first inference contract, step 3 should explicitly:

- derive parcel priors from parcel metadata before sensor fusion
- preserve local-versus-public divergence as a machine-readable signal
- run a public-only foil path alongside the fused path for contrastive explanation

## Current reference-implementation boundary

- sibling repo `../oesis-runtime` is the canonical Python implementation tree for the current reference services.
- The implemented reference path fully covers bench-air packet validation and normalization, public weather and smoke adapters, parcel inference, parcel-platform governance flows, and shared-map aggregation.
- `mast-lite`, `weather-pm-mast`, `flood-node`, and `thermal-pod` are already part of the singular parcel-kit architecture, but their family-specific normalized observation families remain planned extensions to the current Python package.

That means architecture inclusion does not imply field-hardened readiness.
Several node families are architecturally present before they are honest to call deployed.

## System surfaces

### Parcel operator parcel surface

- one parcel-state output
- one parcel-view summary
- one evidence-summary explanation path
- one sharing and rights-control surface

That parcel-state output should now be understood as containing both:

- functional parcel statuses for the occupant-facing surface
- additive audit fields for priors, divergence, and fact-vs-foil explanation

### Operator and governance surface

- one sharing-store model
- one rights-request lifecycle
- one access-log and retention-cleanup path
- one export-bundle path for parcel data portability

### Neighborhood surface

- one coarse shared-map aggregation path
- no raw parcel publication
- thresholded participation and revocation handling before publication

Revocation and some sharing flows may remain **partial** or **docs-only** until later accepted slices (for example program-phase `v0.5` in `../current/pre-1.0-version-progression.md`). Do not describe them as fully executed product guarantees unless implementation status says so.

## Common packet envelope

Across node families, the packet shape should stay visually and structurally aligned around:

- `schema_version`
- `node_id`
- `observed_at`
- `firmware_version`
- `location_mode`
- `sensors`
- `derived`
- `health`

Optional family-specific fields may include:

- `install_role`
- `privacy_mode`

This lets hardware vary without forcing the software stack to relearn the whole packet grammar for each node family.

## Observation family map

The packet families should normalize into explicit observation families rather than one overloaded observation type.

| Packet contract | Intended normalized observation | Ingest | Inference |
| --- | --- | --- | --- |
| `oesis.bench-air.v1` | `air.node.snapshot` | implemented | consumed |
| `oesis.bench-air.v1` from `mast-lite` | `air.node.snapshot` with outdoor install metadata | partially implemented through shared lineage | consumed (same type) |
| `oesis.circuit-monitor.v1` | `equipment.circuit.snapshot` | implemented | consumed (auto-derives `equipment_state_observation`) |
| `oesis.weather-pm-mast.v1` | `air.pm.snapshot` | implemented | not yet consumed by inference |
| `oesis.flood-node.v1` | `flood.low_point.snapshot` | implemented | not yet consumed by inference |
| `oesis.thermal-pod.v1` | `thermal.scene.snapshot` | not yet implemented | not yet implemented |

**Ingest vs inference distinction:** "implemented" in the ingest column means the normalizer exists and produces valid observations. "consumed" in the inference column means the inference engine accepts that observation type when computing parcel-state. Weather-pm and flood observations normalize successfully but do not yet feed into parcel-state inference — they are available for future inference integration or downstream use.

## Design consequences

### Do not force one physical box

The current hardware families exist because placement requirements differ:

- indoor air belongs indoors
- sheltered outdoor readings belong outdoors
- flood sensing belongs at the low point
- thermal scene sensing needs a fixed, privacy-reviewed field of view

Trying to collapse these into one enclosure would trade away data quality and truthfulness for apparent simplicity.

### Do force one system contract

What should be singular is:

- parcel identity
- node registry
- transport expectations
- normalized observation families
- calibration records
- dwelling-facing parcel outputs

### Do require a field-hardening bundle before using deployed language

No node should be described in the docs as deployed or field-ready unless the repo documents:

- protected power posture
- local buffering or durable storage posture
- serviceable wiring and connector posture
- enclosure support parts and moisture posture
- physical node identity label
- service access posture
- spare-parts posture for active node families

## Strong-timeline sequencing

### Phase 1 shipping lane

- `bench-air-node`
- public-context ingest
- parcel-state inference
- parcel-platform UI and rights controls

Even in this narrow lane, parcel-state should already preserve:

- auditable parcel priors
- divergence from public baseline where local evidence disagrees
- public-only comparison outputs for later verification

This is primarily a `deployment maturity v0.1` lane with selective movement toward `deployment maturity v1.0` documentation.

### Phase 1.5 integrated parcel lane (maps to program-phase `v0.2` promotion)

- add `mast-lite`
- use one parcel registry record to bind indoor and outdoor nodes
- expose source-aware evidence summaries in the parcel view

This is the first meaningful **`deployment maturity v1.0` lane** for the **two-node kit** once the **`v0.2`** promotion criteria are satisfied — not automatically “done” because docs exist.

### Hazard-module lane

- add `flood-node` only for parcels where runoff is a real use case
- keep flood evidence conservative and low-point scoped

Flood maturity should remain parcel-specific until rigid mount, zero reference, and field marker discipline are documented.

### Second-wave outdoor lane

- graduate from `mast-lite` to `weather-pm-mast`
- add PM-specific normalization and inference only after the simpler outdoor lane is stable

This is better treated as a `deployment maturity v1.5` target than a default `v1.0` requirement.

### Research lane

- keep `thermal-pod` behind a separate privacy and usefulness review gate

## Immediate spec work still needed

- canonical auth and provisioning posture for parcel operator-run nodes
- normalized observation schemas for flood, weather/PM, and thermal nodes
- calibration record format shared across node classes
- install metadata standard that inference can trust
- shared field-hardening checklist used across node families
- explicit maturity labeling so controlled-review docs do not overstate deployability

## Recommended implementation decisions

- Use sibling repo `../oesis-runtime` as the canonical Python implementation tree.
- Treat `mast-lite`, not `weather-pm-mast`, as the first outdoor critical-path node.
- Treat `flood-node` as an attachable parcel hazard module, not a universal default.
- Keep `thermal-pod` outside the first integrated pilot unless its contract is normalized and privacy-reviewed.
- Plan **`v1.5` bridge** hardware and support objects per `node-taxonomy.md` (indoor response, outage, equipment-state, action/outcome logs, building/site metadata) so the system can model response rather than stop at parcel status; treat **full controls-compatibility inventory** as primarily **`v2.5`** per `architecture-gaps-by-stage.md`.

## What success looks like

The singular design is successful when one parcel can have multiple node classes, one coherent parcel view, one clear privacy posture, and one implementation path through the software stack without duplicating logic or pretending all hazards come from the same physical sensor package.
