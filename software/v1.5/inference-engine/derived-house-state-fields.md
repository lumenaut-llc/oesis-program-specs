# Derived House-State Fields v1.5

## Purpose

Versioned pointer for the derived house-state field computation logic that
supports the v1.5 measurement-to-intervention bridge.

## What this covers

- IO ratio baseline characterization (structural smoke infiltration signature)
- Indoor rise rate and time-to-threshold heat projection
- Thermal profile self-calibration from ground-truth sources

## Design authority

The full computation logic, qualifying conditions, and threshold tables are in
`../../inference-engine/derived-house-state-fields.md`.

The contract fields these computations populate are in
[`v1.5/house-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/house-state-schema.md) under `indoor_response`:

- `infiltration` — IO ratio, baseline, envelope class
- `thermal_dynamics` — rise rate, time-to-threshold, recommendation

## Why it belongs in `v1.5`

These derived fields are the bridge between raw indoor sensing and actionable
closed-loop reasoning:

- IO ratio baseline conditions the expected efficacy of smoke interventions
  (tight homes see ~90% PM2.5 reduction from purifiers; leaky homes ~55%)
- Time-to-threshold projection converts raw temperature data into an actionable
  window for pre-cooling recommendations
- Thermal profile self-calibration improves over time when higher-fidelity
  sources (CT clamp, thermostat API) provide ground truth

Without these derived fields, the smoke and heat closed loops cannot produce
parcel-specific outcome predictions.

## Related

- `../../inference-engine/derived-house-state-fields.md` (full logic)
- `../../inference-engine/thermal-slope-inference.md` (HVAC mode inference)
- [`v1.5/house-state-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/house-state-schema.md)
- [`v1.5/equipment-state-observation-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/equipment-state-observation-schema.md)
