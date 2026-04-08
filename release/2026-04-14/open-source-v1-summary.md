# Open Source V1 Summary

## Purpose

State what "open source v1" means for the April 14, 2026 public preview and give outside readers one canonical starting point for the public release surface.

This summary is a release guide, not legal advice.

## What v1 means in this repository

For this preview, `v1` means:

- the public release surface is intentionally defined
- public materials point to canonical governance, privacy, and release docs
- each asset class has a clear intended license direction
- contributors and reviewers can tell what is public now versus what remains held back
- private homeowner-contributed parcel-linked data is not swept into the open-release story

This is not yet the full enabling technical open release.

## Public now

The April 14 public preview may include:

- mission, principles, and program overview
- high-level architecture and modular system framing
- governance, privacy, and data-ownership posture
- claims, limitations, and safety-language boundaries
- contributor and stewardship posture
- release-direction and intended license posture by asset class
- selected non-enabling media and overview documentation

See:

- `README.md`
- `NOTICE.md`
- `../../privacy-governance/data-ownership.md`
- `../../privacy-governance/privacy.md`
- `../../privacy-governance/claims-and-safety-language.md`
- `../../../legal/GOVERNANCE.md`
- `../../../legal/public-preview-scope.md`
- `../../../legal/ip.md`

## Not public yet

During the preview period, the project is not treating the following as part of the public v1 surface:

- implementation-enabling source code tied to the narrow filing candidate
- detailed packet contracts, decision logic, thresholds, or scoring rules
- detailed privacy-preserving neighborhood-sharing mechanics
- full schematics, PCB layouts, fabrication files, or detailed CAD tied to withheld internals
- calibration and tuning procedures that materially enable reproduction
- real homeowner-contributed parcel-linked datasets

See:

- `../../../legal/public-preview-scope.md`
- `../../../legal/holdback-list.md`

## Asset classes and release posture

The repository uses an asset-class model rather than one blanket repo license.

Current working direction:

- platform and service software: `AGPLv3-or-later`
- firmware: `AGPLv3-or-later` unless final review selects a narrower copyleft software license
- hardware design files: `CERN-OHL-S v2`
- documentation and governance text: `CC BY-SA 4.0`
- synthetic datasets and test fixtures: dataset-specific terms approved for release
- real homeowner-contributed parcel-linked data: not open by default

See:

- `../../../LICENSES.md`
- `asset-class-license-and-publication-matrix.md`

## Non-negotiable v1 boundaries

Open release of code, hardware, or docs does not mean:

- all technical materials are already public
- all files in the repository are under one identical license
- private homeowner data becomes open data
- preview publication grants rights in withheld materials
- the project is claiming emergency authority, guaranteed safety, or official alerts

## Contributor and reviewer expectations

Contributors and reviewers should be able to answer these questions before publishing, linking, or merging public-facing material:

1. Is the material inside the public preview scope?
2. Does it expose held-back technical detail?
3. Does it include or imply rights to real homeowner-contributed parcel-linked data?
4. Does it match the governing asset-class license or notice?
5. Does it preserve the project's claims, privacy, and governance boundaries?

Use:

- `contributor-and-review-guide.md`
- `../../../legal/contribution-policy/README.md`
- `../../../legal/GOVERNANCE.md`

## Canonical reading order

For the v1 public surface, start here:

1. `README.md`
2. `NOTICE.md`
3. `open-source-v1-summary.md`
4. `asset-class-license-and-publication-matrix.md`
5. `../../privacy-governance/data-ownership.md`
6. `../../privacy-governance/privacy.md`
7. `../../privacy-governance/claims-and-safety-language.md`
8. `../../../legal/GOVERNANCE.md`
9. `../../../legal/public-preview-scope.md`
10. `../../../legal/ip.md`

## Why this document exists

This file is the short explanation that ties the repository notice, program notice, release notice, site entrypoint, and asset-class license plan together.

If a public-facing page or README needs one link that explains the v1 open-release posture, link to this file first.
