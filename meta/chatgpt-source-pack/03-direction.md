---
title: Direction
status: canonical-summary
updated: 2026-04-13
sources:
  - architecture/v1.0/README.md
  - program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md
  - program/operating-packet/functional-state-and-response-model.md
  - architecture/system/integrated-parcel-system-spec.md
  - architecture/system/node-taxonomy.md
  - architecture/system/architecture-gaps-by-stage.md
  - architecture/system/phase-roadmap.md
  - architecture/system/product-requirements-phase-1.md
  - ../oesis-public-site/src/app/roadmap/page.tsx
---

# Direction

This file holds the longer-range direction while keeping future work clearly separated from current truth.

It now includes the debated future lane, the root phasing and response-bridge docs, and the system-level target documents that define the integrated parcel system, node taxonomy, stage gaps, roadmap, and phase-1 product requirements.

Conventions for path/label interpretation are defined once in
`README.md` for this source-pack.

## Why This File Exists

This summary is followed by verbatim source-file copies so the synthesized guidance and the underlying canonical text stay together in one markdown.

## Included Source Files

- `architecture/v1.0/README.md`
- `program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`
- `program/operating-packet/functional-state-and-response-model.md`
- `architecture/system/integrated-parcel-system-spec.md`
- `architecture/system/node-taxonomy.md`
- `architecture/system/architecture-gaps-by-stage.md`
- `architecture/system/phase-roadmap.md`
- `architecture/system/product-requirements-phase-1.md`
- `../oesis-public-site/src/app/roadmap/page.tsx`

## Verbatim Source Content

### File: `architecture/v1.0/README.md`

```md
# Technical Architecture v1.0

## Purpose

Define the debated target architecture for Open Environmental Sensing and
Inference System beyond the current reference stack.

## Status

Debated target architecture.

`v1.0` is proposal space. It should capture stronger future architecture without
pretending that those changes are already implemented.

This directory is the explicit `v1.0` lane. It exists beside the frozen
`../current/` `v0.1` lane so the project can debate and prototype future
architecture without rewriting current truth.

Future pre-`1.0` capability bundles may exist before `v1.0`, but they should be
promoted only when the accepted runnable slice changes materially. This
directory should not be used as a parking place for every minor compatible
addition.

## Reading order

1. `../debate-map.md`
2. `goals-and-deltas.md`
3. `proposed-architecture.md`
4. `product-requirements-phase-1.md`
5. `phase-roadmap.md`
6. `integrated-parcel-system-spec.md`
7. `node-taxonomy.md`
8. `architecture-gaps-by-stage.md`
9. `open-questions.md`
10. `decision-log.md`

## Future-lane end-state docs

These files hold the stronger target-lane wording for the next product shape
without mutating the frozen `../current/` lane:

- `product-requirements-phase-1.md`
- `phase-roadmap.md`
- `integrated-parcel-system-spec.md`
- `node-taxonomy.md`
- `architecture-gaps-by-stage.md`

## Guardrail

Anything written in `v1.0/` should stay clearly separate from the implemented,
partial, docs-only, and planned classifications used for current reference
surfaces.

## Contributor rule

If a document changes the meaning of the current reference stack, move that
content back to `../current/`.

If a document proposes a stronger target lane, a new boundary, or a future
contract/runtime direction, keep it here.
```

### File: `program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`

```md
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
```

### File: `program/operating-packet/functional-state-and-response-model.md`

```md
# Functional state and response model

**Canonical incorporation:** Contract-level narrative → [`contracts/parcel-state-schema.md`](../../contracts/parcel-state-schema.md) and [`architecture/current/architecture-object-map.md`](../../architecture/current/architecture-object-map.md) (parcel state §9); phasing table aligns with [`09-phasing-v0.1-v1.0-v1.5.md`](09-phasing-v0.1-v1.0-v1.5.md).

This note defines how **hazard state**, **functional state**, and **response state** relate to each other and to **`parcel state`** over program phases. It is a **runtime-adjacent architecture brief**. JSON shapes, field names, and normative contracts remain canonical in **`oesis-program-specs`** (for example `contracts/parcel-state-schema.md` and related artifacts).

## Why three layers

Today the project often speaks in one bundle: “parcel state.” That is hard to evolve without either **over-claiming** (implying adaptation that does not exist) or **overloading** one object (mixing environment, operations, and parcel-operator actions).

Splitting into three nested ideas keeps **`v0.1` simple**, makes **`v1.0` more honest** about operational meaning, and lets **`v1.5`** add response and verification **without corrupting** the baseline hazard story.

## Definitions

### Hazard state

What the environment is **believed** to be doing at or near the parcel, with **confidence**, **evidence mode**, and **provenance** (local observation, shared neighbor signal, regional inference, stale, etc.). This stays close to fused environmental estimates (air, heat, water-related signals as applicable).

### Functional state

What hazard-related conditions **mean operationally** for the dwelling and parcel: shelter viability, egress/reentry, asset exposure, route or access degradation at parcel-adjacent scope, utility dependence flags, and related summaries. This is **impact-oriented**: it connects estimates to “what matters for decisions” without yet claiming what was **done** about it.

### Response state

What **actions** are available, **taken**, or **verified**, and whether outcomes **changed** measurable conditions: interventions, logs, before/after windows, verification results, and (later) response history. This is where **adaptation learning** begins; it must not **inflate** hazard confidence by itself.

## Flow

```mermaid
flowchart LR
  evidence[Evidence_and_context]
  hazard[Hazard_state]
  functional[Functional_state]
  response[Response_state]
  evidence --> hazard
  hazard --> functional
  functional --> response
```

Upstream **evidence** and **context** (parcel priors, node registry, public feeds) feed **hazard state**. **Functional state** interprets hazard for operations. **Response state** records and verifies actions; its outputs can inform **future** hazard/functional estimates (for example indoor conditions after an intervention) without conflating layers.

## By program phase

Aligns with [`09-phasing-v0.1-v1.0-v1.5.md`](09-phasing-v0.1-v1.0-v1.5.md) and the object map in [`05-revised-architecture-blueprint.md`](05-revised-architecture-blueprint.md).

| Phase | Hazard | Functional | Response |
|-------|--------|------------|----------|
| **`v0.1`** | Core: fused estimate with evidence mode and provenance in the parcel pipeline | May appear as **reasons** or compact flags inside the existing parcel-facing surface; not required as a separate persisted object family | **Out of scope** as a first-class model |
| **`v1.0`** | Stronger trust, history, and neighbor signal; same epistemic discipline | **Explicit** functional translation (stronger than **`v0.1`**), still without a full route/block engine | **Out of scope** except possibly manual notes outside core contract |
| **`v1.5`** | Unchanged in role; must not be silently “upgraded” by response data | Tied to **parcel condition** and operational summaries users need | **Intervention**, **verification**, **house-state**, **compatibility** support objects as in **`09`** |

## Contract posture

- **`v1.5`** additions (house state, interventions, device events, node health) should live in **separate support objects** or extensions **documented against** the core parcel-state contract, rather than overloading core fields in ways that confuse **hazard** confidence with **response** quality.
- **Functional state** should not claim **verified** outcomes; **response state** owns verification and effect-size language subject to evidence quality ceilings.

## Non-goals (here)

- Full **automation** or **bounded control** execution semantics
- **Public parcel-resolution** maps or **civic** infrastructure dashboards
- Replacing **official** hazard products; this model **complements** them at parcel-relevant resolution

## Related reading

- [`07-information-layer-and-functional-recovery.md`](07-information-layer-and-functional-recovery.md) — evidence-to-impact and functional recovery framing
- [`00-version-labels-and-lanes.md`](00-version-labels-and-lanes.md) — naming for runtime lanes vs program phases
```

### File: `architecture/system/integrated-parcel-system-spec.md`

```md
# Integrated Parcel System Spec

## Purpose

Define the single parcel-level system design that connects the current hardware families into one coherent implementation path across hardware, ingest, inference, parcel UX, and later shared-map outputs.

## Timeline posture

This spec is optimized for a strong timeline and a phase-1 single-parcel release.

- keep one canonical Python implementation tree
- keep existing docs-facing script paths stable
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
- **Later staged additions** — capability-stage **`v1.5`** bridge objects (indoor response, outage, equipment-state, action/outcome logs, richer metadata), then **`v2` / `v2.5`** guidance and full controls-compatibility inventory, then **`v4`** route/community surfaces. Names and roles live in `node-taxonomy.md`.

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
It is primarily a `deployment maturity v0.1` slice: strong for bench proof, packet contracts, and parcel operator-local evidence, but not the same as a fully field-hardened parcel kit.

### Tier 2: first full home-and-parcel kit (next promotion target)

- `bench-air-node` for indoor conditions
- `mast-lite` for sheltered outdoor reference conditions
- optional `flood-node` only on parcels where runoff is operationally relevant

This tier is the **intended default integrated design** for the first field-credible parcel kit and aligns with program-phase **`v0.2`** once promoted. It is the first honest **`deployment maturity v1.0` target** for the **kit as a whole**, because it introduces the field-hardening bundle in `../../hardware/parcel-kit/field-hardening-checklist.md` needed to call the parcel kit deployed rather than merely buildable.

Until **`v0.2` promotion** criteria are satisfied, treat Tier 2 as **next promotion**, not as “already proven in the reference runtime.” `mast-lite` share of the bench-air packet lineage is still **partially implemented** (see observation family map below).

### Tier 3: richer outdoor parcel kit

- replace or graduate `mast-lite` into `weather-pm-mast`
- keep `bench-air-node`
- keep `flood-node` as an optional hazard module

This is the better second-wave parcel kit after the simpler outdoor node is stable.
It is better treated as a `deployment maturity v1.5` target, because the PM mast raises the bar for power design, airflow, maintenance, local buffering, and serviceability.

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
- `software/*/scripts/*.py` remains in place as a compatibility layer for docs, smoke checks, and operator-facing commands.
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

| Packet contract | Intended normalized observation | Status |
| --- | --- | --- |
| `oesis.bench-air.v1` | `air.node.snapshot` | implemented |
| `oesis.bench-air.v1` from `mast-lite` | `air.node.snapshot` with outdoor install metadata | partially implemented through shared lineage |
| `oesis.weather-pm-mast.v1` | `air.pm_weather.snapshot` | not yet implemented |
| `oesis.flood-node.v1` | `flood.low_point.snapshot` | not yet implemented |
| `oesis.thermal-pod.v1` | `thermal.scene.snapshot` | not yet implemented |

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
- Keep `software/*/scripts/` as compatibility entrypoints only.
- Treat `mast-lite`, not `weather-pm-mast`, as the first outdoor critical-path node.
- Treat `flood-node` as an attachable parcel hazard module, not a universal default.
- Keep `thermal-pod` outside the first integrated pilot unless its contract is normalized and privacy-reviewed.
- Plan **`v1.5` bridge** hardware and support objects per `node-taxonomy.md` (indoor response, outage, equipment-state, action/outcome logs); treat **full controls-compatibility inventory** as primarily **`v2.5`** per `architecture-gaps-by-stage.md`.

## What success looks like

The singular design is successful when one parcel can have multiple node classes, one coherent parcel view, one clear privacy posture, and one implementation path through the software stack without duplicating logic or pretending all hazards come from the same physical sensor package.
```

### File: `architecture/system/node-taxonomy.md`

```md
# Node and Evidence Taxonomy

## Purpose

Give one repo-wide vocabulary for **hardware node families**, **geography-gated modules**, and **non-node evidence surfaces**, with explicit **capability-stage** and **promotion** labels so taxonomy is not mistaken for shipped product.

## Governing rules

- The **parcel** remains the primary object; nodes and adapters are evidence layers used to compute parcel-level conditions and statuses.
- **Taxonomy names** may exist in docs before hardware folders or runtime normalization land. Treat missing implementations as `planned` or `partial` unless a specific promotion says otherwise.
- Do not collapse **accepted runnable slice** (for example program-phase `v0.1`, next `v0.2`), **capability stage** (`current v1`, `v1.5`, …), and **deployment maturity** (`deployment maturity v0.1`, …). See `version-and-promotion-matrix.md`.

## Current-truth hardware (accepted reference path today)

| Identifier | Role | Notes |
| --- | --- | --- |
| `bench-air-node` | Indoor or sheltered bench reference; `oesis.bench-air.v1` lineage | Proven end-to-end ingest → parcel view for this family |

## Next-promotion kit hardware (not the same as “fully proven”)

| Identifier | Role | Notes |
| --- | --- | --- |
| `mast-lite` | First sheltered-outdoor reference; same packet lineage as bench-air | Architecturally in scope; runtime normalization and field validation are **partial** until the `v0.2` promotion bar in `../current/pre-1.0-version-progression.md` is met |

## Geography-gated and second-wave hardware modules

Attach only when parcel risk, region, and use case justify them. None of these are universal defaults.

| Identifier | Role | Typical staging |
| --- | --- | --- |
| `flood-node` | Low-point runoff depth and rise-rate evidence | Optional hazard module; `deployment maturity` and normalization still planned for dedicated flood observation family |
| `weather-pm-mast` | Richer outdoor PM, wind, rainfall | Second-wave outdoor lane after `mast-lite` is stable; higher ops burden |
| `freeze-node` | Cold-climate pipe-risk and exposed-space thermal evidence | Planned geography module; not required for warm-climate pilots |

## Research- or privacy-gated hardware

| Identifier | Role | Notes |
| --- | --- | --- |
| `thermal-pod` | Fixed-scene derived thermal context | R&D lane; keep outside default pilot until contract, usefulness, and retention posture are reviewed |

## Capability-stage v1.5 bridge (planned hardware and adapters)

These convert the program from “outdoor and parcel sensing only” toward **hazard → house state → action → verified outcome**. They belong in the **v1.5** capability stage as support objects and evidence types, not as implied **current v1** baseline.

| Identifier | Kind | Minimum intent |
| --- | --- | --- |
| `indoor-response-node` | Hardware family (planned) | Indoor PM2.5, indoor temperature, indoor RH — bridge from parcel forcing to in-home exposure |
| `power-outage-node` | Hardware family or adapter (planned) | Mains up/down, backup power present/active; connectivity degradation where measurable |
| `equipment-state-adapter` | Non-node or adapter surface | Read-side HVAC mode, fan, recirculation vs fresh air, purifier, shade/window, sump/pump where available |
| `action-log` | Support object | Household or building actions (mode changes, purifier run, drain clearing, barrier install, backup activation) |
| `outcome-log` / response verification | Support object | Whether actions improved observed conditions over defined windows (for example 30–90 minutes for smoke-related PM response) |
| Building/site metadata | Parcel-context extensions | Orientation, exposure, shading, drainage, vents, filter path — overlaps `parcel-context-schema.md` v1.5 optional fields |

**First closed-loop priority (spec direction):** smoke protection — outdoor PM, indoor PM, smoke-protect posture, bounded actions such as recirculation / fan / purifier, then verify indoor PM response over a bounded time window.

## Capability-stage v2.5 — controls compatibility (not v1.5 execution)

**Full compatibility inventory** by interface class (for example Matter, Home Assistant, BACnet relevance, smart plugs, local controllers), integration tiers, and bounded-control policy versioning is primarily **v2.5**, even when draft schema files exist for forward compatibility.

- **v1.5** may capture **observed** equipment state and coarse **house-capability** hints.
- **v2.5** is where compatibility mapping and bounded controls become first-class operational requirements. See `architecture-gaps-by-stage.md` and `phase-roadmap.md` Stage D.

## Capability-stage v4 — route and community surfaces

| Identifier | Kind | Notes |
| --- | --- | --- |
| `route-and-community-surface` | Data and model layer | Egress, shared refuge, drainage chokepoints, block-level weak points — staged later; not a default hardware expectation for early pilots |

Prefer public data, shared reports, and selected instrumentation over universal “community chokepoint” nodes in early phases.

## Geography mapping (planning aid)

- **Wildfire / smoke regions:** emphasize `mast-lite` (when promoted), `indoor-response-node`, optional `weather-pm-mast`, equipment-state for HVAC/purifier.
- **Flood / runoff regions:** `flood-node` where relevant, sump/pump equipment-state, drainage metadata.
- **Heat-burden regions:** `indoor-response-node`, shading/HVAC equipment-state, optional `thermal-pod` later.
- **Cold / freeze regions:** `freeze-node` where justified, `power-outage-node`, heating-system equipment-state.
- **Storm / outage-prone regions:** `power-outage-node`, backup power signals, communications dependency metadata in parcel context.

## Recommended sequencing (spec)

1. **Baseline parcel sensing:** `bench-air-node`, parcel inference, shared evidence discipline (`current v1`).
2. **Next promotion:** `v0.2` indoor + sheltered outdoor kit — `bench-air-node` + `mast-lite` with field-hardening and acceptance evidence (`../current/pre-1.0-version-progression.md`).
3. **v1.5 bridge:** indoor response, outage, equipment-state signals, building/site metadata, action and outcome logs.
4. **v2 / v2.5:** bounded guidance, then compatibility inventory and bounded controls.
5. **v4:** route and neighborhood resilience surfaces.

## Related docs

- `version-and-promotion-matrix.md`
- `integrated-parcel-system-spec.md`
- `deployment-maturity-ladder.md`
- `architecture-gaps-by-stage.md`
- `phase-roadmap.md`
- `../../contracts/parcel-context-schema.md`
- `../../hardware/v0.1/README.md`
```

### File: `architecture/system/architecture-gaps-by-stage.md`

```md
# Architecture Gaps By Stage

## Purpose

Place the major missing operational-architecture surfaces into the project's
existing capability stages and deployment-maturity overlay instead of treating
them as one flat backlog.

This document is meant to answer:

- how the current public project version `v0.1` relates to the stage map
- what must be defined in `current v1`
- what should first become a separate support surface in `v1.5`
- what belongs to bounded guidance in `v2`
- what should wait for bounded controls, adaptation, or route/block resilience

## How `v0.1` relates to the stage map

If this document is read through the project-version lens rather than the
internal capability-stage lens, the current public version is `v0.1`.

`v0.1` should not be treated as the same thing as:

- capability stage `current v1`
- later capability stages such as `v1.5`, `v2`, or `v2.5`
- deployment-maturity labels such as `deployment maturity v0.1` or `deployment maturity v1.0`

Instead, keep the labels separate:

- `v0.1` = public project or release version
- `current v1`, `v1.5`, `v2`, `v2.5`, `v3`, `v4` = capability stages
- `deployment maturity v0.1`, `v1.0`, `v1.5`, `v2.0` = hardware and operations maturity overlay

That means a public release like `v0.1` may document, prototype, or expose only
part of the capability roadmap, and it may include hardware lanes at different
deployment-maturity levels.

For the current repo posture, `v0.1` should be read as a public release with:

- conservative claims
- parcel-first sensing and inference as the center of gravity
- governance and release-boundary docs as first-class assets
- mixed hardware maturity, from bench proof to early field-hardening work

It should not be read as:

- full device-operations maturity
- full measurement-trust execution
- bounded controls
- parcel adaptation
- route or block resilience

In other words, `v0.1` is a release label, not a substitute for either the
capability-stage map or the deployment-maturity overlay.

## Planning rule

Not every important gap belongs in the same version.

Some gaps should become:

- `current v1` constraints or baseline contracts
- `v1.5` support objects and trust surfaces
- `v2` policy or recommendation layers
- `v2.5` control and compatibility surfaces
- `v3` adaptation-memory surfaces
- `v4` route/block and shared-resilience surfaces

The repo also uses a separate deployment-maturity overlay for hardware and
operations. That overlay should carry the field-hardening, serviceability,
maintenance, and device-operations burden rather than being silently folded into
the capability stages.

## At-a-glance placement

| Gap area | Earliest stage where it must become explicit | Why |
| --- | --- | --- |
| device identity, packet timing, buffering, and staleness rules | `current v1` | the parcel-sensing baseline is not honest without them |
| field-hardening and deployment quality | `current v1` plus deployment maturity | a parcel claim depends on where and how the node was installed |
| node health, deployment metadata, and device event history | `v1.5` | these are support objects that should not break the core parcel-state contract |
| measurement-trust and maintenance-informed trust penalties | `v1.5` | stronger trust needs separate support objects and calibration posture |
| observed equipment / house-state signals (read-side HVAC, fan, purifier, backup power, sump) | `v1.5` | bridge objects for response curves; not the same as a full compatibility inventory |
| custody execution and transformation provenance | `current v1` baseline, stronger in `v2` | private-by-default must be technically real before higher-stage sharing grows |
| decision-policy layer above hazard inference | `v2` | guidance should be separate from sensing and hazard estimation |
| compatibility mapping and bounded controls | `v2.5` | control surfaces should wait until the advisory and policy layers are clear |
| adaptation memory and outcome learning | `v3` | repeated-event learning is later than baseline guidance |
| route/block resilience and shared weak-point logic | `v4` | these extend beyond one parcel and depend on the earlier layers |
| replay, simulation, and regression discipline | `current v1` baseline, stronger every stage after | verification is cross-cutting and should grow with each stage |

## `current v1`

### What belongs here

`current v1` is still only parcel sensing and inference.
That means this stage should define the minimum operational architecture needed
to keep the sensing baseline honest, not a full later-stage control platform.

The `v0.1` release may document or publish parts of this baseline, but `v0.1`
is not synonymous with `current v1`.

### Gaps that should be explicit now

#### Device-operations baseline

These do not need to become a large standalone service yet, but they should be
documented and visible in the baseline:

- node identity and registry expectations
- firmware and config version visibility in packets or related records
- first-boot / claim assumptions for reference nodes
- minimal boot-reason and last-seen posture

#### Temporal integrity and resilience baseline

These should be explicit in the current reference path:

- `measured_at`, `recorded_at`, `received_at`, and freshness semantics
- local buffering assumptions for active node families
- idempotent ingest or replay expectations
- outage, stale-data, and late-arrival handling rules
- evidence-mode behavior when local data is delayed or degraded

#### Field-operations baseline

These are already part of honest parcel interpretation and should stay in the
`current v1` baseline:

- field-hardening bundle before any node is called deployed
- node-family maturity targets
- install-quality and mount-quality language
- dry-reference / geometry rules for `flood-node`
- sheltered-placement and serviceability rules for outdoor lanes

#### Privacy-execution baseline

The policy docs are not enough by themselves.
`current v1` should keep these technical boundaries explicit:

- local-only versus uploaded paths
- private, shared, and public custody boundaries
- export, deletion, and revocation baseline behavior
- provenance for any intentionally shared or public output

#### Verification baseline

The baseline should already include:

- schema and example validation
- reference replay and idempotency checks
- evidence-mode and confidence regression checks
- docs that distinguish `implemented`, `partial`, `docs-only`, and `planned`

### What should not be backfilled into `current v1`

Do not quietly redefine `current v1` to mean:

- full device lifecycle automation
- full measurement-trust execution
- bounded control orchestration
- adaptation learning
- route or block resilience intelligence

## `v1.5`

### Role of this stage

`v1.5` is the minimum bridge stage.
It should add separate support objects and trust surfaces without breaking the
core parcel-state contract.

### Gaps that first belong here

#### Device-operations support objects

These should become first-class support surfaces in `v1.5`:

- node-health object
- deployment-metadata object
- device-event object
- heartbeat and lifecycle event posture
- maintenance and replacement traceability

#### Measurement-trust architecture

This is the earliest stage where trust should become more than a single quality
flag:

- sensor-health quality
- deployment-quality penalties
- freshness and completeness penalties
- calibration or correction version visibility
- maintenance-informed trust penalties

#### House and intervention bridge objects

`v1.5` should also hold:

- house-state support objects
- **read-side** equipment-state signals (for example HVAC mode, fan, recirculation vs fresh air, purifier, backup-power posture, sump/pump where available)
- coarse **house-capability** summaries where they describe what exists, not a full integration matrix
- intervention events
- verification outcomes

**Split for honesty:** a full **controls-compatibility inventory** (interface classes such as Matter, Home Assistant, BACnet, smart plugs; integration tiers; control-policy versioning) is primarily **`v2.5`**, not `v1.5`. Draft schema files may exist for forward compatibility, but `v1.5` should not be read as “compatibility mapping is operationally complete.”

These are the minimum additional objects needed so the architecture can evolve
toward adaptation without pretending that the adaptation engine already exists.

## `v2`

### Role of this stage

`v2` is where bounded adaptation guidance becomes real.
This is the right stage to separate hazard estimation from decision policy.

### Gaps that first belong here

- explicit parcel decision-policy layer
- policy versioning and override posture
- recommendation surfaces that are separate from hazard-state certainty
- status reasoning that cites evidence, trust state, and missing evidence
- stronger custody-execution and transformation-provenance rules for outputs that leave the strict private baseline

### Core rule

`parcel confidence <= evidence quality ceiling`

If the measurement or deployment-trust surface is degraded, parcel guidance must
inherit that ceiling rather than silently overclaiming confidence.

## `v2.5`

### Role of this stage

`v2.5` is the first stage where bounded controls and compatibility mapping
should become first-class surfaces.

### Gaps that first belong here

- **compatibility inventory by parcel and interface class** (this is the primary home for the full inventory; `v1.5` may hold drafts or coarse capability hints only)
- advisory-only versus soft-integration versus harder-integration tiers
- failed-control and manual-override logging
- clearer device config and control-policy versioning
- bounded control verification loops

## `v3`

### Role of this stage

`v3` is the parcel adaptation engine stage.
This is where repeated-event learning and service-informed adaptation logic
become justified.

### Gaps that first belong here

- action-effect memory
- repeated-event learning
- stronger recalibration and replacement effects on trust history
- lifecycle-aware adaptation summaries
- parcel-specific response-curve memory

## `v4`

### Role of this stage

`v4` extends beyond one parcel into route, egress, block, and shared-resilience
surfaces.

### Gaps that first belong here

- route and block weak-point logic
- neighborhood-scale external-evidence operations
- node-placement value for shared resilience
- route/block replay and simulation surfaces
- community intervention ranking and refuge planning support

## Cross-cutting deployment-maturity overlay

Some architecture gaps are best placed on the hardware and operations overlay,
not only on the capability roadmap.

### `deployment maturity v0.1`

Bench prototype and bring-up posture:

- basic node identity
- provisional calibration
- prototype power and wiring
- serial or local validation center of gravity

### `deployment maturity v1.0`

First field-hardened parcel kit:

- protected power
- local buffering or durable storage
- connectorized/serviceable wiring
- enclosure and mounting posture
- physical identity labels
- service-access posture
- install metadata sufficient for honest interpretation

### `deployment maturity v1.5`

Trust and device-operations hardening:

- stronger node-health reporting
- maintenance logging
- calibration/correction versioning
- buffer and freshness execution
- device lifecycle and replacement history

### `deployment maturity v2.0`

Decision-policy and adaptation support on top of a hardened evidence path:

- policy versioning
- stronger verification and replay posture
- trust-aware operational guidance
- adaptation support that depends on hardened evidence quality

## Recommended sequencing rule

When a missing surface appears, ask two questions:

1. Is this required to keep `current v1` honest?
2. If not, what is the earliest later stage where it should become a first-class surface?

That prevents two common failures:

- overloading `current v1` with later-stage architecture
- leaving baseline operational assumptions so vague that `current v1` overclaims maturity

## Related docs

- `phase-roadmap.md`
- `deployment-maturity-ladder.md`
- `version-and-promotion-matrix.md`
- `node-taxonomy.md`
- `integrated-parcel-system-spec.md`
- `../../contracts/v0.1/README.md`
- `../../hardware/parcel-kit/field-hardening-checklist.md`
- `../../hardware/parcel-kit/pilot-field-kit.md`
```

### File: `architecture/system/phase-roadmap.md`

```md
# Phase Roadmap

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

### Key additions

- house-state data such as indoor PM2.5, indoor temperature/RH, HVAC mode, fan state, recirculation/fresh-air state, purifier state, and backup-power state
- building and site metadata such as orientation, exposure, shading, low points, drainage paths, vent locations, HVAC type, filter path, filter size, and higher-MERV capability
- intervention and response records such as action logs, outcome logs, and before/after response windows
- **read-side** equipment-state and coarse capability hints (what exists / what is observed), without requiring a full **controls-compatibility inventory** — that inventory (interface classes, integration tiers, policy versioning) is primarily **Stage D / `v2.5`**

### Design rule

Keep parcel-state mostly stable in this stage.
Store the new `v1.5` data in separate support objects rather than overloading the current state contract.

### Core success test

Can the platform begin measuring response curves such as outdoor PM versus indoor PM, outdoor heat versus indoor heat response, rainfall versus low-point/access degradation, and action timestamp versus improvement?

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
```

### File: `architecture/system/product-requirements-phase-1.md`

```md
# Product Requirements: Current v1 Home Resilience Assistant

## Purpose

Define the current `v1` single-parcel release that delivers immediate value with one participating home and no neighborhood dependency.

## Product statement

The current `v1` release helps occupants understand current home and parcel conditions, why those conditions matter, and what actions to consider during environmental disruption.

## Primary product promise

Useful alone on day one.
More informative when public context is available.
Honest about uncertainty.
Not yet a full parcel adaptation or automation system.

## Version boundary

`current v1` is the parcel sensing and inference baseline.

It should prove:
- local sensing
- parcel-state inference
- confidence, freshness, and provenance
- private-by-default data handling
- partial-adoption usefulness

It should not yet claim:
- intervention verification as a product guarantee
- ranked retrofit optimization
- automation compatibility as a core UX promise
- autonomous protective house behavior

## Target user

Primary user:

- a parcel operator or renter who wants home-specific resilience guidance during smoke, heat, flood, freeze, or outage conditions

Secondary users:

- caregivers
- highly weather-exposed households
- households with poor public-data fit due to microclimate or drainage variation

## Core jobs to be done

- tell me what is happening at my home right now
- tell me if the situation is getting worse
- tell me what the system is basing that on
- tell me what reasonable actions I should consider now
- help me prepare before conditions become severe

## In-scope hazards for current v1

- smoke and indoor air burden
- heat burden
- flooding and runoff where local sensing is available
- freeze and cold burden where supported
- outage and shelter readiness

## User-facing objects

### Readiness cards

The home screen should present a small set of readiness states:

- shelter readiness
- air quality readiness
- heat readiness
- flood readiness
- power readiness
- route readiness

Each state should include:

- current label
- confidence
- freshness
- short why-this-status explanation
- recommended next steps

### Event timeline

The user should be able to see:

- what changed
- when it changed
- whether the situation is improving, stable, or worsening

### Evidence view

The product should let the user inspect:

- local observations
- public context used
- parcel priors applied
- where local conditions diverged from regional baseline
- what the public-only path would have concluded
- missing evidence
- stale evidence

## Functional requirements

### FR1: Current parcel-state generation

The system shall generate current readiness states from:

- local sensor observations
- parcel and home context
- optional public context
- explicit freshness and confidence logic

The system shall also preserve, inside the parcel-state output:

- parcel-prior application details
- local-versus-public divergence records
- a public-only counterfactual path for explanation and later scoring

### FR2: Conservative recommendation engine

The system shall provide parcel operator-readable next-step recommendations tied to current state and evidence mode.

Recommendations should:

- be specific enough to be useful
- avoid pretending to be official emergency instructions
- degrade to generic preparedness language when evidence is weak

### FR3: Hazard-specific trend detection

The system shall identify when conditions are:

- worsening
- improving
- stable
- stale or unknown

For hazards with public baseline context, the system shall also identify when
local parcel conditions materially diverge from the regional baseline.

### FR4: Alerting

The system shall notify the user when:

- a readiness state worsens materially
- confidence drops enough to affect interpretation
- a key sensor goes stale or unhealthy
- public context indicates newly elevated concern

### FR5: Sensor-health awareness

The system shall expose whether conclusions are limited by:

- sensor location
- stale readings
- connectivity loss
- read failures
- unsupported hazard observability

### FR6: Setup and context capture

The product shall capture enough home and parcel context to improve interpretation, such as:

- indoor, sheltered, or outdoor installation mode
- basic parcel characteristics
- relevant structure characteristics
- optional user-specified sensitivities or priorities later

### FR7: Honest stage boundary

The system shall not imply that later-stage adaptation features already exist in the current product.

Examples:
- recommendations may mention recirculation or filtration if available, but the product should not imply that HVAC state is already being monitored unless that data path actually exists
- the product may reference future support for intervention verification, but it should not present verification claims as current `v1` functionality

## Non-functional requirements

### NFR1: Truthfulness

The product shall prefer `unknown` or low-confidence outcomes instead of stronger but weakly supported claims.

### NFR2: Privacy

The product shall default to private household data handling and make any sharing decision explicit and reversible.

### NFR3: Explainability

Every major state shall be accompanied by enough explanation for a user to understand the result.

For any parcel state influenced by public context, the explanation should be able
to answer:

- what public data alone would have concluded
- what local parcel evidence changed
- which parcel metadata priors shaped the baseline expectation

### NFR4: Graceful degradation

The product shall remain usable when:

- public context is unavailable
- sensors are partially stale
- connectivity is degraded

### NFR5: Low operational burden

The product shall avoid overwhelming the user with noisy alerts or complex setup steps.

### NFR6: Democratic and operator-controlled posture

The product shall preserve parcel stewardship, private-by-default handling, and voluntary participation so the network can grow without becoming a centralized household surveillance system.

## Candidate current-v1 recommendations

### Smoke and air

- close windows
- switch HVAC to recirculate if available
- run filtration
- move to the cleanest room
- delay outdoor activity
- ventilate only during a safer outdoor window

### Heat

- move activity to the coolest room
- pre-cool before forecast heat if possible
- close blinds or shade exposed rooms
- start backup cooling plan
- hydrate and reduce exertion

### Flood and runoff

- inspect drains and low points
- move vulnerable items
- avoid specific routes if route confidence is low
- prepare barriers or pumps if already owned

### Freeze

- protect exposed pipes
- maintain minimum indoor temperature
- drip pipes if appropriate for the user’s locale and setup

### Outage

- check backup power status
- reduce nonessential loads
- preserve device charging
- prepare shelter-in-place resources

## Current-v1 data requirements

- local sensor observations
- sensor health metadata
- parcel identifier and basic context
- home installation context
- public smoke and weather context where available
- event history for trend detection

## Minimum bridge after current v1

The next stage after this product is `v1.5`, not a jump directly to automation.

`v1.5` adds:
- indoor PM2.5
- indoor temperature and RH
- HVAC mode, fan state, and recirculation/fresh-air state
- purifier state
- backup-power state
- building and site metadata for orientation, shading, drainage, and filter-path constraints
- intervention and outcome logging
- coarse house capability and equipment-state support objects

Full control-compatibility inventory belongs later with bounded-controls work
rather than in the minimum `v1.5` bridge.

These additions should land as separate support objects instead of breaking the current parcel-state shape.

## Phase-1 success metrics

- a user can explain the current home state in plain language
- recommendation cards are opened and acted on during meaningful events
- alert precision is acceptable to pilot users
- users report value during both routine and elevated conditions
- the product remains useful even without neighbor participation
- the system can quantify whether local evidence improved prediction quality versus the public-only baseline

## Explicit non-goals

- neighborhood mutual-aid coordination
- raw shared block maps
- city dashboards
- exact wildfire-front or evacuation prediction
- medical diagnosis
- authoritative emergency command language
- bounded automation or device control
- verified adaptation-performance scoring
- parcel-specific retrofit ranking

## Risks and watchouts

- overclaiming on hazards the current hardware cannot directly observe
- confusing indoor microclimate readings with parcel-wide outdoor truth
- alert fatigue
- legal exposure from recommendation language
- weak setup information leading to misinterpretation

## Dependencies for later phases

- recommendation engine policy
- neighborhood signal transformation methods
- additional hardware classes for flood, wind, and other hazards
- block-level governance and sharing controls
- `v1.5` support objects for house state, coarse capability / equipment state, intervention, and verification
- later `v2.5` control-compatibility inventory and bounded-controls policy
```

### File: `../oesis-public-site/src/app/roadmap/page.tsx`

```tsx
import Link from "next/link";
import { ProgramPhasesRoadmap } from "@/components/ProgramPhasesRoadmap";
import { ScopeCallout } from "@/components/ScopeCallout";
import { buildMetadata } from "@/lib/metadata";
import { programPhases } from "@/data/siteContent";

const pageTitle = "Roadmap | Open Environmental Sensing and Inference System";
const pageDescription =
  "Nine-phase program roadmap: goals, main deliverables, and current status for the OESIS public initiative.";

export const metadata = buildMetadata({
  title: pageTitle,
  description: pageDescription,
  pathname: "/roadmap/"
});

export default function RoadmapPage() {
  return (
    <>
      <section className="page-intro">
        <p className="eyebrow">Program</p>
        <div className="section-head page-intro-head">
          <div>
            <h1>Roadmap</h1>
            <p className="lede">
              The full program has long-range scope. Read phases as a <strong>now / next / later</strong> story:{" "}
              <strong>Active</strong> and <strong>Next</strong> describe what the initiative is emphasizing now and
              immediately after; <strong>Planned</strong> phases are direction—not a claim that later-stage capabilities
              are already operational. For the problem and evidence model in plain language, see{" "}
              <Link href="/why-it-matters/">Why it matters</Link> and <Link href="/how-it-works/">How it works</Link>.
            </p>
            <p className="lede">
              Expectations belong on a patient timeline: the most consequential value—trusted parcel-scale practice,
              neighborhood adoption, and verified loops in the field—will most likely compound over{" "}
              <strong>many years</strong>, on the order of a <strong>decade</strong>, not inside a single phase label.
              The roadmap exists to keep that honest: narrow shipped slices now, staged direction later.
            </p>
          </div>
        </div>
      </section>

      <ScopeCallout />

      <section className="panel roadmap-panel program-phases-panel">
        <div className="section-head">
          <div>
            <p className="section-kicker">Nine phases</p>
            <h2>Phased roadmap</h2>
            <p>
              For narrative context on why these phases exist, see <Link href="/program/">Program</Link>.
              Engineering-style version labels and intermediate capabilities remain documented there for implementers.
            </p>
          </div>
        </div>
        <ProgramPhasesRoadmap phases={programPhases} />
      </section>
    </>
  );
}
```
