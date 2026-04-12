# ADR 0001: Bench-Air Claim Boundary

- Status: Proposed
- Date: 2026-03-30
- Owners: Open Environmental Sensing and Inference System
- Related workstreams:
  - hardware/bench-air-node
  - software/ingest-service
  - software/inference-engine
  - software/parcel-platform
  - legal/privacy

## Context

The bench-air-node is the first concrete evidence producer in the Open
Environmental Sensing and Inference System repo. It already has a packet
schema, firmware notes, and a reference ingest-to-parcel pipeline.

That makes it useful as the first end-to-end validation device, but also creates a risk: the system can begin implying parcel-level hazard confidence that the bench-air-node is not capable of supporting by itself.

The node is currently described as an indoor or sheltered USB-powered build with temperature, humidity, pressure, and gas-trend sensing. Its BME680 or BME688 gas-resistance output is useful for trend detection, not as a direct pollutant concentration or smoke concentration measurement. Indoor or sheltered placement can also be strongly biased by HVAC, cooking, direct sun, garages, and other local conditions.

The repo therefore needs a clear architectural boundary between:

- what the bench-air-node can honestly measure
- what the platform may infer from it with clear limitation language
- what it must not imply from bench-air evidence alone

## Decision

The bench-air-node is designated as an evidence producer and pipeline-validation node, not a standalone parcel hazard truth source.

The following claims are allowed from bench-air evidence:

- local indoor or sheltered microclimate observations
- temperature and humidity trend reporting at the install location
- pressure reporting at the install location
- gas-resistance trend changes worth flagging for inspection
- device-health and packet-freshness reporting
- low-confidence parcel evidence input when combined with explicit uncertainty handling

The following claims are not allowed from bench-air evidence alone:

- direct smoke concentration measurement
- parcel-wide outdoor smoke condition
- parcel-wide outdoor heat condition
- flood condition
- authoritative shelter, reentry, egress, or asset-safety claims
- strong parcel status transitions without corroborating evidence or explicit `unknown` handling

The following product rules apply:

- Bench-air gas-resistance values must be treated as anomaly or trend signals, not direct smoke concentration.
- Indoor or sheltered bench-air readings must not be presented as equivalent to parcel-wide outdoor conditions.
- When bench-air evidence is the only available local input, parcel-state outputs should bias toward `unknown` or low-confidence estimates unless public context and parcel context materially support a stronger claim.
- Parcel operator-facing language must describe bench-air as one evidence layer, not as parcel truth.
- Reference implementations may demonstrate pipeline behavior, but they must not be mistaken for production-valid hazard logic.

## Consequences

Positive consequences:

- keeps the first MVP honest about what is and is not directly observed
- preserves bench-air as a high-value bring-up tool without overclaiming
- reduces the risk of teaching the wrong inference posture through example code
- creates a cleaner upgrade path to `mast-lite`, `weather-pm-mast`, and `flood-node`

Negative consequences:

- bench-air-only demos may appear less decisive because more outputs should remain `unknown` or low confidence
- some current example inference behavior will need to be revised
- the parcel platform may need to emphasize evidence and freshness before status certainty

## Alternatives considered

Treat bench-air as an MVP parcel smoke and heat node.

This was rejected because it would encourage stronger parcel claims than the current hardware and install context can support.

Rely on UI copy alone to soften overclaim risk.

This was rejected because the architectural boundary should exist in system design and inference rules, not only in product wording.

## Follow-up work

- revise `software/inference-engine/scripts/infer_parcel_state.py` so bench-air evidence does not behave like direct smoke concentration
- document parcel context fields required to interpret indoor, sheltered, and outdoor observations
- define evidence-mode and observability rules that distinguish direct observation from inference
- update parcel-platform presentation guidance so bench-air-only outputs emphasize uncertainty
