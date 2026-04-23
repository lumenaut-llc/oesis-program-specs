# Component Boundaries v0.1

## Purpose

Define the current architectural ownership boundaries across implementation,
contracts, subsystem docs, and governance.

## Status

Current reference boundary map.

## Boundary layers

### Canonical implementation

- sibling **`oesis-runtime`** checkout (`../../../oesis-runtime` from this file;
  **`../oesis-runtime`** from the program-specs repository root)

This is the current executable truth for the reference services.

### Subsystem architecture and operator surface

- `../../software/ingest-service/`
- `../../software/inference-engine/`
- `../../software/parcel-platform/`
- `../../software/shared-map/`

These directories explain local responsibilities, interfaces, risks, and
operator-facing execution paths.

### Formal contracts

- `../../contracts/`

Schemas, examples, and contract definitions live here rather than in the
versioned architecture canon.

### Program-level technical posture

- `technical-philosophy.md`
- `reference-stack.md`
- `implementation-posture.md`
- `../system/calibration-program.md`
- `../system/adapter-trust-program.md`

These files define the current cross-subsystem architecture.

### Governance and release constraints

- `../../legal/privacy/`
- `../../legal/`

These materials constrain what the architecture may do and claim.

## Boundary rules

- ingest accepts and normalizes evidence but should not become the hazard engine
- inference reasons about parcel state but should not become the UI layer
- parcel platform presents parcel state but should not recompute inference
- shared-map stays downstream of parcel-private reasoning and policy-gated
- docs-facing wrappers should not become competing implementations of the sibling
  **`oesis-runtime`** checkout (see **Canonical implementation** above)
- calibration program and adapter-trust program own admissibility policy; ingest enforces and emits the decision; inference and parcel-platform consume but do not override
- build specs in `oesis-builds/specs/<node>/` and adapter specs in `oesis-builds/specs/adapters/<adapter>/` own the §F metadata declaration; program-specs owns the policy those specs declare against

## Version rule

Subsystems and major features should identify which architecture
version they target and what their status is relative to that version.
