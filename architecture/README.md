# Architecture

## Purpose

Provide the canonical home for versioned architecture across the program.

This directory now combines:

- current truthful reference architecture
- debated future architecture
- system-level architectural and operating-model narratives
- lightweight conformance rules for how new work should attach to the canon

It does not replace subsystem docs, formal contracts, governance policy, or
executable code.

## Layout

### `current/`

The frozen truthful reference architecture for `v0.1`.

Use `current/` for:

- the current technical philosophy
- the current runnable reference stack
- the current implementation posture
- current component boundaries and ownership rules
- the current implementation-aligned milestone sequence

Treat `current/` as the default current-truth lane for contributors, reviewers,
and runtime-aligned documentation.

### `future/`

The debated target architecture for `v1.0`.

Use `future/` for:

- architectural goals beyond the current reference stack
- proposed boundary or topology changes
- open questions and tradeoffs
- decisions under discussion

Treat `future/` as explicit proposal space. It should stay clearly separate from
what is already implemented or accepted in the frozen `v0.1` lane.

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
9. `current/pre-1.0-version-progression.md`
10. `decisions/debate-map.md`
11. `future/README.md` when you want the debated target lane

## Version mapping

Use these names consistently:

- `current/` = frozen `v0.1`
- `future/` = debated `v1.0`
- `decisions/` = cross-version doctrine and debate scaffolding

## Pre-1.0 policy

Use pre-`1.0` version numbers for accepted capability bundles, not for every
individual node, element, or partial implementation step.

That means:

- keep `v0.1` as the accepted current baseline until a broader runnable slice is
  explicitly promoted
- use milestones and implementation-status tracking for incremental compatible
  growth inside the current lane
- create a new `v0.x` only when the accepted reference slice changes in a way
  that materially expands the runnable system boundary
- keep `v1.0` for the point where the system is materially broader than the
  narrow first working slice

The older `../technical-architecture/` tree remains as a transitional pointer.
When there is any ambiguity, prefer the `current/` and `future/` entrypoints in
this directory.

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
