# Control Compatibility Schema

## Purpose

Define the private `v1.5` support object that records what parcel systems can be influenced, through which interface class, and with what locality assumptions.

## Core fields

- `parcel_id`
- `updated_at`
- `local_controller`
- `control_surfaces`

## Minimum object

```json
{
  "parcel_id": "parcel_001",
  "updated_at": "2026-04-03T18:20:00Z",
  "local_controller": {
    "available": true,
    "controller_type": "home_assistant"
  },
  "control_surfaces": [
    {
      "control_id": "thermostat_main",
      "system_type": "thermostat",
      "interface_class": "home_assistant",
      "locality": "local_only",
      "integration_tier": "soft_integration",
      "enabled": false,
      "override_rule": "homeowner_opt_in_required"
    }
  ]
}
```

## Design rules

- private parcel data by default
- compatibility is not permission
- locality must stay explicit: `local_only`, `cloud_required`, `hybrid`, or `unknown`
- early integration targets should remain reversible, bounded, low-risk, and verifiable
