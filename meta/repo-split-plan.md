# Repo Split Plan

## Purpose

Make the current monorepo easier to navigate by separating:

- the runnable reference system
- the program-definition and release machinery
- the public preview site

This plan follows the current boundary model already described in:

- `architecture/current/component-boundaries.md`
- `architecture/current/implementation-posture.md`

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

- `program/`
- `contracts/`
- `architecture/`
- `release/`
- `hardware/`
- `software/`
- `legal/`
- `operations/`
- `media/`
- `shared/`
- `meta/`
- `oesis_build/`
- repo-level docs such as `README.md`, `NOTICE.md`, and `LICENSES.md`, plus `meta/CONTRIBUTING.md`

### Ownership: `oesis-public-site`

Purpose:

- own the Next.js-based public preview site
- keep frontend build and deployment separate from runtime and release docs

Primary contents:

- sibling repo `../oesis-public-site`

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

- `program/`
- `contracts/`
- `architecture/`
- `release/`
- `hardware/`
- `software/`
- `legal/`
- `operations/`
- `media/`
- `shared/`
- `meta/`
- `oesis_build/`
- `README.md`
- `NOTICE.md`
- `meta/CONTRIBUTING.md`
- `LICENSES.md`

### Move to `oesis-public-site`

- sibling repo `../oesis-public-site`

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
- inventory runtime dependencies on `contracts/`, `architecture/`, `release/`, `hardware/`, `software/`, `legal/`, `operations/`, `media/`, `shared/`, `meta/`, and `sites/`
- define bundle formats and ownership rules
- stop adding new cross-tree relative-path dependencies

### Phase 1: split `oesis-public-site`

- move the local `sites/public-preview/` app first and then retire it behind a pointer
- keep content handoff simple at first if necessary
- replace same-repo assumptions with a public-content bundle

Why first:

- separate toolchain
- narrowest dependency surface
- lowest operational risk

### Phase 2: split `oesis-runtime`

- move the local `oesis/` runtime tree and smoke-check scripts
- replace docs-tree example and config reads with runtime-owned assets or a contracts bundle
- make runtime checks pass without the local specs repo tree present

### Phase 3: reframe the remaining repo as `oesis-program-specs`

- keep architecture, release, governance, hardware, contracts, and publication support together
- treat the repo as the program-definition source of truth rather than as the runtime home

### Phase 4: re-evaluate `oesis_build`

- split `oesis_build/` only if it becomes independently reusable and stable
- otherwise keep it with `oesis-program-specs`

## Success criteria

The split is healthy when:

- `oesis-runtime` can run validation and smoke checks without a local specs repo tree
- `oesis-program-specs` can state implementation truth using imported runtime evidence rather than filesystem co-location
- `oesis-public-site` can build from approved content bundles rather than raw internal docs paths
- no repo depends on another via relative filesystem traversal

## Phase 5: Hardware split (complete)

**Decision:** Extract `hardware/` into standalone `oesis-hardware` repository.

**Rationale:**
- 155 files including 11 Arduino sketches and 2 Python firmware scripts — actual executable code, not specifications
- Separate license (CERN-OHL-S-2.0) from the rest of the repo
- Different audience (hardware builders) and change cadence from software architecture
- Zero coupling to oesis-runtime (runtime only validates `hardware_family` enum fields)

**What moved:**
- All node families: bench-air-node, mast-lite, flood-node, weather-pm-mast, thermal-pod, circuit-monitor
- Cross-node resources: parcel-kit (BOMs, checklists, power guide)
- Version lane directories: v0.1 through v1.5
- Calibration reference

**What stayed:**
- `hardware/LICENSE` (CERN-OHL-S-2.0 text, referenced by LICENSES.md)
- `hardware/README.md` (redirect stub pointing to oesis-hardware)

**Cross-reference approach:** All ~100 relative markdown links from specs into hardware converted to GitHub URLs (`https://github.com/lumenaut-llc/oesis-hardware/blob/main/...`). Outbound references from hardware docs to specs also converted to GitHub URLs.

**Result:** Four-repo structure:

| Repo | Identity | License |
|------|----------|---------|
| oesis-program-specs | Architecture, contracts, governance, release | CC BY-SA 4.0 / AGPL-3.0 |
| oesis-runtime | Python reference services | AGPL-3.0 |
| oesis-hardware | Sensor node specs, firmware, BOMs | CERN-OHL-S-2.0 / AGPL-3.0 |
| oesis-public-site | Public preview website | AGPL-3.0 |

## Current working rule

Now that extraction is complete:

- treat sibling repo `../oesis-runtime` as the runtime source of truth
- treat sibling repo `../oesis-hardware` as the hardware specification and firmware source of truth
- treat `contracts/`, `architecture/`, `legal/privacy/`, and `legal/` as the specification and policy source of truth
- treat sibling repo `../oesis-public-site` as the canonical publication surface
- treat local `oesis/` and `sites/public-preview/` paths as migration pointers only
