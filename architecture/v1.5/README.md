# Architecture v1.5

## Lane

This directory is the `v1.5/` lane.

Use it for the narrow bridge from parcel sensing into house state, action, and
measured outcome reasoning.

If you need cross-version roadmap or taxonomy framing, use `../system/`.
If you need broader debated target-lane architecture, use `../v1.0/`.

## Purpose

Hold the bridge-stage architecture notes for the measurement-to-intervention
foundation.

This is not the frozen `current/` lane and not the broader debated `v1.0`
target-lane bundle. It is the explicit place for architecture notes that define
the minimum bridge from parcel sensing into house-state, action, and measured
outcome reasoning.

## Use this directory for

- `v1.5` bridge-specific architecture notes
- house-state and verification models
- explicit closed-loop definitions and exit criteria

## Keep elsewhere

- cross-version roadmap, taxonomy, and operating-model narratives in `../system/`
- broader target-lane architecture in `../v1.0/`
- frozen current-truth docs in `../current/`

## Starting points

- `house-state-and-verification-model.md`
- `../system/phase-roadmap.md`
- `../system/node-taxonomy.md`
- `../system/architecture-gaps-by-stage.md`

## Why this lane is thin

This directory intentionally holds only **narrow bridge-stage specifics** that don't belong in the cross-version `../system/` lane. Most v1.5 architecture content — roadmap, node taxonomy, gaps, choices — lives in `system/` because it is cross-version. A reader navigating to `v1.5/` looking for "the v1.5 architecture" will find one narrow doc here; the rest is in `system/` and is **cited**, not duplicated, by design.

### Where v1.5 content actually lives (authoritative map)

| v1.5 concern | Canonical location |
|---|---|
| Bridge-stage surface definitions (indoor-response-node, power-outage-node, equipment-state-adapter, action-log, outcome-log, building metadata) | [`house-state-and-verification-model.md`](house-state-and-verification-model.md) (this lane) |
| Stage-B deployment posture (power tier, IP, transport, calibration rigor per v1.5 surface) | [`../system/phase-roadmap.md`](../system/phase-roadmap.md) Stage B |
| How v1.5 bridge surfaces fit the node taxonomy (Tier 1 passive / Tier 2 cloud / Tier 3 direct acquisition model) | [`../system/node-taxonomy.md`](../system/node-taxonomy.md) "Capability-stage v1.5 bridge" section |
| Operational-architecture gaps specific to v1.5 | [`../system/architecture-gaps-by-stage.md`](../system/architecture-gaps-by-stage.md) v1.5 row |
| Architectural choices (class / power / IP / transport / calibration / adapter tier) at v1.5 | [`../system/architectural-choices-by-stage.md`](../system/architectural-choices-by-stage.md) v1.5 row |
| Adapter-trust program for Tier 1 / Tier 2 data (load-bearing at v1.5) | [`../system/adapter-trust-program.md`](../system/adapter-trust-program.md) |
| Part sheets for v1.5 bridge hardware (indoor-response-node, power-outage-node, circuit-monitor) | [`../system/parts/`](../system/parts/) |
| Per-phase narrative and between-stage deltas | [`../system/architectural-choices-by-stage.md`](../system/architectural-choices-by-stage.md) "Per-phase narrative" and "Between-stage deltas" sections |
| Program-packet v1.5 phase framing | [`../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`](../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md) v1.5 section |

The thinness of this directory is not a gap. It is the lane model working as intended: cross-version content stays in `system/` to avoid being duplicated across `current/`, `v1.0/`, and `v1.5/` with drift risk.
