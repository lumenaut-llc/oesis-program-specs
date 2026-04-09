# Node Registry Schema

## Purpose

Define the parcel-scoped registry object that binds one or more physical nodes to one parcel, one software stack, and one homeowner-facing parcel view.

## Core fields

- `updated_at`
- `parcel_id`
- `nodes`

Each node entry includes:

- `node_id`
- `node_class`
- `hardware_family`
- `schema_version`
- `observation_family`
- `location_mode`
- `install_role`
- `transport_mode`
- `power_mode`
- `calibration_state`
- `installed_at`
- `last_seen_at`
- `enabled`

Optional fields:

- `firmware_version`
- `privacy_mode`

## Minimum object

```json
{
  "updated_at": "2026-04-01T18:00:00Z",
  "parcel_id": "parcel_123",
  "nodes": [
    {
      "node_id": "bench-air-01",
      "node_class": "indoor_air",
      "hardware_family": "bench-air-node",
      "schema_version": "oesis.bench-air.v1",
      "observation_family": "air.node.snapshot",
      "location_mode": "indoor",
      "install_role": "indoor_reference",
      "transport_mode": "https_push",
      "power_mode": "usb_c_mains",
      "calibration_state": "verified",
      "installed_at": "2026-03-29T18:00:00Z",
      "last_seen_at": "2026-04-01T17:58:00Z",
      "enabled": true
    }
  ]
}
```

## Design rules

- There is one node registry per parcel, not one registry per node.
- `parcel_id` lives at the registry layer so hardware packets do not need to carry exact parcel identity.
- `node_id` must be unique within the registry and should remain stable across firmware updates.
- `hardware_family` describes the physical build lineage, while `schema_version` describes the emitted packet contract.
- `observation_family` describes the normalized ingest output expected from that packet lineage.
- `install_role` captures why the node exists in the parcel system, not just where it is mounted.
- `enabled: false` means the node remains historically known but should not be treated as active evidence.
- `privacy_mode` is optional and primarily relevant to node classes such as `thermal-pod`.

## Why this object matters

The integrated parcel design depends on multiple specialized nodes behaving like one system.
The node registry is the bridge between:

- hardware installation
- ingest authorization and parcel binding
- calibration tracking
- inference observability assumptions
- operator troubleshooting

## Related docs

- `../../architecture/current/README.md`
- `node-observation-schema.md`
- `parcel-context-schema.md`
- `sharing-settings-schema.md`
- `../system-overview/integrated-parcel-system-spec.md`
- `../build-guides/integrated-parcel-kit-bom.md`
