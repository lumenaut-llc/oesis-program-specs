# Thermal Slope Inference for HVAC Mode Detection

## Purpose

Infer whether HVAC is actively cooling, heating, or idle by comparing observed
indoor temperature slope against expected passive thermal behavior. This provides
a low-confidence but zero-friction alternative to direct CT clamp or API-based
HVAC state detection.

When no smart thermostat API or circuit-monitor hardware is available, thermal
slope inference is the only way to approximate equipment operating state from a
standard parcel sensor kit.

## Method

### 1. Compute observed indoor temperature slope

Perform linear regression over the last 30 minutes of indoor temperature
readings. Minimum evidence requirement: 4 readings at 5-minute intervals (6
readings preferred). Fewer than 4 readings within the window produces no
inference (`confidence_band: "none"`).

The result is `observed_slope` in degrees Fahrenheit per hour.

### 2. Compute expected passive slope

The expected passive slope models what indoor temperature would do with no active
conditioning, driven only by thermal exchange with outdoor air:

```
expected_passive_slope = passive_exchange_rate * (outdoor_temp - indoor_temp)
```

`passive_exchange_rate` is a per-parcel calibration constant (default
0.05 degF/hr per degF delta for a typical single-family wood-frame home).
Thermal mass class adjustments:

| Thermal mass class | passive_exchange_rate | Typical construction |
| --- | --- | --- |
| `light` | 0.07 | Mobile home, poorly insulated frame |
| `medium` (default) | 0.05 | Standard wood-frame residential |
| `heavy` | 0.03 | Masonry, concrete, well-insulated new build |

### 3. Compute deviation

```
deviation = observed_slope - expected_passive_slope
```

A negative deviation means the house is cooling faster than passive exchange
predicts. A positive deviation means it is warming faster.

### 4. Classify HVAC mode

| Condition | Classification | `confidence_band` |
| --- | --- | --- |
| `abs(deviation) < 0.3` | `idle_or_off` | `low` |
| `deviation < -0.8` | `cooling_active` | `low` |
| `deviation > 0.8` | `heating_active` | `low` |
| `deviation < -1.5` | `cooling_active` | `medium` |
| `deviation > 1.5` | `heating_active` | `medium` |
| `0.3 <= abs(deviation) <= 0.8` | `unknown` | `low` |

## Confidence levels

This method always produces `low` or `medium` confidence. It never reaches
`high`.

Known limitations:

- Cannot distinguish recirculate from fresh-air mode. This is critical for smoke
  response and means thermal slope inference alone is insufficient to confirm
  smoke-protect posture.
- Cannot detect fan-only mode reliably. Fan operation without compressor produces
  negligible temperature change.
- Degrades during rapid outdoor temperature changes (sunrise/sunset transitions,
  frontal passages). When outdoor temperature changes more than 5 degF within the
  30-minute regression window, classification degrades to `unknown`.
- Cannot distinguish active heating from solar gain on south-facing structures.

## Self-calibration

When a higher-fidelity source is also present for the same parcel (CT clamp via
circuit-monitor node, or thermostat API via equipment-state adapter), the system
should use the ground-truth operating state to calibrate per-parcel thermal
response constants.

Calibration targets:

- `passive_cooling_rate`: observed slope when HVAC is confirmed off and outdoor
  temperature exceeds indoor by at least 5 degF
- `passive_heating_rate`: observed slope when HVAC is confirmed off and indoor
  temperature exceeds outdoor by at least 5 degF
- `active_cooling_slope`: typical slope during confirmed cooling operation
- `active_heating_slope`: typical slope during confirmed heating operation

Update method: exponential moving average with `alpha = 0.1` (slow adaptation,
resistant to transients). Only update when the ground-truth source has
`confidence_band: "high"` and the 30-minute regression window has at least 5
readings.

Calibrated constants are stored per parcel in parcel context and survive across
inference engine restarts.

## Integration with equipment-state-observation

Thermal slope inference produces an `equipment-state-observation` record with:

- `source.source_kind`: `"inferred"`
- `source.source_name`: `"thermal_slope_inference"`
- `source.method`: `"indoor_temp_linear_regression_vs_passive_model"`
- `source.ttl_seconds`: `600` (10 minutes; inference should be refreshed at
  least this often)
- `confidence_band`: `"low"` or `"medium"` per the classification table above

The tiered adapter registry in the inference engine tries sources in this order:

1. Direct measurement (CT clamp, panel-level sensing) -- highest priority
2. Adapter-derived (cloud API or local integration) -- second priority
3. Inferred (thermal slope or other passive methods) -- fallback only

If a higher-tier source is fresh (within its TTL), the thermal slope inference
result is suppressed in the output but may still run in the background for
calibration purposes.

## When NOT to use

Suppress thermal slope classification and emit `unknown` during:

- **Cooking events**: rapid indoor temperature spikes from oven or stovetop use.
  Heuristic: indoor temperature increase exceeding 2 degF in 10 minutes without
  corresponding outdoor change.
- **Door/window open events**: rapid indoor temperature change from infiltration.
  Detectable when indoor temperature rapidly converges toward outdoor temperature
  at a rate exceeding the `heavy` thermal mass class passive rate.
- **First 30 minutes after HVAC mode change**: transient response period where
  the system is between steady states. If the previous equipment-state-observation
  recorded a different mode within the last 30 minutes, suppress classification.
- **Insufficient outdoor temperature data**: if the outdoor temperature source is
  stale (older than 30 minutes) or missing, passive slope cannot be computed.

## Related docs

- [`v1.5/equipment-state-observation-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/equipment-state-observation-schema.md)
- [`v1.5/schemas/equipment-state-observation.schema.json`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/schemas/equipment-state-observation.schema.json)
- `../../architecture/system/node-taxonomy.md`
- `architecture.md`
- `open-questions.md`
