# Contracts

## Purpose

Canonical contract definitions for parcels, nodes, observations, states, permissions, provenance, and later-stage support objects.

## Minimum contents

- packet schemas from hardware and external feeds
- normalized observation objects
- parcel-state outputs
- provenance and freshness fields
- identity and permission linkages

## Current status

The current center of gravity remains the `current v1` observation, parcel-context, and parcel-state contracts.

`v1.5` adds separate support objects for:
- house state
- house capability
- control compatibility
- intervention events
- verification outcomes

Those support objects should not be mistaken for a breaking change to the current parcel-state contract.

Machine-readable starter artifacts now live in:
- `schemas/node-observation.schema.json`
- `schemas/node-registry.schema.json`
- `schemas/parcel-state.schema.json`
- `schemas/house-state.schema.json`
- `schemas/house-capability.schema.json`
- `schemas/control-compatibility.schema.json`
- `schemas/intervention-event.schema.json`
- `schemas/verification-outcome.schema.json`
- `schemas/sharing-settings.schema.json`
- `schemas/consent-record.schema.json`
- `schemas/rights-request.schema.json`
- `schemas/shared-neighborhood-signal.schema.json`
- `schemas/sharing-store.schema.json`
- `schemas/operator-access-event.schema.json`
- `schemas/rights-request-store.schema.json`
- `schemas/export-bundle.schema.json`
- `schemas/retention-cleanup-report.schema.json`
- `examples/node-observation.example.json`
- `examples/node-registry.example.json`
- `examples/normalized-observation.example.json`
- `examples/parcel-state.example.json`
- `examples/house-state.example.json`
- `examples/house-capability.example.json`
- `examples/control-compatibility.example.json`
- `examples/intervention-event.example.json`
- `examples/verification-outcome.example.json`
- `examples/sharing-settings.example.json`
- `examples/consent-record.example.json`
- `examples/rights-request.example.json`
- `examples/shared-neighborhood-signal.example.json`
- `examples/sharing-store.example.json`
- `examples/operator-access-event.example.json`
- `examples/rights-request-store.example.json`
- `examples/export-bundle.example.json`
- `examples/retention-cleanup-report.example.json`

## Related workstreams

- hardware node design
- ingest service contracts
- inference engine inputs
- privacy and governance

## Next docs to add

- `node-observation-schema.md`
- provenance summary model
- sharing settings model
- consent record model
- rights request model
- shared neighborhood signal model
- sharing store model
- operator access event model
- rights request store model
- export bundle model
- retention cleanup report model
