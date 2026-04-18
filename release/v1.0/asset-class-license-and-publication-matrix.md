# Asset-Class License And Publication Matrix

## Purpose

Turn the repository licensing plan into a reviewer-friendly v1 reference that explains what is public now, what terms apply, and what still requires separate release review.

This matrix is a release guide, not legal advice.

## How to read this matrix

- `Public status` describes whether the asset class is currently part of the public v1 release surface.
- `Intended terms` describes the current release direction and should be read together with `../../LICENSES.md`.
- `Not public by default` means the asset class is separately governed or requires explicit release designation before publication.

## Matrix

| Asset class | Example locations | Public status for v1 | Intended terms | Notes |
| --- | --- | --- | --- | --- |
| Program and platform software | `software/`, `contracts/`, released reference tooling | Public when intentionally included in the release surface | `AGPLv3-or-later` | Public software should carry clear notices and remain consistent with the current release scope. |
| Firmware | [`oesis-hardware`](https://github.com/lumenaut-llc/oesis-hardware)`/*/firmware/` | Public when intentionally included in the release surface | `AGPLv3-or-later` unless final review selects a narrower copyleft software license | Treat firmware like software for release-scope review and provenance checks. Lives in the separate `oesis-hardware` repository. |
| Hardware design files | [`oesis-hardware`](https://github.com/lumenaut-llc/oesis-hardware): node READMEs, build guides, wiring, calibration, firmware notes, released CAD/docs | Public when intentionally included in the release surface | `CERN-OHL-S v2` | Hardware design packages are open only to the extent the released files and notices make clear. Lives in the separate `oesis-hardware` repository. |
| Documentation and governance text | `README.md`, `program/`, `architecture/`, `release/`, `legal/` | Public when intentionally included in the release surface | `CC BY-SA 4.0` | Public docs should point to canonical policy and scope documents rather than improvised summaries. |
| Synthetic examples and test fixtures | [`v0.1/examples/`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/examples/), examples in `oesis-runtime`, synthetic fixtures | Public when clearly synthetic and rights-clean | Dataset-specific approved terms such as `CDLA Permissive 2.0`, `CC BY 4.0`, or another approved release term | Keep synthetic examples clearly marked so they are not confused with real parcel-linked data. |
| Project-controlled v1 dataset and approved public snapshots | intentionally designated dataset bundles | Public only when explicitly designated and licensed | Dataset-specific terms such as `CDLA-Sharing-1.0` | A dataset becomes public because it is intentionally released under explicit terms, not because the rest of the project is open. |
| Redistributed public reference datasets | upstream weather, smoke, map, or hazard sources | Public only under upstream source terms and pass-through notices | Upstream source terms | Do not relabel third-party data as project-owned open data. |
| Future participant-contributed parcel-linked datasets | future parcel operator or pilot participant data | Not public by default | Not covered by a blanket repository-wide open-data license | Privacy and ownership controls override any broad reading of \"open source.\" |
| Non-release materials | secrets, non-cleared third-party data, internal historical planning artifacts | Not public by default | No public grant beyond applicable notices | Governed by `../../legal/public-preview-scope.md`, `../../legal/holdback-list.md`, and release-owner checks. |
| Names, logos, and branding | project names, marks, visual identity | Public reference only unless separately granted | No trademark or branding license unless expressly stated | Open copyright licensing does not imply trademark permission. |

## V1 interpretation rules

Use these rules when classifying a file or folder:

1. If the file is intentionally released and carries or inherits the applicable asset-class term, it may be part of the public v1 surface.
2. If the file contains future participant parcel-linked data, it is not part of the general open-release story by default.
3. If the file depends on upstream third-party data, keep the upstream terms attached and visible.
4. If a more specific file notice exists, that notice controls.
5. If no final per-file license is attached yet, treat `LICENSES.md` as the intended asset-class direction rather than a blanket legal grant.

## Reviewer questions

Before calling an asset "open" in v1, confirm:

- Is the asset intentionally included in the current release surface?
- Does the intended term match the asset class?
- Does any more specific notice override the matrix?
- Is any dataset explicitly designated and licensed, rather than implied public?
- Would an outside reader misunderstand this asset as permission to use non-release materials or private data?

## Related documents

- `open-source-v1-summary.md`
- `open-release-v1-audit-checklist.md`
- `../../LICENSES.md`
- `../../legal/ip.md`
- `../../legal/public-preview-scope.md`
- `../../legal/holdback-list.md`
