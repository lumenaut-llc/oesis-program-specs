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
- house capability and control-compatibility records
- intervention events
- verification outcomes

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

- compatibility inventory by parcel and interface class
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
- `integrated-parcel-system-spec.md`
- `../data-model/README.md`
- `../build-guides/field-hardening-checklist.md`
- `../build-guides/pilot-field-kit.md`
