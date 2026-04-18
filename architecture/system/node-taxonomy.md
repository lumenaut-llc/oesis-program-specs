# Node and Evidence Taxonomy

## Lane

This document is the `system/` lane version of this topic.

Use it for the repo-wide taxonomy, current-truth hardware posture, and
promotion-aware classification of node and evidence surfaces.

If you need the debated target-lane taxonomy, use `../v1.0/node-taxonomy.md`.

## Purpose

Give one repo-wide vocabulary for **hardware node families**, **geography-gated modules**, and **non-node evidence surfaces**, with explicit **capability-stage** and **promotion** labels so taxonomy is not mistaken for shipped product.

## Governing rules

- The **parcel** remains the primary object; nodes and adapters are evidence layers used to compute parcel-level conditions and statuses.
- **Taxonomy names** may exist in docs before hardware folders or runtime normalization land. Treat missing implementations as `planned` or `partial` unless a specific promotion says otherwise.
- Do not collapse **accepted runnable slice** (for example program-phase `v0.1`, next `v0.2`), **capability stage** (`current v1`, `v1.5`, …), and **deployment maturity** (`deployment maturity v0.1`, …). See `version-and-promotion-matrix.md`.

## Current-truth hardware (accepted reference path today)

| Identifier | Role | Notes |
| --- | --- | --- |
| `bench-air-node` | Indoor or sheltered bench reference; `oesis.bench-air.v1` lineage | Proven end-to-end ingest → parcel view for this family |

## Next-promotion kit hardware (not the same as “fully proven”)

| Identifier | Role | Notes |
| --- | --- | --- |
| `mast-lite` | First sheltered-outdoor reference; same packet lineage as bench-air | Architecturally in scope; runtime normalization and field validation are **partial** until the `v0.2` promotion bar in `../current/pre-1.0-version-progression.md` is met |

## Geography-gated and second-wave hardware modules

Attach only when parcel risk, region, and use case justify them. None of these are universal defaults.

| Identifier | Role | Typical staging |
| --- | --- | --- |
| `flood-node` | Low-point runoff depth and rise-rate evidence | Optional hazard module; ingest and inference implemented (`flood.low_point.snapshot`) |
| `weather-pm-mast` | Richer outdoor PM, wind, rainfall | Second-wave outdoor lane; ingest and inference implemented (`air.pm.snapshot`) |
| `freeze-node` | Cold-climate pipe-risk and exposed-space thermal evidence | Planned geography module; not required for warm-climate pilots |

## Research- or privacy-gated hardware

| Identifier | Role | Notes |
| --- | --- | --- |
| `thermal-pod` | Fixed-scene derived thermal context | R&D lane; keep outside default pilot until contract, usefulness, and retention posture are reviewed |

## Capability-stage v1.5 bridge (planned hardware and adapters)

These convert the program from “outdoor and parcel sensing only” toward **hazard -> house state -> action -> measured outcome**. They belong in the **v1.5** capability stage as support objects and evidence types, not as implied **current v1** baseline.

The point of this stage is not just richer local sensing.
It is to collect the minimum surfaces needed to model how the house responds to conditions and whether an intervention actually helped.

| Identifier | Kind | Minimum intent |
| --- | --- | --- |
| `indoor-response-node` | Hardware family (planned) | Indoor PM2.5, indoor temperature, indoor RH — lets the system see whether the house is buffering occupants from outdoor forcing |
| `power-outage-node` | Hardware family or adapter (planned) | Mains up/down and backup-power posture — continuity and resilience floor during disruption |
| `equipment-state-adapter` | Non-node or adapter surface | Read-side HVAC mode, fan, recirculation vs fresh air, purifier, shade/window, sump/pump where available |
| `circuit-monitor` | Hardware family (implemented) | Non-invasive current-draw monitoring node using split-core CT clamps and PZEM-004T/016. Monitors HVAC and sump pump circuits for operating state, power draw, and cycle timing. Equipment-state adapter that feeds `hvac_mode`, `sump_state`, `equipment_running`, and power draw data into house-state at HIGH confidence. Optional equipment-state module -- not part of default Tier 1-2 parcel kit. See [`circuit-monitor/README.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/circuit-monitor/README.md) |
| `action-log` | Support object | Household or building actions (mode changes, purifier run, drain clearing, barrier install, backup activation) with timestamps and targets |
| `outcome-log` / response verification | Support object | Whether actions improved observed conditions over defined windows (for example 30–90 minutes for smoke-related PM response) |
| `building-and-site-metadata-surface` | Parcel-context extensions | Orientation, roof/color, shading, tree canopy, impervious area, low points, drainage, vents, filter path — part of response interpretation, not decorative metadata |

**Tiered acquisition model for house-state fields:**

Equipment operating state can be acquired at three fidelity tiers. Each tier maps
to a `source_kind` in the `equipment-state-observation` contract. Higher tiers
take priority when available, but lower tiers ensure every parcel has at least
some equipment-state signal.

- **Tier 1 (passive inference):** thermal slope inference from existing indoor
  temperature sensor -- zero additional hardware, LOW confidence. Uses observed
  indoor temperature slope versus expected passive thermal behavior to classify
  HVAC mode. Cannot distinguish recirculate from fresh-air mode. See
  `../../software/inference-engine/thermal-slope-inference.md`.
- **Tier 2 (adapter integration):** cloud API adapters for Ecobee, Nest,
  Sensibo, Honeywell, and similar smart thermostats -- no new hardware if the
  homeowner already has a compatible device, HIGH confidence but cloud-dependent.
  Produces `source_kind: "adapter_derived"`.
- **Tier 3 (direct measurement):** CT clamp circuit-monitor node -- highest
  fidelity, no cloud dependency, HIGH confidence. Produces
  `source_kind: "direct_measurement"`. Optional hardware add-on for parcels
  where equipment-state fidelity is critical (for example smoke-protect
  verification).

The inference engine adapter registry evaluates sources in descending tier order
and uses the freshest high-confidence source available for each parcel.

**First closed-loop priority (spec direction):** smoke protection — outdoor PM, indoor PM, smoke-protect posture, bounded actions such as recirculation / fan / purifier, then verify indoor PM response over a bounded time window.

## Capability-stage v2.5 — controls compatibility (not v1.5 execution)

**Full compatibility inventory** by interface class (for example Matter, Home Assistant, BACnet relevance, smart plugs, local controllers), integration tiers, and bounded-control policy versioning is primarily **v2.5**, even when draft schema files exist for forward compatibility.

- **v1.5** may capture **observed** equipment state and coarse **house-capability** hints.
- **v2.5** is where compatibility mapping and bounded controls become first-class operational requirements. See `architecture-gaps-by-stage.md` and `phase-roadmap.md` Stage D.

## Capability-stage v4 — route and community surfaces

| Identifier | Kind | Notes |
| --- | --- | --- |
| `route-and-community-surface` | Data and model layer | Egress, shared refuge, drainage chokepoints, block-level weak points — staged later; not a default hardware expectation for early pilots |

Prefer public data, shared reports, and selected instrumentation over universal “community chokepoint” nodes in early phases.

## Geography mapping (planning aid)

- **Wildfire / smoke regions:** emphasize `mast-lite` (when promoted), `indoor-response-node`, optional `weather-pm-mast`, equipment-state for HVAC/purifier.
- **Flood / runoff regions:** `flood-node` where relevant, sump/pump equipment-state, drainage metadata.
- **Heat-burden regions:** `indoor-response-node`, shading/HVAC equipment-state, optional `thermal-pod` later.
- **Cold / freeze regions:** `freeze-node` where justified, `power-outage-node`, heating-system equipment-state.
- **Storm / outage-prone regions:** `power-outage-node`, backup power signals, communications dependency metadata in parcel context.

## Recommended sequencing (spec)

1. **Baseline parcel sensing:** `bench-air-node`, parcel inference, shared evidence discipline (`current v1`).
2. **Next promotion:** `v0.2` indoor + sheltered outdoor kit — `bench-air-node` + `mast-lite` with field-hardening and acceptance evidence (`../current/pre-1.0-version-progression.md`).
3. **v1.5 bridge:** indoor response, outage, equipment-state signals, building/site metadata, action and outcome logs.
4. **v2 / v2.5:** bounded guidance, then compatibility inventory and bounded controls.
5. **v4:** route and neighborhood resilience surfaces.

## Related docs

- `version-and-promotion-matrix.md`
- `integrated-parcel-system-spec.md`
- `deployment-maturity-ladder.md`
- `architecture-gaps-by-stage.md`
- `phase-roadmap.md`
- [`parcel-context-schema.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/parcel-context-schema.md)
- [`v0.1/README.md`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/v0.1/README.md)
