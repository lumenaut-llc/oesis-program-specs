# Thermal Slope Inference v1.5

## Purpose

Versioned pointer for the passive HVAC mode inference method that detects
heating/cooling activity from indoor temperature slope analysis.

## Design authority

The full specification — method, classification thresholds, confidence levels,
self-calibration loop, suppression conditions, and integration with the
equipment-state-observation contract — is in
`../../inference-engine/thermal-slope-inference.md`.

## Why it belongs in `v1.5`

Thermal slope inference is the zero-friction fallback (Tier 1) in the tiered
acquisition model for house-state fields. It provides LOW-to-MEDIUM confidence
HVAC state detection using only the existing indoor temperature sensor — no
additional hardware or cloud API required.

This matters for the v1.5 bridge because:

- the smoke closed loop needs to know if HVAC is running before recommending
  recirculation
- the heat closed loop needs rise rate context that implicitly encodes HVAC
  activity
- many early parcels will not have CT clamps or smart thermostats, making
  passive inference the only available source

## Related

- `../../inference-engine/thermal-slope-inference.md` (full specification)
- `derived-house-state-fields.md` (companion derived fields)
- [`v1.5/equipment-state-observation-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/equipment-state-observation-schema.md)
- `../../../architecture/system/node-taxonomy.md` (tiered acquisition model)
