# Backlog

Items are placed by version target. See the
[v1.0 launch checklist](../release/v1.0/v1.0-launch-checklist.md) for gate-level
status and evidence.

## v1.0 Tier A — Internal reference completeness

- [ ] assign named owners to the launch readiness checklist (GL-8, PI-3, SO-4)
- [ ] connect UI copy pack to actual settings and parcel-state surfaces (PU-3)

## v1.0 Tier B — Before external pilot

- [ ] choose one canonical MVP transport and provisioning flow for all node classes (DA-4)
- [ ] draft participant support and complaint handling flow (PI-1 through PI-6)
- [ ] define pilot publication review workflow (RC-1 through RC-5)
- [ ] HTTP-level governance tests — consent enforcement at API response level (GL-6 extension)
- [ ] deployment packaging — Docker or equivalent for pilot operators (execution plan gap #5)

## v1.0 cross-cutting — Anytime quality improvements

- [ ] add diagrams to architecture and contract docs
- [ ] add API route definitions (routes exist in code but not documented as specs)
- [ ] add hardware photos and renders to build guides
- [ ] publish named-vendor SKU decisions for integrated parcel-kit BOM (HR-5; BOM structure exists)
- [ ] convert launch readiness checklist into tracked work items

## v1.5 — Measurement-to-intervention bridge

- [ ] add observation family and normalizer for `oesis.thermal-pod.v1` (if promoted from R&D)
- [ ] write `trust-and-temporal-integrity-model.md` (trust scoring model maturation)

## v2.0+ — Deferred

- [ ] write `lifelines-and-dependencies-model.md` (parcel-to-infrastructure dependency model)

---

## Completed

### Cross-repo infrastructure (2026-04-15)

- cross-repo architecture document (`architecture/system/cross-repo-architecture.md`)
- cross-repo sync check script, version manifest, CI workflows
- runtime ARCHITECTURE.md, hardware CONTRIBUTING.md
- public content bundle refreshed to current specs HEAD
- v0.1-boundary-and-non-goals.md and v1.0-parcel-kit-architecture.md written
- 4-repo split complete (oesis-program-specs, oesis-runtime, oesis-hardware, oesis-public-site)

### v1.0 Tier A implementation (2026-04-15)

- v1.0 acceptance covers bench-air, mast-lite, and flood (`make oesis-v10-accept`)
- trust scoring 5-factor model implemented and validated
- contrastive explanations and divergence analysis in v1.0 inference
- house state, intervention, and verification support objects in v1.0 pipeline
- operator runbooks current for v1.0 node classes (bench-air, mast-lite)
- implementation status matrix, launch checklists, and milestone roadmap refreshed

### v0.5 governance (2026-04-14)

- sharing settings, consent records, and rights requests — v0.5 runtime lane
- data-class annotations — 14-class `DATA_CLASS_GOVERNANCE` dictionary
- revocation handling — mark-not-delete semantics; `revoked_at` stops sharing
- operator access logging — `append_access_event` with 13 call sites
- public map suppression and thresholding — consent gating and k-anonymity

### v0.4 and earlier

- parcel node-registry spec with lifecycle management (v0.4)
- observation families for `oesis.flood-node.v1` and `oesis.weather-pm-mast.v1` (v0.3+)
- privacy governance baseline, permissions matrix, retention/export/deletion/revocation docs
- claims and safety-language standard
- condition-estimate terminology shift
- licensing, dataset release, and contribution governance docs
- machine-readable schemas for sharing settings, consent records, and rights requests
- pilot packet and launch readiness checklist
