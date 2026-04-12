# Parcel State Schema

## Purpose

Define the canonical parcel-level output produced by the inference engine for dwelling-facing use and downstream mapping.

## Version boundary

This schema represents the current `v1` parcel sensing and inference baseline.

It stays stable through `v1.5` so the repo can add house-state, capability, compatibility, intervention, and verification objects without forcing a breaking parcel-state change.

Narrative aliases such as `stay_safe`, `enter_safe`, `escape_safe`, and `asset_safe` may appear in planning documents, but the current repo keeps the existing field names through at least `v2`.

## Core status fields

- `shelter_status`
- `reentry_status`
- `egress_status`
- `asset_risk_status`
- `confidence`
- `evidence_mode`
- `inference_basis`
- `reasons`

Suggested initial enum for status fields:
- `safe`
- `caution`
- `unsafe`
- `unknown`

Suggested initial enum for `evidence_mode`:
- `local_only`
- `local_plus_public`
- `public_only`
- `insufficient`

Suggested initial enum for `inference_basis`:
- `local_only`
- `local_plus_shared`
- `local_plus_public`
- `local_plus_shared_plus_public`
- `public_only`
- `shared_only`
- `shared_plus_public`
- `insufficient`

## Supporting values

- `smoke_probability`
- `flood_probability`
- `heat_probability`
- `explanation_payload`
- `freshness`
- `provenance_summary`

## Minimum parcel-state object

```json
{
  "parcel_id": "parcel_123",
  "computed_at": "2026-03-30T19:46:00Z",
  "shelter_status": "unknown",
  "reentry_status": "unknown",
  "egress_status": "unknown",
  "asset_risk_status": "unknown",
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
      },
      {
        "contribution_id": "local_siting_limit",
        "source_class": "local",
        "source_name": "bench-air-01",
        "role": "limitation",
        "summary": "Current local evidence comes from an indoor node and does not directly represent parcel-wide outdoor conditions.",
        "hazards": ["smoke", "heat", "flood"],
        "weight": 0.72,
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
    ],
    "observation_refs": [
      "obs_example_0001"
    ]
  }
}
```

## Field notes

- `confidence`
  Numeric confidence in the parcel-state assessment, not a claim of physical certainty.
- `reasons`
  Human-readable explanation fragments suitable for UI and audit logs.
- `inference_basis`
  Machine-facing evidence-composition field that distinguishes mixed-source combinations more precisely than the dwelling-facing `evidence_mode`.
- `explanation_payload`
  Structured explanation object for UI composition, notification drafting, and audit support.
  Its `drivers` and `limitations` should be derived from weighted `evidence_contributions`, not maintained as unrelated text lists.
  The payload may also include `system` limitations for missing context or other engine-detected absences that are not true source classes.
- `hazards`
  Hazard-specific supporting scores used to derive the status fields.
- `freshness`
  Explicit recency information so old evidence does not look current.
- `provenance_summary`
  Short reference block pointing to the evidence used for the decision.

## Design rules

- Parcel-state outputs must remain understandable to a parcel operator.
- Status labels should frame conditions and risk, not imply emergency authorization or guarantees.
- Confidence should fall when evidence is sparse, stale, or conflicting.
- Inference should produce `unknown` when evidence quality is too weak for a stronger claim.
- `evidence_mode` may remain a coarse dwelling-facing summary while `inference_basis` carries the exact source composition for backend use.
- Hazard scores support the parcel-state output but do not replace the parcel operator-readable statuses.
- Every parcel-state snapshot should be traceable back to source observations.

## Planned follow-on additions

`v1.5`:
- keep parcel-state stable
- store house-state, capability, compatibility, intervention, and verification data as separate support objects

`v2` and later may add optional presentation summaries such as:
- bounded recommendations
- actionability notes
- recommendation or verification references

Those additions should not erase the current distinction between condition estimate and later-stage adaptation logic.

## Related docs

- `node-observation-schema.md`
- `parcel-context-schema.md`
- `house-state-schema.md`
- `intervention-event-schema.md`
- `verification-outcome-schema.md`
- `explanation-payload-schema.md`
- `../../software/inference-engine/interfaces.md`
- `../../software/parcel-platform/README.md`
