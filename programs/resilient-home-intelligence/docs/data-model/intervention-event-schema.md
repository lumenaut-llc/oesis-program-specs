# Intervention Event Schema

## Purpose

Define the private `v1.5` support object for logging an operational action, bounded control action, or material intervention tied to one parcel.

## Core fields

- `intervention_id`
- `parcel_id`
- `recorded_at`
- `hazard_target`
- `action_kind`
- `initiated_by`
- `status`
- `baseline_window_minutes`
- `evaluation_window_minutes`

## Minimum object

```json
{
  "intervention_id": "intv_001",
  "parcel_id": "parcel_001",
  "recorded_at": "2026-04-03T18:25:00Z",
  "hazard_target": "smoke",
  "action_kind": "hvac_recirculate_on",
  "initiated_by": "homeowner",
  "status": "completed",
  "baseline_window_minutes": 30,
  "evaluation_window_minutes": 90,
  "notes": "manual action after outdoor PM spike"
}
```

## Design rules

- private parcel data by default
- may represent manual, suggested, or bounded-control actions
- should support later verification without implying that the action necessarily worked
