# Review Rubric

## Core Rule

Prefer removing ambiguity over removing files. A lean directory is one where each path has a clear reason to exist, a clear owner, and a clear audience.

## Classify Findings By Confidence

### High-confidence cleanup

Use this class for paths that are almost never intentional source:

- OS or editor cruft such as `.DS_Store`
- runtime or test caches such as `__pycache__`, `.pytest_cache`, and `.ruff_cache`
- local dependency installs such as `node_modules`
- generated build output such as `dist`, `build`, and `.pio`
- compiled artifacts such as `*.pyc`

Default action: delete locally and ensure the path is ignored if it should not be tracked.

### Merge or move candidates

Use this class when the path may be valid but its placement or duplication is suspicious:

- two files serve the same audience with nearly identical content
- a wrapper script and a library module have drifted into parallel implementations
- a cross-cutting convention lives inside one subsystem instead of `shared/`
- a planning note or milestone doc lives outside `meta/`
- a release or export directory mixes authored source with generated output

Default action: identify the canonical owner, then merge or move in the smallest diff possible.

### Needs intent confirmation

Use this class when deletion or consolidation could remove legitimate structure:

- repeated filenames under intentionally parallel subsystem trees
- versioned release artifacts that may be public deliverables
- legal, notice, or policy documents repeated for distribution boundaries
- docs that look thin but exist for navigation or external linking stability
- package entrypoints or CLI shims that intentionally mirror library modules

Default action: explain the tradeoff and ask for confirmation only if the next edit would be risky.

## Questions To Ask Per Candidate

1. Does this path contain original information, or only generated state?
2. If it disappeared, would any consumer lose necessary context or behavior?
3. Is there already another canonical file that owns the same concern?
4. Does the directory boundary express a real concern, audience, or lifecycle?
5. Is this duplication audience-specific, packaging-specific, or merely accidental?
6. Would moving this file improve separation of concerns without increasing indirection?

## Repo-Specific Heuristics

- Keep repo-wide templates, glossary material, standards, and reusable skills under `shared/`.
- Keep planning, manifests, milestones, and ADRs under `meta/`.
- Treat `programs/resilient-home-intelligence/` as the primary authored product tree.
- Treat `rhi/` as the canonical Python package implementation and inspect same-named files under `programs/.../software/**/scripts/` as possible wrappers before merging them.
- Treat repeated filenames under `hardware/*` and `software/*` as intentional symmetry until content proves they are redundant.
- Treat `programs/resilient-home-intelligence/docs/release/**/site/` as a mixed source/output area that deserves extra care before deleting anything.
- Update `meta/repo-manifest.md` after accepted structure changes because this repo keeps an explicit map of tracked canonical files.

## Safe Order Of Operations

1. Remove high-confidence cruft.
2. Add or tighten ignore rules for generated paths if needed.
3. Merge exact duplicates.
4. Move misplaced files into the correct concern boundary.
5. Rename or flatten directories only after the canonical structure is stable.
