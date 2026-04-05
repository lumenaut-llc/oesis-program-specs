# Data Model Examples

These JSON example payloads are intended as implementation scaffolding for the first MVP contracts.

- `node-observation.example.json`
  Example of a raw node packet from `rhi.bench-air.v1`.
- `node-registry.example.json`
  Example of a parcel-scoped registry binding multiple hardware nodes into one system.
- `normalized-observation.example.json`
  Example of the canonical observation object emitted by the ingest boundary.
- `parcel-state.example.json`
  Example of a homeowner-facing parcel-state snapshot after inference.
- `house-state.example.json`
  Example of the separate `v1.5` house-state support object for indoor conditions and current operating state.
- `house-capability.example.json`
  Example of the separate `v1.5` house-capability support object for protective capacity and physical limits.
- `control-compatibility.example.json`
  Example of the separate `v1.5` control-compatibility support object for interface classes and control locality.
- `intervention-event.example.json`
  Example of a `v1.5` intervention record for a bounded operational action.
- `verification-outcome.example.json`
  Example of a `v1.5` verification record tied to an intervention window.
- `parcel-context.example.json`
  Example of parcel installation context and parcel priors supplied to inference.
- `public-context.example.json`
  Example of optional public external context supplied to inference as supporting evidence.
- `raw-public-weather.example.json`
  Example of a source-shaped public weather payload before adapter normalization.
- `raw-public-smoke.example.json`
  Example of a source-shaped public smoke payload before adapter normalization.
- `shared-neighborhood-signal.example.json`
  Example of a delayed, thresholded neighborhood signal object derived from opt-in shared contributions.

These examples should evolve with the prose contracts and the matching JSON Schema files in `../schemas/`.
