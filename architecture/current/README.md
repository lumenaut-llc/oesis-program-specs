# Technical Architecture v0.1

## Purpose

Define the current truthful reference architecture for Open Environmental
Sensing and Inference System.

`v0.1` is the architecture of the current reference stack. It should describe
what is real now, what is only partial, and what remains docs-only or planned.

## Status

Current reference architecture.

Use this version when you need the architecture that matches the present
implementation boundary rather than future proposals.

This directory is the frozen `v0.1` lane. New future-looking architecture work
should go to `../future/` instead of mutating these current-truth files.

Pre-`1.0` growth should normally be tracked through milestones and status
classification rather than a new version number for every added node or
element.

## Scope

`v0.1` covers:

- the current technical philosophy
- the current collection-to-parcel reference stack
- the minimum functioning first-version slice
- the current architecture object map
- current ownership of implementation, docs, contracts, and policy surfaces
- the implementation boundary reflected in the current reference checks
- the current milestone sequence that fits the implemented reference posture

## Reading order

1. `technical-philosophy.md`
2. `reference-stack.md`
3. `minimum-functioning-v0.1.md`
4. `architecture-object-map.md`
5. `implementation-posture.md`
6. `component-boundaries.md`
7. `milestone-roadmap.md`
8. `pre-1.0-version-progression.md`

## Primary source alignment

`v0.1` should stay aligned with:

- `../../architecture/system/technical-philosophy-and-architecture.md`
- `../../architecture/system/integrated-parcel-system-spec.md`
- `../../software/README.md`
- `../../release/v.0.1/implementation-status-matrix.md`

## Contributor rule

If a change describes what is implemented, accepted, or currently runnable, it
belongs here.

If a change describes a target architecture, future boundary, or debated
expansion, it belongs in `../future/`.

If a change is incremental but still compatible with the current accepted slice,
prefer updating milestone and implementation-posture docs before proposing a new
`v0.x`.
