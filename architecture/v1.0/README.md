# Technical Architecture v1.0

## Purpose

Define the debated target architecture for Open Environmental Sensing and
Inference System beyond the current reference stack.

This directory is the canonical versioned home for debated `v1.0` architecture.
The older `../future/` lane remains available only as a compatibility pointer
for older links.

## Status

Debated target architecture.

`v1.0` is proposal space. It should capture stronger future architecture without
pretending that those changes are already implemented.

Future pre-`1.0` capability bundles may exist before `v1.0`, but they should be
promoted only when the accepted runnable slice changes materially. This lane
should not be used as a parking place for every minor compatible addition.

## Role

Use `v1.0/` for:

- target-lane architecture beyond the frozen `current/` `v0.1` slice
- stronger boundaries and product-shape proposals
- open questions, decisions, and tradeoffs specific to the debated lane
- future-lane docs that should stay separate from current implementation truth

## Relationship to other lanes

- `current/` = frozen `v0.1` current-truth architecture
- `v1.0/` = explicit versioned debated target lane
- `v1.5/` = explicit bridge-stage architecture notes
- `system/` = cross-version operating-model and roadmap narratives
- `decisions/` = cross-version doctrine and debate scaffolding

## Transition rule

If a document is really a cross-version system narrative, keep it in `../system/`.
If it is specifically describing the `v1.0` target lane, place it here rather
than in a non-versioned folder.

## Reading order

1. `../decisions/debate-map.md`
2. `goals-and-deltas.md`
3. `proposed-architecture.md`
4. `open-questions.md`
5. `decision-log.md`
6. `../system/product-requirements-phase-1.md`
7. `../system/phase-roadmap.md`
8. `../system/integrated-parcel-system-spec.md`
9. `../system/node-taxonomy.md`
10. `../system/architecture-gaps-by-stage.md`

## Target-lane core docs

Canonical cross-version bodies now live in `../system/` for:

- `product-requirements-phase-1.md`
- `phase-roadmap.md`
- `integrated-parcel-system-spec.md`
- `node-taxonomy.md`
- `architecture-gaps-by-stage.md`

The same filenames remain in `v1.0/` as compatibility redirects so older links
continue to resolve.

## Guardrail

Anything written in `v1.0/` should stay clearly separate from the implemented,
partial, docs-only, and planned classifications used for current reference
surfaces.

## Contributor rule

If a document changes the meaning of the current reference stack, move that
content back to `../current/`.

If a document proposes a stronger target lane, a new boundary, or a future
contract/runtime direction, keep it here.

## Transition note

`../future/` remains available as a redirect-only compatibility lane for older
links, but the preferred debated-lane path is now this explicit version
directory.
