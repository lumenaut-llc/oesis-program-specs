# Proposal — Integrate calibration-program references into oesis-builds

## Status

Proposal. Drafted 2026-04-19. To be applied by the user via the oesis-builds build-vault agent, per the vault-scope rule in `oesis-builds/CLAUDE.md` ("Writes allowed ONLY under oesis-builds/").

## Why this is a proposal, not an edit

`oesis-builds/CLAUDE.md` explicitly scopes that vault's writes to itself:

> **Writes allowed ONLY under `oesis-builds/`.**
> **No writes to `oesis-hardware/`**, `oesis-wiki/`, `oesis-runtime/`, `oesis-program-specs/`, `oesis-contracts/`, or any other sibling.

The symmetric implication — that external agents should respect the vault's ownership of its own content — is sound. This doc captures the edits needed so the build-vault agent (or the user directly) can apply them cleanly.

## Why these edits are needed

Master architecture in `oesis-program-specs` now has:

- `architecture/system/calibration-program.md` — reference instrument program, burn-in gates, admissibility rule, drift policy, §F build-spec metadata block, §G promotion-bar compliance
- `architecture/system/adapter-trust-program.md` — parallel program for Tier 1 / Tier 2 adapter-derived data
- `architecture/system/deployment-maturity-ladder.md` — extended with power / IP / transport tier per deployment class
- `architecture/system/sensor-placement-and-representativeness-guide.md` — extended with sensor variant selection principles
- `architecture/system/calibration-program.md` §F — structured build-spec front-matter block that node specs must declare

The oesis-builds vault is the **execution site** for calibration-program policy. Its `specs/`, `procedures/`, and `references/` directories are where the policy is exercised. Today the vault is aware of calibration infrastructure in a general way (the `references/` directory exists, calibration procedures exist) but does not reference the upstream program doc as the policy source.

## Specific edits proposed

### Edit 1 — `oesis-builds/README.md`

**Anchor:** after the "Accuracy posture (Part E gates)" section.

**Add:** new section —

```markdown
## Relationship to calibration program (upstream policy)

The seven Part E gates above are this vault's **execution** of policy defined upstream in [`oesis-program-specs/architecture/system/calibration-program.md`](../oesis-program-specs/architecture/system/calibration-program.md). That program doc is canonical for:

- What a "characterized reference" means (§A source of truth for reference instrument files under `references/`)
- Burn-in gate policy per sensor family (§B — 48 h for BME680 / BME688 is the platform default)
- Admissibility rule — whether a unit's readings can train hazard-formula coefficients or shape parcel-state claims (§C)
- Drift response and retirement thresholds (§D)
- Calibration log format (§E)
- Build-spec §F metadata block — required front-matter in every `specs/<node>/v0-X.md` file
- Promotion-bar compliance per deployment-maturity tier (§G)

Adapter-derived evidence (Tier 1 passive inference, Tier 2 cloud-API adapters) is governed by the parallel [`adapter-trust-program.md`](../oesis-program-specs/architecture/system/adapter-trust-program.md). Physical sensor nodes in this vault follow calibration-program; any adapter specs that eventually land under `specs/adapters/` follow adapter-trust-program.

Deployment-class standards (power tier, IP tier, transport tier) live in [`deployment-maturity-ladder.md`](../oesis-program-specs/architecture/system/deployment-maturity-ladder.md) "Deployment-class standards". Sensor variant selection principles live in [`sensor-placement-and-representativeness-guide.md`](../oesis-program-specs/architecture/system/sensor-placement-and-representativeness-guide.md).
```

### Edit 2 — `oesis-builds/GUIDE.md`

**Anchor:** in Phase 0 "What to order" subsection, after the "Also order" bullet about reference instruments.

**Add:** a note —

```markdown
The reference instrument program is defined upstream in [`calibration-program.md`](../oesis-program-specs/architecture/system/calibration-program.md) §A. Every reference instrument file under `references/<slug>.md` must satisfy the minimum fields named there (make, model, serial, accuracy statement, traceability chain, last verification date). The `calibrate` command refuses to run against a file that doesn't meet the schema.
```

### Edit 3 — `oesis-builds/CLAUDE.md`

**Anchor:** extend the `calibrate` command description's reference instrument rule.

**Replace:**

```markdown
### `calibrate <unit> [--reference <ref-slug>]`
Walk `procedures/<node>/calibration.md`. Require a **characterized reference**: refuse if `references/<ref-slug>.md` is missing, is `TBD.md`, has `status: placeholder`, or has unpopulated accuracy fields for the parameters being calibrated. Record: date, procedure version, reference instrument (`[[references/...]]`), computed correction factors **interpreted against the spec's Uncertainty Budget** (not hardcoded thresholds), ambient conditions. Append to the Calibration section of `unit.md`. Append to the reference's `## Used by` list. A unit cannot move to `status: calibrated` unless calibration gates pass or are explicitly waived.
```

**With:**

```markdown
### `calibrate <unit> [--reference <ref-slug>]`
Walk `procedures/<node>/calibration.md`. Require a **characterized reference** per [`calibration-program.md`](../oesis-program-specs/architecture/system/calibration-program.md) §A: refuse if `references/<ref-slug>.md` is missing, is `TBD.md`, has `status: placeholder`, or has unpopulated accuracy fields for the parameters being calibrated. The minimum-fields schema (make, model, serial, accuracy statement, traceability chain, last verification date) comes from calibration-program §A and is the contract the reference file must satisfy.

Record: date, procedure version, reference instrument (`[[references/...]]`), computed correction factors **interpreted against the spec's Uncertainty Budget** (not hardcoded thresholds), ambient conditions. Append to the Calibration section of `unit.md`. Append to the reference's `## Used by` list. A unit cannot move to `status: calibrated` unless calibration gates pass or are explicitly waived.

Calibration session log format follows [`calibration-program.md`](../oesis-program-specs/architecture/system/calibration-program.md) §E. Admissibility of the session's resulting readings to the OESIS calibration dataset is governed by calibration-program §C.
```

### Edit 4 — `oesis-builds/specs/bench-air-node/v0-1.md` (addresses G16)

**Anchor:** front-matter — add a new YAML block at the top of the file per calibration-program §F schema.

**Add:**

```yaml
---
node_family: bench-air-node
build_version: v0-1
deployment_class: indoor
deployment_maturity_target: v1.0
measurands:
  - name: temperature_c
    sensor_variant: sht45-breakout-adafruit-5665
    accuracy_statement: "±0.1 °C, 0–60 °C (per Sensirion datasheet)"
    reference_instrument_ref: references/TBD.md  # tracked as G13
  - name: relative_humidity_pct
    sensor_variant: sht45-breakout-adafruit-5665
    accuracy_statement: "±1.0 %RH, 0–100 %RH (per Sensirion datasheet)"
    reference_instrument_ref: references/TBD.md  # tracked as G13
  - name: gas_resistance_ohm
    sensor_variant: bme680-breakout-adafruit-3660
    accuracy_statement: "no absolute accuracy floor; repeatability-gated by burn-in"
    reference_instrument_ref: null  # gas-resistance reference deferred; see calibration-program §A
burn_in:
  required: true
  window_hours: 48  # BME680 platform default per calibration-program §B
protective_fixtures: []  # indoor-only; no shield required
transport:
  primary: serial  # v0.1 floor per G3
  permitted_fallbacks: []
power:
  source: usb
  protection:
    - "reverse-polarity protection (regulator-inherent)"
calibration_program_revision: "2026-04-19"
---
```

Rationale: v0.1 sign-off is not reopened; this front-matter block is a forward-looking declaration for v0.2 promotion per the retroactivity rule in `pre-1.0-version-progression.md`.

### Edit 5 — `oesis-builds/procedures/bench-air-node/bring-up.md` (addresses G20)

**Anchor:** in the acceptance-tests section, add a burn-in gate item.

**Add:** a pass/fail item —

```markdown
- [ ] **Burn-in complete (calibration-program §B):** device has been powered for at least 48 continuous hours before this acceptance check, OR this unit is flagged `burn_in_complete: false` in the ingest pipeline and will not be admitted to the calibration dataset until the window elapses. Burn-in state is recorded in `build-log.md`.
```

## Application via build-vault agent

To apply these edits via the build-vault agent:

```bash
cd oesis-builds
claude
> Apply the five edits in ../oesis-program-specs/meta/proposals/oesis-builds-calibration-program-integration.md. For each edit: read the anchor, add the proposed content exactly as written, record the application in log.md. For edit 4 (bench-air §F block), append a dated entry to decisions/ noting the forward-looking declaration per calibration-program §F.
```

The build-vault agent will respect the append-only / frozen-specs rules and produce a decision entry for the bench-air §F block change as required by the vault's own rules.

## Status after application

- G16 (bench-air §F block missing) → addressed by edit 4
- G20 (bring-up doesn't enforce §B burn-in) → addressed by edit 5 at procedure level; full enforcement still requires ingest-side `burn_in_complete` flag wiring (G14 / G15)
- G13 (reference instrument placeholder) → unchanged; edit 4's `references/TBD.md` pointer makes the dependency explicit but does not resolve it
- Build-vault is now aware of calibration-program as the upstream policy source

## Related

- [`oesis-program-specs/architecture/system/calibration-program.md`](../../architecture/system/calibration-program.md)
- [`oesis-program-specs/architecture/system/adapter-trust-program.md`](../../architecture/system/adapter-trust-program.md)
- [`oesis-program-specs/release/v.0.1/v0.1-gap-register.md`](../../release/v.0.1/v0.1-gap-register.md) — G12 through G24
- `oesis-builds/CLAUDE.md` — vault-scope rules
