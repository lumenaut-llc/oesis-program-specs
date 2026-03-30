# Parcel State Schema

## Purpose

Define the canonical parcel-level output produced by the inference engine for homeowner-facing use and downstream mapping.

## Core status fields

- `stay_status`
- `enter_status`
- `escape_status`
- `asset_status`
- `confidence`
- `evidence_mode`
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
  "stay_status": "caution",
  "enter_status": "unknown",
  "escape_status": "safe",
  "asset_status": "caution",
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
    ],
    "observation_refs": [
      "obs_01HT..."
    ]
  }
}
```

## Field notes

- `confidence`
  Numeric confidence in the parcel-state assessment, not a claim of physical certainty.
- `reasons`
  Human-readable explanation fragments suitable for UI and audit logs.
- `hazards`
  Hazard-specific supporting scores used to derive the status fields.
- `freshness`
  Explicit recency information so old evidence does not look current.
- `provenance_summary`
  Short reference block pointing to the evidence used for the decision.

## Design rules

- Parcel-state outputs must remain understandable to a homeowner.
- Confidence should fall when evidence is sparse, stale, or conflicting.
- Inference should produce `unknown` when evidence quality is too weak for a stronger claim.
- Hazard scores support the parcel-state output but do not replace the homeowner-readable statuses.
- Every parcel-state snapshot should be traceable back to source observations.

## Related docs

- `node-observation-schema.md`
- `../../software/inference-engine/interfaces.md`
- `../../software/parcel-platform/README.md`
