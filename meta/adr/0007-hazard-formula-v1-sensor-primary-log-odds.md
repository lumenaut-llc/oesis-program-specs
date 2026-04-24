# ADR 0007: Hazard Formula v1 — Sensor-Primary Log-Odds Form

- Status: Accepted
- Date: 2026-04-19
- Owners: Open Environmental Sensing and Inference System (technical)
- Related workstreams:
  - software/inference-engine
  - oesis-runtime (planned v1_1/ module)
  - release/v.0.1 (gap-register G11)

## Context

Hazard formula v0 (`config/hazard_thresholds_v0.json` with `parcel_first_hazard.py`) computes smoke and heat probabilities by summing band lookups (`prob += band_value`) then clamping. Three problems:

1. **No provenance.** Every numeric threshold is an expert-elicitation placeholder with no cited source.
2. **No coherent combination math.** Additive probabilities with post-hoc clamping doesn't correspond to any probabilistic model; it cannot be calibrated (Brier score, ECE) and adding evidence doesn't behave like Bayes.
3. **Sensor primacy not expressed.** Public and shared-neighborhood signals combine additively into the same probability, weakening the architectural claim that OESIS is sensor-first.

Meanwhile, pilot incident logs are the only ground-truth source available (not EPA/NWS datasets), and hardware for outdoor temperature sensing (mast-lite) is the v0.2 promotion target — so any formula rewrite must accommodate sensor-primary with sensor capability that is itself still maturing.

## Decision

Adopt a **sensor-primary log-odds formulation** for smoke and heat hazards. For hazard $h$ at parcel $p$ at time $t$:

$$\text{logit}(P_h) = \alpha_h + \beta_h \cdot S_h(t) + \sum_{i} \gamma_{h,i} \cdot \pi_{h,i}(p) + \delta_h \cdot H(t)$$

- $S_h(t)$ is the **sensor evidence term** — dominant by construction.
- $\beta_h$ is the sensor coefficient; required constraint: $|\beta_h| > \sum_i |\gamma_{h,i}|$ (sensor weight exceeds sum of absolute prior coefficients).
- $\gamma_i$ are parcel priors (construction, defensible space, distance to wildland for smoke; heat retention, HVAC for heat).
- $H(t)$ is a sensor-health term, negative-only (degraded health reduces sensor weight, never inverts it).
- **Public and shared sources never appear in the logit.** They calibrate coefficients upstream and feed `divergence_score` channels downstream — reported alongside $P_h$, never folded into it.

Additional commitments:

- Smoke sensor term uses per-device rolling-baseline deviation of gas resistance (48h window, MAD-based σ), not fixed ohm cutoffs.
- Heat sensor term uses per-parcel per-date z-scores against NCEI climate normals (both daily max and daily min), not a fixed HeatRisk onset temperature.
- Every numeric value in the v1 config carries a provenance schema: `value`, `source`, `source_type`, `date`, `note`, plus `n_events` / `ci_95` for internally-fit values.
- Formula specified in [`../../software/inference-engine/hazard-formula-v1.md`](../../software/inference-engine/hazard-formula-v1.md); Phase-0 prerequisites in [`../../software/inference-engine/hazard-formula-v1-phase1.md`](../../software/inference-engine/hazard-formula-v1-phase1.md).

## Consequences

Positive:

- Each coefficient is calibratable against pilot labels via logistic or isotonic fit.
- Brier score and ECE become reportable per hazard.
- Sensor-primacy is a numerical constraint, not a convention.
- Divergence between local sensor and public/shared context is preserved as a separate signal rather than muted by addition.
- Every threshold cites a source; unsourced entries are visible and blocked.

Negative:

- Requires coefficient fitting against pilot data — gated by hardware calibration prerequisites (G13, G14, G17) and by having enough labeled pilot events per hazard (≥10 positive events per coefficient for internal fits, else coefficient stays literature-prior with citation).
- Transition runs v1_1 in shadow against v0 until Brier/ECE beat v0 replayed on the same pilot labels — adds schedule overhead.
- v1 heat primary path requires mast-lite outdoor temperature — blocked by G12.

## Alternatives considered

**Keep v0 bands, add provenance tags to existing values.**
Rejected: bands can be tagged with sources, but the additive-combination math would still be incoherent. Provenance without formula coherence does not fix the calibration problem.

**Fit a small ML model (gradient-boosted tree or shallow NN) against pilot labels.**
Rejected at this stage: pilot event counts are too sparse to avoid overfitting, and interpretability is a program-level requirement ("prefer transparent rules over complex models" per [`../../architecture/system/technical-philosophy-and-architecture.md`](../../architecture/system/technical-philosophy-and-architecture.md) principle 5). May revisit at `v1.5+` when data accumulates.

**Add public/shared signals additively to logit.**
Rejected per user direction: sensor is main source of truth; research and public data are contrast, not evidence. B2 decision reinforces this by separating adapter-derived data into its own trust program (ADR 0010).

## Follow-up work

- Resolve Phase-0 hardware prerequisites per [`../../software/inference-engine/hazard-formula-v1-phase1.md`](../../software/inference-engine/hazard-formula-v1-phase1.md) §0.
- Implement rolling-baseline replay harness in `oesis-runtime/research/rolling_baseline/`.
- Preload NCEI climate normals for every pilot parcel at onboarding.
- Stand up v1_1 shadow module in oesis-runtime when mast-lite hardware + reference instruments are in place.
- Brier/ECE calibration gate must beat v0 replayed on same pilot labels before v1 is promoted.
