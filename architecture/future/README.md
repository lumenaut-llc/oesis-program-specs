# Technical Architecture v1.0

## Purpose

Define the debated target architecture for Open Environmental Sensing and
Inference System beyond the current reference stack.

## Status

Debated target architecture.

`v1.0` is proposal space. It should capture stronger future architecture without
pretending that those changes are already implemented.

This directory is the explicit `v1.0` lane. It exists beside the frozen
`../current/` `v0.1` lane so the project can debate and prototype future
architecture without rewriting current truth.

Future pre-`1.0` capability bundles may exist before `v1.0`, but they should be
promoted only when the accepted runnable slice changes materially. This
directory should not be used as a parking place for every minor compatible
addition.

## Reading order

1. `../debate-map.md`
2. `goals-and-deltas.md`
3. `proposed-architecture.md`
4. `open-questions.md`
5. `decision-log.md`

## Guardrail

Anything written in `v1.0/` should stay clearly separate from the implemented,
partial, docs-only, and planned classifications used for current reference
surfaces.

## Contributor rule

If a document changes the meaning of the current reference stack, move that
content back to `../current/`.

If a document proposes a stronger target lane, a new boundary, or a future
contract/runtime direction, keep it here.
