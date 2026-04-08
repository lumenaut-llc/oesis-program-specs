# Runtime Split Readiness

## Purpose

Record how the executable runtime was separated from the program-spec repository
and what to run to confirm the boundary is healthy.

## Status

**Done.** The canonical runtime lives in the sibling repository `../oesis-runtime`.
This repository (`oesis-program-specs`) holds
architecture, contracts, legal, release, and operator documentation.

## Runtime layout (sibling repo)

- **Examples and inference config** — `oesis/assets/examples/` and
  `oesis/assets/config/inference/` (no dependency on this repo’s tree for default
  execution).
- **v0.1 pipeline** — `oesis.checks.v01.build_v01_runtime_flow` and
  `python3 -m oesis.parcel_platform.reference_pipeline`.
- **Context loading** — `oesis.context.loader` for default parcel and public
  fixtures.
- **Acceptance** — `python3 -m oesis.checks` (`make oesis-accept`), plus
  `make oesis-check` (CLI smoke) and `make oesis-http-check` (HTTP smoke).

Optional overrides: `OESIS_CONTRACTS_BUNDLE_DIR`, `OESIS_INFERENCE_CONFIG_DIR`
(see `../oesis-runtime/README.md`).

## Acceptance criteria (met)

With only `../oesis-runtime` checked out and dependencies installed:

- `python3 -m oesis.ingest.validate_examples` succeeds.
- `python3 -m oesis.parcel_platform.reference_pipeline` succeeds.
- `make oesis-check` succeeds.
- `make oesis-http-check` succeeds.
- Inference config loads from runtime-owned assets unless overridden by env.

## Relationship to contracts in this repo

- **`contracts/`** here remains the published schema and example source of truth
  for the program.
- The runtime may ship **copies** of examples and config under `oesis/assets/`
  for standalone execution; keep them aligned when contracts change.

## Notes

- The goal is not permanent duplication of contracts, but **decoupled execution**:
  the runtime must not assume this repository’s directory layout is present.
- After contract changes, sync or regenerate runtime fixtures as part of your
  release discipline.
