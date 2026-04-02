# Software

The software stack turns private observations, shared signals, and external context into parcel-level outputs and neighborhood condition views.

Read `NOTICE.md` before treating this subtree as a complete released software package.

## Top-level concerns

- permissions and ownership
- provenance and confidence
- parcel state computation
- realtime updates
- inspectable explanations

## Reference commands

- `make rhi-demo`
  Run the current end-to-end reference pipeline from raw node packet to homeowner-facing parcel view.
- `make rhi-validate`
  Validate the machine-readable example payloads used by the reference scripts.
- `make rhi-check`
  Validate examples and the reference pipeline output shape in one smoke check.
- `make rhi-http-check`
  Start the local APIs and validate the ingest-to-inference-to-parcel-view HTTP path.

## Operator guide

- `operator-quickstart.md`
  Short repo-level guide for going from installed nodes to local packet validation, local APIs, and the preview site.

## Canonical Python layout

- `../../../rhi/` is the canonical Python implementation tree for the current MVP services.
- `programs/resilient-home-intelligence/software/*/scripts/` stays in place as a compatibility layer for docs, runbooks, and existing operator commands.
- New implementation work should land in `../../../rhi/` first, then flow through the docs-facing script entrypoints.
- From the `repo/` directory, prefer direct module execution for new runbooks and automation:
  - `python3 -m rhi.ingest.validate_examples`
  - `python3 -m rhi.parcel_platform.reference_pipeline`
  - `python3 -m rhi.ingest.serve_ingest_api --host 127.0.0.1 --port 8787`
  - `python3 -m rhi.inference.serve_inference_api --host 127.0.0.1 --port 8788`
  - `python3 -m rhi.parcel_platform.serve_parcel_api --host 127.0.0.1 --port 8789`
  - `python3 -m rhi.shared_map.serve_shared_map_api --host 127.0.0.1 --port 8792`
