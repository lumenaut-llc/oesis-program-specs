# Interfaces

## Public API surfaces

- `GET /v1/parcels/{parcel_id}/state`
  Return the latest parcel-state snapshot for the parcel.
- `GET /v1/parcels/{parcel_id}/state/history`
  Return prior parcel-state snapshots and freshness metadata.
- `POST /v1/inference/recompute/{parcel_id}`
  Trigger an explicit recompute for one parcel.
- `GET /v1/inference/models`
  Return active hazard model versions or threshold sets.

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
- normalized observation records from `docs/data-model/node-observation-schema.md`

Primary output contract:
- parcel-state snapshot defined in `docs/data-model/parcel-state-schema.md`

Minimum parcel-state output fields:
- `parcel_id`
- `computed_at`
- `stay_status`
- `enter_status`
- `escape_status`
- `asset_status`
- `confidence`
- `evidence_mode`
- `reasons`
- `hazards`
- `freshness`
- `provenance_summary`

Expected engine behavior:
- accept sparse evidence and lower confidence instead of fabricating certainty
- score hazards independently before mapping to parcel-state outputs
- represent stale or missing evidence explicitly in `freshness` and `reasons`
- preserve traceable links back to the source observations used for a decision

## Open questions

- Should the first inference logic be rules-based only, or allow lightweight probabilistic models from the start?
- How should parcel context be represented when exact building features are unknown?
- What minimum evidence should be required before any non-`unknown` status is allowed?
- Should public context be treated as supporting evidence only unless local nodes confirm it?
