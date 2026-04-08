# Architecture

## Purpose

Provide the canonical home for architecture across the program.

This directory now combines:

- current truthful reference architecture
- debated future architecture
- system-level architectural and operating-model narratives
- lightweight conformance rules for how new work should attach to the canon

It does not replace subsystem docs, formal contracts, governance policy, or
executable code.

## Layout

### `current/`

The current truthful reference architecture.

Use `current/` for:

- the current technical philosophy
- the current runnable reference stack
- the current implementation posture
- current component boundaries and ownership rules
- the current implementation-aligned milestone sequence

### `future/`

The debated target architecture.

Use `future/` for:

- architectural goals beyond the current reference stack
- proposed boundary or topology changes
- open questions and tradeoffs
- decisions under discussion

### `system/`

Program-level architectural and operating-model narratives.

Use `system/` for:

- vision and use-case framing
- integrated system specs
- operating models
- product requirements and roadmap framing

### `decisions/`

Cross-version architecture debates and decision scaffolding.

## Reading order

1. `current/README.md`
2. `current/technical-philosophy.md`
3. `current/reference-stack.md`
4. `current/minimum-functioning-v0.1.md`
5. `current/architecture-object-map.md`
6. `current/implementation-posture.md`
7. `current/component-boundaries.md`
8. `current/milestone-roadmap.md`
9. `decisions/debate-map.md`
10. `future/README.md` when you want the debated target lane

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

- identify the target architecture version they are aligning with
- describe their implementation status relative to that version:
  `implemented`, `partial`, `docs-only`, or `planned`
- update contracts and examples when a boundary changes
- update subsystem `architecture.md` when the local architecture changes
- avoid letting architecture claims outrun the current implementation status
