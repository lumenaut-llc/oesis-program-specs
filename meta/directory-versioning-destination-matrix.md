# Directory versioning destination matrix

This matrix defines canonical destinations for the directory-versioning rollout.
Legacy root paths remain as compatibility stubs.

## Conventions

- **Baseline lane**: `v0.1/`
- **Additive lanes**: `v1.0/`, `v1.5/`
- **Compatibility**: old path becomes a redirect stub

## Top-level directory mapping

| Directory | Current canonical path | Canonical destination | Legacy path action |
| --- | --- | --- | --- |
| `contracts/` | `contracts/README.md` | `contracts/v0.1/README.md` | keep `contracts/README.md` as redirect |
| `contracts/` schemas index | `contracts/schemas/README.md` | `contracts/v0.1/schemas/README.md` | keep old file as redirect |
| `contracts/` examples index | `contracts/examples/README.md` | `contracts/v0.1/examples/README.md` | keep old file as redirect |
| `artifacts/` | `artifacts/README.md` | `artifacts/v0.1/README.md` | keep `artifacts/README.md` as redirect |
| `release/` | `release/README.md` | `release/v0.1/README.md` (lane contract) | keep `release/README.md` as redirect |
| `software/` | `software/README.md` | `software/v0.1/README.md` | keep `software/README.md` as redirect |
| `hardware/` | `hardware/README.md` | `hardware/v0.1/README.md` | keep `hardware/README.md` as redirect |
| `operations/` | `operations/README.md` | `operations/v0.1/README.md` | keep `operations/README.md` as redirect |
| `legal/` | `legal/README.md` | `legal/v0.1/README.md` | keep `legal/README.md` as redirect |
| `media/` | `media/README.md` | `media/v0.1/README.md` | keep `media/README.md` as redirect |
| `program/` | `program/README.md` | `program/v0.1/README.md` | keep `program/README.md` as redirect |
| `meta/` | `meta/README.md` | `meta/v0.1/README.md` | keep `meta/README.md` as redirect |

## Explicit exclusions (this pass)

- Do not move release packet files or subsystem-specific deep content trees in
  this pass.
- This rollout prioritizes canonical lane contracts and contract baseline
  docs/assets first, then updates references repo-wide.
