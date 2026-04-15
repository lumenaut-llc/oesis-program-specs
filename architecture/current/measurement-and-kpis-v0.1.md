# Measurement and KPIs (v0.1 posture)

## Purpose

Connect program **measurement intent** to the frozen **`v0.1`** slice: which KPI
families matter **now**, which belong to **pilots** or **later phases**, and how
that relates to acceptance checks—without duplicating the full KPI catalog.

## Status

Current reference **measurement posture**. Detailed KPI suggestions remain in the
root packet `../../program/operating-packet/08-kpi-framework.md`.

This document **complements** `implementation-posture.md` and
`../../release/v0.1/implementation-status-matrix.md` (release label `v0.1`,
filesystem path `v0.1/`); it does not override
status classifications or acceptance commands.

## KPI families (summary)

Full lists and definitions: `../../program/operating-packet/08-kpi-framework.md`.

1. **Technical validity** — Trustworthy evidence: uptime, packet completeness,
   ingest latency, QA pass rates, stale data rate, outputs with provenance and
   confidence labels.
2. **Decision usefulness** — More useful than raw feeds or public-only context:
   current status coverage, actionability, time-to-update after stress, FP/FN
   discipline, locally relevant explanations, engagement during active periods.
3. **Network value** — Benefit from shared participation: confidence uplift with
   nearby evidence, fewer parcels stuck in inferred_regional or stale modes,
   density vs quality, marginal value per node.
4. **Functional and adaptation value** — Beyond awareness: measured outcomes
   after actions, route/access interpretation during events, logged interventions
   with before/after, response history—**tightly coupled** to program-phase
   **`v1.5`** and pilot learning, not the narrow software acceptance bar.
5. **Governance value** — Owner control that is **measurable only where
   enforced**: opt-in sharing, revocation, export, comprehension of private vs
   shared vs derived, trust, visible evidence mode and reasons on critical
   outputs.

## Emphasis by program phase

Aligned with `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`:

- **Narrow `v0.1`:** prioritize **§1 Technical validity** and **§2 Decision
  usefulness** for the reference path. Prove the pipeline and parcel view are
  honest, fresh enough, and explainable.
- **§3 Network value:** apply only where **shared / neighborhood** surfaces are
  **real** (`partial` or better); do not assume mature federation or dense
  adoption in success criteria for the minimal slice. Note:
  `shared-neighborhood-signal-schema.json` exists in the `v0.1` contract set and
  shared-map API is `partial` in the implementation matrix, but the phasing doc
  does **not** list shared signals as a `v0.1` core goal. Treat network-value KPIs
  as applicable to pilot evaluation where shared surfaces happen to exist, not as
  `v0.1` acceptance gates.
- **§4 Functional / adaptation:** **pilots**, research, and **`v1.5`** planning—not
  required gates for `make oesis-accept` / `v0.1-acceptance-criteria.md`.
- **§5 Governance:** measure **only** what the runtime and product **actually
  guarantee**; align claims with `implementation-posture.md` and the matrix (many
  surfaces remain `partial` or `docs-only`).

## Traceability: acceptance criteria → KPI families

`v0.1-acceptance-criteria.md` is the **pass/fail** software checklist. Rough mapping
to `08` buckets:

| Acceptance focus | Primary KPI families |
| ---------------- | -------------------- |
| Valid serial JSON, packet validate/normalize, ingest path | **1** Technical validity |
| Parcel context loaded | **1** (integrity of inputs) |
| Parcel-state with confidence, evidence mode, reasons, freshness, provenance | **1** + **2** |
| Coherent parcel view | **2** Decision usefulness |
| Same path CLI + HTTP (`make oesis-*`) | **1** (repeatable truth path) |

Automated commands prove **structural** and **reference-path** correctness, not
longitudinal field KPIs (uptime over weeks, user-rated actionability)—those sit
in **pilots** and product instrumentation.

## Pilots and field evaluation

Operator checklist: `../../operations/pilots/pilot-operator-checklist.md`.

Overlap:

- Uptime, freshness, stale visibility → **§1**
- Sharing modes, revocation/export logging, access logs → **§5** where behavior
  exists; otherwise track as **gaps**, not scored successes

## Multi-scale extensions (later)

When route, block, and lifeline reasoning mature, extend measurement per
`../../program/operating-packet/08-kpi-framework.md` (“Multi-scale extensions”) and
`../../program/operating-packet/07-information-layer-and-functional-recovery.md` /
`../../program/operating-packet/06-network-of-networks-concepts.md`. Do not treat those as **`v0.1`**
release gates while architecture remains `docs-only` or `planned` for those
surfaces.

## Closed-loop verification KPIs (v1.5+)

> **Note:** these KPIs apply from `v1.5` onward. They are not `v0.1`
> acceptance criteria but are included here for forward planning so the
> measurement framework is coherent across phases.

| KPI | Definition |
| --- | --- |
| `loops_triggered` | Total hazard events where the system generated a recommendation. |
| `loops_with_action_logged` | Subset of `loops_triggered` where an `intervention-event` was recorded. |
| `loops_with_verified_outcome` | Subset of `loops_triggered` where a `verification-outcome` was recorded within the response window. |
| `loop_completion_ratio` | `loops_with_verified_outcome` / `loops_triggered`. |
| `target_delta_met_ratio` | Proportion of verified loops where the expected improvement was achieved. |

Null or confounded loops still count in `loops_triggered`. The metric
measures system coverage, not just success. A low `loop_completion_ratio`
may indicate instrumentation gaps, operator dropout, or hazard events that
resolve before action is possible -- all of which are useful signals for
product improvement.

## Related docs

- `../../program/operating-packet/08-kpi-framework.md` — full KPI catalog
- `v0.1-acceptance-criteria.md` — frozen software acceptance
- `implementation-posture.md` — implemented / partial / planned truth
- `milestone-roadmap.md` — when milestones unlock new measurement
- `../../release/v0.1/implementation-status-matrix.md` (release label `v0.1`, filesystem path `v0.1/`) — status authority
