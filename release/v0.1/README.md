# Release

Release-packet lanes and publication controls for program-specs materials.

## Lane contract

- **Baseline lane**: release label **`v0.1`** is canonical at `v0.1/` in this
  subtree.
- **Archived compatibility lane**: earlier preview packet materials remain in
  `v.0.1/` for historical diffs and link compatibility.
- **Additive lanes**: `v1.0/`, `v1.5/`, and later lanes carry forward packet
  deltas without mutating older release packets.
- **Compatibility policy**: when prose label (`v0.1`) and legacy filesystem
  path (`v.0.1/`) differ, spell both explicitly and keep redirect pointers for
  old links.
- **Canonical scope mapping**: release labels must stay aligned with
  `../../architecture/system/version-and-promotion-matrix.md`.

## Mutation rule

Do not overwrite prior release-lane packet files with later-lane wording.
Create or update the proper version lane instead.

## Related

- `../../program/v0.1/README.md`
- `../../architecture/system/version-and-promotion-matrix.md`
- `../../architecture/current/pre-1.0-version-progression.md`
