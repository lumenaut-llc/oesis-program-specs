# House Capability Schema

## Purpose

Define the private `v1.5` support object that captures parcel-specific protective capacity and physical limits.

## Why this exists

The platform needs to know what the house can plausibly do before it can recommend credible interventions.

## Core fields

- `parcel_id`
- `updated_at`
- `protective_capacity`
- `hvac_profile`
- `site_profile`

## Minimum object

```json
{
  "parcel_id": "parcel_001",
  "updated_at": "2026-04-03T18:20:00Z",
  "protective_capacity": {
    "backup_power_available": false,
    "portable_purifier_present": true,
    "clean_air_room_ready": false
  },
  "hvac_profile": {
    "system_type": "forced_air",
    "recirculation_available": true,
    "filter_size": "16x25x1",
    "higher_merv_support": "unknown"
  },
  "site_profile": {
    "orientation_class": "southwest_exposed",
    "shading_posture": "mixed",
    "drainage_posture": "driveway_low_point_present"
  }
}
```

## Design rules

- private parcel data by default
- captures capability and constraint, not active runtime state
- stays separate from control compatibility because "can the house benefit from this?" and "can the platform control this?" are different questions
