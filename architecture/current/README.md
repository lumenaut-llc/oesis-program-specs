# Technical Architecture v0.1

## Lane

This directory is the `current/` lane.

Use it for the frozen `v0.1` reference architecture and other current-truth
docs that should match accepted runnable scope.

If you need debated target-lane architecture, use `../v1.0/`.
If you need bridge-stage architecture notes, use `../v1.5/`.
If you need cross-version narrative and operating-model framing, use `../system/`.

## Purpose

Define the current truthful reference architecture for Open Environmental
Sensing and Inference System.

`v0.1` is the architecture of the current reference stack. It should describe
what is real now, what is only partial, and what remains docs-only or planned.

The **narrow program-phase `v0.1` slice** is the frozen anchor in this directory.
`milestone-roadmap.md` also orders **later milestones** that stage growth toward
program-phase **`v1.0`** breadth—without treating those later stages as current
truth here.

## Status

Current reference architecture.

Use this version when you need the architecture that matches the present
implementation boundary rather than future proposals.

This directory is the frozen `v0.1` lane. New future-looking architecture work
should go to `../v1.0/` instead of mutating these current-truth files.

Pre-`1.0` growth should normally be tracked through milestones and status
classification rather than a new version number for every added node or
element.

## Scope

`v0.1` covers:

- the current technical philosophy
- the current collection-to-parcel reference stack
- the minimum functioning first-version slice
- the current architecture object map
- current ownership of implementation, docs, contracts, and policy surfaces
- the implementation boundary reflected in the current reference checks
- the current milestone sequence that fits the implemented reference posture
  (including how milestones relate to program phases—see `milestone-roadmap.md`)
- measurement posture and KPI family emphasis for the frozen slice (see
  `measurement-and-kpis-v0.1.md`)

## Program plan and framing

Files in this directory are **frozen current reference** architecture. Program
mission, phase vocabulary, thesis, layered blueprint, and long-horizon framing are
authored **alongside** them (repo root and `program/`):

- `../../program/v0.1/README.md` — mission, long-term direction, phase label summary
- `../../program/operating-packet/00-version-labels-and-lanes.md` — program phases, runtime lanes, marketing naming
- `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` — full `v0.1` / `v1.0` / `v1.5` narrative
- `../../program/operating-packet/01-core-thesis-and-framing.md` — thesis and wording guardrails
- `../../program/operating-packet/05-revised-architecture-blueprint.md` — layered model and near-term sensing order
- `../../program/operating-packet/07-information-layer-and-functional-recovery.md` — information-layer target
- `../../program/operating-packet/functional-state-and-response-model.md` — bridge toward response / verification
  objects (`v1.5`-era planning)
- `../../program/operating-packet/04-architecture-review-keep-dangerous-change-now.md` — expanded keep /
  dangerous / change review (judgments also summarized in `technical-philosophy.md`)
- `../../program/operating-packet/08-kpi-framework.md` — detailed KPI catalog (posture in
  `measurement-and-kpis-v0.1.md`)

**Phase ↔ milestone mapping** lives in `milestone-roadmap.md` in this directory.

## Reading order

1. `technical-philosophy.md`
2. `reference-stack.md`
3. `minimum-functioning-v0.1.md`
4. `milestone-roadmap.md` — delivery sequence and relationship to program phases
5. `v0.1-runtime-modules.md` — runtime package map (sibling checkout
   `../../../oesis-runtime`; see `implementation-posture.md` canonical homes)
6. `v0.1-acceptance-criteria.md` — CLI/HTTP acceptance for the frozen slice
7. `measurement-and-kpis-v0.1.md` — KPI family emphasis and traceability to acceptance
8. `architecture-object-map.md`
9. `implementation-posture.md`
10. `component-boundaries.md`
11. `pre-1.0-version-progression.md`

## Primary source alignment

`v0.1` should stay aligned with:

- `../../program/v0.1/README.md`
- `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`
- `../../architecture/system/technical-philosophy-and-architecture.md`
- `../../architecture/system/integrated-parcel-system-spec.md`
- `../../software/v0.1/README.md`
- `../../release/v.0.1/implementation-status-matrix.md` (release label
  `v0.1`, filesystem path `v.0.1/`)
- `../../program/operating-packet/08-kpi-framework.md`

## Contributor rule

If a change describes what is implemented, accepted, or currently runnable, it
belongs here.

If a change describes a target architecture, future boundary, or debated
expansion, it belongs in `../v1.0/`.

If a change is incremental but still compatible with the current accepted slice,
prefer updating milestone and implementation-posture docs before proposing a new
`v0.x`.
