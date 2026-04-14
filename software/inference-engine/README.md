# Inference Engine

## Purpose

The logic layer that turns normalized observations, public context, and explicit uncertainty handling into parcel-level statuses.

## Current responsibilities

- consume normalized observations from the ingest service
- combine parcel evidence with hazard-specific heuristics or models
- produce parcel-state outputs with confidence, freshness, and reasons
- keep provenance attached to every parcel decision
- avoid overclaiming when evidence is sparse, stale, or conflicting

## Needs from other workstreams

- glossary alignment
- governance rules
- procurement assumptions for node capabilities
- hazard model inputs

## MVP focus

The first MVP should support parcel inference from a small evidence set:
- bench-air-node observations
- optional public weather context
- parcel metadata required for basic interpretation

The goal is not perfect classification. The goal is a transparent first-pass parcel state with explicit uncertainty and reasons.

Sheltered-outdoor **`mast-lite`** observations share the bench-air packet contract; treating them as first-class evidence across ingest, trust, and parcel view is part of **program-phase `v0.2`** when promoted — see `../../architecture/system/version-and-promotion-matrix.md`.

## Adjacent systems

- ingest service delivers normalized observations
- parcel platform reads parcel-state outputs
- shared-map may later consume parcel-level summaries
- privacy and governance define which evidence can be shared across parcel boundaries

## Implementation scaffold

Executable inference entrypoints live in the sibling `oesis-runtime`
repository. From that repo root, prefer
`python3 -m oesis.inference.infer_parcel_state` or
`python3 -m oesis.inference.serve_inference_api` for new execution guidance.

The first executable inference reference is
`python3 -m oesis.inference.infer_parcel_state`. It reads a normalized
observation example, applies intentionally simple rules, and emits a parcel-state
snapshot that matches the MVP data contract.
