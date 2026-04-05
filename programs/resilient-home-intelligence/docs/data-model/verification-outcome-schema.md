# Verification Outcome Schema

## Purpose

Define the private `v1.5` support object for recording whether an intervention appears to have improved conditions during a verification window.

## Core fields

- `verification_id`
- `parcel_id`
- `intervention_id`
- `evaluated_at`
- `metric_name`
- `baseline_value`
- `outcome_value`
- `assessment`
- `confidence_band`

## Minimum object

```json
{
  "verification_id": "verify_001",
  "parcel_id": "parcel_001",
  "intervention_id": "intv_001",
  "evaluated_at": "2026-04-03T19:40:00Z",
  "metric_name": "indoor_pm25_ugm3",
  "baseline_value": 42.0,
  "outcome_value": 19.5,
  "assessment": "improved",
  "confidence_band": "medium",
  "response_window_minutes": 75,
  "summary": "Indoor PM fell during the verification window after recirculation and purifier use."
}
```

## Design rules

- private parcel data by default
- must stay distinct from hazard confidence
- should support `improved`, `no_change`, `worsened`, or `inconclusive`
- verification should help later ranking and learning, not inflate present-tense certainty
