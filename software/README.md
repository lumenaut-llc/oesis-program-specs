# Software

The software stack turns private observations, shared signals, and external context into parcel-level outputs and neighborhood condition views.

Read `NOTICE.md` before treating this subtree as a complete released software package.

## Lane contract

- **Baseline lane**: root subsystem docs in this directory (`ingest-service/`,
  `inference-engine/`, `parcel-platform/`, `shared-map/`) are the accepted
  current software posture.
- **Lane index**: `v0.1/` provides baseline lane entrypoints and compatibility
  mapping to canonical baseline docs.
- **Additive lanes**: `v1.0/` and `v1.5/` carry explicit forward-lane software
  deltas.
- **Canonical implementation mapping**: runtime code truth stays in sibling
  `../../oesis-runtime`; this subtree is documentation-only posture.

## Top-level concerns

- permissions and ownership
- provenance and confidence
- parcel state computation
- realtime updates
- inspectable explanations

## Reference commands

- `make oesis-demo`
  Run the current end-to-end reference pipeline from raw node packet to dwelling-facing parcel view.
- `make oesis-validate`
  Validate the machine-readable example payloads used by the reference scripts.
- `make oesis-check`
  Validate examples and the reference pipeline output shape in one smoke check.
- `make oesis-http-check`
  Start the local APIs and validate the ingest-to-inference-to-parcel-view HTTP path.

## Operator guide

- `operator-quickstart.md`
  Short repo-level guide for going from installed nodes to local packet validation, local APIs, and the preview site.

## Baseline subsystem entrypoints

- `inference-engine/README.md`
- `ingest-service/README.md`
- `parcel-platform/README.md`
- `shared-map/README.md`

## Baseline lane index

- `v0.1/README.md`
- `v0.1/operator-quickstart.md`
- `v0.1/ingest-service/README.md`
- `v0.1/inference-engine/README.md`
- `v0.1/parcel-platform/README.md`
- `v0.1/shared-map/README.md`

## Canonical Python layout

- sibling repo `../../oesis-runtime` is the canonical Python implementation tree for the current MVP services.
- `scripts/rhi_*.sh` remains as a legacy command compatibility layer during the migration.
- runnable software entrypoints belong in `../../oesis-runtime` only.
- new implementation work should land in `../../oesis-runtime` first and remain there.
- From the `repo/` directory, prefer direct module execution for new runbooks and automation:
  - `python3 -m oesis.ingest.validate_examples`
  - `python3 -m oesis.parcel_platform.reference_pipeline`
  - `python3 -m oesis.ingest.serve_ingest_api --host 127.0.0.1 --port 8787`
  - `python3 -m oesis.inference.serve_inference_api --host 127.0.0.1 --port 8788`
  - `python3 -m oesis.parcel_platform.serve_parcel_api --host 127.0.0.1 --port 8789`
  - `python3 -m oesis.shared_map.serve_shared_map_api --host 127.0.0.1 --port 8792`

## Architecture conformance

New subsystems and major features should:

- read `../../architecture/system/version-and-promotion-matrix.md` and `../../architecture/system/node-taxonomy.md` so **program-phase** slices, **capability stages** (`v1.5` vs `v2.5` for control compatibility), and **deployment maturity** are not conflated
- identify the target `architecture/` version they align with
- prefer explicit versioned documentation lanes such as `v1.0/` and `v1.5/`
  when writing forward-looking software docs
- declare their current status relative to that version:
  `implemented`, `partial`, `docs-only`, or `planned`
- update subsystem `architecture.md` when local design boundaries change
- update contracts, schemas, and examples when a boundary changes
- keep implementation truth in `../../oesis-runtime` rather than creating competing
  implementations in this docs repository
