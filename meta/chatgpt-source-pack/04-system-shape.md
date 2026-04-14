---
title: System Shape
status: canonical-summary
updated: 2026-04-13
sources:
  - software/ingest-service/architecture.md
  - software/ingest-service/interfaces.md
  - software/inference-engine/architecture.md
  - software/inference-engine/interfaces.md
  - software/parcel-platform/architecture.md
  - software/parcel-platform/interfaces.md
  - ../oesis-runtime/oesis/inference/infer_parcel_state.py
  - ../oesis-runtime/oesis/inference/serve_inference_api.py
---

# System Shape

This file is the most implementation-near view of what the app and runtime actually do.

It now covers the full runtime software path: ingest architecture and interfaces, inference architecture and interfaces, parcel-platform architecture and interfaces, and the live inference implementation and HTTP surface in the sibling runtime repo.

Conventions for path/label interpretation are defined once in
`README.md` for this source-pack.

## Why This File Exists

This summary is followed by verbatim source-file copies so the synthesized guidance and the underlying canonical text stay together in one markdown.

## Included Source Files

- `software/ingest-service/architecture.md`
- `software/ingest-service/interfaces.md`
- `software/inference-engine/architecture.md`
- `software/inference-engine/interfaces.md`
- `software/parcel-platform/architecture.md`
- `software/parcel-platform/interfaces.md`
- `../oesis-runtime/oesis/inference/infer_parcel_state.py`
- `../oesis-runtime/oesis/inference/serve_inference_api.py`

## Verbatim Source Content

### File: `software/ingest-service/architecture.md`

```md
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

- hardware node packets such as `oesis.bench-air.v1`
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
```

### File: `software/ingest-service/interfaces.md`

```md
# Interfaces

## Public API surfaces

- `POST /v1/ingest/node-packets`
  Accept a single node packet payload plus optional transport metadata.
- `POST /v1/ingest/node-batch`
  Optional future batch endpoint for buffered offline uploads.
- `GET /v1/ingest/health`
  Report service health and current schema support.
- `GET /v1/ingest/schemas`
  Return supported packet schema versions and deprecation status.

## Internal events / jobs

- `observation.normalized`
  Emitted when a packet is accepted and transformed into a canonical observation.
- `ingest.packet.rejected`
  Emitted when validation or authorization fails.
- `node.health.updated`
  Emitted when ingest derives node freshness or repeated-failure signals.
- `ingest.quarantine.created`
  Emitted when a payload should be preserved for manual review.

## Data contracts

Primary MVP contract:
- `oesis.bench-air.v1`
  Defined in `contracts/node-observation-schema.md`

Shared-lineage contract:
- `oesis.bench-air.v1` from `mast-lite`
  Same packet family with outdoor or sheltered install metadata. Treat
  end-to-end use in the widened parcel kit as part of **program-phase `v0.2`**
  promotion rather than proof of a separate current-truth contract by itself.

Planned next bridge contracts:
- indoor-response observation family
  Future `v1.5` bridge input for indoor PM2.5, indoor temperature, and indoor
  RH. This is a priority addition for response modeling, but not part of the
  current implemented MVP contract set yet.
  Minimum useful fields should include:
  - `observed_at`
  - `parcel_id` or parcel-resolvable `node_id`
  - `pm25_ugm3`
  - `temperature_c`
  - `relative_humidity_pct`
  - quality / health flags
- power-state observation family
  Future `v1.5` bridge input for mains up/down and backup-power posture.
  Minimum useful fields should include:
  - `observed_at`
  - `mains_state`
  - `backup_power_present`
  - `backup_power_active`
  - optional richer battery / generator posture later
- equipment-state snapshot family
  Future `v1.5` support input for HVAC mode, fan, recirculation, purifier,
  window/shade, or pump state where available.
  Minimum useful fields should include:
  - `captured_at`
  - `hvac_mode`
  - `fan_state`
  - `air_source_mode` or recirculation vs fresh-air state
  - purifier / shade / pump state where applicable

Planned next bridge support events:
- action-log entry
  Record what the house or household did, such as switching to recirculation,
  starting a purifier, lowering shades, or activating backup power.
- outcome / verification record
  Record whether conditions improved afterward over a bounded response window.

First external adapter contract:
- raw public weather payload
  Normalized by `scripts/normalize_public_weather_context.py` into the canonical public-context object defined in `contracts/public-context-schema.md`
- raw public smoke payload
  Normalized by `scripts/normalize_public_smoke_context.py` into the canonical public-context object defined in `contracts/public-context-schema.md`

Expected minimum request body:

```json
{
  "schema_version": "oesis.bench-air.v1",
  "node_id": "bench-air-01",
  "observed_at": "2026-03-30T19:45:00Z",
  "firmware_version": "0.1.0",
  "location_mode": "indoor",
  "sensors": {
    "sht45": {
      "present": true,
      "temperature_c": 23.4,
      "relative_humidity_pct": 41.8
    },
    "bme680": {
      "present": true,
      "temperature_c": 24.1,
      "relative_humidity_pct": 40.9,
      "pressure_hpa": 1012.6,
      "gas_resistance_ohm": 145230
    }
  },
  "derived": {
    "temperature_c_primary": 23.4,
    "relative_humidity_pct_primary": 41.8,
    "pressure_hpa": 1012.6,
    "voc_trend_source": "gas_resistance_ohm"
  },
  "health": {
    "uptime_s": 1820,
    "wifi_connected": true,
    "free_heap_bytes": 214332,
    "read_failures_total": 0,
    "last_error": null
  }
}
```

Expected acceptance behavior:
- reject packets without a supported `schema_version`
- reject packets without `node_id` or `observed_at`
- accept partial sensor content if presence and failure state are explicit
- attach an `ingested_at` server timestamp
- persist raw packet and normalized observation together or with a traceable link

Normalized observation shape:
- `observation_id`
- `node_id`
- `parcel_id` when node-to-parcel mapping is known
- `observed_at`
- `ingested_at`
- `observation_type`
- `values`
- `health`
- `provenance`
- `raw_packet_ref`

First normalized public-context shape:
- `context_id`
- `source_kind`
- `source_name`
- `observed_at`
- `coverage_mode`
- `parcel_id`
- `hazards`
- `summary`

## Open questions

- Should initial auth rely on shared API keys, signed packets, or a trusted private network boundary?
- How long should raw packets be retained once normalized observations exist?
- Should the ingest service enrich packets with parcel mapping immediately, or leave that join to downstream consumers?
- What freshness threshold should cause a packet to be accepted but marked stale versus rejected outright?
```

### File: `software/inference-engine/architecture.md`

```md
# Architecture

## Summary

The inference engine consumes normalized observations and produces parcel-state snapshots. It should remain separate from ingest so raw evidence handling, schema validation, and transport concerns do not get mixed with hazard reasoning. The engine evaluates each parcel using available evidence, computes hazard-specific probabilities or scores, and then maps those into parcel operator-readable statuses with confidence and explanation payloads.

The engine should produce condition estimates rather than implied safety authorizations, and it should preserve enough provenance for audit without leaking private parcel detail into downstream shared surfaces.

The current parcel-first direction also requires the engine to preserve three
distinct reasoning surfaces inside the parcel-state output:

- parcel metadata priors that shape baseline expectations
- local-versus-public divergence records that expose hyperlocal mismatch
- contrastive fact-versus-foil explanations showing what local evidence changed

The current-truth reference path is still the narrow parcel-sensing baseline.
Support for `mast-lite` as a meaningful second local evidence source belongs to
the widened two-node kit and should be described as **program-phase `v0.2`**
when promoted, not as though the accepted baseline already expanded. Later
**`v1.5`** bridge objects such as house state, action logs, and verification
remain separate support surfaces rather than additions to the current
parcel-state contract.

The next serious product step after that widened kit is the **measurement-to-
intervention bridge**. For inference, that means learning to reason over:

- outdoor hazard evidence
- indoor response evidence
- household operating state
- action records
- measured outcome windows

without collapsing those later surfaces back into the current parcel-state
baseline.

The first serious closed-loop target should be smoke protection:

- outdoor evidence
- indoor PM / temperature / RH response
- bounded household action such as recirculation + fan + purifier
- measured improvement over a bounded response window such as 30–90 minutes

## Core objects

- normalized observation
- parcel context
- hazard evidence set
- hazard score or probability
- parcel-state snapshot
- explanation payload
- divergence record
- public-only counterfactual
- contrastive explanation
- provenance summary

## Inputs

- normalized observations from the ingest service
- parcel metadata such as structure type or node placement context
- parcel-context records describing installation role and parcel priors
- optional shared neighborhood signals when the parcel's sharing mode and policy allow them
- optional public context such as weather or smoke layers
- hazard-specific thresholds or model parameters
- versioned parcel-prior rule configuration
- versioned divergence-threshold configuration
- policy constraints on whether shared neighborhood evidence is allowed for the parcel's active sharing mode

## Outputs

- parcel-state snapshots
- hazard-specific supporting scores
- explanation payloads for UI and auditability
- parcel-prior application summaries
- divergence records with persistence and confidence
- public-only foil outputs for audit and verification
- contrastive explanations with verification placeholders
- confidence and freshness values
- source-mode metadata suitable for provenance summaries

Later bridge and response outputs should remain separate first-class records,
for example:

- response-window comparisons
- intervention recommendations
- verification results

Those should sit beside parcel-state rather than being hidden inside it.

## Internal modules

- parcel evidence assembler
- hazard scoring module
- parcel-prior resolver
- divergence classifier
- uncertainty and freshness evaluator
- status mapper
- contrastive explanation generator
- parcel-state persistence writer
- provenance sanitizer for downstream presentation layers

## External dependencies

- observation store
- parcel metadata store
- optional public hazard feeds
- policy rules from privacy and governance docs
- threshold or model configuration source
- machine-readable public-context freshness policy
- machine-readable hazard-threshold configuration

## Realtime needs

- The engine should update a parcel quickly after new evidence arrives, but correctness and traceability matter more than sub-second latency.
- It should tolerate partial evidence and recompute when new observations fill gaps.
- It should support both event-driven updates and scheduled recomputation.

## Risks

- pretending sparse indoor observations are enough to make strong parcel safety claims
- hiding uncertainty behind a single status label
- mixing hazard scoring rules with presentation logic
- failing to represent stale evidence clearly
- allowing public feeds to overwhelm dwelling-scale local evidence without explanation
- hiding hyperlocal divergence inside a fused score instead of preserving it as evidence
- letting parcel metadata influence outcomes without exposing which factors changed the baseline
- letting shared-neighborhood evidence affect parcel outputs without preserving source distinctions
- letting stale public context continue to influence parcel outputs as if it were current
- adding action or control logic before the system can verify whether conditions
  actually improved
```

### File: `software/inference-engine/interfaces.md`

```md
# Interfaces

## Public API surfaces

- `GET /v1/parcels/{parcel_id}/state`
  Return the latest parcel-state snapshot for the parcel.
- `GET /v1/parcels/{parcel_id}/state/history`
  Return prior parcel-state snapshots and freshness metadata.
- `POST /v1/inference/recompute/{parcel_id}`
  Trigger an explicit recompute for one parcel.
- `GET /v1/inference/models`
  Return active hazard model versions or threshold sets, including public-context policy versions when applicable.

## Internal events / jobs

- `observation.normalized`
  Triggers parcel evidence refresh for affected parcels.
- `parcel.state.updated`
  Emitted when a new parcel-state snapshot is produced.
- `parcel.state.stale`
  Emitted when freshness falls below configured expectations.
- `inference.recompute.requested`
  Used for scheduled backfills or manual reruns.

## Data contracts

Primary input contract:
- normalized observation records from `contracts/node-observation-schema.md`
- optional parcel context records from `contracts/parcel-context-schema.md`
- optional shared neighborhood signal records from `contracts/v0.1/schemas/shared-neighborhood-signal.schema.json`
- optional public context records from `contracts/public-context-schema.md`

Current-truth input posture remains centered on the narrow baseline. Shared-lineage
`mast-lite` observations may feed the engine, but treating them as a promoted
second local evidence lane belongs to **program-phase `v0.2`** in
`../../architecture/system/version-and-promotion-matrix.md`.

Primary output contract:
- parcel-state snapshot defined in `contracts/parcel-state-schema.md`

Minimum parcel-state output fields:
- `parcel_id`
- `computed_at`
- `shelter_status`
- `reentry_status`
- `egress_status`
- `asset_risk_status`
- `confidence`
- `evidence_mode`
- `inference_basis`
- `explanation_payload`
  Includes weighted `evidence_contributions` that the engine uses to derive UI-facing drivers and limitations.
- `reasons`
- `hazards`
- `hazard_statuses`
- `parcel_priors_applied`
- `divergence_records`
- `public_only_counterfactual`
- `contrastive_explanations`
- `freshness`
- `provenance_summary`

Expected engine behavior:
- accept sparse evidence and lower confidence instead of fabricating certainty
- score hazards independently before mapping to parcel-state outputs
- treat local-vs-public divergence as a first-class signal rather than an error to smooth away
- apply parcel metadata as auditable priors before local/public evidence fusion
- represent stale or missing evidence explicitly in `freshness` and `reasons`
- preserve traceable links back to the source observations used for a decision
- preserve traceable links to public context when external evidence contributes to a decision
- preserve distinctions between local private evidence, shared neighborhood evidence, and public context
- emit a public-only foil path so the system can explain what local evidence changed
- preserve verification hooks so later scoring can compare fused predictions against public-only predictions
- avoid emitting language that implies emergency authorization or guaranteed safety
- downgrade or ignore stale public context according to a defined freshness policy
- read hazard thresholds from versioned configuration where practical
- read trust gates for stale-data suppression, low-confidence limits, and disagreement handling from versioned configuration where practical

Required parcel-first explanation posture:

- `divergence_records` should capture direction, magnitude, and persistence of local-versus-public mismatches
- `parcel_priors_applied` should enumerate which parcel fields affected baseline probabilities
- `public_only_counterfactual` should be stable enough for audit and later verification
- `contrastive_explanations` should answer "why this parcel result instead of the public-only result?"

Later **`v1.5`** bridge objects such as house-state and verification records
should influence future recommendation or response surfaces without silently
changing the current parcel-state contract.

Minimum next bridge support inputs should include:

- indoor-response observations with indoor PM2.5, temperature, and RH
- power-state observations with mains and backup-power posture
- equipment-state snapshots for HVAC mode, fan state, recirculation vs
  fresh-air state, purifier state, and related bounded-response signals
- action-log entries describing what the house or household did
- outcome / verification records describing whether measured conditions improved

Priority next closed loop:
- smoke protection should be the first serious end-to-end response proof:
  outdoor evidence, indoor-response evidence, bounded action, then measured
  verification over a defined response window.
- the first useful smoke-response window should support bounded comparisons such
  as outdoor state at trigger time, indoor PM change over roughly 30–90 minutes,
  and whether recirculation / fan / purifier actions corresponded to improvement
- until those bridge objects exist as real support inputs, inference should stay
  honest about being primarily a parcel-state engine rather than a response
  engine.

## Open questions

- Should the first inference logic be rules-based only, or allow lightweight probabilistic models from the start?
- How should parcel context be represented when exact building features are unknown?
- What minimum evidence should be required before any non-`unknown` status is allowed?
- Should public context be treated as supporting evidence only unless local nodes confirm it?
```

### File: `software/parcel-platform/architecture.md`

```md
# Architecture

## Summary

The parcel platform is the presentation and access layer for a single parcel. It should not recompute hazard logic itself. Instead, it reads parcel-state snapshots from the inference engine, combines them with parcel metadata and safe-to-display provenance details, and renders a parcel operator-readable current view plus limited history.

It is also the primary surface for showing sharing choices, consent state, and parcel operator rights controls without blurring private parcel data, shared data, public context, and derived estimates.

## Core objects

- parcel profile
- current parcel-state snapshot
- parcel-state history item
- explanation payload
- freshness block
- provenance summary
- sharing settings summary
- consent notice version reference
- export/delete request record

## Inputs

- parcel-state snapshots from the inference engine
- parcel metadata and display preferences
- optional user-entered parcel notes or context
- policy constraints on what evidence can be displayed
- current sharing-mode settings
- consent and notice records needed to explain enabled sharing
- structured explanation payload from inference

## Outputs

- dwelling-facing parcel condition-estimate view
- parcel-state history view
- API responses for current state and recent history
- sharing settings and notices view
- export/delete/revocation request entry points
- future alerts or notification candidates

## Internal modules

- parcel-state reader
- explanation formatter
- freshness and confidence presenter
- history query module
- access-control and privacy filter
- consent and sharing-settings presenter
- rights request coordinator

## External dependencies

- inference engine output store or API
- parcel metadata store
- identity and access layer
- privacy and governance policy rules
- consent and audit record store

## Realtime needs

- The current parcel view should update quickly when a new parcel-state snapshot is available.
- History can tolerate slower retrieval as long as the latest state stays responsive.
- The platform should make staleness obvious rather than quietly serving old results.
- Sharing setting changes should take effect promptly where the implementation supports them. **Revocation and some governance paths may remain partial or docs-only** until later accepted slices; do not assume sub-second or fully verified revocation behavior unless implementation status and release materials say so (see `../../architecture/system/version-and-promotion-matrix.md`).

## Risks

- rebuilding inference logic in the UI layer
- collapsing confidence, freshness, and status into one oversimplified label
- exposing more provenance detail than privacy rules allow
- hiding missing evidence in a way that implies certainty
- hiding enabled sharing modes or making revocation harder than activation
- presenting condition estimates as operational safety instructions
```

### File: `software/parcel-platform/interfaces.md`

```md
# Interfaces

## Public API surfaces

- `GET /v1/parcels/{parcel_id}`
  Return parcel metadata needed by the UI.
- `GET /v1/parcels/{parcel_id}/state`
  Return the latest parcel-state snapshot plus explanation and freshness.
- `GET /v1/parcels/{parcel_id}/state/history`
  Return recent parcel-state history.
- `GET /v1/parcels/{parcel_id}/evidence-summary`
  Return a display-safe summary of evidence sources used by the latest state.
- `POST /v1/parcels/state/evidence-summary`
  Build a display-safe evidence summary directly from a parcel-state payload in the reference scaffold.
- `GET /v1/parcels/{parcel_id}/sharing`
  Return the current sharing-mode settings, notice versions, and revocation status.
- `POST /v1/parcels/{parcel_id}/sharing`
  Update sharing-mode settings with an explicit notice/version reference.
- `GET /v1/parcels/{parcel_id}/house-state`
  Return the latest private house-state support object if one exists.
- `POST /v1/parcels/{parcel_id}/house-state`
  Upsert the private house-state support object for one parcel.
- `GET /v1/parcels/{parcel_id}/capabilities`
  Return the latest private house-capability support object if one exists.
- `POST /v1/parcels/{parcel_id}/capabilities`
  Upsert the private house-capability support object for one parcel.
- `GET /v1/parcels/{parcel_id}/controls`
  Return the latest private control-compatibility support object if one exists.
- `POST /v1/parcels/{parcel_id}/controls`
  Upsert the private control-compatibility support object for one parcel.
- `GET /v1/parcels/{parcel_id}/interventions`
  Return private intervention-event records for one parcel.
- `POST /v1/parcels/{parcel_id}/interventions`
  Append a private intervention-event record for one parcel.
- `GET /v1/parcels/{parcel_id}/verification`
  Return private verification-outcome records for one parcel.
- `POST /v1/parcels/{parcel_id}/verification`
  Append a private verification-outcome record for one parcel.
- `POST /v1/parcels/{parcel_id}/rights/export`
  Create an export request for parcel operator-visible parcel data.
- `POST /v1/parcels/{parcel_id}/rights/delete`
  Create a deletion request for account-controlled parcel data.
- `GET /v1/admin/reference-state/summary`
  Return the current file-backed sharing, rights-request, and access-log summary used by the reference governance stack.
- `POST /v1/admin/rights/process-export`
  Complete a queued export request and write a JSON export bundle in the configured export directory.
- `POST /v1/admin/rights/process-delete`
  Complete a queued delete request and remove parcel sharing state from the reference store.
- `POST /v1/admin/retention/cleanup`
  Run conservative retention cleanup over the reference rights-request and access-log stores.

## Internal events / jobs

- `parcel.state.updated`
  Refresh cached current-state views.
- `parcel.profile.updated`
  Refresh parcel metadata and access rules.
- `parcel.notification.candidate`
  Future event for noteworthy status changes or sharp confidence shifts.
- `parcel.sharing.updated`
  Refresh visibility and downstream sharing enforcement.
- `parcel.rights_request.created`
  Track export or deletion workflow state.
- `parcel.house_state.updated`
  Refresh house-state-dependent recommendation or verification views later.
- `parcel.intervention.logged`
  Track a bounded action or retrofit event.
- `parcel.verification.logged`
  Track the outcome window tied to a prior intervention.

## Data contracts

Primary input contract:
- parcel-state snapshot from `contracts/parcel-state-schema.md`

Primary response shape for current state:
- `parcel_id`
- `computed_at`
- `statuses`
- `confidence`
- `evidence_mode`
- `inference_basis`
- `explanation_payload`
- `reasons`
- `hazards`
- `freshness`
- `provenance_summary`
- `data_classes_visible`
- `sharing_summary`

`current v1` remains centered on parcel-state.
**Capability stage `v1.5` bridge** support objects stay separate from the state payload so the current contract does not break.

**Staging note:** `house_capability` and related fields target **coarse / read-side** equipment and capability hints. **`control_compatibility`** may hold **draft** records early, but the **full compatibility inventory** (interface classes, integration tiers, bounded-control policy) is primarily **`v2.5`** — see `../../architecture/system/architecture-gaps-by-stage.md`.

Support-object response shapes:

- `house_state`
- `house_capability`
- `control_compatibility` (draft-optional under `v1.5`; complete inventory posture under `v2.5`)
- `interventions`
- `verification_outcomes`

Primary response shape for evidence summary:
- `parcel_id`
- `computed_at`
- `evidence_mode`
- `inference_basis`
- `confidence`
- `headline`
- `confidence_band`
- `top_drivers`
- `top_limitations`
- `source_breakdown`
- `grouped_contributions`
- `source_modes`
- `freshness`

Suggested response example:

```json
{
  "parcel_id": "parcel_123",
  "computed_at": "2026-03-30T19:46:00Z",
  "statuses": {
    "shelter": "unknown",
    "reentry": "unknown",
    "egress": "unknown",
    "asset_risk": "unknown"
  },
  "confidence": 0.30,
  "evidence_mode": "insufficient",
  "inference_basis": "insufficient",
  "explanation_payload": {
    "headline": "Estimate uses limited local evidence with low parcel certainty.",
    "basis": {
      "evidence_mode": "insufficient",
      "inference_basis": "insufficient",
      "confidence_band": "low"
    },
    "drivers": [
      "Indoor gas-resistance trend shows a moderate change."
    ],
    "limitations": [
      "The local node is indoor and does not represent parcel-wide outdoor conditions.",
      "No flood-capable local sensor or public flood context is present."
    ],
    "evidence_contributions": [
      {
        "contribution_id": "local_gas_trend",
        "source_class": "local",
        "source_name": "bench-air-01",
        "role": "driver",
        "summary": "Indoor gas-resistance trend shows a moderate change.",
        "hazards": ["smoke"],
        "weight": 0.32,
        "visibility": "dwelling_safe"
      }
    ],
    "source_breakdown": {
      "local": true,
      "shared": false,
      "public": false,
      "parcel_context": false,
      "system": true
    }
  },
  "reasons": [
    "Local gas-resistance trend shows a moderate change, but it is not a direct smoke concentration measurement.",
    "Current local evidence comes from an indoor node and does not directly represent parcel-wide outdoor conditions.",
    "No flood-capable local sensor or public flood context is present, so flood-related outputs remain unknown.",
    "Confidence is limited because the current decision uses sparse single-node evidence."
  ],
  "hazards": {
    "smoke_probability": 0.12,
    "flood_probability": 0.00,
    "heat_probability": 0.02
  },
  "freshness": {
    "latest_observation_at": "2026-03-30T19:45:00Z",
    "seconds_since_latest": 60,
    "stale": false
  },
  "provenance_summary": {
    "observation_count": 1,
    "source_modes": [
      "dwelling_node"
    ]
  },
  "data_classes_visible": [
    "private_parcel_data",
    "derived_parcel_state"
  ],
  "sharing_summary": {
    "private_only": true,
    "network_assist": false,
    "neighborhood_aggregate": false,
    "research_or_pilot": false
  }
}
```

## Open questions

- How much raw evidence detail should a parcel operator see before the UI becomes noisy or misleading?
- Should the platform expose hazard probabilities directly, or mostly keep them behind explanation text and status labels?
- What should trigger a parcel operator notification: status transitions, freshness failures, confidence drops, or all three?
- Which parts of provenance should be hidden or generalized when data comes from shared neighborhood context?
- Which sharing updates should require step-up confirmation because they materially expand data use?
- Which support-object fields are genuinely required in the **`v1.5` bridge** versus better left optional until live pilots show their value?
- When does **`control_compatibility`** graduate from optional draft capture to **`v2.5`**-complete inventory requirements?
- Which future bounded-control permissions must be separated from ordinary data-sharing controls?
```

### File: `../oesis-runtime/oesis/inference/infer_parcel_state.py`

```python
#!/usr/bin/env python3

import argparse
import json
import sys
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

from oesis.common.repo_paths import EXAMPLES_DIR, INFERENCE_CONFIG_DIR
from oesis.inference.parcel_first_hazard import (
    apply_public_and_shared_support,
    build_contrastive_explanations,
    build_divergence_records,
    build_parcel_prior_details,
    build_state_snapshot,
    derive_public_baseline_confidence,
    derive_public_baseline_hazards,
)

CONFIG_DIR = INFERENCE_CONFIG_DIR
PUBLIC_CONTEXT_POLICY_PATH = CONFIG_DIR / "public_context_policy.json"
HAZARD_THRESHOLDS_PATH = CONFIG_DIR / "hazard_thresholds_v0.json"
TRUST_GATES_PATH = CONFIG_DIR / "trust_gates_v0.json"


class InferenceError(Exception):
    pass


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clamp_probability(value: float) -> float:
    return max(0.0, min(1.0, round(value, 2)))


def status_from_probability(probability: float, *, unknown_floor: float = 0.2) -> str:
    if probability < unknown_floor:
        return "unknown"
    if probability < 0.4:
        return "safe"
    if probability < 0.7:
        return "caution"
    return "unsafe"


def parse_time(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def validate_normalized_observation(payload: dict):
    required = [
        "observation_id",
        "node_id",
        "parcel_id",
        "observed_at",
        "ingested_at",
        "observation_type",
        "values",
        "health",
        "provenance",
    ]
    for field in required:
        if field not in payload:
            raise InferenceError(f"normalized observation missing required field: {field}")

    if payload["observation_type"] != "air.node.snapshot":
        raise InferenceError("observation_type must be air.node.snapshot")


def validate_public_context(payload: dict):
    required = [
        "context_id",
        "source_kind",
        "source_name",
        "observed_at",
        "coverage_mode",
        "parcel_id",
        "hazards",
        "summary",
    ]
    for field in required:
        if field not in payload:
            raise InferenceError(f"public context missing required field: {field}")

    if payload["source_kind"] != "public_context":
        raise InferenceError("public context source_kind must be public_context")


def validate_parcel_context(payload: dict):
    required = ["parcel_id", "site_profile", "node_installations", "parcel_priors"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"parcel context missing required field: {field}")


def validate_shared_neighborhood_signal(payload: dict):
    required = ["generated_at", "min_participants", "sharing_settings", "contributions"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"shared neighborhood signal missing required field: {field}")


def validate_house_state(payload: dict):
    required = ["parcel_id", "captured_at", "indoor_response", "power_state"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"house state missing required field: {field}")


def validate_house_capability(payload: dict):
    required = ["parcel_id", "effective_at", "capabilities"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"house capability missing required field: {field}")


def validate_intervention_event(payload: dict):
    required = ["parcel_id", "event_id", "occurred_at", "action_type", "action_source"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"intervention event missing required field: {field}")


def validate_verification_outcome(payload: dict):
    required = ["parcel_id", "verification_id", "verified_at", "hazard_type", "result_class"]
    for field in required:
        if field not in payload:
            raise InferenceError(f"verification outcome missing required field: {field}")


@lru_cache(maxsize=1)
def _public_context_policy() -> dict:
    return load_json(PUBLIC_CONTEXT_POLICY_PATH)


@lru_cache(maxsize=1)
def _hazard_thresholds() -> dict:
    return load_json(HAZARD_THRESHOLDS_PATH)


@lru_cache(maxsize=1)
def _trust_gates() -> dict:
    return load_json(TRUST_GATES_PATH)


def get_policy_for_source(source_name: str) -> dict:
    policy = _public_context_policy()
    default_policy = policy["default_policy"]
    override = policy.get("source_overrides", {}).get(source_name, {})
    return {
        "fresh_max_age_seconds": override.get("fresh_max_age_seconds", default_policy["fresh_max_age_seconds"]),
        "aging_max_age_seconds": override.get("aging_max_age_seconds", default_policy["aging_max_age_seconds"]),
        "stale_max_age_seconds": override.get("stale_max_age_seconds", default_policy["stale_max_age_seconds"]),
        "hazard_multiplier": default_policy["hazard_multiplier"],
        "confidence_adjustment": default_policy["confidence_adjustment"],
    }


def probability_from_lt_bands(value: float | None, bands: list[dict], default_probability: float) -> float:
    if value is None:
        return default_probability
    for band in bands:
        if value < band["lt"]:
            return band["probability"]
    return default_probability


def probability_from_gte_bands(value: float | None, bands: list[dict], default_probability: float) -> float:
    if value is None:
        return default_probability
    for band in bands:
        if value >= band["gte"]:
            return band["probability"]
    return default_probability


def build_closed_loop_summary(
    *,
    house_state: dict | None,
    intervention_event: dict | None,
    verification_outcome: dict | None,
    smoke_config: dict,
) -> dict:
    summary = {
        "hazard_type": "smoke",
        "status": "not_attempted",
        "summary": "No smoke-response loop has been attempted yet.",
    }

    if house_state and house_state.get("indoor_response"):
        indoor_response = house_state["indoor_response"]
        summary["current_indoor_response"] = {
            "pm25_ugm3": indoor_response.get("pm25_ugm3"),
            "temperature_c": indoor_response.get("temperature_c"),
            "relative_humidity_pct": indoor_response.get("relative_humidity_pct"),
        }

    smoke_intervention = intervention_event and intervention_event.get("action_type") in {
        "hvac_recirculate_on",
        "purifier_started",
        "fan_continuous_on",
    }

    if smoke_intervention:
        summary["status"] = "awaiting_verification"
        summary["action_type"] = intervention_event.get("action_type")
        summary["action_source"] = intervention_event.get("action_source")
        summary["summary"] = (
            f"Smoke-response action `{intervention_event.get('action_type')}` was recorded; "
            "verification is still pending or incomplete."
        )

    if verification_outcome and verification_outcome.get("hazard_type") == "smoke":
        window = verification_outcome.get("response_window_minutes")
        before = verification_outcome.get("before", {})
        after = verification_outcome.get("after", {})
        before_pm = before.get("indoor_pm25_ugm3")
        after_pm = after.get("indoor_pm25_ugm3")
        delta = None
        ratio = None
        if isinstance(before_pm, (int, float)) and isinstance(after_pm, (int, float)):
            delta = round(before_pm - after_pm, 2)
            ratio = round((before_pm - after_pm) / before_pm, 2) if before_pm > 0 else None

        window_ok = (
            isinstance(window, int)
            and smoke_config["verification_window_min_minutes"] <= window <= smoke_config["verification_window_max_minutes"]
        )
        improved = (
            verification_outcome.get("result_class") == "improved"
            and window_ok
            and delta is not None
            and ratio is not None
            and delta >= smoke_config["improvement_absolute_min_ugm3"]
            and ratio >= smoke_config["improvement_ratio_min"]
        )

        summary.update(
            {
                "response_window_minutes": window,
                "before": before,
                "after": after,
                "improvement_delta": delta,
                "improvement_ratio": ratio,
                "intervention_ref": verification_outcome.get("intervention_ref"),
            }
        )

        if improved:
            summary["status"] = "verified_improved"
            summary["summary"] = (
                f"Smoke-response loop verified improvement over {window} minutes"
                + (
                    f" after `{intervention_event.get('action_type')}`."
                    if smoke_intervention
                    else "."
                )
            )
        elif verification_outcome.get("result_class") == "worsened":
            summary["status"] = "verified_not_improved"
            summary["summary"] = "Smoke-response verification showed worsening conditions over the measured window."
        elif verification_outcome.get("result_class") == "unchanged":
            summary["status"] = "verified_not_improved"
            summary["summary"] = "Smoke-response verification did not show a meaningful indoor improvement over the measured window."
        else:
            summary["status"] = "inconclusive"
            summary["summary"] = "Smoke-response verification is present but remains inconclusive."

    return summary


def public_context_age_seconds(public_context: dict, *, now: datetime) -> int:
    return max(0, int((now - parse_time(public_context["observed_at"])).total_seconds()))


def public_context_freshness_band(public_context: dict, *, now: datetime) -> str:
    policy = get_policy_for_source(public_context["source_name"])
    age_seconds = public_context_age_seconds(public_context, now=now)
    if age_seconds <= policy["fresh_max_age_seconds"]:
        return "fresh"
    if age_seconds <= policy["aging_max_age_seconds"]:
        return "aging"
    if age_seconds <= policy["stale_max_age_seconds"]:
        return "stale"
    return "expired"


def combine_public_contexts(public_contexts: list[dict]) -> dict | None:
    if not public_contexts:
        return None

    for context in public_contexts:
        validate_public_context(context)

    first = public_contexts[0]
    combined_summary = []
    combined_source_names = []
    combined_hazards = {
        "smoke_probability": 0.0,
        "heat_probability": 0.0,
        "flood_probability": 0.0,
    }
    combined_observed_at = first["observed_at"]
    members = []

    for context in public_contexts:
        if context["parcel_id"] != first["parcel_id"]:
            raise InferenceError("public contexts must share the same parcel_id")
        if context["coverage_mode"] != first["coverage_mode"]:
            raise InferenceError("public contexts must share the same coverage_mode")
        combined_source_names.append(context["source_name"])
        combined_summary.extend(context.get("summary", []))
        for hazard_name in combined_hazards:
            combined_hazards[hazard_name] = max(
                combined_hazards[hazard_name],
                context["hazards"][hazard_name],
            )
        if parse_time(context["observed_at"]) > parse_time(combined_observed_at):
            combined_observed_at = context["observed_at"]
        members.append(
            {
                "source_name": context["source_name"],
                "observed_at": context["observed_at"],
                "hazards": context["hazards"],
                "summary": context.get("summary", []),
                "raw_context": context.get("raw_context"),
            }
        )

    return {
        "context_id": "combined_public_context",
        "source_kind": "public_context",
        "source_name": ",".join(combined_source_names),
        "observed_at": combined_observed_at,
        "coverage_mode": first["coverage_mode"],
        "parcel_id": first["parcel_id"],
        "hazards": combined_hazards,
        "summary": combined_summary,
        "members": members,
    }


def build_shared_neighborhood_context(shared_signal: dict) -> dict | None:
    validate_shared_neighborhood_signal(shared_signal)

    allowed_parcels = {
        item["parcel_ref"]
        for item in shared_signal.get("sharing_settings", [])
        if item.get("neighborhood_aggregate") and not item.get("revocation_pending")
    }

    eligible = []
    for contribution in shared_signal.get("contributions", []):
        if contribution.get("source_class") != "shared_data":
            continue
        parcel_ref = contribution.get("parcel_ref")
        if parcel_ref not in allowed_parcels:
            continue
        eligible.append(contribution)

    if len(eligible) < shared_signal["min_participants"]:
        return None

    cell_counts = {}
    for contribution in eligible:
        cell_id = contribution["cell_id"]
        cell_counts[cell_id] = cell_counts.get(cell_id, 0) + 1

    best_cell_id = None
    best_count = 0
    for cell_id, count in cell_counts.items():
        if count > best_count:
            best_cell_id = cell_id
            best_count = count

    if best_cell_id is None or best_count < shared_signal["min_participants"]:
        return None

    cell_contributions = [item for item in eligible if item["cell_id"] == best_cell_id]
    hazard_keys = ("smoke_probability", "flood_probability", "heat_probability")
    hazards = {}
    for hazard_key in hazard_keys:
        hazards[hazard_key] = round(
            sum(item["hazards"][hazard_key] for item in cell_contributions) / len(cell_contributions),
            2,
        )

    max_delay = max(item.get("delayed_minutes", 0) for item in cell_contributions)
    summary = [
        f"Shared neighborhood signal from {len(cell_contributions)} contributing parcels in {best_cell_id} suggests nearby conditions worth watching."
    ]
    if hazards["smoke_probability"] >= 0.3:
        summary.append("Nearby shared signals suggest modest smoke concern in the surrounding cell.")
    elif hazards["heat_probability"] >= 0.3:
        summary.append("Nearby shared signals suggest modest heat concern in the surrounding cell.")

    return {
        "context_id": "shared_neighborhood_context",
        "source_kind": "shared_data",
        "source_name": "shared_neighborhood_signal",
        "observed_at": shared_signal["generated_at"],
        "coverage_mode": "cell",
        "parcel_id": None,
        "hazards": hazards,
        "summary": summary,
        "member_count": len(cell_contributions),
        "max_delay_minutes": max_delay,
        "cell_id": best_cell_id,
    }


def get_location_mode(payload: dict) -> str:
    raw_packet = payload.get("raw_packet", {})
    return raw_packet.get("location_mode", "indoor")


def find_node_installation(parcel_context: dict | None, node_id: str) -> dict | None:
    if not parcel_context:
        return None
    for installation in parcel_context.get("node_installations", []):
        if installation.get("node_id") == node_id:
            return installation
    return None


def classify_local_context(payload: dict, parcel_context: dict | None = None) -> dict:
    installation = find_node_installation(parcel_context, payload["node_id"])
    location_mode = installation.get("location_mode", get_location_mode(payload)) if installation else get_location_mode(payload)
    is_indoor = location_mode == "indoor"
    is_sheltered = location_mode == "sheltered"
    is_outdoor = location_mode == "outdoor"
    local_observability = "low"
    if is_outdoor:
        local_observability = "moderate"
    elif is_sheltered:
        local_observability = "limited"

    return {
        "location_mode": location_mode,
        "is_indoor": is_indoor,
        "is_sheltered": is_sheltered,
        "is_outdoor": is_outdoor,
        "local_observability": local_observability,
        "install_role": installation.get("install_role", "unknown") if installation else "unknown",
        "exposure_bias_flags": installation.get("exposure_bias_flags", []) if installation else [],
        "has_parcel_context": parcel_context is not None,
    }


def prior_adjustment(prior_value: str | None, *, low: float = -0.02, moderate: float = 0.0, high: float = 0.04) -> float:
    mapping = {
        "low": low,
        "moderate": moderate,
        "high": high,
        "unknown": 0.0,
        None: 0.0,
    }
    return mapping.get(prior_value, 0.0)


def derive_hazards(
    payload: dict,
    parcel_context: dict | None = None,
    house_state: dict | None = None,
    house_capability: dict | None = None,
    verification_outcome: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
    *,
    now: datetime,
) -> dict:
    values = payload["values"]
    health = payload["health"]
    context = classify_local_context(payload, parcel_context=parcel_context)
    smoke_config = _hazard_thresholds()["smoke"]
    heat_config = _hazard_thresholds()["heat"]
    sensor_penalties = _hazard_thresholds()["sensor_penalties"]
    parcel_prior_details = build_parcel_prior_details(parcel_context)

    smoke_probability = smoke_config["base_probability"]
    gas_resistance = values.get("gas_resistance_ohm")
    smoke_probability = probability_from_lt_bands(
        gas_resistance,
        smoke_config["gas_resistance_bands"],
        smoke_config["default_probability"],
    )

    indoor_response = house_state.get("indoor_response", {}) if house_state else {}
    indoor_pm25 = indoor_response.get("pm25_ugm3")
    indoor_smoke_probability = probability_from_gte_bands(
        indoor_pm25,
        smoke_config["indoor_pm25_bands"],
        smoke_probability,
    )
    smoke_probability = max(smoke_probability, indoor_smoke_probability)

    heat_probability = heat_config["base_probability"]
    temperature_c = values.get("temperature_c_primary")
    heat_probability = probability_from_gte_bands(
        temperature_c,
        heat_config["temperature_bands"],
        heat_config["base_probability"],
    )

    if context["is_indoor"]:
        heat_probability -= heat_config["indoor_penalty"]
    elif context["is_sheltered"]:
        heat_probability -= heat_config["sheltered_penalty"]

    heat_probability += parcel_prior_details["heat"]["adjustment"]
    smoke_probability += parcel_prior_details["smoke"]["adjustment"]

    if house_capability:
        capabilities = house_capability.get("capabilities", {})
        if capabilities.get("recirculation_available"):
            smoke_probability += 0.01

    if verification_outcome and verification_outcome.get("hazard_type") == "smoke":
        if verification_outcome.get("result_class") == "worsened":
            smoke_probability += 0.03

    flood_probability = 0.0

    if not health.get("wifi_connected", False):
        smoke_probability -= sensor_penalties["wifi_disconnected"]
        heat_probability -= sensor_penalties["wifi_disconnected"]

    if health.get("read_failures_total", 0) > 0:
        smoke_probability -= sensor_penalties["read_failures"]
        heat_probability -= sensor_penalties["read_failures"]

    flood_probability = max(flood_probability, parcel_prior_details["flood"]["probability"])

    return apply_public_and_shared_support(
        {
            "smoke_probability": smoke_probability,
            "flood_probability": flood_probability,
            "heat_probability": heat_probability,
        },
        public_context=public_context,
        shared_context=shared_neighborhood_context,
        now=now,
        public_context_freshness_band=public_context_freshness_band,
        get_policy_for_source=get_policy_for_source,
    )


def derive_confidence(
    payload: dict,
    hazards: dict,
    *,
    now: datetime,
    parcel_context: dict | None = None,
    house_state: dict | None = None,
    house_capability: dict | None = None,
    intervention_event: dict | None = None,
    verification_outcome: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
) -> float:
    observed_at = parse_time(payload["observed_at"])
    age_seconds = max(0, int((now - observed_at).total_seconds()))
    context = classify_local_context(payload, parcel_context=parcel_context)

    confidence = 0.52
    if payload["health"].get("read_failures_total", 0) > 0:
        confidence -= 0.1
    if not payload["health"].get("wifi_connected", False):
        confidence -= 0.04
    if context["is_indoor"]:
        confidence -= 0.14
    elif context["is_sheltered"]:
        confidence -= 0.08
    if not context["has_parcel_context"]:
        confidence -= 0.08
    if "hvac_possible" in context["exposure_bias_flags"]:
        confidence -= 0.04
    if age_seconds > 900:
        confidence -= 0.1
    if age_seconds > 3600:
        confidence -= 0.15

    if max(hazards.values()) < 0.2:
        confidence -= 0.08
    if house_state is not None:
        confidence += 0.08
    if house_capability is not None:
        confidence += 0.04
    if intervention_event is not None:
        confidence += 0.02
    if verification_outcome is not None and verification_outcome.get("result_class") != "inconclusive":
        confidence += 0.03
    if public_context:
        member_contexts = public_context.get("members", [public_context])
        confidence_adjustment = min(
            0.18,
            sum(
                get_policy_for_source(member["source_name"])["confidence_adjustment"][
                    public_context_freshness_band(member, now=now)
                ]
                for member in member_contexts
            ),
        )
        confidence += confidence_adjustment
    if shared_neighborhood_context:
        confidence += 0.06

    return clamp_probability(confidence)


def derive_reasons(
    payload: dict,
    confidence: float,
    evidence_contributions: list[dict],
    *,
    parcel_context: dict | None = None,
    public_context: dict | None = None,
    parcel_prior_details: dict | None = None,
    contrastive_explanations: list[dict] | None = None,
) -> list[str]:
    reasons = []
    context = classify_local_context(payload, parcel_context=parcel_context)
    parcel_priors = parcel_context.get("parcel_priors", {}) if parcel_context else {}

    for contribution in evidence_contributions[:6]:
        reasons.append(contribution["summary"])

    if parcel_prior_details:
        for hazard_name in ("heat", "smoke", "flood"):
            summary = parcel_prior_details[hazard_name]["summary"]
            if summary:
                reasons.append(summary)
    elif parcel_priors.get("heat_retention_class") == "high":
        reasons.append("Parcel prior suggests elevated heat retention, which modestly raises heat support.")
    elif parcel_priors.get("heat_retention_class") == "low":
        reasons.append("Parcel prior suggests lower heat retention, which modestly reduces heat support.")

    if context["is_indoor"]:
        reasons.append("Current local evidence comes from an indoor node and does not directly represent parcel-wide outdoor conditions.")
    elif context["is_sheltered"]:
        reasons.append("Current local evidence comes from a sheltered node and only partially represents wider parcel conditions.")
    else:
        reasons.append("Current local evidence comes from one outdoor-capable node and still reflects only part of the parcel.")

    if confidence >= 0.5 and public_context:
        reasons.append("Confidence improves because public context supports the local evidence, but parcel certainty is still limited.")
    elif confidence >= 0.5:
        reasons.append("The current decision is based on a single dwelling-associated node without confirming public context.")

    if contrastive_explanations:
        reasons.append(contrastive_explanations[0]["contrast"]["summary"])

    deduped = []
    seen = set()
    for reason in reasons:
        if reason not in seen:
            deduped.append(reason)
            seen.add(reason)

    if not deduped:
        deduped.append("Available evidence is limited, so the parcel state remains mostly unknown.")

    return deduped


def make_evidence_contribution(
    *,
    contribution_id: str,
    source_class: str,
    source_name: str,
    role: str,
    summary: str,
    hazards: list[str],
    weight: float,
    visibility: str = "dwelling_safe",
    freshness_band: str | None = None,
) -> dict:
    contribution = {
        "contribution_id": contribution_id,
        "source_class": source_class,
        "source_name": source_name,
        "role": role,
        "summary": summary,
        "hazards": hazards,
        "weight": round(weight, 2),
        "visibility": visibility,
    }
    if freshness_band is not None:
        contribution["freshness_band"] = freshness_band
    return contribution


def build_evidence_contributions(
    *,
    payload: dict,
    parcel_context: dict | None,
    parcel_prior_details: dict,
    house_state: dict | None,
    house_capability: dict | None,
    intervention_event: dict | None,
    verification_outcome: dict | None,
    shared_context: dict | None,
    public_context: dict | None,
    divergence_records: list[dict],
    hazards: dict,
    confidence: float,
    stale: bool,
    now: datetime,
) -> list[dict]:
    contributions = []
    context = classify_local_context(payload, parcel_context=parcel_context)

    gas_resistance = payload["values"].get("gas_resistance_ohm")
    if gas_resistance is not None:
        if gas_resistance < 100000:
            summary = "Local gas-resistance trend suggests an indoor or sheltered air anomaly worth checking."
            weight = 0.48
        elif gas_resistance < 180000:
            summary = "Local gas-resistance trend shows a moderate change, but it is not a direct smoke concentration measurement."
            weight = 0.32
        else:
            summary = "Local gas-resistance trend appears comparatively steady."
            weight = 0.12
        contributions.append(
            make_evidence_contribution(
                contribution_id="local_gas_trend",
                source_class="local",
                source_name=payload["node_id"],
                role="driver",
                summary=summary,
                hazards=["smoke"],
                weight=weight,
            )
        )

    temperature_c = payload["values"].get("temperature_c_primary")
    if temperature_c is not None:
        if temperature_c >= 34:
            summary = (
                "Indoor temperature is elevated at the node location, which may indicate local heat burden."
                if context["is_indoor"]
                else "Measured temperature is elevated at the node location and may contribute to heat concern."
            )
            weight = 0.52
        elif temperature_c >= 24:
            summary = (
                "Indoor temperature is somewhat elevated at the node location."
                if context["is_indoor"]
                else "Measured temperature is modestly elevated at the node location."
            )
            weight = 0.28
        else:
            summary = "Local temperature does not currently suggest elevated heat concern."
            weight = 0.1
        contributions.append(
            make_evidence_contribution(
                contribution_id="local_temperature",
                source_class="local",
                source_name=payload["node_id"],
                role="driver",
                summary=summary,
                hazards=["heat"],
                weight=weight,
            )
        )

    siting_summary = "Current local evidence comes from one outdoor-capable node and still reflects only part of the parcel."
    siting_weight = 0.28
    if context["is_indoor"]:
        siting_summary = "Current local evidence comes from an indoor node and does not directly represent parcel-wide outdoor conditions."
        siting_weight = 0.72
    elif context["is_sheltered"]:
        siting_summary = "Current local evidence comes from a sheltered node and only partially represents wider parcel conditions."
        siting_weight = 0.56
    contributions.append(
        make_evidence_contribution(
            contribution_id="local_siting_limit",
            source_class="local",
            source_name=payload["node_id"],
            role="limitation",
            summary=siting_summary,
            hazards=["smoke", "heat", "flood"],
            weight=siting_weight,
        )
    )

    if parcel_context:
        installation = find_node_installation(parcel_context, payload["node_id"])
        if installation:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="parcel_install_role",
                    source_class="parcel_context",
                    source_name=installation.get("install_role", "unknown"),
                    role="limitation",
                    summary=(
                        f"Install role {installation.get('install_role', 'unknown')} constrains how strongly this node "
                        "represents wider parcel conditions."
                    ),
                    hazards=["smoke", "heat", "flood"],
                    weight=0.44,
                )
            )
        else:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="parcel_missing_installation",
                    source_class="parcel_context",
                    source_name=parcel_context["parcel_id"],
                    role="limitation",
                    summary="Parcel context is present, but this node lacks a matching installation record.",
                    hazards=["smoke", "heat", "flood"],
                    weight=0.46,
                )
            )
    else:
        contributions.append(
            make_evidence_contribution(
                contribution_id="missing_parcel_context",
                source_class="system",
                source_name=payload["parcel_id"],
                role="limitation",
                summary="Parcel installation context is missing, so siting relevance and parcel priors cannot improve interpretation.",
                hazards=["smoke", "heat", "flood"],
                weight=0.64,
            )
        )

    if parcel_context:
        if parcel_prior_details["heat"]["factors"]:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="parcel_heat_prior",
                    source_class="parcel_context",
                    source_name=parcel_context["parcel_id"],
                    role="driver",
                    summary=parcel_prior_details["heat"]["summary"],
                    hazards=["heat"],
                    weight=min(0.3, abs(parcel_prior_details["heat"]["adjustment"]) + 0.08),
                )
            )
        if parcel_prior_details["smoke"]["factors"]:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="parcel_smoke_prior",
                    source_class="parcel_context",
                    source_name=parcel_context["parcel_id"],
                    role="driver",
                    summary=parcel_prior_details["smoke"]["summary"],
                    hazards=["smoke"],
                    weight=min(0.34, abs(parcel_prior_details["smoke"]["adjustment"]) + 0.12),
                )
            )
        contributions.append(
            make_evidence_contribution(
                contribution_id="parcel_flood_prior",
                source_class="parcel_context",
                source_name=parcel_context["parcel_id"],
                role="driver",
                summary=parcel_prior_details["flood"]["summary"],
                hazards=["flood"],
                weight=min(0.38, parcel_prior_details["flood"]["probability"] * 8 + 0.08),
            )
        )

    for record in divergence_records:
        hazard = {
            "pm25": "smoke",
            "temperature_c": "heat",
            "flood_stage": "flood",
        }.get(record["parameter"], "smoke")
        role = "driver" if record["magnitude"] in {"moderate", "high", "extreme"} else "limitation"
        summary = (
            f"Local {record['parameter']} diverged from {record['regional_source']} by {record['abs_diff']:.1f} "
            f"({record['direction']}, {record['persistence_class']})."
        )
        contributions.append(
            make_evidence_contribution(
                contribution_id=f"divergence_{record['parameter']}",
                source_class="system",
                source_name=record["regional_source"],
                role=role,
                summary=summary,
                hazards=[hazard],
                weight=min(0.62, (record["z_score"] or 0.0) * 0.12 + 0.12),
            )
        )

    if house_state:
        indoor_response = house_state.get("indoor_response", {})
        indoor_pm25 = indoor_response.get("pm25_ugm3")
        indoor_temp = indoor_response.get("temperature_c")
        if indoor_pm25 is not None:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="indoor_pm25_support",
                    source_class="local",
                    source_name=house_state.get("source_summary", {}).get("source_kind", "private_support_object"),
                    role="driver",
                    summary=f"Indoor PM2.5 support data is available ({round(indoor_pm25, 1)} ug/m3).",
                    hazards=["smoke"],
                    weight=0.26 if indoor_pm25 >= 12 else 0.14,
                )
            )
        if indoor_temp is not None:
            contributions.append(
                make_evidence_contribution(
                    contribution_id="indoor_temperature_support",
                    source_class="local",
                    source_name=house_state.get("source_summary", {}).get("source_kind", "private_support_object"),
                    role="driver",
                    summary=f"Indoor response temperature support is available ({round(indoor_temp, 1)} C).",
                    hazards=["heat"],
                    weight=0.14,
                )
            )
        power_state = house_state.get("power_state", {})
        if power_state:
            mains_state = power_state.get("mains_state", "unknown")
            backup_active = power_state.get("backup_power_active")
            contributions.append(
                make_evidence_contribution(
                    contribution_id="power_state_support",
                    source_class="local",
                    source_name=house_state.get("source_summary", {}).get("source_kind", "private_support_object"),
                    role="driver" if mains_state == "down" else "limitation",
                    summary=(
                        "Household continuity data shows mains power is down."
                        if mains_state == "down"
                        else "Household continuity data is available for mains and backup-power posture."
                    ),
                    hazards=["heat", "flood"],
                    weight=0.22 if mains_state == "down" and not backup_active else 0.12,
                )
            )

    if house_capability:
        capabilities = house_capability.get("capabilities", {})
        equipment_state = house_capability.get("equipment_state", {})
        if capabilities.get("recirculation_available") or capabilities.get("portable_purifier_present"):
            contributions.append(
                make_evidence_contribution(
                    contribution_id="protective_capability_present",
                    source_class="parcel_context",
                    source_name=payload["parcel_id"],
                    role="driver",
                    summary="Protective capability metadata indicates recirculation and/or purifier support is available.",
                    hazards=["smoke"],
                    weight=0.18,
                )
            )
        if equipment_state:
            state_parts = []
            if equipment_state.get("air_source_mode"):
                state_parts.append(f"air mode={equipment_state['air_source_mode']}")
            if equipment_state.get("fan_state"):
                state_parts.append(f"fan={equipment_state['fan_state']}")
            if equipment_state.get("purifier_state"):
                state_parts.append(f"purifier={equipment_state['purifier_state']}")
            if state_parts:
                contributions.append(
                    make_evidence_contribution(
                        contribution_id="equipment_state_support",
                        source_class="parcel_context",
                        source_name=payload["parcel_id"],
                        role="driver",
                        summary=f"Read-side equipment state is available ({', '.join(state_parts)}).",
                        hazards=["smoke", "heat"],
                        weight=0.2,
                    )
                )

    if intervention_event:
        contributions.append(
            make_evidence_contribution(
                contribution_id="intervention_history_present",
                source_class="system",
                source_name=intervention_event.get("event_id", "intervention_event"),
                role="driver",
                summary=f"An intervention record is present ({intervention_event.get('action_type', 'unknown_action')}).",
                hazards=["smoke", "heat", "flood"],
                weight=0.16,
            )
        )

    if verification_outcome:
        result_class = verification_outcome.get("result_class", "inconclusive")
        contributions.append(
            make_evidence_contribution(
                contribution_id="verification_history_present",
                source_class="system",
                source_name=verification_outcome.get("verification_id", "verification_outcome"),
                role="driver" if result_class == "improved" else "limitation",
                summary=(
                    "A prior verification record suggests conditions improved after an intervention."
                    if result_class == "improved"
                    else "A verification record is present but does not yet show clear improvement."
                ),
                hazards=[verification_outcome.get("hazard_type", "smoke")],
                weight=0.18 if result_class == "improved" else 0.14,
            )
        )

    if house_state:
        contributions.append(
            make_evidence_contribution(
                contribution_id="house_state_support",
                source_class="local",
                source_name=house_state.get("source_summary", {}).get("source_kind", "private_support_object"),
                role="driver",
                summary="Private house-state support data is available for indoor response and continuity reasoning.",
                hazards=["smoke", "heat", "flood"],
                weight=0.1,
            )
        )

    if house_capability:
        contributions.append(
            make_evidence_contribution(
                contribution_id="house_capability_support",
                source_class="parcel_context",
                source_name=payload["parcel_id"],
                role="driver",
                summary="Protective capability and equipment-state metadata are available for later response reasoning.",
                hazards=["smoke", "heat", "flood"],
                weight=0.08,
            )
        )

    if intervention_event:
        contributions.append(
            make_evidence_contribution(
                contribution_id="intervention_history_present",
                source_class="system",
                source_name=intervention_event.get("event_id", "intervention_event"),
                role="limitation",
                summary="Intervention records are present, but current parcel-state remains a condition estimate rather than a response score.",
                hazards=["smoke", "heat", "flood"],
                weight=0.08,
            )
        )

    if verification_outcome:
        contributions.append(
            make_evidence_contribution(
                contribution_id="verification_history_present",
                source_class="system",
                source_name=verification_outcome.get("verification_id", "verification_outcome"),
                role="limitation",
                summary="Verification records are available for later closed-loop reasoning, but they do not directly change the current parcel-state.",
                hazards=["smoke", "heat", "flood"],
                weight=0.08,
            )
        )

    if public_context:
        for member in public_context.get("members", [public_context]):
            member_hazards = []
            if member["hazards"]["smoke_probability"] >= 0.1:
                member_hazards.append("smoke")
            if member["hazards"]["heat_probability"] >= 0.1:
                member_hazards.append("heat")
            if member["hazards"]["flood_probability"] >= 0.03:
                member_hazards.append("flood")
            if member_hazards:
                freshness_band = public_context_freshness_band(member, now=now)
                contributions.append(
                    make_evidence_contribution(
                        contribution_id=f"public_{member['source_name']}",
                        source_class="public",
                        source_name=member["source_name"],
                        role="driver",
                        summary=member.get("summary", ["Public context contributed to the estimate."])[0],
                        hazards=member_hazards,
                        weight={
                            "fresh": 0.48,
                            "aging": 0.32,
                            "stale": 0.18,
                            "expired": 0.0,
                        }[freshness_band],
                        freshness_band=freshness_band,
                    )
                )
                if freshness_band in {"aging", "stale", "expired"}:
                    contributions.append(
                        make_evidence_contribution(
                            contribution_id=f"public_{member['source_name']}_freshness_limit",
                            source_class="public",
                            source_name=member["source_name"],
                            role="limitation",
                            summary={
                                "aging": "Some regional public context is aging, so it provides limited support.",
                                "stale": "Some regional public context is stale and contributes little weight to the current parcel estimate.",
                                "expired": "Some available public context was too old to materially affect the current parcel estimate.",
                            }[freshness_band],
                            hazards=member_hazards,
                            weight={
                                "aging": 0.28,
                                "stale": 0.46,
                                "expired": 0.7,
                            }[freshness_band],
                            freshness_band=freshness_band,
                        )
                    )

    if shared_context:
        shared_hazards = []
        if shared_context["hazards"]["smoke_probability"] >= 0.2:
            shared_hazards.append("smoke")
        if shared_context["hazards"]["heat_probability"] >= 0.2:
            shared_hazards.append("heat")
        if shared_context["hazards"]["flood_probability"] >= 0.05:
            shared_hazards.append("flood")
        contributions.append(
            make_evidence_contribution(
                contribution_id="shared_cell_signal",
                source_class="shared",
                source_name=shared_context["cell_id"],
                role="driver",
                summary=shared_context["summary"][0],
                hazards=shared_hazards or ["smoke"],
                weight=0.34,
            )
        )
        contributions.append(
            make_evidence_contribution(
                contribution_id="shared_scope_limit",
                source_class="shared",
                source_name=shared_context["cell_id"],
                role="limitation",
                summary="Shared neighborhood signals are nearby supporting context, not direct confirmation of this parcel's conditions.",
                hazards=["smoke", "heat", "flood"],
                weight=0.42,
            )
        )

    if hazards["flood_probability"] == 0:
        contributions.append(
            make_evidence_contribution(
                contribution_id="missing_flood_evidence",
                source_class="parcel_context" if parcel_context else "local",
                source_name=payload["node_id"] if not parcel_context else parcel_context["parcel_id"],
                role="limitation",
                summary="No flood-capable local sensor or public flood context is present.",
                hazards=["flood"],
                weight=0.58,
            )
        )

    if stale:
        contributions.append(
            make_evidence_contribution(
                contribution_id="stale_local_observation",
                source_class="system",
                source_name="freshness_gate",
                role="limitation",
                summary="The latest local observation is aging out and may no longer reflect current parcel conditions.",
                hazards=["smoke", "heat", "flood"],
                weight=_trust_gates()["freshness_gate"]["stale_weight"],
            )
        )

    if confidence < _trust_gates()["confidence_gate"]["low_confidence_threshold"]:
        contributions.append(
            make_evidence_contribution(
                contribution_id="low_confidence_gate",
                source_class="system",
                source_name="confidence_gate",
                role="limitation",
                summary="Confidence is limited because the current estimate relies on sparse or weakly representative evidence.",
                hazards=["smoke", "heat", "flood"],
                weight=_trust_gates()["confidence_gate"]["weight"],
            )
        )

    public_members = public_context.get("members", [public_context]) if public_context else []
    strongest_public_smoke = max((member["hazards"]["smoke_probability"] for member in public_members), default=0.0)
    strongest_public_heat = max((member["hazards"]["heat_probability"] for member in public_members), default=0.0)
    strongest_shared_smoke = shared_context["hazards"]["smoke_probability"] if shared_context else 0.0
    strongest_shared_heat = shared_context["hazards"]["heat_probability"] if shared_context else 0.0

    disagreement = _trust_gates()["cross_source_disagreement"]

    if (
        gas_resistance is not None
        and gas_resistance >= disagreement["smoke_local_steady_min_gas_resistance_ohm"]
        and max(strongest_public_smoke, strongest_shared_smoke) >= disagreement["smoke_external_support_threshold"]
    ):
        contributions.append(
            make_evidence_contribution(
                contribution_id="smoke_disagreement_gate",
                source_class="system",
                source_name="cross_source_agreement",
                role="limitation",
                summary="Regional or neighborhood smoke context is stronger than the local node trend, so the estimate remains conservative.",
                hazards=["smoke"],
                weight=disagreement["weight"],
            )
        )

    if (
        temperature_c is not None
        and temperature_c < disagreement["heat_local_cool_max_temp_c"]
        and max(strongest_public_heat, strongest_shared_heat) >= disagreement["heat_external_support_threshold"]
    ):
        contributions.append(
            make_evidence_contribution(
                contribution_id="heat_disagreement_gate",
                source_class="system",
                source_name="cross_source_agreement",
                role="limitation",
                summary="Regional or neighborhood heat context is stronger than the local node reading, so parcel heat interpretation remains cautious.",
                hazards=["heat"],
                weight=disagreement["weight"],
            )
        )

    return contributions


def confidence_band(confidence: float) -> str:
    if confidence >= 0.75:
        return "high"
    if confidence >= 0.45:
        return "medium"
    return "low"


def build_explanation_payload(
    *,
    confidence: float,
    evidence_mode: str,
    inference_basis: str,
    evidence_contributions: list[dict],
    divergence_records: list[dict],
    contrastive_explanations: list[dict],
    support_objects_present: list[str],
    parcel_context: dict | None,
    shared_context: dict | None,
    public_context: dict | None,
) -> dict:
    sorted_drivers = sorted(
        (item for item in evidence_contributions if item["role"] == "driver"),
        key=lambda item: item["weight"],
        reverse=True,
    )
    sorted_limitations = sorted(
        (item for item in evidence_contributions if item["role"] == "limitation"),
        key=lambda item: item["weight"],
        reverse=True,
    )
    drivers = [item["summary"] for item in sorted_drivers[:3]]
    limitations = [item["summary"] for item in sorted_limitations[:3]]
    if not limitations:
        limitations = ["Evidence limits are currently low enough that few explicit caveats were generated."]

    headline = (
        f"Estimate uses {inference_basis.replace('_', ' ')} evidence with "
        f"{confidence_band(confidence)} confidence."
    )

    return {
        "headline": headline,
        "basis": {
            "evidence_mode": evidence_mode,
            "inference_basis": inference_basis,
            "confidence_band": confidence_band(confidence),
        },
        "drivers": drivers,
        "limitations": limitations,
        "evidence_contributions": evidence_contributions,
        "source_breakdown": {
            "local": True,
            "shared": shared_context is not None,
            "public": public_context is not None,
            "parcel_context": parcel_context is not None,
            "system": any(item["source_class"] == "system" for item in evidence_contributions),
        },
        "support_objects_present": support_objects_present,
        "divergence_summary": [item["contrast"]["summary"] for item in contrastive_explanations[:2]],
        "top_divergence_records": divergence_records[:3],
    }


def infer_parcel_state(
    payload: dict,
    *,
    computed_at: str | None = None,
    parcel_context: dict | None = None,
    house_state: dict | None = None,
    house_capability: dict | None = None,
    intervention_event: dict | None = None,
    verification_outcome: dict | None = None,
    shared_neighborhood_context: dict | None = None,
    public_context: dict | None = None,
) -> dict:
    validate_normalized_observation(payload)
    if parcel_context is not None:
        validate_parcel_context(parcel_context)
    if house_state is not None:
        validate_house_state(house_state)
    if house_capability is not None:
        validate_house_capability(house_capability)
    if intervention_event is not None:
        validate_intervention_event(intervention_event)
    if verification_outcome is not None:
        validate_verification_outcome(verification_outcome)
    if shared_neighborhood_context is not None:
        validate_shared_neighborhood_signal(shared_neighborhood_context)
    if public_context is not None:
        validate_public_context(public_context)

    now = parse_time(computed_at) if computed_at else datetime.now(timezone.utc)
    computed_at = (computed_at or now_iso())
    observed_at = parse_time(payload["observed_at"])
    age_seconds = max(0, int((now - observed_at).total_seconds()))
    stale = age_seconds > 900
    context = classify_local_context(payload, parcel_context=parcel_context)

    shared_context = build_shared_neighborhood_context(shared_neighborhood_context) if shared_neighborhood_context else None
    parcel_prior_details = build_parcel_prior_details(parcel_context)

    hazards = derive_hazards(
        payload,
        parcel_context=parcel_context,
        house_state=house_state,
        house_capability=house_capability,
        verification_outcome=verification_outcome,
        shared_neighborhood_context=shared_context,
        public_context=public_context,
        now=now,
    )
    confidence = derive_confidence(
        payload,
        hazards,
        now=now,
        parcel_context=parcel_context,
        house_state=house_state,
        house_capability=house_capability,
        intervention_event=intervention_event,
        verification_outcome=verification_outcome,
        shared_neighborhood_context=shared_context,
        public_context=public_context,
    )
    status_config = _hazard_thresholds()["status_mapping"]
    state_rules = _hazard_thresholds()["state_rules"]
    status_snapshot = build_state_snapshot(
        hazards=hazards,
        context=context,
        confidence=confidence,
        stale=stale,
        status_config=status_config,
        state_rules=state_rules,
        status_from_probability=status_from_probability,
    )

    evidence_mode = "local_only"
    has_nonexpired_public_context = False
    if public_context:
        member_contexts = public_context.get("members", [public_context])
        has_nonexpired_public_context = any(
            public_context_freshness_band(member, now=now) != "expired" for member in member_contexts
        )

    if public_context and has_nonexpired_public_context and not stale and confidence >= state_rules["insufficient_confidence_floor"]:
        evidence_mode = "local_plus_public"
    if stale or confidence < state_rules["insufficient_confidence_floor"]:
        evidence_mode = "insufficient"

    inference_basis = "local_only"
    if stale or confidence < state_rules["insufficient_confidence_floor"]:
        inference_basis = "insufficient"
    elif shared_context and has_nonexpired_public_context:
        inference_basis = "local_plus_shared_plus_public"
    elif shared_context:
        inference_basis = "local_plus_shared"
    elif has_nonexpired_public_context:
        inference_basis = "local_plus_public"

    public_only_hazards, _ = derive_public_baseline_hazards(
        parcel_context=parcel_context,
        house_capability=house_capability,
        verification_outcome=verification_outcome,
        shared_context=shared_context,
        public_context=public_context,
        now=now,
        public_context_freshness_band=public_context_freshness_band,
        get_policy_for_source=get_policy_for_source,
    )
    public_only_confidence = derive_public_baseline_confidence(
        payload=payload,
        hazards=public_only_hazards,
        now=now,
        parcel_context=parcel_context,
        house_capability=house_capability,
        verification_outcome=verification_outcome,
        shared_context=shared_context,
        public_context=public_context,
        public_context_freshness_band=public_context_freshness_band,
        get_policy_for_source=get_policy_for_source,
    )
    public_only_statuses = build_state_snapshot(
        hazards=public_only_hazards,
        context=context,
        confidence=public_only_confidence,
        stale=stale,
        status_config=status_config,
        state_rules=state_rules,
        status_from_probability=status_from_probability,
    )
    divergence_records = build_divergence_records(
        payload=payload,
        parcel_context=parcel_context,
        house_state=house_state,
        public_context=public_context,
    )
    contrastive_explanations = build_contrastive_explanations(
        payload=payload,
        computed_at=computed_at,
        parcel_context=parcel_context,
        house_state=house_state,
        house_capability=house_capability,
        public_context=public_context,
        shared_context=shared_context,
        fact_hazards=hazards,
        fact_confidence=confidence,
        fact_statuses=status_snapshot,
        foil_hazards=public_only_hazards,
        foil_confidence=public_only_confidence,
        foil_statuses=public_only_statuses,
        divergence_records=divergence_records,
    )

    evidence_contributions = build_evidence_contributions(
        payload=payload,
        parcel_context=parcel_context,
        parcel_prior_details=parcel_prior_details,
        house_state=house_state,
        house_capability=house_capability,
        intervention_event=intervention_event,
        verification_outcome=verification_outcome,
        shared_context=shared_context,
        public_context=public_context,
        divergence_records=divergence_records,
        hazards=hazards,
        confidence=confidence,
        stale=stale,
        now=now,
    )
    support_objects_present = [
        name
        for name, obj in (
            ("house_state", house_state),
            ("house_capability", house_capability),
            ("intervention_event", intervention_event),
            ("verification_outcome", verification_outcome),
        )
        if obj is not None
    ]
    closed_loop_summary = build_closed_loop_summary(
        house_state=house_state,
        intervention_event=intervention_event,
        verification_outcome=verification_outcome,
        smoke_config=_hazard_thresholds()["smoke"],
    )
    reasons = derive_reasons(
        payload,
        confidence,
        evidence_contributions,
        parcel_context=parcel_context,
        public_context=public_context,
        parcel_prior_details=parcel_prior_details,
        contrastive_explanations=contrastive_explanations,
    )
    explanation_payload = build_explanation_payload(
        confidence=confidence,
        evidence_mode=evidence_mode,
        inference_basis=inference_basis,
        evidence_contributions=evidence_contributions,
        divergence_records=divergence_records,
        contrastive_explanations=contrastive_explanations,
        support_objects_present=support_objects_present,
        parcel_context=parcel_context,
        shared_context=shared_context,
        public_context=public_context,
    )

    source_modes = [payload["provenance"]["source_kind"]]
    if shared_context:
        source_modes.append(shared_context["source_kind"])
    if public_context:
        source_modes.append(public_context["source_kind"])
    if support_objects_present:
        source_modes.append("private_support_object")

    return {
        "parcel_id": payload["parcel_id"],
        "computed_at": computed_at,
        "shelter_status": status_snapshot["shelter_status"],
        "reentry_status": status_snapshot["reentry_status"],
        "egress_status": status_snapshot["egress_status"],
        "asset_risk_status": status_snapshot["asset_risk_status"],
        "confidence": confidence,
        "evidence_mode": evidence_mode,
        "inference_basis": inference_basis,
        "explanation_payload": explanation_payload,
        "reasons": reasons,
        "hazards": hazards,
        "hazard_statuses": {
            "smoke": status_snapshot["smoke_status"],
            "heat": status_snapshot["heat_status"],
            "flood": status_snapshot["flood_status"],
        },
        "parcel_priors_applied": parcel_prior_details,
        "divergence_records": divergence_records,
        "public_only_counterfactual": {
            "hazards": public_only_hazards,
            "hazard_statuses": {
                "smoke": public_only_statuses["smoke_status"],
                "heat": public_only_statuses["heat_status"],
                "flood": public_only_statuses["flood_status"],
            },
            "confidence": public_only_confidence,
        },
        "closed_loop_summary": closed_loop_summary,
        "contrastive_explanations": contrastive_explanations,
        "freshness": {
            "latest_observation_at": payload["observed_at"],
            "seconds_since_latest": age_seconds,
            "stale": stale,
        },
        "provenance_summary": {
            "observation_count": 1,
            "source_modes": source_modes,
            "observation_refs": [
                payload["observation_id"]
            ],
            "support_object_refs": support_objects_present,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Infer a parcel-state snapshot from a normalized observation.")
    parser.add_argument(
        "input",
        nargs="?",
        default=str(EXAMPLES_DIR / "normalized-observation.example.json"),
        help="Path to a normalized observation JSON file.",
    )
    parser.add_argument(
        "--computed-at",
        default=None,
        help="Optional RFC 3339 timestamp to use as the computation time.",
    )
    parser.add_argument(
        "--parcel-context",
        default=None,
        help="Optional path to a parcel context JSON file to combine with local evidence.",
    )
    parser.add_argument("--house-state", default=None, help="Optional path to a house-state JSON file.")
    parser.add_argument("--house-capability", default=None, help="Optional path to a house-capability JSON file.")
    parser.add_argument("--intervention-event", default=None, help="Optional path to an intervention-event JSON file.")
    parser.add_argument("--verification-outcome", default=None, help="Optional path to a verification-outcome JSON file.")
    parser.add_argument(
        "--shared-neighborhood-signal",
        default=None,
        help="Optional path to a shared neighborhood signal JSON file to combine with local evidence.",
    )
    parser.add_argument(
        "--public-context",
        action="append",
        default=[],
        help="Optional path to a public context JSON file to combine with local evidence. May be passed more than once.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()

    try:
        payload = load_json(input_path)
        parcel_context = load_json(Path(args.parcel_context).resolve()) if args.parcel_context else None
        house_state = load_json(Path(args.house_state).resolve()) if args.house_state else None
        house_capability = load_json(Path(args.house_capability).resolve()) if args.house_capability else None
        intervention_event = load_json(Path(args.intervention_event).resolve()) if args.intervention_event else None
        verification_outcome = load_json(Path(args.verification_outcome).resolve()) if args.verification_outcome else None
        shared_neighborhood_signal = (
            load_json(Path(args.shared_neighborhood_signal).resolve())
            if args.shared_neighborhood_signal
            else None
        )
        public_contexts = [load_json(Path(path).resolve()) for path in args.public_context]
        public_context = combine_public_contexts(public_contexts)
        result = infer_parcel_state(
            payload,
            computed_at=args.computed_at,
            parcel_context=parcel_context,
            house_state=house_state,
            house_capability=house_capability,
            intervention_event=intervention_event,
            verification_outcome=verification_outcome,
            shared_neighborhood_context=shared_neighborhood_signal,
            public_context=public_context,
        )
    except (InferenceError, FileNotFoundError, json.JSONDecodeError, KeyError) as exc:
        print(f"ERROR {input_path}: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### File: `../oesis-runtime/oesis/inference/serve_inference_api.py`

```python
#!/usr/bin/env python3

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .infer_parcel_state import InferenceError, combine_public_contexts, infer_parcel_state


MODEL_INFO = {
    "model_id": "hazard-logic-v0",
    "mode": "rules-based",
    "status": "active",
}


class InferenceRequestHandler(BaseHTTPRequestHandler):
    server_version = "OESISInference/0.1"

    def _send_json(self, status: int, payload: dict):
        body = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        content_length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(content_length)
        try:
            return json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise InferenceError(f"request body: invalid JSON: {exc}") from exc

    def do_GET(self):
        if self.path == "/v1/inference/health":
            self._send_json(
                HTTPStatus.OK,
                {
                    "ok": True,
                    "service": "inference-engine",
                    "model": MODEL_INFO,
                },
            )
            return

        if self.path == "/v1/inference/models":
            self._send_json(HTTPStatus.OK, {"models": [MODEL_INFO]})
            return

        self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def do_POST(self):
        if self.path != "/v1/inference/parcel-state":
            self._send_json(HTTPStatus.NOT_FOUND, {"error": "not_found"})
            return

        computed_at = self.headers.get("X-OESIS-Computed-At")
        try:
            payload = self._read_json()
            normalized_observation = payload.get("normalized_observation", payload)
            parcel_context = payload.get("parcel_context")
            house_state = payload.get("house_state")
            house_capability = payload.get("house_capability")
            intervention_event = payload.get("intervention_event")
            verification_outcome = payload.get("verification_outcome")
            shared_neighborhood_context = payload.get("shared_neighborhood_context")
            public_context_payload = payload.get("public_context")
            public_contexts = payload.get("public_contexts", [])
            if public_context_payload and public_contexts:
                raise InferenceError("request body must provide either public_context or public_contexts, not both")
            combined_public_context = None
            if public_contexts:
                combined_public_context = combine_public_contexts(public_contexts)
            elif public_context_payload:
                combined_public_context = public_context_payload
            parcel_state = infer_parcel_state(
                normalized_observation,
                computed_at=computed_at,
                parcel_context=parcel_context,
                house_state=house_state,
                house_capability=house_capability,
                intervention_event=intervention_event,
                verification_outcome=verification_outcome,
                shared_neighborhood_context=shared_neighborhood_context,
                public_context=combined_public_context,
            )
        except (InferenceError, KeyError) as exc:
            self._send_json(
                HTTPStatus.BAD_REQUEST,
                {
                    "ok": False,
                    "error": "invalid_observation",
                    "detail": str(exc),
                },
            )
            return

        self._send_json(
            HTTPStatus.ACCEPTED,
            {
                "ok": True,
                "parcel_state": parcel_state,
            },
        )

    def log_message(self, format, *args):
        return


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a tiny local inference API for normalized observation testing.")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind.")
    parser.add_argument("--port", type=int, default=8788, help="Port to listen on.")
    return parser.parse_args()


def main():
    args = parse_args()
    server = ThreadingHTTPServer((args.host, args.port), InferenceRequestHandler)
    print(f"Listening on http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
```
