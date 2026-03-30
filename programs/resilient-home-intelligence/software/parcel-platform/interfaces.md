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

## Internal events / jobs

- `parcel.state.updated`
  Refresh cached current-state views.
- `parcel.profile.updated`
  Refresh parcel metadata and access rules.
- `parcel.notification.candidate`
  Future event for noteworthy status changes or sharp confidence shifts.

## Data contracts

Primary input contract:
- parcel-state snapshot from `docs/data-model/parcel-state-schema.md`

Primary response shape for current state:
- `parcel_id`
- `computed_at`
- `statuses`
- `confidence`
- `evidence_mode`
- `reasons`
- `hazards`
- `freshness`
- `provenance_summary`

Suggested response example:

```json
{
  "parcel_id": "parcel_123",
  "computed_at": "2026-03-30T19:46:00Z",
  "statuses": {
    "stay": "caution",
    "enter": "unknown",
    "escape": "safe",
    "asset": "caution"
  },
  "confidence": 0.54,
  "evidence_mode": "local_only",
  "reasons": [
    "Indoor air observations show an abrupt gas-trend change.",
    "No confirming outdoor or neighborhood evidence is available."
  ],
  "hazards": {
    "smoke_probability": 0.42,
    "flood_probability": 0.05,
    "heat_probability": 0.27
  },
  "freshness": {
    "latest_observation_at": "2026-03-30T19:45:00Z",
    "seconds_since_latest": 60,
    "stale": false
  },
  "provenance_summary": {
    "observation_count": 3,
    "source_modes": [
      "homeowner_node"
    ]
  }
}
```

## Open questions

- How much raw evidence detail should a homeowner see before the UI becomes noisy or misleading?
- Should the platform expose hazard probabilities directly, or mostly keep them behind explanation text and status labels?
- What should trigger a homeowner notification: status transitions, freshness failures, confidence drops, or all three?
- Which parts of provenance should be hidden or generalized when data comes from shared neighborhood context?
