# Implementation Status Matrix

## Status

Internal controlled-review document for the v0.1 release period.

Use this to separate what is working now from what is only documented, planned, or policy direction.

Do not treat this file as a public-site asset by default.

## Purpose

The release packet contains a large amount of high-quality documentation.
This matrix exists so reviewers do not confuse:

- verified reference behavior
- reference-only admin or governance utilities
- hardware build readiness
- policy direction that is not yet product behavior

This matrix also separates:

- architectural inclusion
- runnable reference behavior
- deployment maturity and field-hardening readiness

## Status key

- `implemented`
  Working in the current reference path and backed by a concrete check, command, or runnable service.
- `partial`
  Real code or hardware path exists, but coverage is narrow, staged, or still bounded by important gaps.
- `docs-only`
  The rule, contract, or process is documented, but there is not yet a matching operational or product surface.
- `planned`
  Intentionally on the roadmap, but not yet implemented in the current reference path.

## Version note

This matrix tracks maturity, not release numbering by itself.

Use it together with the versioned architecture docs this way:

- version numbers such as `v0.1` or a future `v0.x` identify accepted product
  slices
- status labels identify how complete each surface is within or around those
  slices

Do not treat every `partial`, `docs-only`, or newly added element as requiring a
new version number.

## Current snapshot

This matrix reflects the current local reference state after these checks passed from the **`oesis-runtime`** checkout (sibling repo; Python **3.11+** per `pyproject.toml`):

- `make oesis-validate`
- `make oesis-check`
- `make oesis-http-check`
- `make oesis-accept`

**2026-04-08 — v0.1 completeness review:** the commands above were re-run successfully on Python 3.11.1, along with `make oesis-v10-accept`, `make oesis-v10-check`, and `make oesis-v10-http-check`. Hardware-side, `python3 -m oesis.ingest.extract_latest_packet` plus `python3 -m oesis.ingest.ingest_packet` were exercised on a synthetic serial log; the bench-air **operator runbook** was aligned to these module entrypoints. See `v0.1-scope-matrix.md`, `v0.1-gap-register.md`, `v0.1-pilot-minimum-subset.md`, `v0.1-osi-diagrams.md` (Mermaid), and `v0.1-osi-diagrams-text.md` (plain text) in this directory for scope, gaps, pilot-tier gates, and OSI layer views of each path.

**2026-04-15 — v1.0 Tier A refresh:** All six acceptance suites (v0.1 through v1.0) pass via `python3 -m oesis.checks --lane <lane>`. Flood, weather-PM, and mast-lite observation families promoted from planned/partial to implemented. Bridge objects (house-state, intervention, verification, equipment-state, source-provenance) promoted from planned to partial — runtime inference integration exists but standalone API endpoints do not. Sharing/consent and revocation promoted from docs-only to implemented (v0.5 acceptance). Launch checklist at 17/44 gates complete. Hardware split to `oesis-hardware` repo complete; 4-repo structure operational.

## Deployment maturity note

The repo now uses a separate deployment maturity overlay in addition to the capability roadmap.
In this matrix:

- `implemented` means the reference path or hardware bring-up path exists
- `implemented` does not automatically mean `deployment maturity v1.0`
- a documented hardware lane may still be below a field-hardened deployed posture

## Software and APIs

| Surface | Status | Evidence | Current boundary | Next gap |
| --- | --- | --- | --- | --- |
| Example payload validation | implemented | `make oesis-validate` | Example schemas and checked-in payloads validate cleanly. | Keep examples aligned with new observation families. |
| Reference packet-to-parcel pipeline | implemented | `make oesis-check`, `make oesis-demo` | One reference path runs from node packet through parcel state and parcel view. | Expand beyond the current air-node lineage. |
| Local ingest API | implemented | `python3 -m oesis.ingest.serve_ingest_api`, `make oesis-http-check` | Accepts `oesis.bench-air.v1` packets and normalizes them. | Bind ingest authorization and parcel binding to stronger live-node workflows. |
| Local inference API | implemented | `python3 -m oesis.inference.serve_inference_api`, `make oesis-http-check` | Produces parcel-state outputs from normalized observation plus context. | Extend coverage to more observation families. |
| Local parcel-platform API | implemented | `python3 -m oesis.parcel_platform.serve_parcel_api`, `make oesis-http-check` | Builds parcel views and evidence summaries in the current reference flow. | Distinguish reference governance flows from fuller product UX. |
| Bench-air packet normalization | implemented | `python3 -m oesis.ingest.ingest_packet`, example packet validation | Current ingest path explicitly supports `oesis.bench-air.v1`. | Keep schema stable while new node classes come online. |
| Mast-lite through shared packet lineage | implemented | `make oesis-v02-accept` through `make oesis-v10-accept`; v1.0 acceptance normalizes mast-lite packets and infers parcel state | Uses `oesis.bench-air.v1` lineage with `location_mode: "sheltered"`. Shared normalizer; no family-specific normalization needed. | Field-hardening bundle (protected power, buffering, enclosure) not yet closed — see HR-2. |
| Flood low-point observation family | implemented | `make oesis-v03-accept` through `make oesis-v10-accept`; `normalize_flood_packet.py` in runtime | `flood.low_point.snapshot` normalization and value extraction (water_depth_cm, distance_cm, dry_reference_distance_cm) work in the canonical Python path. | Independent field build reproduction not yet confirmed. |
| Weather PM outdoor observation family | implemented | `make oesis-v10-accept`; `normalize_weather_pm_packet.py` in runtime | `air.pm_weather.snapshot` normalization works in the v1.0 canonical path. | Hardware deployment maturity remains below field-ready. |
| Thermal scene observation family | planned | integrated parcel spec | `thermal-pod` remains in a separate R&D lane. | Implement `thermal.scene.snapshot` only after privacy and usefulness boundaries are stronger. |

## Governance, rights, and shared-map surfaces

| Surface | Status | Evidence | Current boundary | Next gap |
| --- | --- | --- | --- | --- |
| Rights request processing utility | partial | `oesis.parcel_platform.process_rights_requests`, parcel API admin routes | Reference delete-processing flow exists for controlled/admin use. | Add a user-facing or operationally complete request lifecycle surface. |
| Export bundle utility | partial | `oesis.parcel_platform.export_parcel_bundle`, parcel API admin routes | Reference export flow exists and can write a machine-readable bundle. | Connect export to a fuller product or support workflow. |
| Retention cleanup utility | partial | parcel API admin route `/v1/admin/retention/cleanup` | Reference cleanup flow exists in the parcel-platform tree. | Turn retention policy into a clearer operational surface with owners. |
| Operator access logging in reference flows | partial | access-log handling inside `serve_parcel_api.py` and related utilities | Reference logging exists for admin actions. | Prove complete parcel-linked access logging in broader operations. |
| Shared-map aggregate API | partial | `python3 -m oesis.shared_map.serve_shared_map_api` | Aggregated neighborhood testing path exists. | Integrate it into broader checks and real review flows. |
| Public shared map | docs-only | `public_map_supported: False` in shared-map API | The reference stack explicitly does not support a public parcel-resolution map. | Keep public-map red lines enforced if the shared-map surface grows. |
| Sharing settings, consent, and rights schemas | implemented | `make oesis-v05-accept`; consent lifecycle (grant, eligibility, rejection), sharing settings, and rights processing tested end-to-end | v0.5 acceptance validates full consent and sharing lifecycle at API level. | Product UI for operator sharing management (PU-7) not yet built. |
| Revocation behavior as product guarantee | implemented | `make oesis-v05-accept`; revocation stops future sharing, shared-map suppresses revoked parcels | v0.5 acceptance proves revocation cutoff and map suppression. | HTTP-level consent filtering on API responses not yet tested (V05-G14). |

## Hardware and field path

| Surface | Status | Evidence | Current boundary | Next gap |
| --- | --- | --- | --- | --- |
| Bench-air-node build path | implemented | build guide, operator runbook (ingest via `oesis-runtime` modules), firmware examples, `serial-json-contract.md` aligned with packaged examples | Indoor or sheltered bench node is the current fastest working hardware slice, but the default posture is still `deployment maturity v0.1`. | Document fixed harness, stable enclosure or stand, identity label, and local logging posture before using stronger deployed language; gather more repeatable field evidence. |
| Mast-lite build and install path | partial | build guide, operator runbook, procurement and installation checklists | First sheltered outdoor node is integrated into the parcel-kit path, but not yet field-hardened by default. | Close the field-hardening bundle around protected power, buffering, connectorized wiring, enclosure support, and serviceability. |
| Tier 1 and Tier 2 procurement path | docs-only | `parcel-kit-procurement-checklist.md` | A non-author now has a documented first purchase path, but the repo has not yet proven it through named BOM decisions or completed parcel builds. | Convert purchase guidance into named BOM sources and part decisions. |
| Tier 1 and Tier 2 installation path | docs-only | `parcel-installation-checklist.md` | Indoor and sheltered outdoor siting rules are documented, including the field-hardening gate for deployed language. | Add real install records and field photos under controlled review. |
| Flood-node hardware path | partial | flood-node build/runbook/calibration docs | Hardware path exists, but it is not part of the default first kit and remains a parcel-specific experimental field lane. | Add low-point install records, rigid geometry and marker discipline, and software observation support. |
| Weather-pm-mast hardware path | partial | weather-pm-mast docs and firmware lane | Second-wave hardware lane exists; treat as a `deployment maturity v1.5` target rather than a default pilot requirement. | Complete PM power, airflow, interface, buffering, and maintenance posture before making it critical-path hardware. |
| Thermal-pod hardware path | partial | thermal-pod docs | Separate R&D lane exists and should stay below general field-ready language. | Resolve privacy, retention, power, storage, and usefulness questions before folding it into the parcel kit. |

## Bridge and response-layer objects (capability-stage v1.5+)

| Surface | Status | Evidence | Current boundary | Next gap |
| --- | --- | --- | --- | --- |
| House-state support object | partial | `contracts/v1.0/schemas/house-state.schema.json`; v1.0 inference consumes house_state in `infer_parcel_state()` | Schema, example, and runtime inference integration exist. House-state influences closed-loop summaries and recommendation content. | No standalone parcel-platform endpoint (`/house-state`); no pilot-validated data. |
| House-capability support object | partial | `contracts/v1.5/schemas/house-capability.schema.json`; v1.0 inference consumes house_capability | Schema, example, and runtime inference integration exist. | No standalone endpoint; v1.5 bridge scope. |
| Intervention-event record | partial | `contracts/v1.5/schemas/intervention-event.schema.json`; v1.0 inference consumes intervention_event | Schema, example, and runtime inference integration exist. Closed-loop summary generation works. | No standalone endpoint; no real intervention data yet. |
| Verification-outcome record | partial | `contracts/v1.5/schemas/verification-outcome.schema.json`; v1.0 inference consumes verification_outcome | Schema, example, and runtime inference integration exist. Verification assessment in inference pipeline works. | No standalone endpoint; no real verification data yet. |
| Equipment-state-observation | partial | `contracts/v1.0/schemas/equipment-state-observation.schema.json`; v1.0 inference consumes equipment_state_observation | Schema, example, and v1.0 inference integration exist. Equipment state flows into parcel-state reasoning. | No standalone ingest normalization path or endpoint. |
| Source-provenance-record | partial | `contracts/v1.0/schemas/source-provenance-record.schema.json`; v1.0 inference consumes source_provenance_record | Schema, example, and v1.0 inference integration exist. Provenance informs trust scoring. | No standalone provenance tracking endpoint. |
| Control-compatibility | planned | `contracts/v1.5/schemas/control-compatibility.schema.json` | Schema and example exist; draft capture may begin under v1.5 bridge. | Full compatibility inventory is a v2.5 deliverable — see `../../architecture/system/architecture-gaps-by-stage.md`. |

## Release, legal, and public surfaces

| Surface | Status | Evidence | Current boundary | Next gap |
| --- | --- | --- | --- | --- |
| Public preview site scaffold | implemented | sibling workspace `../../oesis-public-site` (Next.js 15); publication anchors and exclusions in `src/data/publicationPolicy.ts` and `src/generated/publicContentBundle.ts`, generated from program-specs `artifacts/public-content-bundle/public-content-bundle.json` | The site is its own repo; there is no `release/.../site/` tree in program-specs. | Regenerate the bundle when release roots change; keep `legal/public-preview-scope.md` aligned. |
| Public preview packet | implemented | `NOTICE.md`, release README, governance/privacy docs | Packet is assembled for public-safe preview readers. | Keep the packet aligned with the actual implementation boundary. |
| Reviewer packet assembly | implemented | `reviewer-packet-index.md` | Controlled packet lanes are now explicit. | Use named release owners to decide who receives which packet. |
| Counsel packet assembly | implemented | `legal/send-to-counsel-checklist.md` and related filing docs | Archival counsel handoff path exists if later needed. | Only use if the project reopens a separate patent/counsel lane. |
| Pilot packet assembly | implemented | pilot playbooks and pilot/research agreement template | Pilot docs exist for operator and participant review. | Assign named pilot owners and turn packet rules into operating practice. |
| Launch readiness ownership and completion | partial | `v1.0-launch-checklist.md`: 17 of 44 gates complete, 2 in progress, 25 not started | Tier A (internal reference) substantively complete. Tier B (external pilot) gates remain largely not started. | Assign named owners to remaining gates; close HR-2 and HR-4 when evidence arrives. |

## How to use this matrix

Before publishing, sending, or presenting anything:

1. Confirm the surface is marked `implemented` or that the audience understands it is only `partial`, `docs-only`, or `planned`.
2. Pair this matrix with `reviewer-packet-index.md` before sending controlled-review materials.
3. Do not let a documented policy or schema stand in for product behavior.
4. Do not let architectural inclusion stand in for field-hardened readiness.
5. Re-run the reference checks before changing any row from `partial` or `docs-only` to `implemented`.
6. Promote a new `v0.x` only when the accepted runnable slice changes materially and the architecture scope, contract/runtime boundaries, and acceptance evidence have all been updated together.
