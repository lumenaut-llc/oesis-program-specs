# Architecture

## Summary

The ingest service is the trust boundary between raw evidence producers and the rest of the platform. It receives packets from dwelling-associated nodes and selected public feeds, checks whether the payloads are structurally valid and current enough to use, converts them into canonical observation objects, and publishes those observations for downstream reasoning.

In `v0.1`, this is also the practical home/platform collection boundary. The
first meaning of network is getting node data into this ingest path reliably
enough for parcel reasoning to begin.

The accepted current-truth slice is still centered on the `bench-air-node`
path. `mast-lite` shares that packet lineage, but treating the two-node indoor +
sheltered-outdoor path as a promoted baseline is a **program-phase `v0.2`**
question tied to architecture, runtime behavior, and evidence together rather
than docs alone. See `../../architecture/system/version-and-promotion-matrix.md`.

The next important ingest expansion is **not** merely more outdoor weather
hardware. The next meaningful bridge surfaces are:

- indoor-response observations
- power-state observations
- equipment-state snapshots
- action-log events
- outcome / verification records

Those are the ingest-side prerequisites for moving from parcel sensing toward
the later **hazard → house state → action → verified outcome** chain.

## Core objects

- raw packet
- collection path / ingest receipt
- ingest receipt
- normalized observation
- node registry entry
- ingest error record
- provenance summary

## Inputs

- hardware node packets: `oesis.bench-air.v1`, `oesis.circuit-monitor.v1`,
  `oesis.weather-pm-mast.v1`, `oesis.flood-node.v1`
- future external feeds such as weather, smoke, or flood context
- node registration metadata
- optional transport metadata such as remote IP, signal quality, or retry count

## Outputs

- canonical observation records
- ingest acknowledgements or error responses
- dead-letter or quarantine records for invalid payloads
- freshness and health summaries for downstream consumers

Planned next bridge outputs should also include support-object persistence or
event publication for:

- indoor PM / temperature / RH observations
- mains / backup-power posture
- HVAC / purifier / recirculation / similar equipment state
- action and verification records tied to later response windows

## Internal modules

- transport adapter
- schema validator
- node identity and authorization check
- normalizer
- persistence writer
- event publisher
- quarantine logger

## External dependencies

- node registry or configuration store
- observation storage backend
- message bus or job queue
- clock source for server-side receipt timestamps
- policy inputs from privacy and governance docs

## Realtime needs

- Node-originated packets should be accepted with low latency so a single parcel can see recent conditions quickly.
- The service should tolerate intermittent connectivity and out-of-order arrival.
- Exact realtime guarantees are less important than trustworthy freshness metadata.

## Risks

- mixing transport concerns with schema concerns until neither boundary is clear
- accepting stale or replayed packets without enough provenance to detect them
- over-normalizing early and losing raw evidence needed for debugging
- baking parcel-specific logic into ingest instead of keeping it in inference
- retaining more personally sensitive metadata than necessary
