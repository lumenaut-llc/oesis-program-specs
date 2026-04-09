# Licensing plan

This file is the working licensing matrix for the repository structure and April 14, 2026 open-release posture.

For a shorter v1-facing explanation, see `release/v1.0/asset-class-license-and-publication-matrix.md`.

It is a project planning document, not legal advice.

## Recommended split

- platform and service software: AGPLv3-or-later
- firmware: AGPLv3-or-later unless a narrower final review selects a different copyleft software license
- hardware design files: CERN-OHL-S v2
- documentation, specifications, and governance text: CC BY-SA 4.0
- synthetic example datasets and test fixtures: CDLA Permissive 2.0, CC BY 4.0, or other dataset-specific terms approved for the release
- project-controlled v1 parcel dataset and approved public shared-dataset snapshots, if any: CDLA-Sharing-1.0 unless a later documented dataset decision selects different terms
- redistributed public reference datasets: keep under upstream source terms with attribution and pass-through notices
- future participant-contributed parcel-linked datasets: not open by default and not covered by a blanket repository-wide open-data license

## Current release note

During the current April 14 release:

- this matrix describes the intended public license split for approved release artifacts
- archival provisional-planning materials remain internal and are not public release assets by default
- no blanket open-data license applies to future participant-contributed parcel-linked data
- the project-controlled v1 dataset may be intentionally released under explicit dataset terms

## Rationale

- `AGPLv3-or-later` best matches the current commons-protective direction for platform and networked service code where preventing quiet enclosure matters more than frictionless proprietary adoption.
- applying the same copyleft software direction to firmware keeps the message simpler during release, while still leaving room for final legal review if a narrower firmware-specific license choice is preferred.
- `CERN-OHL-S v2` fits open hardware designs where improvements should remain in the commons.
- `CC BY-SA 4.0` fits the current direction for documentation and governance text where the goal is to keep adapted public documentation in the commons rather than maximize permissive reuse.
- `CDLA-Sharing-1.0` fits the current goal for the project-controlled v1 dataset because it supports open reuse while pushing modifications and published downstream versions to stay open.
- future participant-contributed parcel-linked environmental data should not be forced into a blanket open-data license because that would overrule owner control for later contributors who did not opt into a public release.

## Data licensing guardrails

- Do not imply that participation in neighborhood sharing grants the public a right to reuse future participant parcel-linked data.
- Treat the project-controlled v1 dataset as an explicitly chosen public artifact, not as proof that all future parcel-linked data is open by default.
- Include provenance, scope notes, and licensing text with any public dataset release.
- If a future participant, pilot, or research dataset is ever released, it should be governed by a separate review and dataset-specific terms rather than the repository-wide license file.

## Open questions still reserved for final legal review

- whether firmware should remain aligned with `AGPLv3-or-later` or move to a different copyleft software license
- whether later public shared-dataset releases should remain on `CDLA-Sharing-1.0` or move to another dataset-specific license such as `ODbL`
- whether any future patent non-assert or additional patent grant language should accompany the final release
- how trademark and certification rules should be stated alongside the copyright licenses

These choices are a working product-governance recommendation, not legal advice.
