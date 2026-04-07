# Runtime Split Readiness

## Purpose

Record the concrete work that was required before the runtime moved into the
canonical sibling repository `../oesis-runtime` and stopped depending on the
specs repository layout.

## Status

Completed. The in-repo runtime mirror has been retired and replaced with a
migration pointer.

## Current blockers

The runtime originally read examples and config directly from the specs docs
and software-doc tree.

### Example payload coupling

These runtime modules currently depend on `docs/data-model/examples/` through `oesis.common.repo_paths.DOCS_EXAMPLES_DIR`:

- `oesis/ingest/validate_examples.py`
- `oesis/ingest/normalize_packet.py`
- `oesis/ingest/normalize_public_weather_context.py`
- `oesis/ingest/normalize_public_smoke_context.py`
- `oesis/inference/infer_parcel_state.py`
- `oesis/parcel_platform/reference_pipeline.py`
- `oesis/parcel_platform/format_parcel_view.py`
- `oesis/parcel_platform/format_evidence_summary.py`
- `oesis/parcel_platform/serve_parcel_api.py`
- `oesis/shared_map/aggregate_shared_map.py`

### Runtime script coupling

These scripts currently read doc-owned examples directly:

- `scripts/oesis_http_smoke_check.sh`

Current direct dependency:

- `docs/data-model/examples/node-observation.example.json`

### Config coupling

This runtime module currently reads config directly from the software docs tree:

- `oesis/inference/infer_parcel_state.py`

Current config source:

- `software/inference-engine/config/public_context_policy.json`
- `software/inference-engine/config/hazard_thresholds_v0.json`
- `software/inference-engine/config/trust_gates_v0.json`

## Required boundary changes

### 1. Give runtime its own asset home

Create a runtime-owned home for:

- example payloads needed for smoke checks and default CLI inputs
- inference config required for local execution

Suggested shape:

- `oesis/assets/examples/`
- `oesis/assets/config/inference/`

### 2. Stop reading examples from the specs tree

Change runtime code so default behavior reads from runtime-owned assets.

Allowed follow-up options:

- package those assets directly in `oesis-runtime`
- generate them from a published `contracts-bundle`
- support an override path for alternate bundles in CI or release checks

### 3. Treat docs examples as spec-owned copies

After runtime owns its execution fixtures:

- `oesis-program-specs` remains source of truth for published schemas and public examples
- runtime examples become either packaged fixtures or imported bundle contents
- same-file co-location should no longer be assumed

### 4. Replace filesystem reach-through in smoke checks

`scripts/oesis_http_smoke_check.sh` should read one of:

- a runtime-owned fixture path
- a provided contracts-bundle path

It should not assume the monorepo docs tree is present.

## Acceptance criteria

The runtime is ready to split when:

- `python3 -m oesis.ingest.validate_examples` works without the specs repo tree
- `python3 -m oesis.parcel_platform.reference_pipeline` works without the specs repo tree
- `./scripts/oesis_smoke_check.sh` works without the specs repo tree
- `./scripts/oesis_http_smoke_check.sh` works without the specs repo tree
- inference config is loaded from runtime-owned assets or an explicit bundle input

## Suggested implementation order

1. Introduce runtime-owned asset directories and a single loader module.
2. Point all default runtime example reads to that loader.
3. Move inference config reads behind the same runtime-owned boundary.
4. Update smoke checks to use runtime-owned assets.
5. Only then move the runtime package and scripts into `../oesis-runtime`.

## Notes

- The goal is not to duplicate ownership of contracts forever.
- The goal is to stop coupling runtime execution to repo-relative documentation paths.
- Once the split is stable, examples can be synced from published contract bundles instead of being hand-copied.
