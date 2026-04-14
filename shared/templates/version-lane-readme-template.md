# Version-lane README template

Use this structure for top-level directories that need architecture-style lane
semantics.

## Purpose

State what this subtree is authoritative for.

## Lane contract

- **Baseline lane**: root/unversioned paths (accepted default, typically `v0.1`)
- **Additive lanes**: `v1.0/`, `v1.5/`, etc. (forward deltas only)
- **Compatibility lanes**: redirect-only aliases for older links
- **Canonical lane**: where readers should prefer current truth for this topic

If prose labels and filesystem paths differ (for example label `v0.1` at path
`v.0.1/`), document both explicitly.

## Mutation rule

Do not silently replace baseline files with future-lane content. Put forward
changes in additive lanes or explicit redirect stubs.

## Status labels

When useful, tag docs with:

- `implemented`
- `partial`
- `docs-only`
- `planned`

## Related references

Link to:

- `architecture/system/version-and-promotion-matrix.md`
- `architecture/system/node-taxonomy.md` (if relevant)
- any canonical lane README for this subtree
