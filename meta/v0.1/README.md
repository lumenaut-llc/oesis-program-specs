# Meta

Planning, decisions, milestones, and coordination artifacts that apply to the whole repo.

This folder also holds tracked starter-package context under `../starter-package/`
so bootstrap and prompt files do not live only outside the repo.

## Lane contract

- **Baseline lane**: `v0.1/` docs are the active planning and coordination
  surfaces.
- **Additive lanes**: create explicit versioned planning folders only when
  planning tracks materially diverge by lane.
- **Compatibility policy**: when planning docs move, keep brief redirect stubs
  for frequently referenced paths.
- **Canonical mapping**: release/version language in planning docs should align
  with `../../architecture/system/version-and-promotion-matrix.md`.

## Mutation rule

Do not silently overwrite historical planning intent in place when a newer lane
changes direction. Either update with explicit status markers or add lane-scoped
planning docs.
