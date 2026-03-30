# Data Model

## Purpose

Canonical definitions for parcels, nodes, observations, states, permissions, and provenance.

## Minimum contents

- packet schemas from hardware and external feeds
- normalized observation objects
- parcel-state outputs
- provenance and freshness fields
- identity and permission linkages

## Current status

Parcel-state fields are stubbed in `parcel-state-schema.md`. The first concrete evidence contract should be documented in `node-observation-schema.md` for the bench-air-node MVP.

Machine-readable starter artifacts now live in:
- `schemas/node-observation.schema.json`
- `schemas/parcel-state.schema.json`
- `examples/node-observation.example.json`
- `examples/normalized-observation.example.json`
- `examples/parcel-state.example.json`

## Related workstreams

- hardware node design
- ingest service contracts
- inference engine inputs
- privacy and governance

## Next docs to add

- `node-observation-schema.md`
- node registry model
- provenance summary model
