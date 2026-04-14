# Interfaces

## Public API surfaces

### Stateless reference endpoints (reference implementation)

The reference runtime uses a stateless POST pattern where the caller supplies
a parcel-state payload and receives formatted output. This avoids requiring
persistent state in the parcel-platform service.

- `POST /v1/parcels/state/view`
  Build a dwelling-facing parcel view from a parcel-state payload.
- `POST /v1/parcels/state/evidence-summary`
  Build a display-safe evidence summary directly from a parcel-state payload.
- `GET /v1/parcel-platform/health`
  Report service health and current runtime lane.

### Stateful RESTful endpoints (future production target)

When the system has persistent parcel-state storage and a parcel registry,
the following endpoints should wrap the stateless formatting with lookup
and caching:

- `GET /v1/parcels/{parcel_id}`
  Return parcel metadata needed by the UI.
- `GET /v1/parcels/{parcel_id}/state`
  Return the latest parcel-state snapshot plus explanation and freshness.
- `GET /v1/parcels/{parcel_id}/state/history`
  Return recent parcel-state history.
- `GET /v1/parcels/{parcel_id}/evidence-summary`
  Return a display-safe summary of evidence sources used by the latest state.

These endpoints are not yet implemented in the reference runtime. They require
observation persistence and parcel-state caching — v0.4+ scope.
- `GET /v1/parcels/{parcel_id}/sharing`
  Return the current sharing-mode settings, notice versions, and revocation status.
- `POST /v1/parcels/{parcel_id}/sharing`
  Update sharing-mode settings with an explicit notice/version reference.
- `GET /v1/parcels/{parcel_id}/house-state`
  Return the latest private house-state support object if one exists.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
- `POST /v1/parcels/{parcel_id}/house-state`
  Upsert the private house-state support object for one parcel.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
- `GET /v1/parcels/{parcel_id}/capabilities`
  Return the latest private house-capability support object if one exists.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
- `POST /v1/parcels/{parcel_id}/capabilities`
  Upsert the private house-capability support object for one parcel.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
- `GET /v1/parcels/{parcel_id}/controls`
  Return the latest private control-compatibility support object if one exists.
  **Status: planned** — draft capture under v1.5; full inventory is v2.5.
- `POST /v1/parcels/{parcel_id}/controls`
  Upsert the private control-compatibility support object for one parcel.
  **Status: planned** — draft capture under v1.5; full inventory is v2.5.
- `GET /v1/parcels/{parcel_id}/interventions`
  Return private intervention-event records for one parcel.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
- `POST /v1/parcels/{parcel_id}/interventions`
  Append a private intervention-event record for one parcel.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
- `GET /v1/parcels/{parcel_id}/verification`
  Return private verification-outcome records for one parcel.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
- `POST /v1/parcels/{parcel_id}/verification`
  Append a private verification-outcome record for one parcel.
  **Status: planned** — capability-stage v1.5 bridge surface; no runtime implementation.
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

  > **Recommended direction:** Statuses plus short explanations as the default view. Confidence bands (low/medium/high) rather than numeric probabilities. Raw evidence detail available in the evidence-summary endpoint for advanced users or pilot operators.

- Should the platform expose hazard probabilities directly, or mostly keep them behind explanation text and status labels?

  > **Recommended direction:** Keep probabilities behind explanation text and status labels for the dwelling-facing UI. Expose numeric probabilities only in the evidence-summary for advanced users. Never show raw probabilities without accompanying explanation.

- What should trigger a parcel operator notification: status transitions, freshness failures, confidence drops, or all three?

  > **Recommended direction:** Status transitions and freshness failures for v0.1. Confidence drops are too noisy until the inference engine has stable thresholds. Add confidence-drop notifications in v1.0 after pilot calibration.

- Which parts of provenance should be hidden or generalized when data comes from shared neighborhood context?

  > **Recommended direction:** Hide contributing parcel identifiers and exact observation timestamps from shared context. Show only the aggregate signal type, cell identifier, and delay metadata. Provenance must never enable singling out a contributing parcel.

- Which sharing updates should require step-up confirmation because they materially expand data use?

  > **Recommended direction:** Any transition that moves data from private-only to neighborhood-aggregate or research/pilot sharing should require explicit step-up confirmation with a notice version reference. Narrowing sharing should not require step-up.

- Which support-object fields are genuinely required in the **`v1.5` bridge** versus better left optional until live pilots show their value?

  > **Recommended direction:** House-state first (it has the clearest standalone value for recommendation content). Intervention and verification timelines only after house-state proves useful in at least one pilot. Keep all bridge fields optional until pilot evidence justifies requiring them.

- When does **`control_compatibility`** graduate from optional draft capture to **`v2.5`**-complete inventory requirements?

  > **Recommended direction:** Keep invisible in the parcel UI until v2.5. Draft capture is an API-level concern for pilot operators, not a user-facing feature. Graduate to complete inventory only when integration tiers and bounded-control policy are defined.

- Which future bounded-control permissions must be separated from ordinary data-sharing controls?

  > **Recommended direction:** Any permission that could trigger a physical action (HVAC mode change, fan activation, shade control) must be separated from data-sharing controls and governed by its own consent and audit path. This separation is a v2.5+ concern and should not be conflated with current sharing settings.
