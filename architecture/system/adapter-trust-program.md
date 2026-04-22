# Adapter Trust Program

## Lane

`system/` lane. Sibling doc to [`calibration-program.md`](calibration-program.md).

This doc defines the trust posture for **adapter-derived** evidence — data obtained through cloud APIs, third-party integrations, or passive inference rather than through a physical sensor owned by the project. It is structured in parallel to `calibration-program.md` so both produce the same final decision (admissibility of a reading to coefficient fitting and to inference) through different evidence paths.

## Purpose

`calibration-program.md` assumes a physical sensor that can be pointed at a characterized reference instrument, burned in, and checked for drift. That model does not apply to:

- cloud-API adapters for third-party devices (Ecobee, Nest, Sensibo, Honeywell, SwitchBot, and similar)
- utility or weather feeds consumed as evidence rather than as context
- passive inference (Tier 1 in the `node-taxonomy.md` tiered acquisition model, for example thermal-slope HVAC inference)

Adapter-derived evidence needs its own trust posture because its failure modes are not physical drift or conditioning — they are API contract changes, schema drift, authentication lapses, source-authority revocation, and upstream transformations invisible to the consumer.

This program defines what trust looks like for that class of evidence, at policy level. Per-adapter execution lives in the adapter's build spec and runbook, analogous to how per-device calibration lives under `oesis-builds/procedures/<node>/`.

## Relation to version axes

Per [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md), this doc touches only the deployment-maturity axis (adapters carry their own maturity) and implementation-status axis. It does **not** introduce a capability-stage label and does not promote accepted runnable slices.

## Relation to capability stage

Adapter-derived evidence is a first-class surface in **capability stage `v1.5`** per [`architecture-gaps-by-stage.md`](architecture-gaps-by-stage.md): equipment-state-adapter, house-state bridge surfaces, and action/outcome logs all rely on adapter-derived data. The nodes and surfaces named there (`equipment-state-adapter`, `circuit-monitor` for Tier 3, `indoor-response-node`) each carry data of different tiers per `node-taxonomy.md`.

Program-phase `v0.2` (bench-air + mast-lite) is Tier 3 only; this program has no gating role in v0.2 promotion. It becomes load-bearing at the `v1.5` bridge and beyond.

## Governing principles

1. **Adapter trust is not sensor calibration.** Different failure modes, different evidence. Shared output (admissibility decision) but independent mechanisms.
2. **Source authority is the anchor.** A physical sensor's anchor is its reference instrument. An adapter's anchor is the **source authority** — the API, account, or derivation rule that produces the data. Changing the source authority re-baselines trust from scratch, the same way a replaced physical sensor re-baselines calibration.
3. **API contract is first-class evidence.** Adapters ship against a pinned version of an external API contract. A silent upstream change without a contract version bump is a trust failure, even if values still arrive.
4. **Cross-check against Tier 3 where possible.** When direct measurement is available for the same parcel, adapter-derived values are cross-checked against it at onboarding and periodically. Divergence triggers reduced trust, not silent acceptance.
5. **Passive inference is the weakest tier.** Tier 1 data (passive inference from existing sensors) is admissible only when the inference method itself is characterized and the derived field carries its method-version reference.

## Program components

### A. Source authority registry

Every adapter-derived measurand must be traceable to a declared **source authority** — the external system or derivation rule producing the data.

For each source authority, the program requires a file under `oesis-builds/procedures/adapters/<adapter>/source.md` with:

- source name (e.g., "Ecobee v1 Developer API")
- authentication model (OAuth2 app, API key, PAT, etc.) and credential scope
- pinned API contract version and effective date
- data fields consumed (mapped to internal measurand names)
- known refresh cadence and rate limits
- documented failure modes (auth revocation, rate limit, API deprecation, schema drift)
- initial cross-check against a Tier 3 reference where applicable (e.g., Ecobee indoor temperature vs indoor-response-node temperature)
- point of contact or SLA if one exists
- last verification date

Passive inference methods (Tier 1) are treated as source authorities too: the **method itself** is the source, with a version string and a characterization record.

### B. Onboarding gate

Before any adapter's data is admissible, it must clear:

- schema validation: the adapter produces the documented fields in the documented types
- authentication validation: credential scope matches declared scope (no over-broad permissions)
- cross-check against Tier 3 where a direct measurement exists for the same parcel and measurand: residual error within the bound declared in the adapter's build spec
- documented initial verification record under `procedures/adapters/<adapter>/verification/<parcel_id>-<date>.md`

For passive inference, the onboarding gate is a **method characterization**: documented derivation, expected accuracy bounds, known failure modes, and the test set against which bounds were measured.

### C. Admissibility

An adapter-derived reading is admissible to the calibration dataset and to inference only if all of the following hold:

1. **Source authority registered.** A current source file exists under section A.
2. **API contract version matches pinned version.** Runtime compares the adapter's reported contract version to the pinned version; mismatches produce `contract_version_drift` inadmissibility.
3. **Onboarding gate passed for this parcel.** Cross-check and initial verification on record for this specific parcel.
4. **Credentials current.** Adapter authentication has not expired or been revoked since last verification.
5. **Cadence honored.** Readings arrive within the documented refresh cadence; stale readings beyond a configured freshness window are inadmissible.
6. **Tier-appropriate confidence.** Tier 2 (cloud adapter) readings may be primary when Tier 3 is unavailable. Tier 1 (passive inference) readings are admissible only to the inference fields the method is characterized for; they are not admissible as direct-measurement substitutes.
7. **Source-derived uncertainty within bounds.** If the adapter provides its own uncertainty or confidence field, the value falls within the bound declared in the adapter's build spec.
8. **No open adapter incident.** The source authority has no open incident or deprecation notice that would invalidate readings in the observation's window.

Admissibility decision is computed in runtime; facts required to compute it are carried on the normalized observation. The canonical fact set parallels the schema additions for physical sensors in [`calibration-program.md`](calibration-program.md) §C:

- `adapter_source_ref: string` — pointer to the source file under section A
- `adapter_contract_version: string` — version string the reading was produced against
- `adapter_onboarding_ref: string` — pointer to the parcel's initial verification record
- `adapter_credential_last_verified_at: timestamp`
- `adapter_tier: enum` — one of `tier_1_passive`, `tier_2_adapter`, `tier_3_direct` per `node-taxonomy.md`

Runtime produces the same-shape outputs as calibration-program §C:

- `admissible_to_calibration_dataset: bool`
- `admissibility_reasons: [string]` with adapter-specific reason codes (`contract_version_drift`, `credentials_expired`, `onboarding_missing`, `cadence_stale`, `source_incident_open`, `tier_insufficient`)

**Inadmissible ≠ discarded.** Inadmissible adapter readings remain in raw logs for audit and for future re-processing if the source authority's posture is restored.

### D. Drift policy

Adapter drift is different from sensor drift. Three failure modes, with response tiers:

- **Silent schema drift.** API returns same field names with changed semantics. Caught by periodic cross-check against Tier 3 where available, or by manual audit. Response: suspend admissibility for affected measurand until source file is updated and onboarding gate re-passed.
- **Contract version bump.** API provider announces new version. Response: verify the pinned version in the source file; re-run onboarding gate against the new version; update pinned version only after cross-check passes.
- **Source authority revocation or deprecation.** Credential revoked, account suspended, or API sunset. Response: immediate inadmissibility for all readings from that source; remediation is source-dependent (new auth, migration to successor API, or adapter retirement).

Specific thresholds for cross-check tolerance and revocation cadences live in each adapter's build spec, not in this doc.

### E. Adapter session log format

Each adapter-verification session produces a record with at minimum:

- session timestamp (UTC)
- adapter identity (source name, contract version, credential scope)
- parcel this verification applies to
- measurand(s) verified
- raw adapter reading(s) and raw Tier 3 reference reading(s) where available
- residual error against reference if applicable
- session outcome: `pass`, `cross-check drift`, `schema drift`, `credential failure`, `source incident`
- operator identity
- next re-verification due date

Verification logs live alongside the parcel's install metadata and the adapter's build spec. They are authoritative when admissibility checks reference "this adapter's current verification state on this parcel."

### F. Build-spec metadata block

Every adapter configuration in `oesis-builds/specs/adapters/<adapter>/v0-X.md` carries a front-matter metadata block, parallel in shape to calibration-program §F:

```yaml
---
adapter_family: <string, e.g. "ecobee-adapter">
build_version: <string, e.g. "v0-1">
tier: tier_1_passive | tier_2_adapter | tier_3_direct
source_authority_ref: <path to source file under oesis-builds/procedures/adapters/<adapter>/source.md>
pinned_contract_version: <string>
measurands:
  - name: <e.g. "hvac_mode">
    source_field: <e.g. "runtime.equipmentStatus">
    expected_type: <e.g. "enum">
    uncertainty_bound: <adapter-declared confidence>
    tier_3_cross_check_ref: <path to Tier 3 cross-check procedure if applicable, else null>
  - name: <next measurand>
    ...
onboarding_requirements:
  cross_check_against_tier_3: true | false
  initial_verification_window_hours: <number>
credential_model:
  type: oauth2 | api_key | pat
  scope: <string>
  refresh_cadence_hours: <number or null>
deployment_maturity_target: v0.1 | v1.0 | v1.5 | v2.0
adapter_trust_program_revision: <commit hash or date>
---
```

The block is consumed by the same (future, planned) admissibility tooling that reads the calibration-program §F block for physical sensors. Both feed the same decision; the tooling branches on which program's rules apply per the `tier` field.

### G. Promotion-bar compliance

Adapter-derived evidence participates in slice promotion (per [`../current/pre-1.0-version-progression.md`](../current/pre-1.0-version-progression.md) item 5) under this program, not under calibration-program. Per-tier compliance:

- **`v0.1` (bench prototype):** build-spec metadata block (§F) exists; cross-check and onboarding may be informal.
- **`v1.0` (first fielded kit):** all components §A–§F complete; onboarding gate enforced per parcel; Tier 3 cross-check on record where applicable.
- **`v1.5` (trust hardening):** §A–§F complete; verification logs versioned; schema-drift detection active; source-incident watch on record.
- **`v2.0` (decision-policy):** §A–§F complete; cross-adapter consistency audit on record; retirement and replacement paths documented.

Slice promotions that include adapter-derived evidence (earliest: capability stage `v1.5` bridge surfaces) inherit these tiers through the promotion bar.

## Maturity ladder mapping

Same tier labels as `calibration-program.md`, applied to adapters rather than sensors:

| Deployment maturity | Source registry | Onboarding gate | Admissibility | Drift policy | Log format |
|---|---|---|---|---|---|
| `v0.1` | Best-available; may be uncharacterized | Informal | Not admissible to coefficient fits | Not tracked | Informal lab notes |
| `v1.0` | Characterized per measurand | Enforced per parcel | Admissible if all §C items hold | Cross-check cadence tracked | Structured log per §E |
| `v1.5` | v1.0 plus versioned verification records | Enforced | Admissible; readings carry contract-version reference | Schema-drift detection; versioned onboarding | Full §E + version field |
| `v2.0` | v1.5 plus cross-adapter consistency audits | Enforced | Admissible; plus cross-adapter bias checks | Retirement and replacement paths enforced | Full §E + version + audit link |

## Implementation status

| Component | Status | Note |
|---|---|---|
| Source authority registry | `planned` | No adapter exists in v0.2 scope |
| Onboarding gate | `planned` | Requires at least one adapter build to exercise |
| Admissibility rule | `planned` | Shares runtime plumbing with calibration-program §C (G15) |
| Drift policy | `planned` | Schema-drift detection is novel surface |
| Adapter session log format | `docs-only` | Format defined; no logs yet |
| Build-spec metadata block | `docs-only` | §F defined here; no adapter spec files exist |

## Gap register references

- **G15** — admissibility tooling runtime wiring is shared between calibration-program and adapter-trust-program; the tooling branches by tier.
- **G18** — adapter-trust-program exists as policy; concrete adapter builds, registries, and verification records are future work gated by capability stage `v1.5`.
- Capability-stage work for `v1.5` bridge surfaces (indoor-response-node, equipment-state-adapter, circuit-monitor) in `phase-roadmap.md` and `architecture-gaps-by-stage.md` depends on this program being in place.

## Related docs

- [`calibration-program.md`](calibration-program.md) — sibling program for physical-sensor trust; same output shape
- [`node-taxonomy.md`](node-taxonomy.md) — Tier 1/2/3 acquisition model; bridge surfaces
- [`deployment-maturity-ladder.md`](deployment-maturity-ladder.md) — maturity tiers this program scales with
- [`version-and-promotion-matrix.md`](version-and-promotion-matrix.md) — canonical axes
- [`architecture-gaps-by-stage.md`](architecture-gaps-by-stage.md) — capability-stage placement
- [`../current/pre-1.0-version-progression.md`](../current/pre-1.0-version-progression.md) — slice promotion bar
- Cross-repo: per-adapter specs at [`oesis-builds/specs/adapters/`](https://github.com/lumenaut-llc/oesis-builds/tree/main/specs) and procedures at [`oesis-builds/procedures/adapters/`](https://github.com/lumenaut-llc/oesis-builds/tree/main/procedures) when these come into existence
