---
title: Node Observation Schema
description: Canonical evidence packet and normalized observation model used between hardware nodes and the ingest service.
section: data-model
audience: [builder, researcher]
order: 2
status: stable
schema_file: node-observation.schema.json
example_file: node-observation.example.json
---

## Purpose

Define the canonical evidence packet and normalized observation model used between hardware nodes and the ingest service.

## First supported schema version

- `rhi.bench-air.v1`

This version covers the bench-air-node MVP and establishes the minimum structure future node schemas should preserve:
- explicit schema versioning
- stable node identity
- observation timestamp
- sensor presence reporting
- health telemetry
- provenance-friendly raw payload retention

## Raw packet contract

Required top-level fields:
- `schema_version`
- `node_id`
- `observed_at`
- `firmware_version`
- `location_mode`
- `sensors`
- `health`

Optional top-level fields:
- `derived`
- `sequence`
- `transport`
- `notes`

Example packet:

```json
{
  "schema_version": "rhi.bench-air.v1",
  "node_id": "bench-air-01",
  "observed_at": "2026-03-30T19:45:00Z",
  "firmware_version": "0.1.0",
  "location_mode": "indoor",
  "sensors": {
    "sht45": {
      "present": true,
      "temperature_c": 23.4,
      "relative_humidity_pct": 41.8
    },
    "bme680": {
      "present": true,
      "temperature_c": 24.1,
      "relative_humidity_pct": 40.9,
      "pressure_hpa": 1012.6,
      "gas_resistance_ohm": 145230
    }
  },
  "health": {
    "uptime_s": 1820,
    "wifi_connected": true,
    "free_heap_bytes": 214332,
    "read_failures_total": 0,
    "last_error": null
  }
}
```

## Normalized observation model

Suggested canonical shape after ingest:

```json
{
  "observation_id": "obs_01HT...",
  "node_id": "bench-air-01",
  "parcel_id": "parcel_123",
  "observed_at": "2026-03-30T19:45:00Z",
  "ingested_at": "2026-03-30T19:45:02Z",
  "observation_type": "air.node.snapshot",
  "values": {
    "temperature_c_primary": 23.4,
    "relative_humidity_pct_primary": 41.8,
    "pressure_hpa": 1012.6,
    "gas_resistance_ohm": 145230
  },
  "provenance": {
    "source_kind": "homeowner_node",
    "schema_version": "rhi.bench-air.v1",
    "firmware_version": "0.1.0",
    "raw_packet_ref": "rawpkt_01HT..."
  }
}
```

## Design rules

- Raw evidence should remain recoverable after normalization.
- Ingest should not convert observations directly into parcel-state outputs.
- Missing sensor values must be explicit, not silently omitted because of read errors.
- Future schemas should extend by version, not by changing the meaning of existing fields in place.
