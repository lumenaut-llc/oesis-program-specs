# Interfaces

## Public API surfaces

- `POST /v1/ingest/node-packets`
  Accept a single node packet payload plus optional transport metadata.
  Requires `X-OESIS-Parcel-Id` header for node-to-parcel binding.
- `POST /v1/ingest/node-batch`
  Optional future batch endpoint for buffered offline uploads.
- `GET /v1/ingest/health`
  Report service health and current schema support.
- `GET /v1/ingest/schemas`
  Return supported packet schema versions and deprecation status.

## Development / debug endpoints

These endpoints support development and operator debugging. They are not part
of the production contract and may be removed or gated in deployment.

- `GET /v1/ingest/debug/last`
  Return the last accepted normalized observation as JSON (in-memory, not
  persisted). Useful for verifying ingest behavior during serial capture.
- `GET /v1/ingest/live`
  Browser-friendly HTML dashboard showing the last accepted packet with
  auto-refresh. Useful during hardware bring-up and field installation.

## Internal events / jobs

- `observation.normalized`
  Emitted when a packet is accepted and transformed into a canonical observation.
- `ingest.packet.rejected`
  Emitted when validation or authorization fails.
- `node.health.updated`
  Emitted when ingest derives node freshness or repeated-failure signals.
- `ingest.quarantine.created`
  Emitted when a payload should be preserved for manual review.

## Data contracts

Primary MVP contract:

- `oesis.bench-air.v1`
  Defined in [`node-observation-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/node-observation-schema.md)

Shared-lineage contract:

- `oesis.bench-air.v1` from `mast-lite`
  Same packet family with outdoor or sheltered install metadata. Treat
  end-to-end use in the widened parcel kit as part of **program-phase `v0.2`**
  promotion rather than proof of a separate current-truth contract by itself.

Planned next bridge contracts:

- indoor-response observation family
  Future `v1.5` bridge input for indoor PM2.5, indoor temperature, and indoor
  RH. This is a priority addition for response modeling, but not part of the
  current implemented MVP contract set yet.
  Minimum useful fields should include:
  - `observed_at`
  - `parcel_id` or parcel-resolvable `node_id`
  - `pm25_ugm3`
  - `temperature_c`
  - `relative_humidity_pct`
  - quality / health flags
- power-state observation family
  Future `v1.5` bridge input for mains up/down and backup-power posture.
  Minimum useful fields should include:
  - `observed_at`
  - `mains_state`
  - `backup_power_present`
  - `backup_power_active`
  - optional richer battery / generator posture later
- equipment-state snapshot family
  Future `v1.5` support input for HVAC mode, fan, recirculation, purifier,
  window/shade, or pump state where available.
  Minimum useful fields should include:
  - `captured_at`
  - `hvac_mode`
  - `fan_state`
  - `air_source_mode` or recirculation vs fresh-air state
  - purifier / shade / pump state where applicable

Planned next bridge support events:

- action-log entry
  Record what the house or household did, such as switching to recirculation,
  starting a purifier, lowering shades, or activating backup power.
- outcome / verification record
  Record whether conditions improved afterward over a bounded response window.

First external adapter contract:

- raw public weather payload
  Normalized by `python3 -m oesis.ingest.normalize_public_weather_context` into the canonical public-context object defined in [`public-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/public-context-schema.md)
- raw public smoke payload
  Normalized by `python3 -m oesis.ingest.normalize_public_smoke_context` into the canonical public-context object defined in [`public-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/public-context-schema.md)

Expected minimum request body:

```json
{
  "schema_version": "oesis.bench-air.v1",
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
  "derived": {
    "temperature_c_primary": 23.4,
    "relative_humidity_pct_primary": 41.8,
    "pressure_hpa": 1012.6,
    "voc_trend_source": "gas_resistance_ohm"
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

Expected acceptance behavior:

- reject packets without a supported `schema_version`
- reject packets without `node_id` or `observed_at`
- accept partial sensor content if presence and failure state are explicit
- attach an `ingested_at` server timestamp
- persist raw packet and normalized observation together or with a traceable link

Normalized observation shape:

- `observation_id`
- `node_id`
- `parcel_id` when node-to-parcel mapping is known
- `observed_at`
- `ingested_at`
- `observation_type`
- `values`
- `health`
- `provenance`
- `raw_packet_ref`

First normalized public-context shape:

- `context_id`
- `source_kind`
- `source_name`
- `observed_at`
- `coverage_mode`
- `parcel_id`
- `hazards`
- `summary`

## Open questions

- Should initial auth rely on shared API keys, signed packets, or a trusted private network boundary?

  > **Recommended direction:** Private-network-only for v0.1 (serial extract or local HTTP). Shared-secret API key for v1.0 live deployment. Per-node tokens with rotation for v1.5+.

- How long should raw packets be retained once normalized observations exist?

  > **Recommended direction:** Retain raw packets for 90 days post-normalization for audit and debugging. Prune after 90 days unless a retention hold is in effect.

- Should the ingest service enrich packets with parcel mapping immediately, or leave that join to downstream consumers?

  > **Recommended direction:** Leave the parcel join to downstream consumers. Ingest should record node_id and let the parcel-platform or inference engine resolve the mapping. This keeps ingest stateless with respect to parcel topology.

- What freshness threshold should cause a packet to be accepted but marked stale versus rejected outright?

  > **Recommended direction:** Accept packets up to 24 hours old but flag any packet older than 15 minutes as stale in the normalized observation's health object. Never reject solely on age — late data is better than lost data for audit purposes.
