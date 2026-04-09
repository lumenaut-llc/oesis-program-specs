# Technical Architecture

## Purpose

Provide a transitional pointer to the canonical versioned architecture home
across the program.

This canon now uses the system name Open Environmental Sensing and Inference
System (`OESIS`). `Resilient Home Intelligence` (`RHI`) remains a legacy
compatibility name during the transition, especially in implementation-facing
identifiers that have not yet been migrated.

The canonical contributor entrypoints now live under:

- `../architecture/current/` for frozen `v0.1`
- `../architecture/future/` for debated `v1.0`
- `../architecture/decisions/` for cross-version doctrine and debates

This directory keeps the older version labels as a reading aid, but it no
longer defines the primary on-disk architecture split.

It still separates:

- current truthful architecture
- debated future architecture
- lightweight conformance rules for how new work should attach to the canon

It does not replace subsystem docs, formal contracts, governance policy, or
executable code.

## Version model

### `v0.1`

The current truthful reference architecture.

Use `v0.1/` for:

- the current technical philosophy
- the current runnable reference stack
- the current implementation posture
- current component boundaries and ownership rules
- the current implementation-aligned milestone sequence

`v0.1` should stay aligned with what is actually runnable, documented, and
verifiable today.

If the project later promotes `v0.2`, `v0.3`, or another pre-`1.0` slice, those
versions should represent accepted capability bundles rather than every added
node, schema field, or partial element.

### `v1.0`

The debated target architecture.

Use `v1.0/` for:

- architectural goals beyond the current reference stack
- proposed boundary or topology changes
- open questions and tradeoffs
- decisions under discussion

`v1.0` is proposal space. It must not be written as if it were already the
implemented system.

Use milestone and implementation-status tracking for smaller compatible growth
before promoting a new pre-`1.0` version.

## Reading order

Prefer the `../architecture/` entrypoints first. Use the files below only when
you specifically want the older `technical-architecture/` pointer view.

1. `v0.1/README.md`
2. `v0.1/technical-philosophy.md`
3. `v0.1/reference-stack.md`
4. `v0.1/minimum-functioning-v0.1.md`
5. `v0.1/architecture-object-map.md`
6. `v0.1/implementation-posture.md`
7. `v0.1/component-boundaries.md`
8. `v0.1/milestone-roadmap.md`
9. `../architecture/current/pre-1.0-version-progression.md`
10. `debate-map.md`
11. `v1.0/README.md` when you want the debated target lane

## What stays outside this directory

- `../contracts/`
  Formal schemas, examples, and contract definitions.
- `../software/*/architecture.md`
  Subsystem-local design and responsibilities.
- `../legal/privacy/` and `../legal/`
  Privacy, governance, claims, and release constraints.
- sibling repo `../oesis-runtime`
  Canonical implementation tree for the current reference services.

## Conformance expectations

Future subsystems and major features should follow these rules:

- identify the target technical-architecture version they are aligning with
- describe their implementation status relative to that version:
  `implemented`, `partial`, `docs-only`, or `planned`
- update contracts and examples when a boundary changes
- update subsystem `architecture.md` when the local architecture changes
- avoid letting architecture claims outrun the current implementation status

## Transitional path

This directory now acts as the transitional pointer while the canonical
current-versus-future architecture split lives in `../architecture/`.
