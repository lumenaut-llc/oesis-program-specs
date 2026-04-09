# Implementation Posture v0.1

## Purpose

Tie the current architecture to the current executable and documented reference
state.

## Status

Current reference implementation posture.

## Canonical homes

- sibling repo `../oesis-runtime`
  Canonical implementation tree for the current reference services.
- `../../../../oesis_build/`
  Canonical build-foundation implementation tree.
- `../../software/*/architecture.md`
  Subsystem-local architecture explanation.
- `../../contracts/`
  Formal contracts, schemas, and examples.
- `../../legal/privacy/` and `../../legal/`
  Policy constraints that shape implementation behavior.

## Current execution evidence

The current local reference posture is anchored by:

- `make oesis-validate`
- `make oesis-check`
- `make oesis-http-check`

These checks are the minimum evidence for calling a surface implemented in the
current reference path.

## Version versus status

Keep these concepts separate:

- `v0.x` version labels describe accepted product slices
- `implemented`, `partial`, `docs-only`, and `planned` describe maturity within
  or around those slices

A new `partial` node lane or documented boundary does not automatically justify
promoting a new `v0.x`.

## Current coverage

### Implemented

- example payload validation
- reference packet-to-parcel pipeline
- local ingest API
- local inference API
- local parcel-platform API
- bench-air packet normalization

### Partial

- mast-lite through the current shared packet lineage
- rights request, export, retention, and operator-access utilities
- shared-map aggregate API
- several hardware build/install lanes beyond the smallest indoor slice

### Docs-only or planned

- richer sharing-settings and consent surfaces
- revocation as a product guarantee
- flood-specific observation family
- weather-pm outdoor observation family
- thermal scene observation family
- public parcel-resolution map support

## Alignment rule

`v0.1` architecture claims should not outrun the implementation-status
classification used in:

- `../../release/v.0.1/implementation-status-matrix.md`

If a surface is only `partial`, `docs-only`, or `planned`, the architecture
should say so.

If a broader accepted runnable slice is promoted later, update the versioned
architecture documents and the evidence set together rather than treating status
changes alone as a version bump.
