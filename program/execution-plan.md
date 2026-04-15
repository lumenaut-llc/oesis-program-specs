# OESIS Program Execution Plan

## Purpose

Single document that maps the full build sequence from current position through
v1.5, connecting version slices, capability stages, milestones, blocker counts,
implementation status, and technical work items across all three repositories.

This is the document to read when you need to answer: **where are we, what's
next, and what does the full path look like?**

## Current position

**Promoted slice:** v0.1
**Date:** 2026-04-15

v0.1 is the only accepted runnable reference slice. The reference pipeline
(ingest → inference → parcel view) runs end to end for one parcel with one
bench-air node. Acceptance commands pass: `make oesis-validate`,
`make oesis-check`, `make oesis-http-check`.

Everything beyond v0.1 is planned, partial, or docs-only.

---

## Version → milestone → capability stage mapping

| Version | Milestone | Capability stage | Theme | Status |
|---------|-----------|-----------------|-------|--------|
| **v0.1** | M1: One parcel, one node | Current v1 (Stage A) | Prove the parcel view | **Promoted** |
| **v0.2** | M2: First integrated parcel kit | Current v1 (Stage A) | Two-node kit (indoor + outdoor) | Not started |
| **v0.3** | M3: Hazard-module expansion | Current v1 (Stage A) | Flood observation family | Not started |
| **v0.4** | M3–M4 bridge | Current v1 (Stage A) | Registry lifecycle + evidence quality | Not started |
| **v0.5** | M5: Shared neighborhood surface (partial) | Current v1 (Stage A) | Governance enforcement | Not started |
| **v1.0** | M2–M5 complete | Current v1 (Stage A) exit | Fielded parcel-intelligence lane | Not started |
| **v1.5** | — | Stage B | Measurement-to-intervention bridge | Not started |

**Key distinction:** Version slices (v0.x) are promotion gates for the
runnable system boundary. Capability stages (A–F) describe classes of product
behavior. Deployment maturity (bench → field → trust-hardened) is a separate
hardware/ops axis. These three axes are independent.

---

## Full sequence: v0.1 through v1.5

### v0.1 — One parcel, one bench-air, one pipeline ✅

**Sign-off:** One parcel, one bench-air lineage, ingest → inference → parcel
view.

**Status:** Promoted. Reference pipeline implemented and acceptance-gated.

| Area | Status |
|------|--------|
| bench-air-node hardware | Implemented |
| Packet normalization (bench-air) | Implemented |
| Parcel inference (single source + public context) | Implemented |
| Parcel view with confidence, evidence mode, reasons | Implemented |
| Private-by-default architectural boundary | Implemented |
| Acceptance commands (`make oesis-validate/check/http-check`) | Implemented |

**Known v0.1 gaps (carried forward):**

| ID | Gap | Deferred to |
|----|-----|-------------|
| G1 | Named BOM vendors | v1.0 |
| G2 | Ingest authorization for live nodes | v1.0 |
| G3 | Wi-Fi transport with TLS | v1.0 |
| G6 | Governance enforcement | v0.5 |

---

### v0.2 — Two-node kit: indoor + sheltered outdoor

**Sign-off:** bench-air + mast-lite bound to one parcel, both streams
normalized and combined, parcel view explains source mix — without claiming
field-hardened deployment, governance enforcement, or flood/thermal coverage.

**Blockers: 5** | Deferred: 2 | Carry-forward: 3

| ID | Blocker | Owner | Current status |
|----|---------|-------|----------------|
| V02-G1 | Mast-lite normalization: outdoor metadata handling in shared packet lineage | Technical | Partial — uses bench-air lineage; no outdoor-specific handling |
| V02-G2 | Node registry: two-node binding with enable/disable | Technical | Partial — schema exists; lifecycle not exercised |
| V02-G3 | Parcel view: indoor vs outdoor evidence attribution | Technical | Planned — v0.1 view does not distinguish sources |
| V02-G4 | Inference: two-source combination (indoor + outdoor + public) | Technical | Planned — single local source only |
| V02-G5 | Mast-lite bench bring-up: repeatable build and serial capture | Hardware | Partial — build guide exists; not independently reproduced |

**Acceptance command:** `make oesis-v02-accept` (AC-1 through AC-6)

**Technical build sequence (oesis-runtime):**

1. Implement outdoor metadata extraction in ingest normalization for mast-lite packets
2. Implement register/bind/disable flow for two-node parcel in node registry
3. Extend inference engine to weight indoor + sheltered outdoor + public context
4. Add source attribution to parcel view (indoor vs outdoor evidence)
5. Validate mast-lite independent build-and-capture cycle (hardware)
6. Implement `make oesis-v02-accept` acceptance test harness
7. Verify v0.1 regression (`make oesis-validate/check/http-check`)

**Contract boundary changes:**
- Node registry supports `node_class: "outdoor_reference"` alongside `"indoor_air"`
- Parcel-state provenance distinguishes indoor and outdoor local sources
- No breaking schema changes (additive only)

---

### v0.3 — Flood-capable runtime

**Sign-off:** flood-node observations normalized through canonical ingest,
flood conditions reflected in parcel-state — without claiming response logic,
sump monitoring, or intervention surfaces.

**Prerequisite:** v0.2 promoted

**Blockers: 6** | Deferred: 1 | Carry-forward: 3

| ID | Blocker | Owner | Current status |
|----|---------|-------|----------------|
| V03-G1 | Flood observation normalization (`flood.low_point.snapshot`) in ingest | Technical | Planned — serial contract exists; no handler |
| V03-G2 | Flood condition derivation in inference (water depth, rise rate) | Technical | Planned — inference does not consume flood fields |
| V03-G3 | Three-node registry support (indoor + outdoor + flood) | Technical | Partial — schema supports it; not exercised |
| V03-G4 | Parcel view flood evidence display | Technical | Planned — no flood evidence in view |
| V03-G5 | Flood-node independent build reproduction | Hardware | Partial — guide exists; not independently confirmed |
| V03-G6 | Flood-node calibration validation (dry reference + depth derivation) | Hardware | Provisional — documented; not field-validated |

**Acceptance command:** `make oesis-v03-accept` (AC-1 through AC-6)

**Technical build sequence (oesis-runtime):**

1. Implement flood packet handler in ingest service for `oesis.flood-node.v1` schema
2. Extend inference engine with flood condition logic (water_depth_cm, rise_rate_cm_per_hr, calibration_state penalties)
3. Register `node_class: "low_point_flood"` in node registry; validate three-node binding
4. Extend parcel view to attribute flood evidence distinct from air quality evidence
5. Validate flood-node independent build cycle (hardware)
6. Validate flood-node calibration procedure
7. Implement `make oesis-v03-accept`; verify v0.2 regression

**Note:** Flood ingest and inference integration work has been partially
implemented in oesis-runtime (flood observation type added to inference engine,
hazard thresholds configured). The v0.3 promotion still requires the full
acceptance test suite to pass.

**Contract boundary changes:**
- Ingest accepts `oesis.flood-node.v1` schema lineage
- Node registry supports `node_class: "low_point_flood"`
- Parcel-state includes flood-derived condition fields (additive)

---

### v0.4 — Registry lifecycle + evidence composition

**Sign-off:** mature node lifecycle, installation metadata, evidence
composition weighting, deployment-quality flags — without claiming trust
scoring as product surface, governance enforcement, or intervention logic.

**Prerequisite:** v0.3 promoted

**Blockers: 6** | Carry-forward: 4

| ID | Blocker | Owner | Current status |
|----|---------|-------|----------------|
| V04-G1 | Node registry lifecycle: register/bind/disable/replace/retire end-to-end | Technical | Partial — schema CRUD exists; lifecycle not exercised |
| V04-G2 | Installation metadata capture surface (CLI, form, or API) | Technical/Product | Docs-only — contract formalized; no capture path |
| V04-G3 | Evidence composition weighting by source class and quality | Technical | Planned — no quality-weighted inference |
| V04-G4 | Deployment-quality flags in registry and parcel view | Technical | Planned — maturity ladder documented; not in runtime |
| V04-G5 | Node replacement continuity (retire old, bind new, maintain parcel) | Technical | Planned — no reference implementation |
| V04-G6 | Evidence explanation: source weighting rationale in explanation payload | Technical | Planned — explanation exists but no weighting rationale |

**Acceptance command:** `make oesis-v04-accept` (AC-1 through AC-6)

**Technical build sequence (oesis-runtime):**

1. Implement full node lifecycle state machine (active → disabled → retired) with replacement flow
2. Build installation metadata capture surface (structured input for mount type, height, orientation, exposure, power source)
3. Implement quality-weighted evidence composition: source class (indoor > outdoor > public), freshness, deployment grade
4. Add `deployment_grade` field to node registry (bench_grade vs field_ready)
5. Extend parcel view to surface deployment grade per contributing node
6. Extend explanation payload with weighting rationale
7. Implement `make oesis-v04-accept`; verify v0.3 regression

**Contract boundary changes:**
- Node registry adds `lifecycle_state` (active, disabled, retired)
- Node registry adds `deployment_grade` (bench_grade, field_ready)
- Deployment-metadata contract integrated as inference input
- Parcel-state provenance includes source weighting rationale

---

### v0.5 — Governance enforcement

**Sign-off:** consent gates sharing, revocation stops it, retention has owners,
export produces auditable output — without claiming full consumer governance UX,
intervention logic, or trust scoring.

**Prerequisite:** v0.4 promoted

**Blockers: 10** | Carry-forward: 3

| ID | Blocker | Owner | Current status |
|----|---------|-------|----------------|
| V05-G1 | Consent enforcement: sharing path checks consent before emitting data | Technical/Governance | Docs-only — schema exists; no query-time check |
| V05-G2 | Revocation behavior: `revoked_at` reliably stops future sharing | Technical/Governance | Docs-only — mark-not-delete documented; no enforcement |
| V05-G3 | Retention cleanup: schedule with named owners and auditable execution | Operations/Technical | Partial — utility exists; no schedule/owner |
| V05-G4 | Export bundle: complete, schema-validated output | Technical | Partial — reference flow exists; not validated |
| V05-G5 | Operator access logging: all parcel-linked admin actions tracked | Technical | Partial — reference logging; coverage not proven |
| V05-G6 | Sharing settings surface: operator-configurable preferences | Technical/Product | Docs-only — schema exists; no input surface |
| V05-G7 | Consent store: operational append-only lifecycle store | Technical | Docs-only — schema exists; no operational store |
| V05-G8 | Rights request processing: operator-mediated or user-facing | Technical/Product | Partial — admin utility; not user-facing |
| V05-G9 | Custody tier enforcement: query-time eligibility checks | Technical | Docs-only — tiers in schema; no query check |
| V05-G10 | End-to-end acceptance test: consent → share → revoke → verify-stopped | Technical | Planned — no integrated test |

**Acceptance command:** `make oesis-v05-accept` (AC-1 through AC-10)

**Technical build sequence (oesis-runtime):**

1. Implement consent-store as operational append-only store (file-backed or DB-backed)
2. Implement sharing-store with operator-configurable preferences
3. Implement query-time consent enforcement: check scope, data_classes, revoked_at, custody_tier before sharing
4. Implement mark-not-delete revocation (set `revoked_at` → stops future sharing)
5. Implement retention cleanup with auditable report matching schema
6. Implement export bundle pipeline with schema validation
7. Audit and complete operator access logging across all admin routes
8. Implement operator-mediated rights request flow
9. Implement `make oesis-v05-accept` with full lifecycle test (AC-9)
10. Verify v0.4 regression

**Contract boundary changes:**
- consent-store becomes operational runtime surface
- sharing-store becomes operational runtime surface
- Sharing queries enforce consent + revocation + custody_tier at query time
- Retention cleanup produces auditable reports
- Export bundle produces validated output
- Operator access log covers all parcel-linked admin actions

---

### v1.0 — Fielded parcel-intelligence lane

**Sign-off:** first materially broader system beyond v0.1 — mast-lite as
sheltered outdoor node, trust scoring, deployment-quality flags, node registry
binding, installation metadata, evidence summaries, basic sharing settings,
consent enforcement — without claiming full consumer UX, push alerting,
intervention logic, or route/block resilience.

**Prerequisite:** v0.5 promoted (governance must be enforced before broader
system)

**Tier model:** Tier A (internal/controlled pilot) has a lower bar than Tier B
(external pilot with participants). Many gaps are Defer for Tier A but Blocker
for Tier B.

**Blockers: 15** (varies by tier)

| ID | Gap | Tier A | Tier B |
|----|-----|--------|--------|
| V1-G1 | Mast-lite field hardening | Defer | **Blocker** |
| V1-G2 | Ingest authorization for live nodes | Defer | **Blocker** |
| V1-G3 | Wi-Fi transport with TLS, identity, retries | Defer | **Blocker** |
| V1-G4 | Live public weather/smoke feeds with API keys | Defer | **Blocker** |
| V1-G5 | Trust scoring: freshness, health, install-quality penalties | **Blocker** | **Blocker** |
| V1-G6 | Node registry binding: full lifecycle, multi-node | **Blocker** | **Blocker** |
| V1-G7 | Installation metadata capture: guided input | Defer | **Blocker** |
| V1-G8 | Sharing/consent enforcement as product behavior | Defer | **Blocker** |
| V1-G9 | Evidence summaries in user-facing view | Defer | **Blocker** |
| V1-G10 | Revocation as product behavior | Defer | **Blocker** |
| V1-G11 | Named BOM vendor decisions | Defer | **Blocker** (if third-party kitting) |
| V1-G12 | Claims/safety language review for participants | Defer | **Blocker** |
| V1-G13 | Append-only observation/state history | Defer | Defer |
| V1-G14 | Deployment-quality flags in registry and view | Defer | **Blocker** |
| V1-G15 | Shared-map aggregate with policy gating | Defer | Defer |

**Acceptance commands:** `make oesis-v10-accept`, `make oesis-v10-check`,
`make oesis-v10-http-check`

**Technical build sequence (oesis-runtime):**

Building on v0.2–v0.5 foundations:

1. Implement trust scoring model (freshness penalty, health penalty, install-quality penalty)
2. Implement append-only observation and state history
3. Build user-facing evidence view (beyond JSON summary)
4. Implement live public weather and smoke feed integration with API keys and fallback
5. Implement ingest authorization and strong parcel binding for live nodes
6. Implement Wi-Fi transport with TLS, device identity, and retry logic
7. Build basic sharing settings UI
8. Implement parcel state with stronger functional translation
9. Implement limited neighborhood/shared signal ingestion (if pilot warrants)
10. Named BOM vendor decisions and procurement path
11. Claims and safety language review for participant-facing materials
12. Implement `make oesis-v10-accept` full acceptance suite

**Product surfaces (new in v1.0):**
- Web PWA or hosted app
- Push/email notifications (rule engine)
- Event timeline (append-only)
- Setup and context capture (guided onboarding)
- Governance UIs (sharing, consent, revocation)

**Hazard coverage honesty:**

| Hazard | v1.0 bar |
|--------|----------|
| Smoke / indoor air | Primary — strongest evidence path |
| Heat burden | Temperature from both nodes + weather context |
| Flood / runoff | Optional where flood-node installed |
| Freeze / cold | Partial via temperature signals |
| Outage / shelter | Reference only; no backup-power sensing |

---

### v1.5 — Measurement-to-intervention bridge

**Sign-off:** proves minimum bridge from parcel sensing into response reasoning
— one honest closed loop of `hazard → house state → action → measured outcome`
with evidence-quality limits carried through.

**Prerequisite:** v1.0 promoted

**This is a capability stage (Stage B), not a separately promoted program
phase.** It describes a class of product behavior that may be delivered within
or after program-phase v1.0 depending on timing.

**New surfaces:**

| Surface type | Examples |
|-------------|----------|
| House-state | indoor-response-node, power-outage-node, equipment-state-adapter |
| Building metadata | orientation, roof type, shading, tree canopy, impervious area, low points, vents, filter path |
| Intervention | action-log, bounded recommendation log |
| Verification | outcome-log, before/after response windows, effect-size estimates |
| Trust support | node health object, deployment metadata, device event history, calibration version |

**First proof path:** Smoke protection closed loop
- outdoor smoke evidence at trigger time
- indoor PM response measurement
- recirculation/fan/purifier posture
- logged action
- indoor improvement over 30–90 minute response window

**Exit criterion:** One honest closed-loop chain of
`hazard → house state → action → measured outcome` with evidence-quality limits
preserved.

---

## Beyond v1.5: capability stages C–F

| Stage | Version | Theme | Key additions |
|-------|---------|-------|---------------|
| C | v2 | Bounded adaptation guidance | Condition model, building response model, intervention ranking, operational recommendations |
| D | v2.5 | Bounded controls + compatibility | Controls inventory, compatibility surfaces (Matter, HA, BACnet), three-tier integration (advisory → soft → hard) |
| E | v3 | Parcel adaptation engine | Time-to-threshold, compound hazard, action-effect memory, household capacity modeling |
| F | v4 | Parcel + route + block resilience | Route/egress layer, neighborhood weak-point layer, community intervention ranking, shared infrastructure |

These stages are documented in `architecture/system/phase-roadmap.md` but do
not yet have release-lane packets. Planning for C–F should not begin until
Stage B (v1.5) exit criteria are met.

---

## Deployment maturity (separate axis)

Hardware field-readiness progresses independently from capability stages:

| Maturity | Bar | Current node status |
|----------|-----|---------------------|
| v0.1 (bench) | Prototype, provisional calibration | bench-air ✅, mast-lite (early prototype), flood-node (early prototype) |
| v1.0 (field-ready) | Protected power, buffering, connectorized wiring, enclosure, identity, service access | No node yet meets this bar |
| v1.5 (trust-hardened) | Device-ops, calibration versioning, maintenance-informed trust | — |
| v2.0 (policy-aware) | Decision-policy and adaptation support | — |

**Shared field-hardening bundle** (applies to all nodes targeting v1.0
maturity): protected power with brownout/battery, local circular buffer,
connectorized wiring, weatherproof enclosure, human-readable identity label,
service access without deinstallation.

---

## Cross-cutting workstreams

These advance continuously across versions:

| Workstream | Current status | Next milestone |
|-----------|---------------|----------------|
| Deployment maturity and field-hardening | bench-air v0.1 only | Mast-lite field-hardening (V1-G1) |
| Privacy and consent tooling | Docs-only / partial | Consent enforcement (v0.5) |
| Sensor health scoring | Partial (node health fields) | Trust scoring (v1.0) |
| Observability and provenance | Implemented in reference | Strengthen for multi-source |
| Calibration and deployment guidance | Provisional for all nodes | Field-validated calibration |
| Claims and safety language | Standards documented | Participant-facing review (v1.0 Tier B) |
| Local-first and degraded connectivity | Not implemented | Wi-Fi transport with retry (v1.0) |

---

## Three-repo coordination

| Repository | Role | Version alignment |
|-----------|------|-------------------|
| **oesis-program-specs** | Specifications, contracts, architecture, release planning | Version lane markers, release packets, acceptance criteria |
| **oesis-runtime** | Python reference implementation | Runtime code, acceptance commands, `make oesis-v0x-accept` |
| **oesis-public-site** | Next.js public preview | Public-facing materials; follows release-lane publication allowlist |

**Build validation commands** (in oesis-runtime, proxied from oesis-program-specs):

| Command | Scope |
|---------|-------|
| `make oesis-validate` | Schema validation (v0.1) |
| `make oesis-check` | Offline reference pipeline (v0.1) |
| `make oesis-http-check` | HTTP smoke test (v0.1) |
| `make oesis-accept` | Offline acceptance (v0.1) |
| `make oesis-v02-accept` | v0.2 acceptance suite (proposed) |
| `make oesis-v03-accept` | v0.3 acceptance suite (proposed) |
| `make oesis-v04-accept` | v0.4 acceptance suite (proposed) |
| `make oesis-v05-accept` | v0.5 acceptance suite (proposed) |
| `make oesis-v10-accept` | v1.0 acceptance suite (proposed) |

---

## Summary: the critical path

```
v0.1 ✅ ──→ v0.2 ──→ v0.3 ──→ v0.4 ──→ v0.5 ──→ v1.0 ──→ v1.5
  │           │         │         │         │         │         │
  │           │         │         │         │         │         └─ one closed loop:
  │           │         │         │         │         │            hazard → house state →
  │           │         │         │         │         │            action → measured outcome
  │           │         │         │         │         │
  │           │         │         │         │         └─ fielded parcel kit
  │           │         │         │         │            trust scoring + field-hardening
  │           │         │         │         │            15 gaps (tier-dependent)
  │           │         │         │         │
  │           │         │         │         └─ governance enforcement
  │           │         │         │            consent + revocation + retention + export
  │           │         │         │            10 blockers
  │           │         │         │
  │           │         │         └─ registry lifecycle + evidence quality
  │           │         │            install metadata + deployment flags
  │           │         │            6 blockers
  │           │         │
  │           │         └─ flood observation family
  │           │            water depth + rise rate + calibration
  │           │            6 blockers
  │           │
  │           └─ two-node kit (indoor + outdoor)
  │              mast-lite normalization + two-source inference
  │              5 blockers
  │
  └─ one parcel, one bench-air, one pipeline ✅
```

**Total blockers from here to v1.0:** 42 (across v0.2–v0.5 gaps) + 15 (v1.0
gaps, many overlapping with resolved v0.x work)

**Estimated critical-path dependencies:**
- v0.2 is independent of v0.3–v0.5 (can start immediately)
- v0.3 requires v0.2 (builds on two-node registry)
- v0.4 requires v0.3 (extends registry and evidence composition)
- v0.5 requires v0.4 (governance builds on mature registry)
- v1.0 requires v0.5 (governance must be enforced before broader system)
- v1.5 requires v1.0 (response measurement requires fielded kit)

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
