# Repo Split Plan

## Purpose

Make the current monorepo easier to navigate by separating:

- the runnable reference system
- the program-definition and release machinery
- the public preview site

This plan follows the current boundary model already described in:

- `programs/open-environmental-sensing-and-inference-system/technical-architecture/v0.1/component-boundaries.md`
- `programs/open-environmental-sensing-and-inference-system/technical-architecture/v0.1/implementation-posture.md`

## Target repos

### Ownership: `oesis-runtime`

Purpose:

- own the runnable Python reference services
- own the packet-to-parcel reference pipeline
- own runtime smoke checks

Primary contents:

- `oesis/`
- runtime-facing scripts from `scripts/`
- runtime-focused CI and task runner files

### Ownership: `oesis-program-specs`

Purpose:

- own architecture, contracts, examples, governance, and release posture
- own the materials that describe, constrain, and publish the system
- own build and publication support that is still tightly coupled to the program

Primary contents:

- `programs/open-environmental-sensing-and-inference-system/`
- `shared/`
- `meta/`
- `oesis_build/`
- repo-level docs such as `README.md`, `NOTICE.md`, `CONTRIBUTING.md`, and `LICENSES.md`

### Ownership: `oesis-public-site`

Purpose:

- own the Astro-based public preview site
- keep frontend build and deployment separate from runtime and release docs

Primary contents:

- `sites/public-preview/`

## Ownership rules

### `oesis-runtime`

Owns:

- executable service behavior
- local APIs
- runtime validation and smoke checks
- reference output generation

Consumes:

- published contract bundles from `oesis-program-specs`

Must not own:

- canonical architecture claims
- release packet truth
- policy and governance source documents

### `oesis-program-specs`

Owns:

- architecture canon
- schemas and checked examples
- implementation-status claims
- release packet and publication constraints
- governance, privacy, and legal materials
- hardware and operator documentation

Consumes:

- implementation evidence from `oesis-runtime`
- approved public-site artifacts when needed

Must not own:

- primary runtime implementations

### `oesis-public-site`

Owns:

- frontend application code
- public-safe presentation logic
- site build and deploy configuration

Consumes:

- public-safe content bundles from `oesis-program-specs`

Must not own:

- canonical schema and policy sources
- internal review-only release materials

## Planned file mapping

### Move to `oesis-runtime`

- `oesis/`
- `scripts/oesis_smoke_check.sh`
- `scripts/oesis_http_smoke_check.sh`

### Move to `oesis-program-specs`

- `programs/open-environmental-sensing-and-inference-system/`
- `shared/`
- `meta/`
- `oesis_build/`
- `README.md`
- `NOTICE.md`
- `CONTRIBUTING.md`
- `LICENSES.md`

### Move to `oesis-public-site`

- `sites/public-preview/`

## Cross-repo artifacts

The split should be driven by explicit published artifacts rather than relative filesystem reads.

### `contracts-bundle`

Published by `oesis-program-specs`.

Contents:

- schemas
- checked example payloads
- version metadata
- bundle changelog if needed

Consumed by:

- `oesis-runtime`
- `oesis-public-site` when the site needs public-safe structured examples or contract metadata

### `runtime-evidence-bundle`

Published by `oesis-runtime`.

Contents:

- results for `oesis-validate`, `oesis-check`, and `oesis-http-check`
- supported-surface metadata
- optionally generated reference outputs

Consumed by:

- `oesis-program-specs`

### `public-content-bundle`

Published by `oesis-program-specs`.

Contents:

- public-safe markdown or JSON
- approved media and diagrams
- release metadata intended for the preview site

Consumed by:

- `oesis-public-site`

## Migration order

### Phase 0: prepare inside the monorepo

- document target repo boundaries
- inventory runtime dependencies on `programs/`, `shared/`, `meta/`, and `sites/`
- define bundle formats and ownership rules
- stop adding new cross-tree relative-path dependencies

### Phase 1: split `oesis-public-site`

- move `sites/public-preview/` first
- keep content handoff simple at first if necessary
- replace same-repo assumptions with a public-content bundle

Why first:

- separate toolchain
- narrowest dependency surface
- lowest operational risk

### Phase 2: split `oesis-runtime`

- move `oesis/` and runtime smoke-check scripts
- replace docs-tree example and config reads with runtime-owned assets or a contracts bundle
- make runtime checks pass without the local `programs/` tree present

### Phase 3: reframe the remaining repo as `oesis-program-specs`

- keep architecture, release, governance, hardware, contracts, and publication support together
- treat the repo as the program-definition source of truth rather than as the runtime home

### Phase 4: re-evaluate `oesis_build`

- split `oesis_build/` only if it becomes independently reusable and stable
- otherwise keep it with `oesis-program-specs`

## Success criteria

The split is healthy when:

- `oesis-runtime` can run validation and smoke checks without a local `programs/` tree
- `oesis-program-specs` can state implementation truth using imported runtime evidence rather than filesystem co-location
- `oesis-public-site` can build from approved content bundles rather than raw internal docs paths
- no repo depends on another via relative filesystem traversal

## Near-term working rule

Until the split is complete:

- treat `oesis/` as the runtime source of truth
- treat `programs/.../docs/data-model/`, `technical-architecture/`, `docs/privacy-governance/`, and `legal/` as the specification and policy source of truth
- treat `sites/public-preview/` as a separate publication surface, even while it still lives in this repo
