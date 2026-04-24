# Hazard Formula v1 — Phase 1 Preparation

## Purpose

Operational prerequisites that must land before v1 coefficient fitting can start. This doc turns the plan in `hazard-formula-v1.md` into four concrete artifacts:

1. Calibration dataset schema for pilot incident logs.
2. Pilot-log readiness checklist — runnable as a validation pass over existing logs.
3. Gas-resistance rolling-baseline prototype algorithm and replay harness.
4. NWS HeatRisk reference data approach, including a correction to the v1 heat sensor term.

Scope is program-phase `v0.2` / Milestone 2 (capability stage `current v1`) per `../../architecture/current/milestone-roadmap.md`. Not required for v0.1 sign-off.

## Status

Draft, 2026-04-19.

## Phase 0 — Hardware prerequisites (blocking)

The statistical work in sections 1–4 assumes sensor data trustworthy enough to calibrate coefficients against. A hardware-readiness audit on 2026-04-19 found three blockers that must be resolved before coefficient fitting can begin. Attempting to fit coefficients before these are in place would encode bring-up drift, un-referenced readings, and missing hardware lanes into the "evidence-based" formula — the exact failure mode the v1 sensor-primacy contract is meant to prevent.

**Policy home.** P0.1 and P0.2 below operationalize requirements that now live at platform level in [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md). That doc is the single source of truth for reference-instrument standards, burn-in policy, and admissibility of readings to the calibration dataset. The Phase 0 items here are the hazard-formula-side view of the same contract.

### P0.1 — Characterized reference instrument

**Blocker.** [`oesis-builds/procedures/bench-air-node/calibration.md`](https://github.com/lumenaut-llc/oesis-builds/blob/main/procedures/bench-air-node/calibration.md) requires a characterized reference instrument for every calibration session, but `references/TBD.md` is a placeholder. No unit has been calibrated against a real referent. Coefficient fitting against this data would be statistically precise but physically meaningless.

Done when: at least one reference instrument file exists per measurand per deployment class under [`oesis-builds/procedures/<node>/references/`](https://github.com/lumenaut-llc/oesis-builds/tree/main/procedures), matching the file format and minimum fields specified in [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §A.

### P0.2 — Burn-in gate enforced in bring-up acceptance

**Blocker for gas-resistance term only.** BME680 gas resistance needs 24–48 h conditioning on first power-up before the baseline is physically stable. [`oesis-builds/specs/bench-air-node/v0-1.md:211`](https://github.com/lumenaut-llc/oesis-builds/blob/main/specs/bench-air-node/v0-1.md#L211) currently checks "trending gradually," which is a posture observation, not a gate. The first 48 h of every device's data must be excluded from the calibration dataset, or the rolling baseline fits will encode conditioning artifacts.

Done when: bring-up acceptance includes an explicit 48 h burn-in window per [`../../architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md) §B, and the ingest pipeline tags observations as `burn_in_complete: false` until that window has passed for each device. Admissibility rule in calibration-program §C then excludes pre-burn-in readings automatically.

### P0.3 — Mast-lite build spec (decision: option A, 2026-04-19)

**Blocker for heat primary path.** The canonical heat sensor term in [`hazard-formula-v1.md`](hazard-formula-v1.md) assumes an outdoor temperature source. Bench-air-node is documented as indoor-only ([`oesis-builds/specs/bench-air-node/v0-1.md:26`](https://github.com/lumenaut-llc/oesis-builds/blob/main/specs/bench-air-node/v0-1.md#L26)). Mast-lite is referenced in architecture and milestone docs but has no build spec, no calibration procedure, no BOM, no radiation-shield specification in `oesis-builds/`. The formula is ahead of the hardware.

**Decision (2026-04-19):** write the spec (option A). The alternative — scoping heat to bridge-path-only — was rejected because the indoor-bridge path cannot physically represent parcel-wide outdoor heat, which is the claim the parcel-state output needs to support.

Done when:
- `oesis-builds/specs/mast-lite/v0-1.md` exists with BOM, wiring, firmware pin-out, and a reproducible build procedure.
- `oesis-builds/procedures/mast-lite/calibration.md` exists, citing at least one characterized reference instrument (may reuse the bench-air reference from P0.1, or add a distinct outdoor-suitable referent).
- Radiation-shield design is documented inside the build spec, with a thermal-loading acceptance test. Readings from a unit without a verified shield are not admissible into the calibration dataset.
- Build has been independently reproduced at least once (per Milestone 2 acceptance).

Tracked in gap register as G12. Milestone 2 acceptance criteria updated to reflect the spec requirements as gate items.

### P0 → P1 ordering

Sections 1–4 are all valid work items, but they build on P0:

- Section 1 (calibration dataset schema) can be drafted without P0, but the first dataset version that admits records cannot be cut until P0.1 and P0.2 are resolved.
- Section 2 (readiness checklist) should add P0.1 and P0.2 as additional pass criteria before the checklist is run.
- Section 3 (rolling-baseline replay) can prototype against any trace but cannot promote its parameters out of `research/` until P0.1 gives a referent for "good."
- Section 4 (HeatRisk approach) is purely informational until P0.3 is resolved; the primary heat path can't be exercised otherwise.

## Section 1 — Calibration dataset schema

### Record format

Each record is one labeled hazard window at one parcel. Storage: JSONL, one record per line. Canonical field set:

```json
{
  "record_id": "<uuid>",
  "parcel_id": "<string>",
  "hazard": "smoke | heat",
  "window_start": "<ISO 8601 UTC>",
  "window_end": "<ISO 8601 UTC>",
  "label": "present | absent | uncertain",
  "label_source": "operator_field_report | public_advisory | dispatch_record | sensor_corroboration | self_report",
  "label_confidence": "high | medium | low",
  "labeler_id": "<string>",
  "labeled_at": "<ISO 8601 UTC>",
  "parcel_context_snapshot_ref": "<path or hash of parcel_context at window_start>",
  "sensor_trace_ref": "<path or hash of raw packet trace covering window_start - 72h to window_end + 1h>",
  "public_context_snapshot_ref": "<optional path or hash>",
  "notes": "<freeform, short>"
}
```

Field rules:

- `window_start` / `window_end` are the **event** window, not the alert window. If labeled from a public advisory, use the advisory's effective period, not the time the operator read it.
- `parcel_context_snapshot_ref` must reference a snapshot taken at or before `window_start`. Pulling "current" parcel context when labeling a past event introduces data leakage — fit coefficients would encode today's parcel, not the parcel at event time.
- `sensor_trace_ref` must cover at least 72 h of pre-window history so rolling-baseline terms can be computed without truncation.
- `label` of `uncertain` keeps the record for EDA and negative-class sampling analysis but is excluded from coefficient fitting.

### Label source hierarchy

Preferred order when multiple sources exist for the same window, highest trust first:

1. `dispatch_record` — fire department / EMS record naming the parcel or immediate vicinity.
2. `public_advisory` — NWS, AirNow, or equivalent active during the window and covering the parcel.
3. `operator_field_report` — signed operator observation with contemporaneous notes.
4. `sensor_corroboration` — multi-source sensor agreement (mast-lite + bench-air + public AQI) only when no human/agency source exists. Marked `label_confidence: low`.
5. `self_report` — parcel occupant, marked `low` unless corroborated.

Label source is **not** the same as sensor trace. Using the bench-air sensor itself as the label for its own prediction creates a circular fit; `sensor_corroboration` must use sources the model does not train on.

### Negative-class sampling

Coefficient fits require negative examples (hazard absent). Three sampling strategies, pick per hazard and document per dataset:

- **Random windows** — uniformly sampled from non-event parcel-time. Cheap but class imbalance hurts calibration.
- **Matched parcels** — for each positive, sample one negative from a similar parcel during a period with no public advisories and no dispatch records. Better calibration; requires parcel-similarity metric (initial: same climate zone + same smoke-exposure class).
- **Stratified by season / time-of-day** — avoids seasonal confounding (e.g., summer positives vs. winter negatives).

Every calibration dataset version must record the negative-sampling method in its manifest.

## Section 2 — Pilot-log readiness checklist

Run this pass against the existing pilot logs before fitting any v1 coefficient. Each check below should be expressible as a query or script against the log store; report pass/fail + counts per hazard.

| # | Check | Pass criterion | Failure mode | Remediation |
|---|---|---|---|---|
| R1 | Labels are outcomes, not prior predictions | Every labeled record has a `label_source` from the hierarchy in §1, and none list the system's own alert as the source | Circular training — model learns to reproduce v0 alerts rather than real events | Relabel from independent source, or exclude from fitting |
| R2 | Label timestamps are event windows, not alert windows | `window_start` / `window_end` match the hazard's occurrence, verifiable against at least one outside source for a sample | Temporal leak; sensor terms evaluated at wrong time | Recompute windows; prefer dispatch or advisory timestamps |
| R3 | Parcel context snapshotted at event time | Every record's `parcel_context_snapshot_ref` exists and predates `window_start`; no "current state" backfill | Priors encode post-event state (e.g., roof replaced after fire) | Rebuild snapshots from historical parcel-context versioned store, or drop records with missing snapshots |
| R4 | Sensor traces include ≥ 72 h preceding baseline window | Every record's trace covers `window_start - 72h` continuously; gaps logged | Rolling baseline term truncates, inflating z-score noise | Pad window from trace store, or exclude; document exclusion rate |
| R5 | Negative-class sampling documented | Manifest names the sampling method; ratio of positives:negatives recorded per hazard | Class imbalance silently shifts calibration | Resample with documented strategy before fitting |

Minimum pass threshold: R1, R3, R5 must pass 100 %. R2 and R4 may pass with documented exclusion rate ≤ 15 %; records that fail drop from the fitting set.

Report format — one row per check, per hazard:

```
R1 smoke  PASS  n_records=42  n_dropped=0   note="all labels from dispatch or advisory"
R1 heat   FAIL  n_records=28  n_dropped=11  note="11 records list v0 alert as label source; exclude"
R2 smoke  PASS  ...
```

## Section 3 — Gas-resistance rolling-baseline prototype

### Algorithm

Per device, per observation:

1. Maintain a sliding window `W_base` of recent gas-resistance readings, default **48 h**.
2. Exclude the most recent `W_exclude` window, default **30 min**, to prevent active events from contaminating the baseline.
3. Compute:
   - `median_base = median(readings in [t - W_base, t - W_exclude])`
   - `mad_base = median(|reading - median_base|)`
   - `sigma_base_robust = 1.4826 * mad_base` (equivalent to stdev under Gaussian assumption)
4. Signal:
   - `z_gas(t) = -(R(t) - median_base) / max(sigma_base_robust, sigma_floor)`
   - Negated so **drops** in gas resistance (consistent with VOC/smoke loading) produce **positive** z.
5. Saturate: `z_gas(t) = clamp(z_gas(t), -3.0, +8.0)`.
6. Emit a **baseline-stability flag**: `unstable` if `sigma_base_robust > sigma_unstable_ceiling` or `n_readings_in_window < n_min`.

### Default parameters (all must carry provenance when promoted)

| Parameter | Default | Rationale for default | Tuning source |
|---|---|---|---|
| `W_base` | 48 h | Long enough to smooth diurnal variation; short enough to adapt to device conditioning | Tune via replay — see validation below |
| `W_exclude` | 30 min | Matches typical smoke event rise time from bench tests | Refine against pilot events |
| `sigma_floor` | device-specific, init 1000 Ω | Prevents divide-by-near-zero on very stable devices | Per-device fit |
| `n_min` | 180 readings (≈ 1 h of 20 s samples) | Below this, dispersion estimate is too noisy | Sensitivity analysis |
| `sigma_unstable_ceiling` | 10× median(sigma_base) across fleet | Flags devices still conditioning or contaminated | Fleet statistics |

### Replay harness

Purpose: compare v0 fixed-ohm bands vs v1 rolling-baseline z on the **same** sensor traces and labels, report signal-to-noise and precision-recall curves.

Inputs:

- sensor trace JSONL per device (bench-air packet stream)
- calibration dataset from §1
- v0 config (`hazard_thresholds_v0.json`, smoke gas-resistance bands)
- v1 parameter set from table above

Outputs (one set per hazard):

- PR curve for v0 score vs labels
- PR curve for v1 z_gas vs labels
- Brier score for each score converted to probability
- Reliability diagram (10-bin)
- Per-device baseline stability distribution
- Event-wise signal-to-noise: mean z_gas during labeled positive windows vs mean during negatives

Promotion bar: v1 must beat v0 on **both** Brier and area-under-PR, on the same dataset, for smoke. No promotion on heat from this prototype alone — heat needs the HeatRisk reference data in §4.

Suggested module layout (paper design, not implementation):

```
oesis-runtime/research/
  rolling_baseline/
    baseline.py              # the algorithm above as a pure function
    replay.py                # load traces + labels, run baseline, produce PR / Brier
    config.py                # parameter set, versioned
    reports/                 # replay outputs land here, named by config version
```

Kept under `research/` not `oesis/inference/v1_1/` because it's a prototype. Promotion to `v1_1/` happens only after the replay beats v0 and the parameters are provenance-tagged.

## Section 4 — NWS HeatRisk reference data approach

### Canonical heat sensor term

The canonical heat sensor term is defined in [`hazard-formula-v1.md`](hazard-formula-v1.md) under "Heat: S_heat(t)". That doc is the single source of truth for the formula.

Summary for context here: $S_{\text{heat}}$ is a combined day/night z-score against per-parcel, per-date local climatology (not a fixed onset temperature), computed from NOAA NCEI 30-year daily Climate Normals preloaded per parcel at onboarding.

The correction happened on 2026-04-19 because the initial v1 draft treated HeatRisk's "category-1 onset" as a fixed per-zone temperature. NWS HeatRisk methodology is percentile-based per grid cell and per date, and uses both daily max and daily min. This doc captures the access paths and fallback logic that support the corrected formula.

### Access paths (ranked by directness)

| Option | What it gives | Latency | Engineering cost |
|---|---|---|---|
| NWS HeatRisk gridded product via the HeatRisk public page and experimental data service | Current HeatRisk category and sub-category value per grid cell | Real-time forecast | Low read, medium parse (images + data layers; confirm terms before programmatic pull) |
| NOAA NDFD (National Digital Forecast Database) GRIB2 grids | Raw forecast temperatures; HeatRisk can be recomputed | Real-time | Medium (GRIB tooling) |
| NOAA NCEI Climate Normals — 30 y daily normals at 1 km grid | Static `T_local_95pct` and `T_local_std` per location per date | Preload once | Low — static dataset |
| CDC Environmental Public Health Tracking HeatRisk layer | Cross-validates against NOAA | Real-time | Low — external confirmation signal |

Recommended path for v1 Phase 1:

1. Preload NCEI climate normals for every pilot parcel at onboarding. This gives `T_local_95pct(date, location)` without an online dependency.
2. When NWS HeatRisk data is available for the forecast window, compute `heat_divergence_forecast` against it; do not add to $P_{\text{heat}}$.
3. Defer programmatic HeatRisk category pull until v1.0 acceptance proves NCEI normals alone are adequate as the local reference.

### Fallback when HeatRisk or NCEI normals unavailable

Use the device's own 10-day rolling 95th percentile of daily max temperature as a degraded local reference. Mark confidence reduced and emit reason "local climatology fallback — NCEI normals unavailable for this parcel."

### Sources

- [NWS HeatRisk overview](https://www.wpc.ncep.noaa.gov/heatrisk/overview.html) — methodology, percentile basis, daily min/max use, CDC integration
- [NWS HeatRisk home](https://www.wpc.ncep.noaa.gov/heatrisk/) — interactive product and scale
- [NOAA HeatRisk expansion announcement](https://www.noaa.gov/news-release/noaa-expands-availability-of-new-heat-forecast-tool-ahead-of-summer) — national rollout context
- [CDC HeatRisk integration](https://ephtracking.cdc.gov/Applications/HeatRisk/) — cross-validation surface

## Section 5 — Deliverables, ready-to-start

Ordered by leverage per unit of effort:

1. **Calibration dataset schema adopted** — §1 as the storage contract; existing logs migrated or a shim view built to produce records in this format.
2. **Run the readiness checklist** (§2) against existing logs; publish the report in the calibration dataset manifest. This alone may reveal that fits need to wait for better label sources.
3. **Rolling-baseline replay harness** built in `oesis-runtime/research/rolling_baseline/`. Run against current bench-air traces and existing labels. Report PR + Brier vs v0.
4. **Preload NCEI climate normals** for pilot parcels. This is a data-ingest job, not a modeling job; can run in parallel with any of the above.
5. **Only after 1-4**: begin coefficient fitting for the v1 log-odds form, per §4 of `hazard-formula-v1.md`.

## Non-goals for Phase 1

- Implementing the v1 inference path in `v1_1/`. That is Phase 2, gated by the replay results.
- Modifying `hazard_thresholds_v0.json` or `parcel_prior_rules_v0.json`. v0 stays stable during v1 shadow.
- Fitting occupant-vulnerability or HVAC-presence coefficients — both deferred in `hazard-formula-v1.md`.
- Flood work of any kind. Blocked on flood-node hardware.

## Related files

- `hazard-formula-v1.md` — full v1 formula spec
- `hazard-logic-v0.md` — v0 posture, still authoritative for flood
- `config/hazard_thresholds_v0.json` — v0 values v1 will eventually replace for smoke and heat
- `../../release/v.0.1/v0.1-gap-register.md` — G11 tracks this rollout
- `../../architecture/current/milestone-roadmap.md` — Milestone 2 scope includes the formula adoption
