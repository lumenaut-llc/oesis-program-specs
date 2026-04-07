# Interfaces

## Public API surfaces

- `POST /v1/ingest/node-packets`
  Accept a single node packet payload plus optional transport metadata.
- `POST /v1/ingest/node-batch`
  Optional future batch endpoint for buffered offline uploads.
- `GET /v1/ingest/health`
  Report service health and current schema support.
- `GET /v1/ingest/schemas`
  Return supported packet schema versions and deprecation status.

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
  Defined in `docs/data-model/node-observation-schema.md`

First external adapter contract:
- raw public weather payload
  Normalized by `scripts/normalize_public_weather_context.py` into the canonical public-context object defined in `docs/data-model/public-context-schema.md`
- raw public smoke payload
  Normalized by `scripts/normalize_public_smoke_context.py` into the canonical public-context object defined in `docs/data-model/public-context-schema.md`

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
- How long should raw packets be retained once normalized observations exist?
- Should the ingest service enrich packets with parcel mapping immediately, or leave that join to downstream consumers?
- What freshness threshold should cause a packet to be accepted but marked stale versus rejected outright?
