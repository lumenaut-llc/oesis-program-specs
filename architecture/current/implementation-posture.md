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

- `../../release/2026-04-14/implementation-status-matrix.md`

If a surface is only `partial`, `docs-only`, or `planned`, the architecture
should say so.
