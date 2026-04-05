# House State Schema

## Purpose

Define the private `v1.5` support object that captures current indoor conditions and household operating state without changing the parcel-state contract.

## Why this exists

The platform cannot evolve from parcel sensing into parcel adaptation if it only captures outside hazard measurements.

This object helps answer:
- what state is the house currently in?
- what systems were available or active during the event?

## Core fields

- `parcel_id`
- `updated_at`
- `observed_at`
- `indoor_air`
- `hvac_state`
- `device_state`

## Minimum object

```json
{
  "parcel_id": "parcel_001",
  "updated_at": "2026-04-03T18:20:00Z",
  "observed_at": "2026-04-03T18:15:00Z",
  "indoor_air": {
    "pm25_ugm3": 18.4,
    "temperature_c": 24.2,
    "relative_humidity_pct": 42.1
  },
  "hvac_state": {
    "mode": "cool",
    "fan_mode": "on",
    "air_mode": "recirculate",
    "filter_condition": "ok"
  },
  "device_state": {
    "purifier_state": "on",
    "backup_power_state": "standby",
    "window_state": "closed",
    "shade_state": "partial",
    "sump_state": "unknown"
  }
}
```

## Design rules

- private parcel data by default
- reflects current operating state, not permission to control anything
- should improve recommendation quality and response analysis, not silently increase hazard confidence on its own
