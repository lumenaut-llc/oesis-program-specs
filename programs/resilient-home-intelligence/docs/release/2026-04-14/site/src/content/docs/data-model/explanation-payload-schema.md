---
title: Explanation Payload Schema
description: Structured explanation object accompanying parcel-state outputs for UI rendering, audit, and notifications.
section: data-model
audience: [builder, researcher]
order: 10
status: draft
---

## Purpose

Define a structured explanation object that accompanies parcel-state outputs so downstream systems do not need to reconstruct explanation logic from flat reason strings alone.

## Why this payload exists

The repo already carries homeowner-readable `reasons` and a compact `provenance_summary`, but mixed-source parcel inference now needs a more structured object for:

- explanation UI rendering
- audit and debugging
- future notifications
- safe filtering of evidence detail by audience

## Minimum explanation payload

```json
{
  "headline": "Estimate uses local, shared, and public evidence with limited parcel certainty.",
  "basis": {
    "evidence_mode": "local_plus_public",
    "inference_basis": "local_plus_shared_plus_public",
    "confidence_band": "medium"
  },
  "drivers": [
    "Regional smoke context suggests modest smoke concern.",
    "Shared neighborhood signals suggest nearby smoke concern."
  ],
  "limitations": [
    "No parcel low-point flood sensor is present.",
    "The local node is installed as a reference indoor node."
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
    "shared": true,
    "public": true,
    "parcel_context": true,
    "system": false
  }
}
```

## Field notes

- `headline` -- One sentence suitable for a parcel detail panel or alert preview.
- `basis` -- Machine-usable explanation metadata.
- `drivers` -- Main contributing factors behind the current estimate.
- `limitations` -- Missing evidence, siting constraints, freshness issues, or other caution points.
- `evidence_contributions` -- Stable, source-aware explanation primitives suitable for UI grouping, debugging, and future notifications.
- `source_breakdown` -- Quick machine-readable view of which source classes contributed.

## Design rules

- The explanation payload should summarize, not duplicate full raw provenance.
- Drivers and limitations should be understandable without exposing private raw evidence unnecessarily.
- The payload should stay stable enough for UI rendering even as the reason list evolves.
- Contribution objects should be additive and machine-usable.
