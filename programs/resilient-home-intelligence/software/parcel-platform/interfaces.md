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
  Create an export request for homeowner-visible parcel data.
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
- parcel-state snapshot from `docs/data-model/parcel-state-schema.md`

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
`v1.5` support objects stay separate from the state payload so the current contract does not break.

Support-object response shapes:

- `house_state`
- `house_capability`
- `control_compatibility`
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
        "visibility": "homeowner_safe"
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
      "homeowner_node"
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

- How much raw evidence detail should a homeowner see before the UI becomes noisy or misleading?
- Should the platform expose hazard probabilities directly, or mostly keep them behind explanation text and status labels?
- What should trigger a homeowner notification: status transitions, freshness failures, confidence drops, or all three?
- Which parts of provenance should be hidden or generalized when data comes from shared neighborhood context?
- Which sharing updates should require step-up confirmation because they materially expand data use?
- Which support-object fields are genuinely required in `v1.5` versus better left optional until live pilots show their value?
- Which future bounded-control permissions must be separated from ordinary data-sharing controls?
