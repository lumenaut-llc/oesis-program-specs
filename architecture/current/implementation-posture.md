# Implementation Posture

## Purpose

Tie the current architecture to the current executable and documented reference
state across all runtime lanes.

## Status

Current reference implementation posture. Updated 2026-04-15.

## Canonical homes

- sibling repo `../../../oesis-runtime` (program-specs checkout and runtime
  checkout are siblings under the same parent directory)
  Canonical implementation tree for the current reference services.
- `../../../../oesis_build/`
  Canonical build-foundation implementation tree.
- `../../software/*/architecture.md`
  Subsystem-local architecture explanation.
- `../../contracts/`
  Formal contracts, schemas, and examples.
- `../../legal/privacy/` and `../../legal/`
  Policy constraints that shape implementation behavior.

## Current execution evidence

The reference posture is anchored by lane-specific acceptance commands:

| Command | Result | What it proves |
|---------|--------|----------------|
| `make oesis-validate` | **PASS** | Schema validation (v0.1) |
| `make oesis-check` | **PASS** | Offline reference pipeline (v0.1) |
| `make oesis-http-check` | untested | HTTP smoke test (v0.1) |
| `make oesis-accept` | **PASS** | v0.1 baseline acceptance |
| `make oesis-v02-accept` | **PASS** | v0.2: indoor + outdoor (2 nodes) |
| `make oesis-v03-accept` | **PASS** | v0.3: flood-capable (3 nodes) |
| `make oesis-v04-accept` | **PASS** | v0.4: multi-node registry lifecycle |
| `make oesis-v05-accept` | **PASS** | v0.5: governance enforcement |
| `make oesis-v10-accept` | **PASS** | v1.0: extended support objects |

**Acceptance test caveat:** These tests are structural smoke tests. They verify
that pipelines execute without error and output data structures contain required
fields. They do **not** assert inference value correctness, behavioral edge
cases, or HTTP-level governance enforcement. See
`../../program/execution-plan.md` for detailed coverage analysis.

**Field or pilot "deployed" is not the same thing.** Install and operations
credibility come from pilot playbooks, operator checklists, and rows in the
implementation status matrix—not from Makefile targets alone.

## Version versus status

Keep these concepts separate:

- `v0.x` version labels describe accepted product slices
- `implemented`, `partial`, `docs-only`, and `planned` describe maturity within
  or around those slices
- **Program phase**, **reference-runtime asset lane**, and **public or marketing**
  release naming are also distinct; see `../../program/v0.1/README.md` and
  `../../program/operating-packet/00-version-labels-and-lanes.md`

## Current coverage by lane

### v0.1 — Baseline (implemented)

- Example payload validation
- Reference packet-to-parcel pipeline (ingest → inference → parcel view)
- Local ingest API, inference API, parcel-platform API
- Bench-air packet normalization
- Parcel-state with confidence, evidence mode, reasons, freshness, provenance
- Private-by-default architectural boundary

### v0.2 — Two-node kit (implemented)

- Mast-lite packet normalization (shared lineage with outdoor metadata)
- Two-node parcel context (node_installations for indoor + outdoor)
- Evidence source mix tracking (evidence_source_nodes populated)
- Two-source inference combination

### v0.3 — Flood-capable runtime (implemented)

- Flood packet normalization (`normalize_flood_packet.py`, 14-field validation)
- Flood condition derivation (water_depth_cm, rise_rate_cm_per_hr, calibration_state)
- Three-node registry binding (indoor + outdoor + flood)
- Flood hazard thresholds configuration

### v0.4 — Registry lifecycle + evidence composition (implemented)

- Node registry lifecycle: load, validate calibration state, filter active, bind metadata
- Calibration state enforcement (provisional, verified, recently_calibrated)
- Multi-node evidence composition with source diversity tracking
- Evidence contributions with individual weights in explanation payload

### v0.5 — Governance enforcement (implemented)

- Consent store: append-only JSON with atomic writes and thread-safe persistence
- Sharing store: operator-configurable preferences
- Data class governance: 14 classes with explicit sharing rules; 9 structurally private
- Consent enforcement: query-time eligibility checks (scope, data_classes, custody_tier, revoked_at)
- Revocation: mark-not-delete semantics; `revoked_at` stops future sharing
- Retention cleanup: time-based pruning with audit metrics
- Export bundle generation: parcel export with metadata
- Rights request processing: delete request execution with audit trail
- Operator access logging: events with actor, action, justification
- Shared map aggregation: consent-gated with minimum participation threshold (k-anonymity)

### v1.0 — Extended support objects (implemented, structural)

- House state as inference input (fallback PM2.5 from indoor response)
- House capability influence on smoke probability
- Intervention event tracking (action logs with verification windows)
- Verification outcome adjustment (+0.03 smoke probability if worsened, +0.02 confidence)
- Closed-loop summaries with PM2.5 delta tracking
- Contrastive explanations (public-only counterfactual)
- Divergence analysis (local vs public disagreement)
- Trust scoring computation (5-factor model: freshness, node_health, calibration_state, install_quality, source_diversity)
- All v0.5 governance inherited and tested

### Calibration program and admissibility (docs-only / planned)

- `../system/calibration-program.md` and `../system/adapter-trust-program.md`: **docs-only** (policy published 2026-04-19)
- Reference instrument program execution (per-measurand per-deployment-class reference files under `oesis-builds/procedures/<node>/references/`): **planned** — tracked as G13
- Burn-in gate enforcement in bring-up acceptance: **planned** — tracked as G14
- Build-spec §F metadata blocks on node specs: **planned** — bench-air G16, mast-lite G12
- Admissibility rule in ingest (`admissible_to_calibration_dataset` + reasons): **planned** — tracked as G15
- Observation schema facts required by admissibility (cross-repo change to `oesis-contracts`): **planned** — tracked as G17
- Adapter-trust program execution: **planned** — tracked as G18; load-bearing at capability stage v1.5

Trust scoring (already listed under v1.0) consumes the `calibration_state` field. Once the calibration program executes, `calibration_state` will be populated by calibration sessions per calibration-program §E rather than by manual declaration.

### Additional normalization (implemented)

- Circuit-monitor packet normalization and equipment-state bridge
- Weather-PM-mast packet normalization

### Not implemented

- Append-only observation/state history (snapshot-oriented)
- Ingest authorization for live nodes
- Wi-Fi transport with TLS
- Live public weather/smoke feeds (uses fixtures)
- Thermal scene observation family
- Installation metadata guided input surface
- Sharing settings product UI
- User-facing evidence view (beyond JSON)
- Reference instrument program (characterized references per measurand per deployment class)
- Build-spec §F metadata blocks
- Admissibility rule runtime wiring
- Observation schema extensions in `oesis-contracts` (admissibility facts)

### Hardware posture

- bench-air-node: implemented (deployment maturity v0.1 bench)
- mast-lite: build guide exists; independent reproduction not confirmed
- flood-node: build guide exists; independent reproduction not confirmed; provisional calibration only
- weather-pm-mast: hardware lane documented; not independently built
- thermal-pod: R&D lane; not part of critical path

## Governance execution status

The v0.5 and v1.0 runtime lanes implement governance as **runtime behavior**:

- **Consent enforcement**: implemented — DATA_CLASS_GOVERNANCE dictionary enforces sharing rules at query time; structurally private classes rejected on consent grant
- **Revocation**: implemented — `revoked_at` timestamp stops future sharing; shared-map suppresses revoked parcels
- **Retention**: implemented — time-based cleanup with auditable reports
- **Export**: implemented — bundle generation with metadata
- **Access logging**: implemented — all consent/revocation/rights operations logged
- **Private-by-default**: enforced at both architectural convention and runtime governance level

**Caveat:** Governance enforcement is tested at the store/API level in acceptance
tests. HTTP-level enforcement (ensuring API responses respect consent) has not
been tested.

## Posture discipline

- Do not promote **shared neighborhood** surfaces to **`implemented`** until
  **collection, ingest, and parcel-private** reasoning are credible on the
  reference path.
- Do not claim **governance** execution beyond what the runtime **enforces**.
  The v0.5 lane enforces consent, revocation, and retention at the store level.
  HTTP-level enforcement is not yet tested.
- **Trust scoring** is implemented. The 5-factor trust score model (freshness,
  node_health, calibration_state, install_quality, source_diversity) computes
  in `compute_trust_score.py` and is integrated into `infer_parcel_state.py`.
  The v1.0 acceptance test validates trust score structure and value ranges.

## Alignment rule

Architecture claims should not outrun the implementation-status classification.
The unified execution plan (`../../program/execution-plan.md`) is the
authoritative source for current position and remaining gaps.

## Related docs

- `../../program/execution-plan.md` — unified execution plan
- `../../program/v0.1/README.md`
- `../../program/operating-packet/00-version-labels-and-lanes.md`
- `../../program/operating-packet/09-phasing-v0.1-v1.0-v1.5.md`
- `technical-philosophy.md`
- `milestone-roadmap.md`
- `architecture-object-map.md`
