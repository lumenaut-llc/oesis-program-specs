# Licensing

## Purpose

Define the licensing structure for code, hardware, documentation, and datasets without undermining homeowner data ownership or privacy commitments.

## Working split

- platform and service software: AGPLv3-or-later
- firmware: AGPLv3-or-later pending final legal review
- hardware design files: CERN-OHL-S v2
- documentation/specifications/governance text: CC BY-SA 4.0
- synthetic examples and test datasets: CDLA Permissive 2.0, CC BY 4.0, or other dataset-specific approved terms
- approved public shared-dataset snapshots: dataset-specific terms, potentially including ODbL where appropriate
- real homeowner-contributed parcel-linked data: separate contractual/data-governance treatment, not a blanket open license

## Release note

For the v0.1 release, this split expresses intended release direction.

It does not mean:

- every asset class is already publicly released
- held-back technical files are approved for publication
- private homeowner data becomes open because the project is open source

## Rules

- repository code licenses do not override source terms for imported public datasets
- no open-data license should be applied by default to real household-contributed data
- future trademark, certification, or compatibility rules should live outside the copyright license itself

## Why this split changed

The repo earlier used a more permissive MVP recommendation. The current release direction is intentionally more commons-protective:

- stronger copyleft for platform code
- reciprocal open-hardware terms for hardware design files
- share-alike terms for public documentation and governance text
- dataset-specific handling for any public shared-data release

## Final-review questions

- should firmware stay aligned with AGPLv3-or-later or move to a different copyleft software license
- whether any future public shared dataset should use ODbL in practice
- what patent and trademark statements should accompany the final open release

## Next docs to add

- dataset release policy
- third-party data source notice template
- trademark and certification policy
