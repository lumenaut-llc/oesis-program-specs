# Architectural Choices By Stage

## Lane

This document is the `system/` lane summary of architectural choices (power strategy, transport, enclosure IP rating, radiation shield, sensor variants, calibration rigor, admissibility policy) as they evolve across program phases and capability stages.

## Purpose

Provide a single-page answer to "what architectural choices apply at each program-phase, in total and between stages." Sibling doc to [`architecture-gaps-by-stage.md`](architecture-gaps-by-stage.md), which covers the same axis for gaps rather than choices.

This doc is a **summary surface**, not a source of truth. When this doc and a cited program doc disagree, the cited program doc wins. Canonical sources:

- [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md) — power / IP / transport tier per deployment class; deployment-maturity rungs
- [`calibration-program.md`](calibration-program.md) — §F build-spec metadata block; §G promotion-bar compliance per tier
- [`adapter-trust-program.md`](adapter-trust-program.md) — parallel program for Tier 1 / Tier 2 adapter-derived data
- [`sensor-placement-and-representativeness-guide.md`](sensor-placement-and-representativeness-guide.md) — placement → deployment class map; sensor variant selection principles
- [`node-taxonomy.md`](node-taxonomy.md) — per-node posture tags and tiered acquisition model
- [`../current/pre-1.0-version-progression.md`](../current/pre-1.0-version-progression.md) — slice promotion bar

## How to read this doc

1. Start with the axis legend to check which version axis you're reasoning about.
2. Go to the master table to see the choice set that applies at a given program-phase.
3. Go to the per-phase narrative for what changes and why.
4. Use the between-stage deltas to see what each promotion actually adds.

If you're designing a new node family, read [`calibration-program.md`](calibration-program.md) §F for the build-spec metadata schema, then declare a posture that matches this doc's cell values for the target phase.

## Axis legend

Per [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md), this repo uses four axes that must not collapse:

- **Program phase** (accepted runnable slice): `v0.1`, `v0.2`, `v0.3`, `v0.4`, `v0.5`, `v1.0` — defines what end-to-end story is promoted.
- **Capability stage**: `current v1`, `v1.5`, `v2`, `v2.5`, `v3`, `v4` — defines the class of product behavior in scope.
- **Deployment maturity**: `v0.1`, `v1.0`, `v1.5`, `v2.0` per family — defines how field-hardened the hardware is.
- **Runtime lane**: `v0.1`–`v1.5` in `oesis-runtime/oesis/assets/` — defines which capability set the runtime activates.

This doc's master-table rows are **program phase**. Cells name the deployment class set, power tier, IP tier, transport tier, deployment-maturity tier, calibration rigor, adapter tier, and admissibility policy that applies at that phase.

## Master table — choices by program-phase

| Phase | Deployment class set | Power tier | IP tier | Transport floor | Deployment-maturity target | Calibration rigor (physical) | Adapter-trust tier (where present) | Admissibility to coefficient fitting |
|---|---|---|---|---|---|---|---|---|
| **`v0.1`** | indoor | USB | IP20 | serial | `v0.1` (bench) | provisional; no characterized reference required | n/a (no adapters) | **not admissible** (§C tier 2 bar not met) |
| **`v0.2`** | indoor + sheltered | USB (indoor); 12V-DC or USB-from-indoor (sheltered) | IP20 / IP44 | serial; Wi-Fi permitted sheltered | `v1.0` (first fielded kit); retroactive for bench-air per `../current/pre-1.0-version-progression.md` | characterized references per measurand per class; burn-in gate enforced; §F metadata block complete | n/a (v0.2 is physical-sensor only) | **admissible** if §C 8-point check passes |
| **`v0.3`** | v0.2 + outdoor (flood-node) | + battery+solar or hardened mains (outdoor) | + IP65 | + serial→LoRa | `v1.0` | v0.2 rigor + flood-node zero-reference + geometry discipline | n/a | admissible per §C |
| **`v0.4`** | same as v0.3 | same | same | same | `v1.0` | multi-node evidence composition; per-device calibration versioning begins | n/a | admissible per §C |
| **`v0.5`** | same as v0.3 | same | same | same | `v1.0` | v0.4 rigor + governance-gated shared-layer eligibility per G22 | n/a | admissible per §C; shared-layer gate per G22 |
| **`v1.0`** (pre-1.0 ladder) | indoor + sheltered + outdoor (where justified) | per deployment class | per deployment class | per deployment class | `v1.0` fleet-wide | all five §A–§E components complete per family; §F block passing validation; §G tier met | Tier 3 only (circuit-monitor possible) | admissible per §C |
| **`v1.5`** (capability-stage bridge) | + indoor bridge surfaces (indoor-response-node, power-outage-node, circuit-monitor) | + battery-backed (power-outage-node); low-power from measured circuit (circuit-monitor) | + electrical-enclosure IP20 (circuit-monitor) | + Wi-Fi / LoRa for bridge surfaces | `v1.5` (trust hardening) — versioned offsets, drift-aware | v1.0 rigor + versioned calibration state + maintenance-informed trust penalties | **Tier 1, 2, 3 all in scope** — adapters governed by `adapter-trust-program.md` | admissible per §C (physical) or adapter-trust §C (adapters); branch by `adapter_tier` |
| **`v2`** (capability-stage guidance) | same physical as `v1.5` | same | same | same | `v1.5` | same | same; adapters at adapter-trust `v1.5` tier | admissible; guidance outputs advisory-only |
| **`v2.5`** (capability-stage controls) | same physical as `v1.5` | same | same | same | `v2.0` (decision-policy support) | v1.5 rigor + cross-node consistency audits | all tiers + bounded-control adapters (Matter / HA / BACnet) at adapter-trust `v2.0` | admissible; bounded-control readouts enforced |
| **`v3`** (adaptation engine) | same physical as `v1.5` | same | same | same | `v2.0` fleet-wide | retirement thresholds enforced in runtime | same | admissible; retired devices excluded |
| **`v4`** (parcel + route + block) | + shared-layer aggregation (derived from per-parcel admissible data) | n/a (derived) | n/a | n/a | inherits per-contributor | inherits per-contributor | inherits | shared-layer contribution gated on per-contributor admissibility per G22 |

**Legend:** "n/a" means the axis does not apply at that phase (e.g., adapter-trust tier is n/a in `v0.1`–`v1.0` because no adapters are in scope).

## Per-phase narrative

### `v0.1` — narrow executable reference slice

**What hardware choice unlocks this phase.** The choice to commit to **one indoor bench-air-node, USB-powered, with serial-only transport** is what makes v0.1 executable without field infrastructure. USB is the lightest possible power assumption; serial is the lightest possible transport assumption. Together they mean a parcel can run on a laptop next to a dev board — no authorization, no Wi-Fi, no outdoor mounting, no IP rating.

**What is deliberately out.** Outdoor sensing, sheltered sensing, PM2.5, radiation shields, adapters, battery/solar power, Wi-Fi transport, field-hardening. All of these are deferred not because they are unimportant, but because including them would force v0.1 to solve field problems before the reference path has proven it can produce one honest parcel view.

**Calibration posture.** Provisional. v0.1 readings are useful for software validation but are **not admissible** to the calibration dataset that feeds hazard-formula coefficient fitting. Production coefficient fits require at least `v0.2` / deployment-maturity `v1.0` data per calibration-program §G.

### `v0.2` — first widened kit (bench-air + mast-lite)

**What hardware choices unlock this phase.** Adding **mast-lite at deployment-class sheltered** is the step from bench to field. Mast-lite requires three choices that v0.1 could avoid: (a) a power path that survives a sheltered outdoor mount (12V-DC or USB-from-indoor through a cable gland), (b) an enclosure rated to IP44 so occasional rain-splash and condensation don't break the unit, (c) a protective fixture (radiation shield) whose thermal-loading acceptance test has been passed — without which outdoor temperature readings are corrupted by solar loading and inadmissible.

**What changes about calibration.** v0.2 is where the calibration program §G `v1.0` tier begins to bind. Characterized reference instruments must be populated per measurand per deployment class; burn-in gate enforced for BME680-bearing nodes; §F metadata block complete for every node family in the kit. Bench-air-node's v0.1 sign-off is not reopened (retroactivity rule in `pre-1.0-version-progression.md`), but bench-air must reach v1.0 calibration posture as part of v0.2 promotion.

**Gap-register tie-ins.** G12 (mast-lite spec), G13 (reference instruments), G14 (burn-in gate), G16 (bench-air §F block) all bite here.

### `v0.3` — first flood-capable slice

**What hardware choices unlock this phase.** Adding **flood-node at deployment-class outdoor** extends the class set. Flood-node needs battery+solar or hardened mains (outdoor class default), IP65 (flood-node installations see standing water), and serial→LoRa (low-point mounts often beyond reliable Wi-Fi). The single most important protective-fixture choice at v0.3 is a rigid mount at a documented low-point with a zero-reference staff gauge — without documented geometry, depth numbers are decoration.

**What is deliberately out.** PM2.5 (deferred to v1.0 with weather-pm-mast), thermal sensing (research-gated).

### `v0.4` — multi-node registry and evidence composition

**What hardware choices unlock this phase.** No new class; multi-node evidence composition across the v0.3 set. The choice at v0.4 is to require per-device calibration versioning so drift can be tracked without contaminating historical inference outputs.

### `v0.5` — governance enforcement

**What hardware choices unlock this phase.** No new hardware. The architectural choice is to gate shared-layer contribution on per-contributor calibration-program admissibility (G22). A well-placed but uncalibrated node cannot contribute to shared-map aggregation.

### `v1.0` (pre-1.0 ladder) — first materially broader system

**What choices unlock this phase.** The whole v0.1–v0.5 architecture reaching **deployment-maturity `v1.0`** fleet-wide. Every node family has a §F metadata block passing validation; every measurand has a characterized reference instrument; every node's reference-calibration is current; §G promotion-bar compliance is formally attested.

### `v1.5` — measurement-to-intervention bridge

**What hardware choices unlock this phase.** The key choice is introducing **adapter-derived data** as first-class evidence alongside physical sensors. Three tiers of adapter:

- **Tier 1 passive inference** (zero hardware; e.g., thermal-slope HVAC detection) — the inference method itself is the source authority.
- **Tier 2 cloud API** (Ecobee, Nest, Sensibo, Honeywell) — no physical power; governed by API contract version and schema-drift detection.
- **Tier 3 direct measurement** (circuit-monitor) — physical power (low-power from measured circuit), electrical-enclosure IP20, Wi-Fi transport.

`indoor-response-node` and `power-outage-node` are new physical-sensor classes at v1.5 as well; `power-outage-node`'s power is **battery-backed** (intrinsic: a continuity monitor that loses power is useless). Calibration rigor steps up to `v1.5` (versioned offsets, drift-aware).

### `v2` — bounded adaptation guidance

**What hardware choices unlock this phase.** None new; software layer on v1.5 hardware. Adapter-trust tier for every consumed adapter must be at `v1.5` (verification logs versioned, schema-drift detection active).

### `v2.5` — bounded controls and compatibility mapping

**What hardware choices unlock this phase.** Introduces control-side adapter surfaces (Matter, Home Assistant, BACnet, smart plugs). Physical-sensor requirements unchanged from v1.5; adapter-trust tier for control adapters must be at `v2.0` (cross-adapter consistency audits, retirement/replacement paths documented). Bounded controls are reversible, low-risk, and verifiable by construction — every action enters an outcome log so its effect can be measured.

### `v3` — parcel adaptation engine

**What hardware choices unlock this phase.** None new. The architectural choice is to require `deployment maturity v2.0` **fleet-wide**: retirement thresholds enforced in runtime, learned priors do not encode defunct devices as baseline.

### `v4` — parcel + route + block resilience

**What hardware choices unlock this phase.** None new per parcel. The scaling choice is that shared-layer contribution is gated on per-contributor admissibility per gap G22 — parcel-private data that fails admissibility does not flow to block-level aggregation.

## Between-stage deltas

What changes at each promotion:

- **`v0.1` → `v0.2`:** adds sheltered deployment class; adds 12V-DC power tier; adds IP44; adds radiation-shield protective fixture; enters calibration-program §G `v1.0` tier; readings become admissible to coefficient fitting.
- **`v0.2` → `v0.3`:** adds outdoor deployment class; adds battery+solar power tier; adds IP65; adds LoRa permitted transport; adds flood-node rigid mount + zero-reference fixture.
- **`v0.3` → `v0.4`:** no class / power / IP / transport change; adds per-device calibration versioning (deployment-maturity `v1.5` anticipation).
- **`v0.4` → `v0.5`:** no hardware change; adds shared-layer eligibility gating on per-contributor admissibility.
- **`v0.5` → pre-1.0 `v1.0`:** all v0.2–v0.5 rigor now **fleet-wide** with §F metadata blocks passing validation; §G tier `v1.0` formally attested for every node family.
- **`v1.0` → capability-stage `v1.5`:** adds adapter-derived data (Tier 1, 2, 3); adds `indoor-response-node` + `power-outage-node` + `circuit-monitor` hardware; adds battery-backed power tier (for continuity-monitor use case); adds electrical-enclosure class (for circuit-monitor); calibration rigor steps to `v1.5` (versioned offsets).
- **`v1.5` → `v2`:** no hardware change; adapter-trust tier floor becomes `v1.5` for every consumed adapter.
- **`v2` → `v2.5`:** adds bounded-control adapters (Matter / HA / BACnet); adapter-trust tier floor becomes `v2.0` for control adapters; calibration-program §G `v2.0` (cross-node bias audits) required.
- **`v2.5` → `v3`:** no hardware change; calibration-program §G `v2.0` now **fleet-wide**; retirement thresholds enforced in runtime.
- **`v3` → `v4`:** no per-parcel hardware change; introduces shared-layer aggregation surfaces; per-contributor admissibility gates shared-layer eligibility per G22.

## Non-goals

- This doc does not replace per-stage docs. It is a summary surface. Per-stage docs (`v0.1-acceptance-criteria.md`, `phase-roadmap.md`, `09-phasing-v0.1-v1.0-v1.5.md`, `v1.0-scope.md`, etc.) carry the authoritative per-stage detail in context.
- This doc does not introduce new vocabulary. Every term it uses is canonical per the sources listed in "Purpose".
- This doc does not promote any accepted slice. Promotion follows `pre-1.0-version-progression.md` item 5 (calibration-program compliance at target deployment-maturity tier).
- **If this doc and the ladder / calibration-program / adapter-trust-program disagree, the ladder / calibration-program / adapter-trust-program wins.** Report the discrepancy and fix this doc.

## Related docs

- [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md) — canonical deployment-class standards
- [`calibration-program.md`](calibration-program.md) — §F / §G; canonical for physical-sensor calibration and admissibility
- [`adapter-trust-program.md`](adapter-trust-program.md) — canonical for adapter-derived data
- [`sensor-placement-and-representativeness-guide.md`](sensor-placement-and-representativeness-guide.md) — placement → deployment class mapping; sensor variant selection
- [`node-taxonomy.md`](node-taxonomy.md) — per-node posture tags
- [`phase-roadmap.md`](phase-roadmap.md) — capability stages with inline deployment posture per stage
- [`integrated-parcel-system-spec.md`](integrated-parcel-system-spec.md) — hardware role map with per-node posture summary
- [`architecture-gaps-by-stage.md`](architecture-gaps-by-stage.md) — sibling doc, same per-stage framing for gaps
- [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md) — four-axis versioning
- [`../current/pre-1.0-version-progression.md`](../current/pre-1.0-version-progression.md) — promotion-bar item 5 (calibration-program compliance)
- [`../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`](../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md) — per-phase deployment posture blocks
