# Backlog

## Immediate

- connect UI copy pack to actual settings and parcel-state surfaces
- assign named owners to the launch readiness checklist
- choose one canonical MVP transport and provisioning flow for all node classes

## Soon

- add diagrams
- add API route definitions
- add hardware photos / renders
- convert launch readiness checklist into tracked work items
- draft participant support and complaint handling flow
- define pilot publication review workflow
- publish an integrated parcel-kit BOM by design tier (partial — parcel-kit BOM exists; named vendor SKUs not yet selected)
- add observation family and normalizer for `oesis.thermal-pod.v1` (flood and weather-pm-mast done in v0.3+)

## Recently completed

- implemented sharing settings, consent records, and rights requests — v0.5 runtime lane (`serve_parcel_api.py`, `make oesis-v05-accept`)
- implemented data-class annotations — 14-class `DATA_CLASS_GOVERNANCE` dictionary with sharing rules in v0.5
- implemented revocation handling — mark-not-delete semantics; `revoked_at` stops future sharing (v0.5)
- implemented operator access logging — `append_access_event` with 13 call sites (v0.5)
- implemented public map suppression and thresholding — `aggregate_shared_map.py` with consent gating and k-anonymity (v0.5)
- canonical Python implementation tree lives in sibling `../oesis-runtime` — repo split complete
- defined and implemented parcel node-registry spec — `manage_node_registry.py` with lifecycle management (v0.4)
- added observation families for `oesis.flood-node.v1` and `oesis.weather-pm-mast.v1` — normalizers implemented (v0.3+)

## Previously completed foundation work

- created privacy governance baseline and permissions matrix
- created retention/export/deletion/revocation policy docs
- created claims and safety-language standard
- shifted parcel outputs to condition-estimate terminology
- created licensing, dataset release, and contribution governance docs
- created operator access, public map, consent, and privacy notice docs
- added machine-readable schemas for sharing settings, consent records, and rights requests
- added pilot packet and launch readiness checklist
