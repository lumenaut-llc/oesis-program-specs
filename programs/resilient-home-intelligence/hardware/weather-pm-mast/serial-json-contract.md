# Serial JSON Contract

## Purpose

Define the exact serial payload shape the weather-pm-mast should emit during first-build bring-up so PM-first outdoor firmware output can be checked locally before any persistent transport exists.

## Transport rule

- emit one complete JSON object per line
- use UTF-8 text over the serial monitor
- keep the serial monitor at `115200`
- do not mix debug chatter into the same line as JSON

## Required packet shape

```json
{
  "schema_version": "rhi.weather-pm-mast.v1",
  "node_id": "weather-pm-mast-01",
  "observed_at": "2026-03-30T19:45:00Z",
  "firmware_version": "0.1.0",
  "location_mode": "outdoor",
  "sensors": {
    "sht45": {
      "present": true,
      "temperature_c": 17.9,
      "relative_humidity_pct": 66.2
    },
    "bme680": {
      "present": true,
      "temperature_c": 18.6,
      "relative_humidity_pct": 64.4,
      "pressure_hpa": 1013.9,
      "gas_resistance_ohm": 149880
    },
    "sps30": {
      "present": true,
      "pm1_ugm3": 7.2,
      "pm2_5_ugm3": 10.8,
      "pm4_ugm3": 12.1,
      "pm10_ugm3": 14.0
    }
  },
  "derived": {
    "temperature_c_primary": 17.9,
    "relative_humidity_pct_primary": 66.2,
    "pressure_hpa": 1013.9,
    "voc_trend_source": "gas_resistance_ohm"
  },
  "health": {
    "uptime_s": 1820,
    "wifi_connected": false,
    "free_heap_bytes": 214332,
    "read_failures_total": 0,
    "last_error": null
  }
}
```

## Current firmware behavior

The first scaffold supports:

- serial-only bring-up with placeholder timestamps
- optional Wi-Fi/NTP time sync if credentials are configured
- PM-first packet output with placeholder PM values until real SPS30 integration is added
