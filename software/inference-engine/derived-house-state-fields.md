# Derived House-State Fields

## Purpose

Document the computation logic for derived house-state fields that make the
smoke and heat closed loops concrete without requiring new hardware. These
fields live inside `indoor_response` as optional objects (`infiltration` and
`thermal_dynamics`) and are computed by the inference engine from existing
indoor-response observations, outdoor context, and equipment-state records.

## Status

Draft

## Owner

Open Environmental Sensing and Inference System

## Related files

- `../../contracts/v1.5/house-state-schema.md`
- `hazard-logic-v0.md`
- `../../contracts/v1.5/schemas/house-state.schema.json`
- `../../contracts/v1.5/schemas/equipment-state-observation.schema.json`

---

## IO Ratio Baseline Characterization

### What it is

The indoor/outdoor PM2.5 ratio under non-event, non-intervention conditions
is the parcel's structural smoke infiltration signature. A well-sealed home
with good filtration will show a low IO ratio even when outdoor PM is
moderately elevated. A leaky home or one with poor filtration will track
outdoor levels closely. This ratio, computed as a rolling baseline, tells the
inference engine what to expect from the smoke closed loop before an event
begins.

### Qualifying conditions for baseline samples

A sample qualifies for the baseline window only when all of the following hold:

1. Outdoor PM2.5 is between 5 and 30 ug/m3. Below 5, sensor noise dominates
   the ratio. Above 30, the parcel may already be in an event and occupant
   behavior (closing windows, running purifiers) distorts the passive
   infiltration signal.
2. Purifier is off (from equipment-state if available; otherwise assume off
   when no equipment-state record exists).
3. HVAC is not in fresh-air or ventilation mode (from equipment-state or
   thermostat API if available).
4. Outdoor PM2.5 exceeds indoor PM2.5 by at least 2 ug/m3. When indoor
   exceeds outdoor, an internal source (cooking, cleaning) is likely active
   and the sample does not represent infiltration behavior.

### Baseline computation

- Window: rolling 30 days.
- Statistic: median of qualifying IO ratio samples.
- Also compute 25th and 75th percentiles (`baseline_io_p25`,
  `baseline_io_p75`) to characterize spread.
- Track `baseline_sample_count` so consumers know whether the baseline is
  mature or provisional.
- Recompute at most once per hour; store `baseline_last_updated`.

### Envelope classification

Derived from `baseline_io_ratio`:

| `baseline_io_ratio` | `envelope_class` |
|---------------------|------------------|
| < 0.20              | `tight`          |
| 0.20 -- 0.40       | `average`        |
| > 0.40              | `leaky`          |
| insufficient data   | `unknown`        |

Minimum sample count for classification: 30 qualifying samples. Below that
threshold, `envelope_class` should remain `unknown`.

### How envelope class conditions smoke loop outcomes

The envelope class sets expected effectiveness for bounded interventions
during a smoke event:

- **tight**: purifier + recirculation should achieve roughly 90% indoor PM
  reduction relative to outdoor. Response window for measurable improvement:
  15-30 minutes.
- **average**: purifier + recirculation should achieve roughly 70% reduction.
  Response window: 30-60 minutes.
- **leaky**: purifier + recirculation achieves roughly 55% reduction at best,
  and improvement may plateau before reaching safe levels. Response window:
  45-90 minutes, with diminishing returns beyond 60 minutes.
- **unknown**: use conservative (leaky) assumptions until baseline matures.

These expected outcomes feed into the verification logic. If measured
improvement after intervention falls significantly short of what the envelope
class predicts, the system should flag the discrepancy for operator review
(possible equipment issue, window left open, or misclassified envelope).

---

## Indoor Rise Rate and Time-to-Threshold

### What it is

During a heat event or power outage, indoor temperature rises as the building
loses its thermal buffer. The rate of rise and the projected time until
conditions become dangerous are the core inputs for the heat closed loop.
These fields let the system distinguish a house that is slowly warming over
many hours from one that will reach dangerous conditions within the hour.

### 2-hour rolling linear regression

Compute a simple linear regression (ordinary least squares) on the most
recent 2 hours of indoor temperature readings, with time in hours as the
independent variable and temperature in Fahrenheit as the dependent variable.

- Convert temperature_c to Fahrenheit for the regression and output fields,
  since heat danger thresholds in the US context are conventionally expressed
  in Fahrenheit.
- The slope is `indoor_rise_rate_f_per_hour`.
- Require at least 6 data points (at 5-minute intervals, this means 30
  minutes of history) before computing. With fewer points, do not emit
  thermal_dynamics.

### R-squared quality gating

`rise_rate_r2` is the coefficient of determination from the regression.

- R2 >= 0.7: the temperature trend is coherent and likely represents genuine
  thermal accumulation or loss. Use the slope and projection with normal
  confidence.
- 0.4 <= R2 < 0.7: noisy trend, possibly caused by intermittent door
  openings, cooking, or short HVAC cycles. Emit the fields but lower
  confidence. Time-to-threshold should carry wider confidence intervals.
- R2 < 0.4: too noisy to project meaningfully. Emit `rise_rate_r2` for
  diagnostic purposes but set `time_to_threshold_hours` to null and
  `recommendation` to `monitor_closely` at most.

### Time-to-threshold projection

When `indoor_rise_rate_f_per_hour` is positive (warming):

```
time_to_threshold_hours = (threshold_f - current_indoor_f) / indoor_rise_rate_f_per_hour
```

When `indoor_rise_rate_f_per_hour` is zero or negative (not warming):
`time_to_threshold_hours` = null.

### Threshold selection

- Default threshold: 88 deg F (31.1 deg C). This is the point where
  sustained indoor exposure creates meaningful health risk for healthy adults.
- Vulnerable occupant threshold: 82 deg F (27.8 deg C). Applied when the
  parcel context indicates vulnerable occupants (elderly, very young, or
  medically fragile). The parcel context field for this is TBD but should
  exist before v1.5 ships.

### Uncertainty propagation

Confidence intervals on time-to-threshold use the standard error of the
regression slope:

```
slope_stderr = standard_error_of_slope_from_regression

ci_delta_hours = (slope_stderr * sqrt(time_to_threshold_hours)) / abs(indoor_rise_rate_f_per_hour)

confidence_interval_low_hours  = time_to_threshold_hours - ci_delta_hours
confidence_interval_high_hours = time_to_threshold_hours + ci_delta_hours
```

Clamp `confidence_interval_low_hours` to a minimum of 0.

When R2 is between 0.4 and 0.7, multiply `ci_delta_hours` by 1.5 to reflect
the additional uncertainty from a noisy regression.

### Recommendation ladder

Maps from projected time-to-threshold with a 1-hour safety buffer subtracted:

| `time_to_threshold_hours` | `recommendation`        |
|--------------------------|-------------------------|
| not warming (null)       | `no_action_needed`      |
| > 7 hours                | `low_urgency`           |
| 4 -- 7 hours             | `monitor_closely`       |
| 2 -- 4 hours             | `pre_cool_recommended`  |
| 0.5 -- 2 hours           | `act_now`               |
| < 0.5 hours              | `immediate_action`      |

Note: these thresholds include the 1-hour safety buffer. A raw projection of
3 hours maps to an effective action window of 2 hours, which falls into
`pre_cool_recommended`.

The `recommendation` field is a household-facing signal, not a parcel-state
status. It should never change `shelter_status` or `reentry_status` in the
parcel-state contract.

---

## Thermal Profile Self-Calibration

### What it is

When a CT clamp on the HVAC breaker or a thermostat API provides ground-truth
HVAC state (on/off, heating/cooling mode), the inference engine can use it to
calibrate parcel-specific passive cooling and heating rates. This makes
time-to-threshold projections more accurate over time because the engine
learns how fast this specific house gains or loses heat when HVAC is off.

### Calibration method

Use an exponential moving average (EMA) with alpha = 0.1 to update the
parcel's calibrated passive rise rate and passive cooling rate:

```
calibrated_rate = alpha * observed_rate + (1 - alpha) * calibrated_rate
```

Where `observed_rate` is the measured temperature change rate during a
confirmed HVAC-off period (from CT clamp or thermostat API).

- Only update when the HVAC-off period is at least 30 minutes (enough for a
  meaningful slope).
- Separate calibrated rates for heating season and cooling season, since
  building thermal behavior differs by direction.
- Alpha = 0.1 provides slow, stable calibration that resists outliers from
  brief door openings or cooking events.

### Convergence timeline

At roughly 3-5 qualifying HVAC-off periods per day during normal cycling,
the EMA reaches useful stability after approximately 100 samples, which is
1-2 weeks of normal HVAC operation. Until then, use uncalibrated regression
slopes directly.

### When calibration is available

If the parcel has a mature calibrated passive rise rate (100+ samples), the
inference engine should:

1. Use the calibrated rate as a Bayesian prior when computing
   `indoor_rise_rate_f_per_hour`, especially when current regression R2 is
   low.
2. Narrow the confidence intervals on time-to-threshold since the
   parcel-specific thermal model reduces uncertainty.
3. Flag significant deviations from the calibrated rate (> 2 sigma) as
   potential anomalies (window left open, equipment malfunction, unusual
   occupant activity).

### Equipment-state dependency

Thermal profile calibration requires equipment-state observations. Without
them, the engine falls back to uncalibrated regression, which is still
useful but less precise. This creates a natural incentive for parcels to
connect CT clamps or thermostat APIs without making those connections
mandatory for the heat closed loop to function at all.

---

## Design constraints

- These derived fields are **computed outputs**, not raw sensor readings. They
  must never be confused with measured values.
- `infiltration` and `thermal_dynamics` are optional objects. The house-state
  contract remains valid without them. The inference engine emits them only
  when sufficient input data exists.
- These fields inform recommendations and verification logic but must not
  silently change parcel-state status fields (`shelter_status`,
  `reentry_status`, etc.).
- All thresholds (envelope class boundaries, temperature danger thresholds,
  recommendation ladder cutoffs) should be externalized into versioned
  configuration files, not hardcoded in inference scripts.
- When input data is insufficient or noisy, the engine should omit the
  derived objects or populate them with conservative defaults and explicit
  uncertainty rather than fabricating precision.
