# House State Schema

## Purpose

Define the minimum private house-state support object added in the **`v1.5`**
bridge so the product can move from parcel sensing toward measured household
response without changing the baseline parcel-state contract.

## Stage placement

This is a **`v1.5`** support object, not part of the `current v1`
parcel-state spine.

It exists to capture the minimum household response evidence needed for the
first serious closed loop:

- indoor PM2.5
- indoor temperature
- indoor relative humidity
- mains status
- backup-power posture

## Minimum object

```json
{
  "parcel_id": "parcel_demo_001",
  "captured_at": "2026-04-14T19:20:00Z",
  "indoor_response": {
    "pm25_ugm3": 18.2,
    "temperature_c": 27.1,
    "relative_humidity_pct": 43.0
  },
  "power_state": {
    "mains_state": "up",
    "backup_power_present": true,
    "backup_power_active": false
  },
  "source_summary": {
    "node_ids": ["indoor-response-01"],
    "source_kind": "private_support_object"
  }
}
```

## Minimum fields

- `parcel_id`
- `captured_at`
- `indoor_response`
- `power_state`

### `indoor_response`

- `pm25_ugm3`
- `temperature_c`
- `relative_humidity_pct`

### `power_state`

- `mains_state`
- `backup_power_present`
- `backup_power_active`

Optional later additions may include:

- `battery_soc_pct`
- `generator_state`
- richer per-room or per-zone indoor-response breakdowns

## Design rules

- This object should stay private by default.
- It should capture **measured house state**, not recommendations.
- It should not silently become a controls object.
- It exists so later intervention and verification records can answer whether
  the house actually protected occupants during smoke, heat, outage, or similar
  events.

## Related docs

- `../parcel-state-schema.md`
- `../parcel-context-schema.md`
- `intervention-event-schema.md`
- `verification-outcome-schema.md`
- `../../architecture/v1.5/house-state-and-verification-model.md`
