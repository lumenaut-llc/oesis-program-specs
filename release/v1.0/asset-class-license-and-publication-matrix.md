# Asset-Class License And Publication Matrix

## Purpose

Turn the repository licensing plan into a reviewer-friendly v1 reference that explains what is public now, what terms apply, and what still requires separate release review.

This matrix is a release guide, not legal advice.

## How to read this matrix

- `Public now` means the asset class can appear in the April 14, 2026 preview if it stays inside `../../../legal/public-preview-scope.md`.
- `Held back` means the asset class or subset is outside the current public preview unless separately cleared.
- `Intended terms` describes the current release direction and should be read together with `../../../LICENSES.md`.

## Matrix

| Asset class | Example locations | Public status for v1 | Intended terms | Notes |
| --- | --- | --- | --- | --- |
| Program and platform software | `software/`, future public service code, public tooling | Limited public direction now; full enabling release later | `AGPLv3-or-later` | Public preview may describe software posture, but not publish held-back implementation details tied to the filing candidate. |
| Firmware | `hardware/*/firmware/` | Limited public direction now; full enabling release later | `AGPLv3-or-later` unless final review selects a narrower copyleft software license | Treat firmware like software for preview scope and holdback review. |
| Hardware design files | hardware CAD, schematics, PCB layouts, fabrication files | High-level overview only during preview | `CERN-OHL-S v2` | Full design packages are held back until release sequencing clears them. |
| Documentation and governance text | `README.md`, `docs/`, `legal/`, preview docs | Public now if inside preview scope | `CC BY-SA 4.0` | Public-facing docs should point to canonical policy docs rather than improvise rights statements. |
| Synthetic examples and test fixtures | synthetic docs, examples, benchmarks, demo fixtures | Public now if clearly synthetic and rights-clean | Dataset-specific approved terms such as `CDLA Permissive 2.0` or `CC BY 4.0` | Mark synthetic examples clearly so they are not confused with real parcel-linked data. |
| Redistributed public reference datasets | upstream public weather, smoke, map, or hazard sources | Public only under upstream source terms and pass-through notices | Upstream source terms | Do not relabel third-party data as project-owned open data. |
| Approved public shared-dataset snapshots | future released derived snapshots | Case-by-case only | Dataset-specific terms, potentially including `ODbL` where actually appropriate | Requires separate review before publication. |
| Real homeowner-contributed parcel-linked data | private parcel observations, parcel-linked history, household-linked outputs | Not public in v1 | Not covered by a blanket open-data license | Privacy and ownership controls override any broad reading of "open source." |
| Held-back technical materials | withheld code, detailed methods, thresholds, packet contracts, detailed CAD | Not public in v1 | No public grant beyond applicable notices | Governed by `../../../legal/public-preview-scope.md` and `../../../legal/holdback-list.md`. |
| Names, logos, and branding | project names, marks, visual identity | Public reference only unless separately granted | No trademark or branding license unless expressly stated | Open copyright licensing does not imply trademark permission. |

## V1 interpretation rules

Use these rules when classifying a file or folder:

1. If the file contains held-back technical detail, it is not part of the public v1 surface even if the surrounding folder is public.
2. If the file contains real homeowner-contributed parcel-linked data, it is not part of the general open-release story.
3. If the file depends on upstream third-party data, keep the upstream terms attached and visible.
4. If a more specific file notice exists, that notice controls.
5. If no final per-file license is attached yet, treat `LICENSES.md` as the intended asset-class direction rather than a blanket legal grant.

## Reviewer questions

Before calling an asset "open" in v1, confirm:

- Is the asset class public now, or only described as a future release class?
- Does the intended term match the asset class?
- Does the file stay inside the preview scope?
- Does any more specific notice override the matrix?
- Would an outside reader misunderstand this asset as permission to use withheld methods or private data?

## Related documents

- `open-source-v1-summary.md`
- `open-release-v1-audit-checklist.md`
- `../../../LICENSES.md`
- `../../../legal/ip.md`
- `../../../legal/public-preview-scope.md`
- `../../../legal/holdback-list.md`
