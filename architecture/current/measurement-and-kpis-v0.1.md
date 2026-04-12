# Measurement and KPIs (v0.1 posture)

## Purpose

Connect program **measurement intent** to the frozen **`v0.1`** slice: which KPI
families matter **now**, which belong to **pilots** or **later phases**, and how
that relates to acceptance checks—without duplicating the full KPI catalog.

## Status

Current reference **measurement posture**. Detailed KPI suggestions remain in the
root packet `../../08-kpi-framework.md`.

This document **complements** `implementation-posture.md` and
`../../release/v.0.1/implementation-status-matrix.md`; it does not override
status classifications or acceptance commands.

## KPI families (summary)

Full lists and definitions: `../../08-kpi-framework.md`.

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

Aligned with `../../09-phasing-v0.1-v1.0-v1.5.md`:

- **Narrow `v0.1`:** prioritize **§1 Technical validity** and **§2 Decision
  usefulness** for the reference path. Prove the pipeline and parcel view are
  honest, fresh enough, and explainable.
- **§3 Network value:** apply only where **shared / neighborhood** surfaces are
  **real** (`partial` or better); do not assume mature federation or dense
  adoption in success criteria for the minimal slice.
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
`../../08-kpi-framework.md` (“Multi-scale extensions”) and
`../../07-information-layer-and-functional-recovery.md` /
`../../06-network-of-networks-concepts.md`. Do not treat those as **`v0.1`**
release gates while architecture remains `docs-only` or `planned` for those
surfaces.

## Related docs

- `../../08-kpi-framework.md` — full KPI catalog
- `v0.1-acceptance-criteria.md` — frozen software acceptance
- `implementation-posture.md` — implemented / partial / planned truth
- `milestone-roadmap.md` — when milestones unlock new measurement
- `../../release/v.0.1/implementation-status-matrix.md` — status authority
