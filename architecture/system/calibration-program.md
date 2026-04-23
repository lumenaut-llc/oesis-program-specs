# Calibration Program

## Lane

This is the `system/` lane document for calibration policy that applies across **every node family** in the repo. It sits alongside `node-taxonomy.md`, `sensor-placement-and-representativeness-guide.md`, and `deployment-maturity-ladder.md`.

## Purpose

Define the calibration policy the whole fleet inherits, so that:

- every node family answers the same questions the same way (reference instruments, burn-in, drift, admissibility),
- calibration requirements scale predictably with `deployment maturity`,
- the hazard formula can fit coefficients only against data that has passed a documented admissibility bar.

This doc is policy. Per-device execution (how a specific bench-air unit or mast-lite unit is calibrated on a given day) lives in the respective `oesis-builds/procedures/<node>/calibration.md`.

## Relation to version axes

Per [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md), this repo uses four axes that must not collapse. This doc touches only two of them:

- **Deployment maturity** — calibration requirements scale with the ladder in [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md). Higher maturity requires stricter calibration posture.
- **Implementation status** — each requirement in this doc is labeled `implemented`, `partial`, `docs-only`, or `planned` at the end.

It does **not** introduce a new axis, does **not** define capability-stage content, and does **not** promote accepted runnable slices. A slice like program-phase `v0.2` (bench-air + mast-lite) may require that its node families meet `deployment maturity v1.0` calibration posture; that dependency belongs to the promotion docs, not here.

## Governing principles

1. **No reading is truth without a referent.** Sensor output is a claim. A calibrated reading is a claim backed by a documented comparison against a characterized reference.
2. **Requirements scale with deployment maturity.** Bench prototypes live under provisional calibration. First-fielded kits require real references. Trust-stage nodes require versioned calibration state. Adaptation-stage nodes require drift policy and replacement handling.
3. **Admissibility is binary.** A reading is either admissible to the calibration dataset used for coefficient fitting, or it isn't. Partial credit creates silent fits against bring-up drift.
4. **Policy at platform; execution per node.** This doc does not prescribe part numbers for reference instruments. Node build specs and calibration procedures name the concrete instruments that satisfy the policy for each measurand.
5. **Traceable over perfect.** A reference instrument with a documented accuracy statement and traceability chain is more useful than a nominally more accurate instrument whose provenance cannot be verified.

## Program components

### A. Reference instrument program

Every measurand consumed by the hazard formula must have at least one characterized reference instrument available for the deployment class in which the node operates.

For each reference instrument, the program requires a file under `oesis-builds/procedures/<node>/references/<instrument>.md` with:

- make, model, and serial number
- measurand(s) and accuracy statement (e.g., "±0.2 °C, 10–40 °C")
- traceability chain (NIST traceable where practical; otherwise document the best available chain)
- calibration certificate reference and last verification date
- storage conditions and permitted environmental exposure
- known failure modes and re-verification cadence

**Sharing:** a single reference instrument may serve multiple node families if it covers the measurand and deployment class of each. The reference file lives once; each using node's calibration procedure references it.

**Minimum coverage for each measurand in scope**, by deployment class:

| Measurand | Indoor class | Sheltered class | Outdoor class |
|---|---|---|---|
| Temperature | characterized reference required | characterized reference required | characterized reference required, rated for the operating envelope |
| Relative humidity | characterized reference required | characterized reference required | characterized reference required, rated for the operating envelope |
| Gas resistance (BME680 VOC trend) | best-available reference acceptable in `deployment maturity v0.1`; characterized reference required to progress | characterized reference required | characterized reference required |
| PM2.5 | reference not required in current hardware lanes (no PM sensor shipped) | reference required before `weather-pm-mast` admits fits | reference required before `weather-pm-mast` admits fits |

### B. Burn-in gate

Sensors that require conditioning on first power-up must complete a documented burn-in window before their readings are admissible to the calibration dataset.

**Current platform defaults** (subject to per-node override in the build spec, with justification):

- **BME680 / BME688 (gas resistance):** 48 h burn-in minimum on first power-up. Per-packet `burn_in_complete` flag required; ingest tags observations until the window passes.
- **SHT45 (temperature / humidity):** no burn-in requirement beyond manufacturer's standard settling; post-mounting acclimatization of 1 h recommended for meaningful rolling baselines.
- **PM sensors (TBD per sensor family):** policy to be added when the first PM-capable node lands.

**Enforcement:** the bring-up acceptance procedure for a node family must include the burn-in gate as a pass/fail item. Nodes that have not passed the gate emit readings tagged `burn_in_complete: false`; these readings are excluded by the admissibility rule below.

### C. Calibration dataset admissibility

A reading is admissible to the calibration dataset used for hazard-formula coefficient fitting only if all of the following hold:

1. **Node identity is current.** The producing node's build version and firmware version are both recorded against a registered `parcel_id`.
2. **Deployment maturity tier met.** The node meets at least `deployment maturity v1.0` (first fielded-kit bundle in [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md)). `deployment maturity v0.1` readings may be used for prototyping analysis but are not admissible for production coefficient fits.
3. **Deployment class honored.** The node's declared deployment class matches the physical installation, and the installation meets the power / IP / transport tier standards set for that class in [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md).
4. **Burn-in complete.** `burn_in_complete: true` at the observation's timestamp, per section B.
5. **Reference calibration current.** The node's most recent calibration session against a characterized reference (per section A) falls within the re-verification cadence for that reference.
6. **Placement representativeness declared.** Per [`sensor-placement-and-representativeness-guide.md`](sensor-placement-and-representativeness-guide.md), the installation's class (A/B/C/D) is recorded. Class-D readings are never admissible; Class-C readings are admissible only when the hazard formula explicitly opts in for that term.
7. **Protective fixtures verified where required.** For outdoor nodes, radiation shield or equivalent fixture has been verified against its thermal-loading acceptance test; pre-verification readings are excluded. For flood nodes, zero-reference and geometry discipline are documented.
8. **Sensor health within bounds at observation time.** `read_failures_total` increment rate below threshold; rolling-baseline dispersion flag not `unstable`; observation age within freshness window.

**Inadmissible ≠ discarded.** Inadmissible readings remain in raw logs for audit, post-hoc analysis, and outcome-label cross-checks. They do not feed coefficient fitting.

#### Schema vs runtime split (decision 2026-04-19)

The admissibility **decision** (the boolean outcome of the eight checks above, with reason codes) is computed in runtime/ingest, not in the canonical observation schema. This keeps the schema stable as admissibility policy evolves, allows different consumers to audit or recompute decisions, and preserves the reasoning trail.

The admissibility **facts** — the static, known-at-emission-time inputs those checks consume — must appear on the canonical observation record in [`oesis-contracts`](https://github.com/lumenaut-llc/oesis-contracts) so every downstream consumer sees the same evidence without recomputing or probing the node registry.

Minimum facts the observation schema must carry (cross-repo change tracked in G17):

- `burn_in_complete: bool` — per section B; ingested from firmware health block or injected by ingest once the device's first-power-up window has elapsed
- `node_calibration_session_ref: string` — opaque reference to the most recent calibration session record per section E
- `node_deployment_maturity: enum` — one of `v0.1`, `v1.0`, `v1.5`, `v2.0` per [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md); declared in the node's build-spec §F block, carried forward on each packet
- `node_deployment_class: enum` — one of `indoor`, `sheltered`, `outdoor` per [`sensor-placement-and-representativeness-guide.md`](sensor-placement-and-representativeness-guide.md); same provenance
- `protective_fixture_verified_at: timestamp | null` — null if not applicable; timestamp of last verified thermal-loading test (or equivalent) otherwise
- `placement_representativeness_class: enum | null` — A/B/C/D per the placement guide; null during pre-install observations

Runtime decisions produced by ingest once facts are present, attached to the normalized observation and never back-propagated to the schema:

- `admissible_to_calibration_dataset: bool`
- `admissibility_reasons: [string]` — enumerated reason codes when false (e.g., `burn_in_incomplete`, `reference_calibration_stale`, `fixture_unverified`); empty list when true

Audit invariant: a normalized observation carrying `admissible_to_calibration_dataset: false` with a populated `admissibility_reasons` list is the durable artifact. Coefficient-fitting pipelines filter on the boolean; audit tooling reads the reasons to explain why a record was excluded.

### D. Drift policy

A device's calibration state drifts over time. The program sets three response tiers:

- **Within tolerance:** periodic re-verification against the reference at the cadence named in section A. No action required.
- **Drift detected, correctable:** when a device's offset vs. reference has grown beyond a configured threshold but below a retirement threshold, log the new correction value to the device's calibration history and version it. Subsequent readings are corrected through the versioned offset. Corresponds to `deployment maturity v1.5` calibration-versioning requirement.
- **Drift beyond retirement threshold:** the device is retired from admissibility until repair or replacement. Readings from the flagged window are marked inadmissible and the replacement device's initial calibration is treated as a fresh session.

Specific numeric thresholds are node- and measurand-specific and live in each node's calibration procedure, not in this doc.

### E. Calibration log format

Each calibration session produces a record with at minimum:

- session timestamp (UTC)
- node identity (build version, firmware version, unit serial)
- reference instrument identity (per section A) and its last-verified date
- measurand(s) exercised
- raw reference reading(s) and raw node reading(s) for each calibration point
- computed offset or correction, if any
- session outcome: `pass`, `within-tolerance drift`, `correctable drift`, `retirement required`
- operator identity
- environmental conditions during session
- next re-verification due date

Calibration logs live alongside install metadata for the device they apply to. They are authoritative when inference or admissibility checks reference "the device's current calibration state."

### F. Build-spec metadata block

Every node build spec in `oesis-builds/specs/<node>/v0-X.md` must include a front-matter metadata block that declares the calibration and deployment posture the node commits to. The block is the structured contract by which node specs and calibration compliance stay greppable and — once admissibility tooling exists — machine-checkable.

Minimum fields:

```yaml
---
node_family: <string, e.g. "bench-air-node">
build_version: <string, e.g. "v0-1">
deployment_class: indoor | sheltered | outdoor
deployment_maturity_target: v0.1 | v1.0 | v1.5 | v2.0
measurands:
  - name: <e.g. "temperature_c">
    sensor_variant: <e.g. "sht45-filtered-pack">
    accuracy_statement: <e.g. "±0.1 °C, 0–60 °C">
    reference_instrument_ref: <path to file under oesis-builds/procedures/<node>/references/>
  - name: <next measurand>
    sensor_variant: <...>
    accuracy_statement: <...>
    reference_instrument_ref: <...>
burn_in:
  required: true | false
  window_hours: <number, or null if not required>
protective_fixtures:
  - name: <e.g. "passive radiation shield">
    acceptance_test_ref: <path to test procedure>
transport:
  primary: serial | wifi | lora | cellular
  permitted_fallbacks: [<list>]
power:
  source: usb | dc_12v | battery_solar | mains_outdoor_psu
  protection: [<list of protections per deployment-maturity-ladder.md>]
calibration_program_revision: <commit hash or date of the calibration-program.md revision this spec commits against>
---
```

Fields are validated against the deployment-class standards in [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md). A build spec whose declared power source, IP rating, or transport does not match the defaults for its declared deployment class must include a justification section referencing the exception.

The block is consumed by (future, planned) admissibility tooling to resolve whether a reading from a given node is admissible without re-reading the full build spec. Until the tooling ships, the block is human-readable contract — node specs are still inspectable, just not automatically enforced.

### G. Promotion-bar compliance

A node family's eligibility to participate in a promoted accepted-runnable slice (per [`../current/pre-1.0-version-progression.md`](../current/pre-1.0-version-progression.md)) depends on the calibration posture it meets.

The promotion bar for a slice names the deployment-maturity tier its node families must reach. This program's compliance bar per tier:

- **`v0.1` (bench prototype):** build-spec metadata block (§F) exists; other components provisional.
- **`v1.0` (first fielded kit):** all five §A–§E components complete for every measurand the node exposes; metadata block (§F) complete and passing validation against `deployment-maturity-ladder.md` class standards.
- **`v1.5` (trust hardening):** §A–§F complete; calibration versioning active; drift logs in the calibration history.
- **`v2.0` (decision-policy):** §A–§F complete; cross-node bias audit on record; retirement thresholds enforced in runtime.

Slice promotion (`v0.2`, `v0.3`, …) inherits these tiers through its promotion bar. The retroactivity rule in `pre-1.0-version-progression.md` applies: already-promoted slices keep their original posture; node families moving into a new slice must meet that slice's tier.

## Maturity ladder mapping

Calibration posture required at each rung of [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md):

| Deployment maturity | Reference instrument | Burn-in gate | Admissibility | Drift policy | Log format |
|---|---|---|---|---|---|
| `v0.1` (bench prototype) | Best-available acceptable; can be uncharacterized for initial software validation | Recommended, not enforced | **Not admissible** to coefficient fits | Not tracked | Informal lab notes acceptable |
| `v1.0` (first fielded kit) | Characterized reference required per measurand, per deployment class | Enforced; `burn_in_complete` flag required | Admissible if all §C items hold | Within-tolerance cadence tracked | Structured log per §E |
| `v1.5` (trust hardening) | v1.0 plus documented re-verification records | Enforced | Admissible; readings carry calibration-version reference | Versioned offsets; correctable-drift path enforced | Full §E + version field |
| `v2.0` (decision-policy) | v1.5 plus cross-node consistency audits | Enforced | Admissible; plus cross-node bias checks | Retirement thresholds enforced | Full §E + version + bias-audit link |

## Implementation status

| Component | Status | Note |
|---|---|---|
| Reference instrument program (this doc) | `docs-only` | Closes policy gap in G13; concrete reference instruments per node remain to be populated |
| Burn-in gate policy (this doc) | `docs-only` | Closes policy gap in G14; per-node enforcement requires bring-up acceptance updates |
| Admissibility rule in ingest | `planned` | Requires new `admissible_to_calibration_dataset` field on normalized observations; not yet implemented |
| Drift policy in runtime | `planned` | No versioned-offset pipeline today |
| Calibration log format | `partial` | `oesis-builds/procedures/bench-air-node/calibration.md` has a procedure template; §E fields not all captured |

## Gap register references

- **G13** — populate at least one characterized reference instrument per measurand per deployment class (execution of §A).
- **G14** — enforce burn-in gate in bring-up acceptance (execution of §B).
- **G12** — mast-lite must meet this calibration program at `deployment maturity v1.0` before Milestone 2 promotion; covered by the mast-lite build spec and calibration procedure once written.
- **P0** gates in [`../software/inference-engine/hazard-formula-v1-phase1.md`](../../software/inference-engine/hazard-formula-v1-phase1.md) are the hazard-formula-side view of this program; admissibility rule in §C is what those gates are gating.

## Related docs

- [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md) — canonical axes
- [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md) — maturity tiers this program scales with
- [`node-taxonomy.md`](node-taxonomy.md) — node families that inherit this program
- [`sensor-placement-and-representativeness-guide.md`](sensor-placement-and-representativeness-guide.md) — placement classes used in admissibility
- [`../../software/inference-engine/hazard-formula-v1.md`](../../software/inference-engine/hazard-formula-v1.md) — the formula whose coefficient fits depend on admissible data
- [`../../software/inference-engine/hazard-formula-v1-phase1.md`](../../software/inference-engine/hazard-formula-v1-phase1.md) — Phase 0 prerequisites that this program operationalizes
- Cross-repo: per-node calibration procedures at [`oesis-builds/procedures/`](https://github.com/lumenaut-llc/oesis-builds/tree/main/procedures) and build specs at [`oesis-builds/specs/`](https://github.com/lumenaut-llc/oesis-builds/tree/main/specs)
