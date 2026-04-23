# Technical Philosophy And Architecture

## Lane

This document is the `system/` lane version of this topic.

Use it for the broader technical posture and architecture doctrine that spans
versioned lanes.

If you need the frozen current-truth philosophy for the accepted `v0.1`
reference slice, use `../current/technical-philosophy.md`.

## Purpose

Define the canonical technical philosophy for Open Environmental Sensing and
Inference System and show how that philosophy turns into system architecture.

This document is the top-level technical posture reference.
Use it to explain why the system is structured the way it is before dropping
into subsystem-specific architecture docs.

## Versioned placement

The current versioned architecture canon now lives under:

- `../../architecture/README.md`
- `../../architecture/current/technical-philosophy.md`
- `../../architecture/v1.0/README.md`

## Technical philosophy

### 1. Start with one parcel, not the network

The system should be useful for one home before neighborhood participation is
added.

That means the first technical question is not "how do we aggregate a map?" but
"how does one parcel produce an honest, inspectable condition estimate from the
evidence it has?"

Network effects matter, but they improve precision and coverage.
They do not unlock the basic right to usefulness.

### 2. Treat the parcel as one system

A parcel may use multiple purpose-built nodes, but it should still behave as one
coherent technical system with:

- one parcel identity
- one node registry
- one ingest path
- one inference engine
- one dwelling-facing parcel view
- one privacy and sharing policy surface

The architecture should converge many device roles into one parcel-level
experience rather than forcing users to reason about disconnected subsystems.

### 3. Keep hardware modular when the world is modular

Different hazards and placements demand different physical forms.

The technical architecture should not force every sensor into one chassis if
that reduces placement quality, calibration honesty, or maintainability.

The parcel kit is a coordinated system of nodes, not a requirement for one
physical enclosure.

### 4. Preserve evidence boundaries

The system should keep a strict separation between:

- raw packets and external feeds
- normalized observations
- inferred parcel-state outputs
- parcel operator presentation
- shared neighborhood outputs

Each stage exists for a reason.
When stages blur together, provenance gets weaker and the product starts making
claims it cannot justify.

### 5. Prefer explicit uncertainty over false smoothness

The technical system should preserve:

- provenance
- freshness
- confidence
- evidence mode
- reasons and explanation payloads

The user experience may simplify presentation, but the architecture must make it
possible to inspect why a result exists and how strong the evidence is.

### 6. Keep privacy and governance inside the design, not outside it

Privacy, sharing, revocation, export, retention, and publication limits are not
documentation afterthoughts.
They are architecture inputs.

Technical components should be designed so privacy and governance rules can
constrain behavior directly instead of being bolted on after implementation.

### 7. Use canonical contracts and thin wrappers

The architecture should prefer one canonical implementation or contract surface
per concern, with thin compatibility layers around it when necessary.

That keeps runbooks, smoke checks, documentation paths, and operator flows
stable without creating multiple competing implementations of the same logic.

### 8. Documentation is part of the technical system

The repo's technical side includes executable code, machine-readable schemas,
operating constraints, and the docs that define boundaries between them.

If the docs and the system behavior diverge, the architecture has failed even if
the code still runs.

### 9. Admissibility is part of evidence boundaries, not an inference side-effect

The system should treat calibration posture and admissibility decisions as
first-class evidence-layer facts, not as ingest hygiene or inference
implementation details.

Two architectural commitments follow:

- **Schema carries the facts, runtime computes the decision.** The canonical
  observation schema carries the facts admissibility depends on (burn-in state,
  calibration session reference, deployment class, protective-fixture
  verification, adapter source authority); the admissibility decision itself —
  the boolean plus reason codes — lives on the normalized observation in
  runtime. This keeps schema stable as admissibility policy evolves, and
  preserves the reasoning trail for audit.

- **Physical-sensor trust and adapter-derived trust are parallel programs.**
  Physical sensors are governed by the calibration program (reference
  instruments, burn-in, drift); adapter-derived evidence (Tier 1 passive
  inference, Tier 2 cloud APIs) is governed by the adapter-trust program
  (source authority, API contract version, schema-drift detection). Both
  produce the same admissibility output through different evidence paths; the
  programs must stay independent to avoid conflating physical and API-contract
  failure modes.

Canonical docs:
[`integrated-parcel-system-spec.md`](integrated-parcel-system-spec.md)
"Calibration and admissibility layer";
[`calibration-program.md`](calibration-program.md);
[`adapter-trust-program.md`](adapter-trust-program.md).

## Architectural shape

### Layer 1. Evidence collection

Purpose-built nodes and selected external feeds generate raw evidence.

Examples include:

- indoor and sheltered parcel nodes
- outdoor reference nodes
- optional hazard-specific nodes
- selected public weather or smoke context

This layer is about evidence capture, not hazard judgment.

### Layer 2. Collection and ingest boundary

In `v0.1`, the first meaning of network is moving node data into the
home/platform ingest path.

Collection exists so parcel reasoning begins with real evidence availability
rather than with abstract parcel conclusions.

### Layer 3. Ingest trust boundary

The ingest service is the trust boundary between raw evidence producers and the
rest of the stack.

Its responsibilities are:

- receive packets and selected feeds
- validate structure and basic acceptability
- normalize inputs into canonical observations
- preserve provenance and freshness context
- reject, quarantine, or flag malformed inputs

Ingest should not quietly become the hazard engine.

### Layer 4. Canonical observation and context model

Once evidence is accepted, it should live in canonical forms that downstream
components can reason about consistently.

This layer includes:

- node registry and parcel identity records
- normalized observations
- parcel context
- public context
- sharing and rights-control records

Canonical data contracts are how the system stays modular without becoming
ambiguous.

### Layer 5. Parcel inference

Inference combines parcel evidence, parcel context, and allowed external context
into parcel-state outputs.

This layer should:

- compute condition estimates rather than hidden magic scores
- distinguish observed evidence from inferred conclusions
- keep uncertainty visible
- apply policy constraints to shared or public-context use

Inference is where reasoning belongs.
It should not be spread across ingest, UI, or map publication layers.

### Layer 6. Parcel operator parcel surface

The parcel platform is the primary product surface.

Its job is to turn parcel-state outputs into a parcel operator-readable, inspectable
experience with:

- current parcel status
- freshness and confidence framing
- explanation and provenance summaries
- sharing settings and rights controls

This layer should present the reasoning clearly without recomputing it.

### Layer 6. Optional shared neighborhood surface

Shared outputs are downstream, optional, and policy-gated.

The shared map exists to provide coarse neighborhood condition context without
turning parcel participation into public parcel surveillance.

This layer should stay:

- thresholded
- delayed when needed
- spatially coarsened
- explicit about participation limits
- separate from parcel-private views

## Cross-cutting architecture rules

### One parcel identity surface

Every technical path should converge on a single parcel identity model rather
than duplicating parcel meaning across packet formats, UI state, and export
logic.

### One canonical implementation tree per executable concern

For the current MVP reference stack, sibling repo `../oesis-runtime` is the
canonical Python implementation tree.
Implementation work and executable entrypoints should remain in the canonical
runtime tree.

### One canonical data contract per boundary

Hardware packets, normalized observations, parcel-state outputs, and sharing
records should each have explicit schemas or interface docs.

The system should avoid untyped boundary drift where each consumer silently
reinterprets the payload differently.

### One clear separation between parcel-private and broader-shared outputs

The architecture must not let internal convenience erase the distinction between:

- parcel-linked private evidence
- parcel-private inferred outputs
- permitted shared signals
- public-safe publication surfaces

This distinction is part of the technical truth model.

### One honest language boundary

Technical outputs should support condition estimates, provenance, and
confidence.
They should not imply emergency authority, guaranteed safety, or hidden
certainty.

## Current reference implementation posture

The current reference stack follows this technical path:

1. nodes emit versioned packets
2. ingest binds packets to parcel identity and normalizes them
3. inference combines parcel evidence with parcel and public context
4. parcel platform renders the dwelling-facing parcel view
5. shared-map publication remains optional and policy-gated

Current implementation posture:

- sibling repo `../oesis-runtime` is the canonical Python implementation tree
- `Makefile` provides stable human-facing task entrypoints
- the public preview site is a controlled presentation surface, not the owner of
  canonical technical truth

## Technical non-goals

The architecture should not drift into:

- a public parcel surveillance system
- a black-box hazard engine with hidden logic
- one oversized hardware enclosure that ignores placement reality
- a product that becomes useful only after dense network adoption
- a UI layer that quietly reimplements inference
- a governance model that exists only in prose and not in technical controls

## Reading path

Use this document first, then read:

- `integrated-parcel-system-spec.md`
- `../../software/ingest-service/architecture.md`
- `../../software/inference-engine/architecture.md`
- `../../software/parcel-platform/architecture.md`
- `../../software/shared-map/architecture.md`
- `../data-model/README.md`
- `../privacy-governance/README.md`

Together these define the current technical posture from philosophy to
implementation boundary.
