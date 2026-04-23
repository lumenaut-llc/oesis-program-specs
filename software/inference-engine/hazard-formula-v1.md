# Hazard Formula v1

## Purpose

Replace the v0 additive-band heuristic with an evidence-based, sensor-primary, log-odds formulation for smoke and heat hazards. Establish provenance, calibration, and divergence-reporting requirements so every number in the production config is traceable to a source and every prediction can be validated against pilot data.

## Status

Draft — supersedes the band logic in `hazard-logic-v0.md` for smoke and heat once adopted. Flood remains on v0 posture until a flood-node exists.

**Revisions:**
- 2026-04-19 — Heat sensor term corrected. Initial draft treated `T_ref` as a fixed HeatRisk category-1 onset temperature per climate zone; NWS HeatRisk methodology is percentile-based per grid cell and per date, and uses both daily max and daily min. Section "Heat: S_heat(t)" rewritten accordingly. See `hazard-formula-v1-phase1.md` §4 for access-path detail and sources.

## Owner

Open Environmental Sensing and Inference System

## Scope

In scope:

- smoke hazard, evidence from `bench-air-node` (gas resistance) and `mast-lite` / `weather-pm-mast` (PM2.5) when available
- heat hazard, evidence from `mast-lite` outdoor temperature (primary) and `bench-air-node` indoor temperature (bridge path only)
- parcel context priors with cited sources
- contrast/divergence reporting against public and shared sources
- calibration posture and validation requirements

Out of scope for v1:

- flood hazard (deferred until flood-node hardware ships)
- occupant vulnerability weighting (requires sourced framework; see `deferred_work`)
- model training beyond logistic/isotonic fits against pilot labels
- neighborhood aggregation beyond divergence signal

## Governing commitments

These are the architectural constraints v1 must preserve. They are stronger than v0.

1. **Sensor is the primary source of truth.** The dominant term in every hazard probability is the local sensor evidence. Research-derived thresholds and public feeds do not add to the probability; they calibrate its coefficients and flag divergence.
2. **Every number cites a source.** Any threshold, coefficient, or multiplier without provenance is marked `expert_elicitation_placeholder` and visible in output.
3. **Formula is probabilistically coherent.** Log-odds form, coefficients with confidence intervals, outputs calibratable against Brier score and ECE. No post-hoc clamping as a substitute for calibration.
4. **Divergence is a first-class output.** Disagreement between local sensor and regional/public/shared context is reported alongside the probability, not silently folded into it.
5. **Prefer `unknown` when evidence is weak.** Unchanged from v0.

## Formula

For hazard $h \in \{\text{smoke}, \text{heat}\}$ at parcel $p$ at time $t$:

$$\text{logit}(P_h) = \alpha_h + \beta_h \cdot S_h(t) + \sum_{i} \gamma_{h,i} \cdot \pi_{h,i}(p) + \delta_h \cdot H(t)$$

where

- $\alpha_h$ is the base log-odds for hazard $h$, calibrated to pilot base rate.
- $S_h(t)$ is the **sensor evidence term**, defined per hazard below. Standardized so $\beta_h$ is comparable across devices.
- $\beta_h$ is the sensor coefficient. Required to exceed the sum of absolute prior coefficients by a configured margin — the numerical expression of the sensor-primacy commitment.
- $\pi_{h,i}(p)$ are parcel priors (construction, defensible space, distance to wildland, etc.), encoded as numeric features with documented scales.
- $\gamma_{h,i}$ are prior coefficients, each with its own source citation.
- $H(t)$ is a sensor-health feature (read failures, baseline-stability flag). $\delta_h$ is small and negative — degraded health reduces the magnitude of the sensor's evidentiary push, it does not invert it.

$P_h$ is then obtained via the logistic function and clipped only to $[10^{-4}, 1 - 10^{-4}]$ for numerical stability.

### Status mapping

Unchanged conceptually from v0 — thresholds convert $P_h$ into `unknown` / `safe` / `caution` / `unsafe`. Thresholds are re-derived from pilot reliability curves, not reused from v0. Confidence floors for `shelter_status`, `egress_status`, and `asset_risk_status` are retained; the confidence score itself becomes a function of sensor-health, observation age, divergence magnitude, and presence of prior context.

## Sensor evidence terms

### Smoke: $S_{\text{smoke}}(t)$

Two sensor inputs, additively combined inside $S_{\text{smoke}}$:

1. **Gas resistance deviation** (bench-air-node, always available):
   - Maintain a rolling per-device baseline of gas resistance over a window $W_{\text{base}}$ (initial target: 48 hours, configurable).
   - Baseline excludes the most recent $W_{\text{exclude}}$ (initial target: 30 minutes) to avoid absorbing active events into the reference.
   - Baseline is the rolling median; dispersion is the rolling MAD (median absolute deviation), converted to a robust $\sigma$ estimate.
   - Signal term: $z_{\text{gas}}(t) = -(R(t) - \text{median}_W) / (1.4826 \cdot \text{MAD}_W)$. Negated so positive values indicate gas-resistance drops (consistent with VOC/smoke loading).
   - Saturates at $z_{\text{gas}} \in [-3, +8]$ to bound the term.

2. **PM2.5 evidence** (mast-lite / weather-pm-mast, when deployed):
   - Use $\log_{10}(\max(1, \text{PM}_{2.5}))$ rather than raw ug/m³ — matches EPA AQI's nonlinear health response and avoids the v0 bands discretizing a continuous signal.
   - When PM2.5 is absent, its contribution to $S_{\text{smoke}}$ is zero, and the confidence score is reduced accordingly. **PM2.5 presence does not shift the probability up; PM2.5 absence makes the estimate less confident, not lower.**

Device-relative baseline replaces the fixed ohm cutoffs in `hazard_thresholds_v0.json:3-17`. This is the single highest-priority accuracy change in v1.

### Heat: $S_{\text{heat}}(t)$

**Correction to initial draft (2026-04-19):** The original draft of this section described $T_{\text{ref}}$ as "the NWS HeatRisk category-1 onset temperature for the parcel's climate zone." Research against the NWS HeatRisk methodology revealed this framing is wrong in two ways that would have encoded into coefficients if not caught:

1. HeatRisk thresholds are **not fixed per climate zone**. They are the warmest 5 % of historical temperatures for each specific grid cell AND each specific date. A February threshold in coastal California is materially lower than its August threshold — same location, different date.
2. HeatRisk evaluates **both daily max AND daily min**. Hot nights carry independent health risk; a single `T_outdoor(t)` term loses that dimension.

The corrected term below treats local climatology as per-parcel, per-date, with separate day and night components. See `hazard-formula-v1-phase1.md` §4 for access paths and the HeatRisk source citations.

Preferred path — **mast-lite outdoor temperature**, combined day/night z-score against local climatology:

- Day term: $S_{\text{heat,day}}(t) = (T_{\text{max,today}} - T_{\text{local,95}}(\text{date, location})) / T_{\text{local,std}}(\text{date, location})$
- Night term: $S_{\text{heat,night}}(t) = (T_{\text{min,overnight}} - T_{\text{local,95,min}}(\text{date, location})) / T_{\text{local,std,min}}(\text{date, location})$
- Combined: $S_{\text{heat}}(t) = \max(S_{\text{heat,day}}(t), \kappa \cdot S_{\text{heat,night}}(t))$ with $\kappa \in (0, 1)$ calibrated against pilot labels.
- Saturates at $S_{\text{heat}} \in [-3, +8]$ consistent with the smoke term bounds.

Local climatology source: NOAA NCEI 30-year daily Climate Normals, preloaded per pilot parcel at onboarding. When NCEI normals are unavailable for a parcel's exact grid cell, fall back to the device's own 10-day rolling 95th percentile of daily max (and separately of daily min) temperature, with an emitted reason string flagging the fallback and a confidence reduction.

Humidity correction: optionally use heat index or WBGT approximation when humidity data is reliable. Default to dry-bulb with a documented accuracy note until humidity sensor calibration is verified.

Bridge path — **bench-air indoor temperature only**:
- Retained for pre-mast-lite deployments but with explicit discount: $\beta_{\text{heat,indoor}} \le 0.4 \cdot \beta_{\text{heat,outdoor}}$.
- Day and night decomposition still applies where data allows, using indoor rolling percentiles per device as the reference if NCEI normals cannot be meaningfully applied to an indoor reading.
- The indoor-penalty concept from `hazard_thresholds_v0.json:68` is preserved in spirit but implemented as a coefficient reduction, not a subtraction from probability.
- Estimates derived solely from indoor readings carry a mandatory reason string: "Parcel-wide outdoor heat not sensor-confirmed; estimate bridges from indoor reading."

## Parcel priors ($\pi$)

### Smoke priors (retain from v0 with re-sourcing)

| Feature | v0 source location | v1 source target |
|---|---|---|
| `zone_zero_clearance_class` | `parcel_prior_rules_v0.json:6` | NFPA 1144; Cal Fire Zone 0 guidance |
| `defensible_space_class` | `parcel_prior_rules_v0.json:7` | NFPA 1144; IBHS Suburban Wildfire Adaptation |
| `roof_class` | `parcel_prior_rules_v0.json:8` | IBHS post-fire structure surveys; ASTM E108 class A |
| `exterior_class` | `parcel_prior_rules_v0.json:9` | IBHS; NIST TN 1910 |
| `vent_class` | `parcel_prior_rules_v0.json:10` | CBC Chapter 7A §706A; WUI vent ember research |
| `window_class` | `parcel_prior_rules_v0.json:11` | IBHS; ASTM E2010 |
| `distance_to_wildland_ft` | `parcel_prior_rules_v0.json:12` | NIST TN 1910 ember-cast findings; Cal Fire post-event reports |

The distance-to-wildland bands in particular likely need to extend farther than 1500 ft. Post-event analysis of recent WUI fires (Camp, Tubbs, Marshall) documents structure ignition >1 mile from active flame. v1 should widen the band set and re-fit multipliers against pilot data where available.

### Heat priors

| Feature | v0 source location | v1 status |
|---|---|---|
| `heat_retention_class` | `parcel_prior_rules_v0.json:2` | Retain; source against ASHRAE 55 and building-envelope thermal mass literature |
| HVAC capability | not in v0 | **New** — presence, cooling capacity, current operational state. Sourced from parcel context if available; flag as missing otherwise |
| Occupant vulnerability | not in v0 | **Deferred** — requires sourced framework (CDC Heat Vulnerability Index is a candidate). Until agreed, not a coefficient |

## Health and divergence terms

### Sensor health $H(t)$

Three features, all negative-only so they can reduce sensor weight but never flip its direction:

- `read_failures_recent` — count of failed reads in last hour.
- `baseline_unstable` — boolean flag when rolling baseline variance exceeds a configured ceiling (sensor not yet conditioned or recovering from contamination).
- `observation_age_min` — minutes since last reading.

### Divergence channels (reported, not summed into $P_h$)

| Channel | Computation | Emitted as |
|---|---|---|
| `smoke_divergence_aqi` | $z_{\text{local smoke}} - z_{\text{regional AQI smoke}}$, normalized to $[-1, +1]$ | sidecar on parcel-state output |
| `smoke_divergence_neighborhood` | local vs. shared neighborhood smoke index | sidecar |
| `heat_divergence_forecast` | mast-lite temp vs. NWS forecast temp for same window | sidecar |
| `heat_divergence_neighborhood` | local vs. shared heat index | sidecar |

Divergence consumers:
- Large positive divergence with confident local sensor → user-visible reason ("local sensor detected conditions regional sources have not").
- Large negative divergence with confident regional source → trust gate may suppress `unsafe` escalation and surface "regional context disagrees with local reading" reason.

Divergence **does not change $P_h$.** It changes confidence, trust gates, and emitted reasons only.

## Provenance schema

Every numeric entry in the production hazard config must carry the following structure. Entries without provenance are rejected by the validation harness.

```json
{
  "value": <number>,
  "source": "<citation string or dataset handle>",
  "source_type": "peer_reviewed | agency_data | insurance_actuarial | internal_empirical | expert_elicitation_placeholder",
  "date": "<YYYY-MM>",
  "note": "<one-sentence context>",
  "n_events": <optional integer, required for internal_empirical>,
  "ci_95": <optional [low, high], required for internal_empirical>
}
```

### Example: smoke base rate and gas-resistance coefficient

```json
{
  "smoke": {
    "formula_version": "v1_logit",
    "alpha": {
      "value": -2.8,
      "source": "pilot_incident_log_2025H2",
      "source_type": "internal_empirical",
      "date": "2026-03",
      "n_events": 42,
      "note": "Base log-odds of labeled smoke-at-parcel events across pilot fleet."
    },
    "beta_gas": {
      "value": 1.2,
      "source": "pilot_logistic_fit_2026Q1",
      "source_type": "internal_empirical",
      "date": "2026-03",
      "n_events": 42,
      "ci_95": [0.7, 1.8],
      "note": "Log-odds change per +1 standardized unit of gas-resistance deviation from rolling baseline."
    },
    "gamma_roof_class_a": {
      "value": -0.4,
      "source": "IBHS 2022 Suburban Wildfire Adaptation Roadmap",
      "source_type": "peer_reviewed",
      "date": "2022-09",
      "note": "Class-A roof reduces ember ignition probability; log-odds reduction calibrated to IBHS ember-bed results."
    }
  }
}
```

## Calibration and validation

### Minimum bar for production adoption

1. **Per-hazard calibration dataset.** Pilot sensor traces paired with labeled hazard outcomes. Each record: `parcel_id`, `window_start`, `window_end`, `hazard`, `label` (∈ {present, absent, uncertain}), `label_source`, `label_date`.
2. **Reliability curve** per hazard, plotted at deployment time and persisted as an artifact beside the config version.
3. **Brier score** and **ECE** reported per hazard; v1 adoption requires both to be better than v0 replayed on the same dataset.
4. **Minimum sample sizes** for any coefficient fitted from pilot data:
   - $\ge 10$ positive events per coefficient, or
   - coefficient stays literature-prior with citation.
5. **CI regression gate** — future config changes must re-run the calibration replay and fail if Brier or ECE regresses beyond a configured tolerance.

### Pilot-log readiness checklist

Before fitting any v1 coefficient from pilot data, confirm:

- [ ] Labels are outcomes, not prior predictions (no circular training).
- [ ] Label timestamps are the event window, not the alert window.
- [ ] Parcel context is snapshotted at the event time, not backfilled from current state.
- [ ] Sensor traces include baseline windows preceding each event (needed for the gas-resistance deviation term).
- [ ] Negative-class sampling is documented (random windows, matched parcels, or stratified).

## Transition plan from v0

1. **Ship v1 in shadow mode.** The v0 engine remains the source of user-visible state; v1 runs in parallel and logs its probabilities and divergence channels to a versioned sink.
2. **Accumulate two-week shadow log** across the pilot fleet, replay pilot incident labels, report Brier/ECE for both v0 and v1.
3. **Promote v1 per hazard independently.** Smoke and heat can flip to v1 at different times if one hazard's calibration matures first.
4. **Deprecate v0 bands** only after v1 has been primary for a defined stabilization window.
5. **Retain `hazard-logic-v0.md`** for flood logic until the flood-node lands and a v1 flood spec is written.

## Deferred work

- Occupant vulnerability coefficient (needs sourced framework).
- PM2.5-only smoke estimates (requires mast-lite or weather-pm-mast at parcel).
- Cross-parcel Bayesian pooling for sparse deployments.
- Automatic detection of sensor conditioning drift (beyond the `baseline_unstable` flag).
- Flood formula v1 (blocked on hardware).

## Related files

- `hazard-logic-v0.md` — v0 posture, still authoritative for flood.
- `config/hazard_thresholds_v0.json` — values v1 replaces for smoke and heat.
- `config/trust_gates_v0.json` — retained; divergence channels feed into it.
- `oesis-runtime/oesis/inference/v1_0/parcel_first_hazard.py` — current implementation site; v1 implementation should live in a `v1_1/` sibling to avoid disrupting the v0 path during shadow evaluation.
- `oesis-runtime/oesis/assets/v0.5/config/inference/parcel_prior_rules_v0.json` — prior multipliers v1 re-sources and converts from multiplicative to log-odds contributions.
