# OESIS Build Decision

## Decision

Keep `oesis_build/` inside the specs repository for now.

## Status

Current split-stage decision.

## Reasoning

`oesis_build/` is still tightly coupled to program-definition concerns:

- canonical source selection
- repository link generation
- release-packet assembly scaffolding
- site publication support

At the current maturity level, splitting it into a fourth repository would add:

- another artifact boundary to maintain
- another release sequence to coordinate
- more cross-repo path and version management before the first three-repo split is stable

## Re-evaluation gate

Revisit a dedicated `oesis-build` repository only after all of the following are true:

1. `oesis-runtime` is operating independently and consuming published contract bundles.
2. `oesis-public-site` is operating independently and consuming published public-content bundles.
3. `oesis-program-specs` is producing bundles and release artifacts without relying on staged compatibility mirrors.
4. `oesis_build/` has at least one consumer beyond the current OESIS program-specs repository.

## Near-term rule

Until those gates are met:

- keep `oesis_build/` in this repository
- treat it as specs-side build and publication infrastructure
- optimize for clear artifact boundaries rather than an additional repo split
