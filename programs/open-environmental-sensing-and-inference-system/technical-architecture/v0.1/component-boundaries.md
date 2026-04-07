# Component Boundaries v0.1

## Purpose

Define the current architectural ownership boundaries across implementation,
contracts, subsystem docs, and governance.

## Status

Current reference boundary map.

## Boundary layers

### Canonical implementation

- `../../../../oesis/`

This is the current executable truth for the reference services.

### Subsystem architecture and operator surface

- `../../software/ingest-service/`
- `../../software/inference-engine/`
- `../../software/parcel-platform/`
- `../../software/shared-map/`

These directories explain local responsibilities, interfaces, risks, and
operator-facing execution paths.

### Formal contracts

- `../../docs/data-model/`

Schemas, examples, and contract definitions live here rather than in the
versioned architecture canon.

### Program-level technical posture

- `technical-philosophy.md`
- `reference-stack.md`
- `implementation-posture.md`

These files define the current cross-subsystem architecture.

### Governance and release constraints

- `../../docs/privacy-governance/`
- `../../legal/`

These materials constrain what the architecture may do and claim.

## Boundary rules

- ingest accepts and normalizes evidence but should not become the hazard engine
- inference reasons about parcel state but should not become the UI layer
- parcel platform presents parcel state but should not recompute inference
- shared-map stays downstream of parcel-private reasoning and policy-gated
- docs-facing wrappers should not become competing implementations of `oesis/`

## Version rule

Subsystems and major features should identify which technical-architecture
version they target and what their status is relative to that version.
