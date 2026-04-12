# Technical Philosophy v0.1

## Purpose

State the current technical philosophy that shapes the OESIS reference
architecture.

## Status

Current reference philosophy.

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

### Prefer explicit uncertainty

Freshness, provenance, confidence, evidence mode, and reasons should remain
visible throughout the stack.

### Governance is an architecture input

Sharing, privacy, publication, revocation, export, and claims boundaries should
shape technical behavior directly rather than living only in prose.

### Use canonical contracts and thin wrappers

One canonical implementation or contract surface should exist per concern, with
thin compatibility layers around it when needed for docs, runbooks, or operator
flows.

## Related docs

- `../../architecture/system/technical-philosophy-and-architecture.md`
- `../../architecture/system/integrated-parcel-system-spec.md`
- `reference-stack.md`
- `minimum-functioning-v0.1.md`
- `component-boundaries.md`
