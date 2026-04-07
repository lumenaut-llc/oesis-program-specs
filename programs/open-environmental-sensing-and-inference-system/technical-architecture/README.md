# Technical Architecture

## Purpose

Provide the canonical home for versioned technical architecture across the
program.

This canon now uses the system name Open Environmental Sensing and Inference
System (`OESIS`). `Resilient Home Intelligence` (`RHI`) remains a legacy
compatibility name during the transition, especially in implementation-facing
identifiers that have not yet been migrated.

This directory separates:

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

### `v1.0`

The debated target architecture.

Use `v1.0/` for:

- architectural goals beyond the current reference stack
- proposed boundary or topology changes
- open questions and tradeoffs
- decisions under discussion

`v1.0` is proposal space. It must not be written as if it were already the
implemented system.

## Reading order

1. `v0.1/README.md`
2. `v0.1/technical-philosophy.md`
3. `v0.1/reference-stack.md`
4. `v0.1/minimum-functioning-v0.1.md`
5. `v0.1/architecture-object-map.md`
6. `v0.1/implementation-posture.md`
7. `v0.1/component-boundaries.md`
8. `v0.1/milestone-roadmap.md`
9. `debate-map.md`
10. `v1.0/README.md` when you want the debated target lane

## What stays outside this directory

- `../docs/data-model/`
  Formal schemas, examples, and contract definitions.
- `../software/*/architecture.md`
  Subsystem-local design and responsibilities.
- `../docs/privacy-governance/` and `../legal/`
  Privacy, governance, claims, and release constraints.
- `../../../oesis/`
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

The older `../architecture/` directory remains as a transitional pointer while
the repo migrates to this versioned structure.
