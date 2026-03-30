# Firmware Notes

## Responsibilities

- boot reliably and identify installed sensors
- sample SHT45 and BME688 on a predictable cadence
- emit timestamped JSON packets with node metadata
- surface health telemetry and read failures without hiding them
- stay simple enough to port later into `mast-lite`

## Sampling cadence

- default bench cadence: every 15 seconds
- quiet long-run mode: every 60 seconds
- warm-up period: discard or flag the first 2 to 5 samples after boot

Gas resistance should be treated as a trend signal, so downstream consumers should look at deltas and rolling windows rather than any single reading.

## Packet shape

Suggested MVP packet:

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
    "bme688": {
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

This packet is intentionally evidence-oriented. It does not attempt to emit `stay_status`, `enter_status`, or other parcel-state fields directly.

## Error handling

- if one sensor fails, continue publishing the remaining sensor data with explicit presence and error fields
- count consecutive read failures per sensor
- trigger a soft restart only after a defined failure threshold, not on a single bad read
- never silently substitute stale values for fresh reads
- expose boot reason and last error in debug logs

## Health telemetry

- uptime
- free heap or equivalent memory watermark
- Wi-Fi connection state if transport is enabled
- sensor presence at boot
- cumulative read failures
- packet sequence counter

## Future enhancements

- local ring buffer for offline replay
- NTP-backed clock sync with explicit drift reporting
- lightweight anomaly flags for rapid smoke or heat changes
- BLE or captive-portal provisioning
- signed packets if node identity assurance becomes important
