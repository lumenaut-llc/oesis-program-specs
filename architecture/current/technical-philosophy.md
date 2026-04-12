# Technical Philosophy v0.1

## Purpose

State the current technical philosophy that shapes the OESIS reference
architecture.

## Status

Current reference philosophy.

This architecture is fit for the long-term direction only when phase boundaries
are defended: the frozen near-term slice must stay truthful, and future scope must
not be spoken as if it were already executable product reality.

## Core rules

### Parcel first

The system should be useful for one home before neighborhood participation is
added.

### One parcel, one system

Multiple purpose-built nodes may exist, but they should still collapse into one
parcel identity, one ingest path, one inference engine, one dwelling-facing
parcel view, and one privacy/sharing surface.

### Modular hardware, coherent parcel behavior

Hardware should stay modular when placement and sensing needs differ. The
software and product experience should still behave like one parcel system.

Near-term sequencing: treat flood-capable families as **opt-in** and thermal as
**non-core** until air-quality evidence plus parcel context is stable on the
reference path—avoid hardware family sprawl ahead of that stability.

### Preserve evidence boundaries

The architecture keeps clear separation between:

- raw packets and external feeds
- collection and ingest transport
- normalized observations
- inferred parcel-state outputs
- parcel operator presentation
- shared neighborhood outputs

### Collection first for evidence availability

In `v0.1`, network primarily means getting node data into the home/platform
ingest path.

The first functioning version should treat collection and ingest as first-class
realities rather than as hidden plumbing beneath parcel conclusions.

Route-scale and block-scale intelligence stay **downstream** of honest,
repeatable parcel outputs on the reference path—not parallel headline scope.

### Prefer explicit uncertainty

Freshness, provenance, confidence, evidence mode, and reasons should remain
visible throughout the stack.

### Governance is an architecture input

Sharing, privacy, publication, revocation, export, and claims boundaries should
shape technical behavior directly rather than living only in prose.

Prefer a **minimum executable governance loop** in product and runtime over
doctrine that outruns implemented behavior; document claims to match what
operators can actually rely on.

### Use canonical contracts and thin wrappers

One canonical implementation or contract surface should exist per concern, with
thin compatibility layers around it when needed for docs, runbooks, or operator
flows.

## Near-term executable slice (`v0.1`)

Freeze the real near-term architecture in one sentence and repeat it wherever
scope is discussed:

`v0.1` = one parcel, one bench-air lineage, one parcel context, one ingest path,
one inference path, one parcel view

Everything broader is downstream. The next broader program-phase target (`v1.0`,
field-hardened parcel kit and related trust surfaces) stages in the reference
runtime as an optional `v1.0` asset lane merged over this baseline. Phase and lane
vocabulary: `../../program/README.md`, `../../00-version-labels-and-lanes.md`.

## Phase discipline

Guardrails against common failure modes:

- Mixing **version labels**, program **phases**, reference-runtime **lanes**, and
  **public or marketing** release names without saying which one you mean.
- Letting **future** capabilities read as **current** implementation in
  architecture prose, roadmaps, or demos.
- Prioritizing **shared neighborhood intelligence** before **collection and ingest**
  are mature on the reference path.
- **Governance** described beyond what the product and runtime **actually enforce**.
- Adding **hardware families** faster than the reference path stabilizes for one
  lineage.
- Treating **parcel-first** as **parcel-only**, contradicting the stated
  parcel-first, multi-scale direction (see `../../program/README.md`).
- Claiming **deployment or field** maturity beyond what is **repeatable and
  checkable** (reference acceptance paths and implementation posture should stay
  ahead of narrative).

Standardize language around **parcel-first** and **multi-scale** using the program
overview and thesis framing; do not invent competing shorthand.

## Related docs

- `../../program/README.md` — program mission, long-term direction, phase labels
- `../../00-version-labels-and-lanes.md` — glossary for phases and runtime lanes
- `../../04-architecture-review-keep-dangerous-change-now.md` — expanded keep /
  dangerous / change-now review
- `../../architecture/system/technical-philosophy-and-architecture.md`
- `../../architecture/system/integrated-parcel-system-spec.md`
- `reference-stack.md`
- `minimum-functioning-v0.1.md`
- `component-boundaries.md`
