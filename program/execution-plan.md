# OESIS Program Execution Plan

## Purpose

Single document that maps the full build sequence from current position through
v1.5, connecting version slices, capability stages, milestones, blocker counts,
implementation status, and technical work items across all four repositories.

This is the document to read when you need to answer: **where are we, what's
next, and what does the full path look like?**

## Current position

**Date:** 2026-04-15

The oesis-runtime has implemented lane-specific code and acceptance tests for
v0.1 through v1.0. All offline acceptance commands pass:

| Command | Result | What it proves |
|---------|--------|----------------|
| `make oesis-accept` | **PASS** | v0.1 baseline: one parcel, one bench-air, full pipeline |
| `make oesis-v02-accept` | **PASS** | v0.2: indoor + outdoor (2 nodes), evidence source mix |
| `make oesis-v03-accept` | **PASS** | v0.3: flood-capable (3 nodes), flood observation normalization |
| `make oesis-v04-accept` | **PASS** | v0.4: multi-node registry lifecycle (3 observations, 3 active nodes) |
| `make oesis-v05-accept` | **PASS** | v0.5: governance (consent + retention + export + revocation) |
| `make oesis-v10-accept` | **PASS** | v1.0: extended support objects (house state, intervention, verification) |

**Important caveat:** These acceptance tests are **structural smoke tests**.
They verify that the pipeline executes without error and that output data
structures contain all required fields. They do **not** assert inference
correctness (e.g., that a high PM2.5 reading produces a specific shelter
status), behavioral edge cases, or HTTP-level governance enforcement. The
distinction between "acceptance test passes" and "fully promoted" matters.

### What's genuinely implemented in the runtime

| Capability | Status | Evidence |
|-----------|--------|----------|
| Bench-air packet normalization | **Implemented** | v0.1 baseline, acceptance-gated |
| Mast-lite packet normalization | **Implemented** | v0.2 lane, shared lineage with outdoor metadata |
| Flood packet normalization | **Implemented** | v0.3 lane, `normalize_flood_packet.py` |
| Weather-PM packet normalization | **Implemented** | Ingest handles `oesis.weather-pm-mast.v1` |
| Circuit-monitor normalization | **Implemented** | Equipment-state bridge |
| Two-source inference (indoor + outdoor + public) | **Implemented** | v0.2 lane |
| Flood condition derivation (water depth, rise rate) | **Implemented** | v0.3 lane, hazard thresholds config |
| Node registry lifecycle (validate, filter, bind) | **Implemented** | v0.4 lane, `manage_node_registry.py` |
| Multi-node evidence composition | **Implemented** | v0.4 lane, `compose_multi_node_evidence()` |
| Calibration state enforcement | **Implemented** | v0.4 lane, provisional/verified/recently_calibrated |
| Consent store (append-only lifecycle) | **Implemented** | v0.5 lane, atomic JSON persistence |
| Sharing store (operator preferences) | **Implemented** | v0.5 lane |
| Consent enforcement (query-time gate) | **Implemented** | v0.5 lane, data class governance |
| Revocation (mark-not-delete) | **Implemented** | v0.5 lane, `revoked_at` stops sharing |
| Structurally private data rejection | **Implemented** | v0.5 lane, 9 private-by-default classes |
| Retention cleanup (auditable) | **Implemented** | v0.5 lane, `run_retention_cleanup.py` |
| Export bundle generation | **Implemented** | v0.5 lane |
| Operator access logging | **Implemented** | v0.5 lane, access event records |
| Rights request processing | **Implemented** | v0.5 lane, `process_rights_requests.py` |
| Shared map with consent gating | **Implemented** | v0.5 lane, `aggregate_shared_map.py` |
| Custody tier enforcement | **Implemented** | v0.5 lane, eligibility checks |
| Minimum participation threshold | **Implemented** | v0.5 lane, k-anonymity suppression |
| House state as inference input | **Implemented** | v1.0 lane, fallback PM2.5 from indoor response |
| Intervention event tracking | **Implemented** | v1.0 lane, action logs with verification windows |
| Verification outcome adjustment | **Implemented** | v1.0 lane, +0.03 smoke prob if worsened, +0.02 confidence |
| Closed-loop summaries | **Implemented** | v1.0 lane, PM2.5 delta tracking |
| Contrastive explanations | **Implemented** | v1.0 lane, public-only counterfactual |
| Divergence analysis | **Implemented** | v1.0 lane, local vs public disagreement |

### What's NOT implemented (genuine remaining gaps)

| Gap | Status | Needed for |
|-----|--------|------------|
| ~~Trust scoring computation~~ | **Resolved** — `compute_trust_score.py` with 5-factor model | ~~v1.0~~ |
| ~~Inference correctness assertions~~ | **Resolved** — value-level assertions in all acceptance tests | ~~All versions~~ |
| HTTP-level governance enforcement testing | **Not tested** — consent tested at API level only | v0.5, v1.0 |
| Live public weather/smoke feeds with API keys | **Not implemented** — uses fixture data | v1.0 Tier B |
| Ingest authorization for live nodes | **Not implemented** — serial capture only | v1.0 Tier B |
| Wi-Fi transport with TLS | **Not implemented** | v1.0 Tier B |
| Mast-lite independent build reproduction | **Not verified** — guide exists, not independently confirmed | v0.2 hardware |
| Flood-node independent build reproduction | **Not verified** — guide exists, not independently confirmed | v0.3 hardware |
| Flood-node field calibration validation | **Not verified** — provisional calibration only | v0.3 hardware |
| Named BOM vendor decisions | **Not done** — docs-only | v1.0 Tier B |
| Installation metadata guided input surface | **Not implemented** — loaded from examples, no operator UI | v1.0 |
| Append-only observation/state history | **Not implemented** — snapshot-oriented | v1.0 |
| Claims and safety language review | **Not done** — standards documented, not participant-reviewed | v1.0 Tier B |
| Deployment-quality flags in user-facing view | **Partial** — tracked in registry, not fully surfaced | v1.0 |
| Evidence summaries in user-facing view | **Partial** — JSON output, not dedicated UI | v1.0 |
| Sharing settings UI | **Not implemented** — API exists, no product surface | v1.0 |

---

## Version → milestone → capability stage mapping

| Version | Milestone | Capability stage | Theme | Software status | Hardware status |
|---------|-----------|-----------------|-------|----------------|-----------------|
| **v0.1** | M1: One parcel, one node | Current v1 (Stage A) | Prove the parcel view | **Acceptance passes** | bench-air implemented |
| **v0.2** | M2: First integrated parcel kit | Current v1 (Stage A) | Two-node kit | **Acceptance passes** | mast-lite build not independently verified |
| **v0.3** | M3: Hazard-module expansion | Current v1 (Stage A) | Flood observation family | **Acceptance passes** | flood-node build not independently verified |
| **v0.4** | M3–M4 bridge | Current v1 (Stage A) | Registry lifecycle + evidence quality | **Acceptance passes** | — |
| **v0.5** | M5 (partial) | Current v1 (Stage A) | Governance enforcement | **Acceptance passes** | — |
| **v1.0** | M2–M5 complete | Current v1 (Stage A) exit | Fielded parcel-intelligence lane | **Acceptance passes** (structural) | Field hardening not done |
| **v1.5** | — | Stage B | Measurement-to-intervention bridge | **Not started** | Not started |

---

## Full sequence: current state and remaining work

### v0.1 — One parcel, one bench-air, one pipeline ✅

**Status:** Promoted. Reference pipeline acceptance-gated.

All v0.1 surfaces implemented: bench-air normalization, single-source inference,
parcel view with confidence/evidence mode/reasons, private-by-default boundary.

---

### v0.2 — Two-node kit: indoor + sheltered outdoor

**Sign-off:** bench-air + mast-lite bound to one parcel, both streams
normalized and combined, parcel view explains source mix.

**Software: acceptance passes.** Runtime implements mast-lite normalization,
two-node parcel context, evidence source mix tracking.

| Surface | Previous status | Current status |
|---------|----------------|----------------|
| Mast-lite packet normalization | partial | **Implemented** — acceptance-gated |
| Node registry two-node binding | partial | **Implemented** — node_installations validated |
| Two-source inference | planned | **Implemented** — indoor + outdoor + public combined |
| Parcel view source attribution | planned | **Implemented** — evidence_source_nodes populated |
| v0.1 regression | implemented | **Implemented** |

**Remaining gaps for full v0.2 promotion:**

| Gap | Type | Status |
|-----|------|--------|
| Mast-lite independent build reproduction | Hardware | **Open** — guide exists; not independently confirmed |
| ~~Inference correctness testing~~ | Testing | **Resolved** — value-level assertions added |

---

### v0.3 — Flood-capable runtime

**Sign-off:** flood-node observations normalized, flood conditions in parcel-state.

**Software: acceptance passes.** Runtime implements flood packet normalization,
flood hazard derivation (water depth bands, rise rate bands, calibration penalty),
three-node registry binding.

| Surface | Previous status | Current status |
|---------|----------------|----------------|
| Flood observation normalization | docs-only | **Implemented** — `normalize_flood_packet.py`, strict field validation |
| Three-node registry binding | docs-only | **Implemented** — acceptance validates flood-node-01 in parcel context |
| Flood condition derivation | planned | **Implemented** — water_depth_cm, rise_rate_cm_per_hr, calibration_state |
| Parcel view flood attribution | planned | **Implemented** — observation_type checked |
| v0.2 regression | partial | **Implemented** |

**Remaining gaps for full v0.3 promotion:**

| Gap | Type | Status |
|-----|------|--------|
| Flood-node independent build reproduction | Hardware | **Open** — guide exists; not independently confirmed |
| Flood-node field calibration validation | Hardware | **Open** — provisional calibration only |
| ~~Inference correctness testing (flood)~~ | Testing | **Resolved** — value-level assertions added |

---

### v0.4 — Registry lifecycle + evidence composition

**Sign-off:** mature node lifecycle, installation metadata, evidence
composition weighting, deployment-quality flags.

**Software: acceptance passes.** Runtime implements node registry lifecycle
(validate, filter active, bind metadata), multi-node evidence composition with
calibration weighting, source diversity tracking.

| Surface | Previous status | Current status |
|---------|----------------|----------------|
| Node registry lifecycle | partial | **Implemented** — load, validate, filter, bind |
| Installation metadata capture | docs-only | **Partial** — loaded from fixture; no guided input surface |
| Evidence composition weighting | planned | **Implemented** — `compose_multi_node_evidence()` |
| Deployment-quality flags | planned | **Partial** — calibration_state in registry; not surfaced in parcel view UI |
| Node replacement continuity | planned | **Implemented** — disabled nodes filtered from active set |
| Explanation weighting rationale | planned | **Implemented** — evidence contributions include weights |
| v0.3 regression | partial | **Implemented** |

**Remaining gaps for full v0.4 promotion:**

| Gap | Type | Status |
|-----|------|--------|
| Installation metadata guided input | Product | **Open** — no operator-facing capture surface |
| Deployment-quality flags in user view | Product | **Open** — tracked internally but not user-visible |
| ~~Quality-based weighting correctness~~ | Testing | **Resolved** — value-level assertions added |

---

### v0.5 — Governance enforcement

**Sign-off:** consent gates sharing, revocation stops it, retention has owners,
export produces auditable output.

**Software: acceptance passes.** Runtime implements full consent lifecycle,
revocation with mark-not-delete, data class governance (9 structurally private
classes), shared map with consent gating and minimum participation threshold,
retention cleanup, export bundles, rights request processing, operator access
logging.

| Surface | Previous status | Current status |
|---------|----------------|----------------|
| Consent enforcement (query-time gate) | docs-only | **Implemented** — data class governance, eligibility checks |
| Revocation behavior | docs-only | **Implemented** — `revoked_at` stops future sharing |
| Retention cleanup | partial | **Implemented** — time-based pruning with audit report |
| Export bundle | partial | **Implemented** — parcel export with metadata |
| Operator access logging | partial | **Implemented** — access events with actor/action/justification |
| Sharing settings surface | docs-only | **Implemented** — API-level; no product UI |
| Consent store | docs-only | **Implemented** — append-only JSON with thread-safe persistence |
| Rights request processing | partial | **Implemented** — delete request execution with audit trail |
| Custody tier enforcement | docs-only | **Implemented** — eligibility checks in shared map |
| End-to-end governance lifecycle | planned | **Implemented** — acceptance test exercises full cycle |
| v0.4 regression | partial | **Implemented** |

**Remaining gaps for full v0.5 promotion:**

| Gap | Type | Status |
|-----|------|--------|
| HTTP-level governance enforcement testing | Testing | **Open** — consent tested at store level only |
| Sharing settings product UI | Product | **Open** — API exists but no operator-facing surface |
| Governance enforcement under concurrent access | Testing | **Open** — thread locks exist but no stress test |

---

### v1.0 — Fielded parcel-intelligence lane

**Sign-off:** first materially broader system beyond v0.1 — trust scoring,
deployment-quality flags, evidence summaries, basic sharing settings, consent
enforcement, house state, intervention tracking, verification outcomes.

**Software: acceptance passes (structural).** Runtime implements house state as
inference input (fallback PM2.5), intervention event tracking (action logs with
verification windows), verification outcome adjustment (+0.03 smoke probability
if worsened, +0.02 confidence for non-inconclusive), closed-loop summaries,
contrastive explanations, divergence analysis.

**Tier model:** Tier A (internal/controlled pilot) has a lower bar than Tier B
(external pilot with participants).

| Gap | Tier A | Tier B | Current status |
|-----|--------|--------|----------------|
| Trust scoring computation | **Resolved** | **Resolved** | **Implemented** — `compute_trust_score.py` integrated |
| Mast-lite field hardening | Defer | **Blocker** | **Open** — hardware |
| Ingest authorization for live nodes | Defer | **Blocker** | **Not implemented** |
| Wi-Fi transport with TLS | Defer | **Blocker** | **Not implemented** |
| Live public weather/smoke feeds | Defer | **Blocker** | **Not implemented** — uses fixtures |
| Installation metadata guided input | Defer | **Blocker** | **Not implemented** — no UI |
| Evidence summaries user-facing view | Defer | **Blocker** | **Partial** — JSON, not UI |
| Revocation as product behavior | Defer | **Blocker** | **Implemented** at API level |
| Sharing/consent as product behavior | Defer | **Blocker** | **Implemented** at API level |
| Named BOM vendor decisions | Defer | **Blocker** | **Not done** |
| Claims/safety language review | Defer | **Blocker** | **Not done** |
| Append-only observation history | Defer | Defer | **Not implemented** |
| Deployment-quality flags in view | Defer | **Blocker** | **Partial** — tracked, not surfaced |
| Shared-map aggregate with policy | Defer | Defer | **Implemented** — consent-gated |
| Node registry full lifecycle | **Resolved** | **Resolved** | **Implemented** in v0.4 |

**Remaining work for v1.0 Tier A (internal pilot):**
1. ~~Implement trust scoring computation~~ — **Resolved**: `compute_trust_score.py` with 5-factor model integrated into `infer_parcel_state.py`
2. ~~Add inference correctness test assertions~~ — **Resolved**: value-level assertions added to all acceptance tests (v0.1–v1.0); confidence range, status enums, hazard probability range, evidence mode, freshness, trust score structure

**Additional work for v1.0 Tier B (external pilot):**
3. Implement ingest authorization for live nodes
4. Implement Wi-Fi transport with TLS, identity, retries
5. Integrate live public weather/smoke feeds with API keys and fallback
6. Build installation metadata guided input surface
7. Build user-facing evidence view (beyond JSON summary)
8. Build sharing settings product UI
9. Complete mast-lite field hardening (hardware)
10. Named BOM vendor decisions and procurement path
11. Claims and safety language review for participant materials

---

### v1.5 — Measurement-to-intervention bridge

**Sign-off:** proves minimum bridge from parcel sensing into response reasoning
— one honest closed loop of `hazard → house state → action → measured outcome`.

**Status: partially implemented.** The v1.0 runtime already accepts house_state,
intervention_event, and verification_outcome as inference inputs and uses them
to modify hazard probabilities and confidence. Closed-loop summaries track
PM2.5 deltas and improvement metrics.

**What exists (from v1.0 lane):**
- House state as fallback PM2.5 source
- House capability influence on smoke probability (+0.01 if recirculation available)
- Intervention event → action logs with verification window timing
- Verification outcome → smoke probability adjustment, confidence boost
- Closed-loop summary with before/after PM2.5 deltas and improvement ratios

**What's still needed for v1.5 exit criteria:**
- indoor-response-node hardware (planned)
- power-outage-node hardware (planned)
- equipment-state-adapter hardware (planned)
- Building and site metadata capture (planned)
- Real response curve measurement (outdoor PM → indoor PM over time)
- One verified closed-loop chain with real sensor data (not fixtures)

---

## Beyond v1.5: capability stages C–F

| Stage | Version | Theme | Key additions |
|-------|---------|-------|---------------|
| C | v2 | Bounded adaptation guidance | Condition model, building response model, intervention ranking |
| D | v2.5 | Bounded controls + compatibility | Controls inventory, compatibility surfaces, three-tier integration |
| E | v3 | Parcel adaptation engine | Time-to-threshold, compound hazard, action-effect memory |
| F | v4 | Parcel + route + block resilience | Route/egress layer, neighborhood weak-point layer |

---

## Deployment maturity (separate axis)

| Maturity | Bar | Current node status |
|----------|-----|---------------------|
| v0.1 (bench) | Prototype, provisional calibration | bench-air ✅, mast-lite (early prototype), flood-node (early prototype) |
| v1.0 (field-ready) | Protected power, buffering, connectorized wiring, enclosure, identity, service access | No node yet meets this bar |
| v1.5 (trust-hardened) | Device-ops, calibration versioning, maintenance-informed trust | — |
| v2.0 (policy-aware) | Decision-policy and adaptation support | — |

---

## Acceptance test coverage honesty

The acceptance tests now verify **pipeline execution, data structure
completeness, and value-level correctness** including:

- ✅ Confidence range [0, 1]
- ✅ Status enum validation (safe, watch, warning, danger, unknown, not_assessed)
- ✅ Evidence mode validation
- ✅ Hazard probability range [0, 1]
- ✅ Freshness non-negative
- ✅ Trust score structure and factor validation (v1.0)
- ✅ Flood values physical reasonableness (v0.3+)
- ✅ Registry calibration state enum (v0.4+)
- ✅ Evidence contribution weight ranges (v0.4+)

They still do **NOT** verify:

- Behavioral inference correctness (e.g., "PM2.5 > 150 µg/m³ → shelter_status must not be safe")
- Behavioral edge cases (concurrent revocations, consent re-grants)
- HTTP-level governance enforcement (consent filtering on API responses)
- Performance under load or real-time constraints

---

## Four-repo coordination

| Repository | Role | Version alignment |
|-----------|------|-------------------|
| **oesis-program-specs** | Specifications, contracts, architecture, release planning | Version lane markers, release packets, acceptance criteria |
| **oesis-runtime** | Python reference implementation | Runtime code, acceptance commands, `make oesis-v0x-accept` |
| **[oesis-hardware](https://github.com/lumenaut-llc/oesis-hardware)** | Sensor node specs, firmware, BOMs, build guides | Hardware maturity tracks deployment maturity ladder; CERN-OHL-S-2.0 / AGPL-3.0 |
| **oesis-public-site** | Next.js public preview | Public-facing materials; follows release-lane publication allowlist |

**Build validation commands** (in oesis-runtime):

| Command | Result | Scope |
|---------|--------|-------|
| `make oesis-validate` | **PASS** | Schema validation (v0.1) |
| `make oesis-check` | **PASS** | Offline reference pipeline (v0.1) |
| `make oesis-http-check` | untested | HTTP smoke test (v0.1) |
| `make oesis-accept` | **PASS** | Offline acceptance (v0.1) |
| `make oesis-v02-accept` | **PASS** | v0.2 indoor + outdoor |
| `make oesis-v03-accept` | **PASS** | v0.3 flood-capable |
| `make oesis-v04-accept` | **PASS** | v0.4 multi-node registry |
| `make oesis-v05-accept` | **PASS** | v0.5 governance |
| `make oesis-v10-accept` | **PASS** | v1.0 extended support objects |

---

## Summary: the honest picture

```
v0.1 ✅ ── v0.2 ✅* ── v0.3 ✅* ── v0.4 ✅* ── v0.5 ✅* ── v1.0 ✅*── v1.5
  │          │           │           │           │           │          │
  │          │           │           │           │           │          └─ needs real
  │          │           │           │           │           │             hardware +
  │          │           │           │           │           │             closed loop
  │          │           │           │           │           │
  │          │           │           │           │           └─ trust scoring ✅;
  │          │           │           │           │              field hardening
  │          │           │           │           │              not done
  │          │           │           │           │
  │          │           │           │           └─ governance
  │          │           │           │              API-level only;
  │          │           │           │              no product UI
  │          │           │           │
  │          │           │           └─ install metadata
  │          │           │              no guided input
  │          │           │
  │          │           └─ flood-node build
  │          │              not independently
  │          │              verified
  │          │
  │          └─ mast-lite build
  │             not independently
  │             verified
  │
  └─ promoted ✅

  ✅* = software acceptance passes (structural);
        hardware and behavioral verification gaps remain
```

**The runtime is much further along than previously documented.** The primary
remaining gaps are:

1. **Hardware verification** — independent build reproductions for mast-lite and flood-node
2. **Product surfaces** — governance works at API level but has no operator-facing UI
3. **Field infrastructure** — no live feeds, no ingest auth, no Wi-Fi transport
4. **HTTP-level governance testing** — consent enforced at store level, not tested on HTTP endpoints
5. **Deployment packaging** — no Docker, systemd, or orchestration configs

---

## Related documents

| Document | Location | Purpose |
|----------|----------|---------|
| Pre-1.0 version progression | `architecture/current/pre-1.0-version-progression.md` | Promotion rules and slice definitions |
| Version and promotion matrix | `architecture/system/version-and-promotion-matrix.md` | Four-axis versioning model |
| Milestone roadmap | `architecture/current/milestone-roadmap.md` | Milestone-to-delivery sequence |
| Phase roadmap | `architecture/system/phase-roadmap.md` | Capability stages A–F |
| Phasing narrative | `program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md` | Program phase detail |
| Deployment maturity ladder | `architecture/system/deployment-maturity-ladder.md` | Hardware field-readiness axis |
| Architecture gaps by stage | `architecture/system/architecture-gaps-by-stage.md` | Gap placement by capability stage |
| Implementation posture | `architecture/current/implementation-posture.md` | Current runtime truth |
| Release lanes | `release/README.md` | Per-version release packets |
| Backlog | `meta/backlog.md` | Immediate and soon-term work items |
