# Artifacts

Generated and publication-bundle artifacts that are derived from canonical docs,
schemas, and examples elsewhere in the repository.

## Lane contract

- **Baseline lane**: `contracts-bundle/` and sibling artifact paths generated for
  the accepted default surface.
- **Additive lanes**: add versioned artifact directories (for example `v1.0/`,
  `v1.5/`) when bundles diverge by lane.
- **Compatibility lanes**: when artifact paths move, keep short redirect stubs
  or index pointers so old links still resolve.
- **Canonical source of truth**: `architecture/`, `contracts/`,
  `software/`, `release/`, and [oesis-hardware](https://github.com/lumenaut-llc/oesis-hardware) remain normative; `artifacts/` is derivative.

## Mutation rule

Do not treat generated artifact files as canonical architecture or contract
truth. Update the source lanes first, then regenerate artifact bundles.

## Current contents

- `contracts-bundle/` — deployment-maturity companion schemas and examples
  staged alongside contract publication material.

## Related

- [`v0.1/README.md`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/README.md)
- `../../architecture/system/version-and-promotion-matrix.md`
- `../../oesis_build/`
