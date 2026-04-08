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
- optional shared neighborhood signal records from `contracts/schemas/shared-neighborhood-signal.schema.json`
- optional public context records from `contracts/public-context-schema.md`

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
- `freshness`
- `provenance_summary`

Expected engine behavior:
- accept sparse evidence and lower confidence instead of fabricating certainty
- score hazards independently before mapping to parcel-state outputs
- represent stale or missing evidence explicitly in `freshness` and `reasons`
- preserve traceable links back to the source observations used for a decision
- preserve traceable links to public context when external evidence contributes to a decision
- preserve distinctions between local private evidence, shared neighborhood evidence, and public context
- avoid emitting language that implies emergency authorization or guaranteed safety
- downgrade or ignore stale public context according to a defined freshness policy
- read hazard thresholds from versioned configuration where practical
- read trust gates for stale-data suppression, low-confidence limits, and disagreement handling from versioned configuration where practical

## Open questions

- Should the first inference logic be rules-based only, or allow lightweight probabilistic models from the start?
- How should parcel context be represented when exact building features are unknown?
- What minimum evidence should be required before any non-`unknown` status is allowed?
- Should public context be treated as supporting evidence only unless local nodes confirm it?
