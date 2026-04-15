# Software v0.3

`v0.3` is a promotion lane marker for the first flood-capable runtime.

## Software posture

- Inherit baseline software docs from `../v0.1/`.
- Add files here only if a `v0.3`-specific software delta is explicitly accepted.
- Until such a delta exists, this directory is intentionally lightweight.

## What v0.3 means for software

- Flood observation family (`flood.low_point.snapshot`) in ingest normalization
- Flood hazard probability in the inference engine
- Parcel-state reflects flood-relevant conditions where flood-node is installed
- Three observation families composable in a single parcel

## How to use this lane

- For current work, use `../v0.1/` and the root-level subsystem directories.
- Add files in this lane only when a concrete `v0.3` software delta is accepted.
- Do not copy `v0.1` files here by default.

## Related

- `../v0.2/README.md`
- `../../release/v0.3/README.md`
- `../inference-engine/architecture.md`
