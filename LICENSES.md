# Licensing plan

This file is the working licensing matrix for the repository structure and April 14, 2026 preview posture.

It is a project planning document, not legal advice.

## Recommended split

- platform and service software: AGPLv3-or-later
- firmware: AGPLv3-or-later unless a narrower final review selects a different copyleft software license
- hardware design files: CERN-OHL-S v2
- documentation, specifications, and governance text: CC BY-SA 4.0
- synthetic example datasets and test fixtures: CDLA Permissive 2.0, CC BY 4.0, or other dataset-specific terms approved for the release
- approved public shared-dataset snapshots, if any: dataset-specific terms, potentially including ODbL where actually appropriate
- redistributed public reference datasets: keep under upstream source terms with attribution and pass-through notices
- real homeowner-contributed parcel-linked datasets: not open by default and not covered by a blanket open-data license

## Preview-phase note

During the April 14 preview:

- this matrix describes intended release direction, not a guarantee that every asset class is fully published yet
- held-back technical materials remain outside publication until separately cleared
- no blanket open-data license applies to real homeowner-contributed parcel-linked data

## Rationale

- `AGPLv3-or-later` best matches the current commons-protective direction for platform and networked service code where preventing quiet enclosure matters more than frictionless proprietary adoption.
- applying the same copyleft software direction to firmware keeps the message simpler during preview, while still leaving room for final legal review if a narrower firmware-specific license choice is preferred.
- `CERN-OHL-S v2` fits open hardware designs where improvements should remain in the commons.
- `CC BY-SA 4.0` fits the current direction for documentation and governance text where the goal is to keep adapted public documentation in the commons rather than maximize permissive reuse.
- public shared-dataset releases need dataset-specific review because some cases may fit `ODbL`, while other cases may be better handled by narrower or source-specific terms.
- Real parcel-linked environmental contributions should not be forced into an open-data license because that conflicts with the platform's private-by-default and opt-in-sharing commitments.

## Data licensing guardrails

- Do not publish real homeowner-contributed raw sensor data under `ODbL`, `CC BY`, or similar open terms in early versions.
- Do not imply that participation in neighborhood sharing grants the public a right to reuse parcel-linked data.
- Treat synthetic examples, benchmark fixtures, and clearly non-sensitive derived demo datasets as the primary open dataset targets.
- If a research or pilot dataset is ever released, it should be governed by a separate review and dataset-specific terms rather than the repository-wide license file.

## Open questions still reserved for final legal review

- whether firmware should remain aligned with `AGPLv3-or-later` or move to a different copyleft software license
- whether any public shared-dataset release in practice should use `ODbL`
- whether any future patent non-assert or additional patent grant language should accompany the final release
- how trademark and certification rules should be stated alongside the copyright licenses

These choices are a working product-governance recommendation, not legal advice.
