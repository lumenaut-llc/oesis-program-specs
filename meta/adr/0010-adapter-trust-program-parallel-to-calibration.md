# ADR 0010: Adapter-Trust Program Parallel to Calibration Program

- Status: Accepted
- Date: 2026-04-19
- Owners: Open Environmental Sensing and Inference System (technical)
- Related workstreams:
  - architecture/system/adapter-trust-program
  - architecture/system/calibration-program
  - release/v.0.1 (gap-register G18)

## Context

Capability-stage `v1.5` introduces adapter-derived evidence into first-class inference per [`../../architecture/system/node-taxonomy.md`](../../architecture/system/node-taxonomy.md) tiered acquisition model:

- **Tier 1** passive inference (e.g., thermal-slope HVAC detection) — zero hardware.
- **Tier 2** cloud-API adapters (Ecobee, Nest, Sensibo, Honeywell, etc.) — no physical power.
- **Tier 3** direct measurement (e.g., circuit-monitor) — physical node governed by calibration-program.

Tier 1 and Tier 2 evidence has fundamentally different failure modes than physical sensors:

- Physical sensors drift due to aging, contamination, conditioning — calibration-program §D addresses this.
- Adapters drift due to **API contract changes, credential revocation, source-authority deprecation, silent schema changes** — none of which calibration-program covers.

Two options:

- **B1.** Extend `calibration-program.md` with an adapter section. One doc, two concept sets.
- **B2.** Parallel `adapter-trust-program.md` mirroring calibration-program's shape.
- **B3.** Defer adapter posture until `v1.5` work is active.

## Decision

**Adopt B2: parallel adapter-trust-program.**

`architecture/system/adapter-trust-program.md` mirrors `calibration-program.md` section-for-section: §A source registry, §B onboarding gate, §C admissibility, §D drift policy, §E session log, §F build-spec metadata block, §G promotion-bar compliance. Both programs produce the **same admissibility output** on normalized observations via the same decision runtime (per ADR 0009 A3), branching on `adapter_tier`.

Rationale for parallel rather than merged: conflating physical-sensor failure modes with adapter-contract failure modes would force the larger vocabulary onto the smaller problem (or vice versa). Separate programs let each grow at its own pace.

## Consequences

Positive:

- **Clean conceptual boundary.** Physical-sensor drift and adapter-contract drift are different problems; they get different programs with aligned structure.
- **Parallel promotion bars.** Adapters reach `deployment maturity v1.0`/`v1.5`/`v2.0` per adapter-trust-program §G independent of physical-sensor fleet maturity.
- **Unified admissibility output.** Both programs feed the same `admissible_to_calibration_dataset` decision on normalized observations, so downstream consumers see one concept.
- **Scoped correctly for current work.** v0.2–v1.0 promotion involves zero adapters; program is docs-only until `v1.5` work begins. No runtime cost today.

Negative:

- **Two policy docs instead of one.** Future maintainers must remember both exist. Mitigated by cross-linking and by both docs using identical section structure.
- **Risk of drift between the two programs.** If calibration-program §C adds a 9th admissibility check and adapter-trust-program §C doesn't, the programs fall out of sync. Mitigated by treating them as paired in any update that touches the §C check list.

## Alternatives considered

**B1: extend calibration-program with adapter section.**
Rejected because calibration-program is already substantial (§A–§G, ~250 lines) and each section's logic is physical-sensor-specific. An adapter section would either repeat the structure (duplicating §A/B/C/D/E for a different concept set) or shoehorn adapter concerns into sections that were built for physical sensors. Neither is clean.

**B3: defer adapter posture until v1.5 active work.**
Rejected because `v1.5` bridge work is already being referenced across roadmap and phasing docs. Leaving the adapter program unspecified until work begins means adapter choices get designed ad-hoc and then retroactively systematized. Writing the program structure now (docs-only) costs little and ensures when `equipment-state-adapter`, `circuit-monitor` Tier 3 feed, or passive thermal-slope inference lands, they have structure to fill rather than inventing it.

## Follow-up work

- Populate adapter-trust-program §A source registry as adapters land (build-vault agent via proposal [`../proposals/oesis-builds-node-skeletons.md`](../proposals/oesis-builds-node-skeletons.md) Skeleton 5 for circuit-monitor).
- Runtime admissibility branching on `adapter_tier` in `oesis-runtime` ingest per ADR 0009. Tracked as G15.
- Cross-repo schema additions for adapter-derived observation facts in `oesis-contracts` v1.5 lane. Tracked as G17/G18.
- Any change to calibration-program §C admissibility rule list should be mirrored in adapter-trust-program §C in the same commit to avoid drift.
