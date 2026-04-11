# Open Source V1 Summary

## Purpose

State what "open source v1" means for the April 14, 2026 open-release period and give outside readers one canonical starting point for the current public release surface.

This summary is a release guide, not legal advice.

## What v1 means in this repository

For the current `v1.0` release:

- the public release surface is intentionally defined
- public materials point to canonical governance, privacy, and release docs
- each asset class has a clear intended or attached license direction
- contributors and reviewers can tell what is public now versus what remains outside release
- private homeowner-contributed parcel-linked data is not swept into the open-release story

This is the current open-release surface for v1, not a blanket release of every future artifact.

## Public now

The current release surface may include:

- mission, principles, and program overview
- technical architecture and modular system framing
- governance, privacy, and data-ownership posture
- claims, limitations, and safety-language boundaries
- contributor and stewardship posture
- release-direction and intended license posture by asset class
- reference software, firmware, hardware docs, schemas, examples, and approved media
- the project-controlled v1 dataset when it is intentionally designated and carries explicit dataset terms

See:

- `../../README.md`
- `../../NOTICE.md`
- `../../program/README.md`
- `../../legal/privacy/data-ownership.md`
- `../../legal/privacy/privacy.md`
- `../../legal/privacy/claims-and-safety-language.md`
- `../../legal/GOVERNANCE.md`
- `../../legal/dataset-release-policy.md`
- `../../legal/ip.md`

## Not public by default

The following are not automatically part of the public v1 surface:

- secrets, credentials, or access tokens
- non-cleared third-party data or licensed materials
- intentionally excluded technical artifacts still governed by `holdback-list.md`
- future participant-contributed parcel-linked datasets
- trademarks, trade dress, or branding rights unless expressly granted

See:

- `../../legal/public-preview-scope.md`
- `../../legal/holdback-list.md`

## Asset classes and release posture

The repository uses an asset-class model rather than one blanket repo license.

Current working direction:

- platform and service software: `AGPLv3-or-later`
- firmware: `AGPLv3-or-later` unless final review selects a narrower copyleft software license
- hardware design files: `CERN-OHL-S v2`
- documentation and governance text: `CC BY-SA 4.0`
- synthetic example datasets and test fixtures: dataset-specific terms approved for release
- project-controlled v1 dataset and approved public snapshots: dataset-specific terms
- future participant-contributed parcel-linked data: not open by default

See:

- `../../LICENSES.md`
- `asset-class-license-and-publication-matrix.md`

## Non-negotiable v1 boundaries

Open release of code, hardware, docs, or an intentionally public dataset does not mean:

- every technical material is public
- every file in the repository is under one identical license
- future participant parcel-linked data becomes open data
- separately withheld materials are granted by implication
- the project is claiming emergency authority, guaranteed safety, or official alerts

## Contributor and reviewer expectations

Contributors and reviewers should be able to answer these questions before publishing, linking, or merging public-facing material:

1. Is the material inside the current public release scope?
2. Does it expose any non-release or held-back technical detail?
3. Does it include or imply rights to real homeowner-contributed parcel-linked data?
4. Does it match the governing asset-class license or notice?
5. Does it preserve the project's claims, privacy, and governance boundaries?

Use:

- `contributor-and-review-guide.md`
- `../../legal/contribution-policy/README.md`
- `../../legal/GOVERNANCE.md`

## Canonical reading order

For the v1 public surface, start here:

1. `../../README.md`
2. `../../NOTICE.md`
3. `open-source-v1-summary.md`
4. `asset-class-license-and-publication-matrix.md`
5. `contributor-and-review-guide.md`
6. `../../legal/privacy/data-ownership.md`
7. `../../legal/privacy/privacy.md`
8. `../../legal/privacy/claims-and-safety-language.md`
9. `../../legal/GOVERNANCE.md`
10. `../../legal/ip.md`

## Why this document exists

This file ties the repository notice, program notice, release notice, website, and asset-class license plan together in one public explanation.

If a public-facing page or README needs one link that explains the v1 open-release posture, link to this file first.
