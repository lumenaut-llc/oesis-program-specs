# Contributing

Thank you for helping with OESIS program specifications, contracts, and release materials.

## Before you open a pull request

1. Read [`NOTICE.md`](NOTICE.md) and [`LICENSES.md`](LICENSES.md).
2. Follow the reviewer-oriented guide [`release/v1.0/contributor-and-review-guide.md`](release/v1.0/contributor-and-review-guide.md).
3. Confirm your changes match the license terms that apply to the paths you touch:
   - Most documentation and specifications in this repository are under **Creative Commons Attribution-ShareAlike 4.0 International** ([`LICENSE`](LICENSE)).
   - Code under [`software/`](software/) and tests is under **GNU Affero General Public License v3.0** ([`software/LICENSE`](software/LICENSE)).
   - Hardware design materials under [`hardware/`](hardware/) are under **CERN-OHL-S-2.0** ([`hardware/LICENSE`](hardware/LICENSE)); **firmware source** in that subtree follows **GNU AGPL v3** ([`software/LICENSE`](software/LICENSE)) per [`LICENSES.md`](LICENSES.md) and [`hardware/NOTICE.md`](hardware/NOTICE.md).
4. If a file has a more specific notice or license statement, that statement controls for that material (see [`NOTICE.md`](NOTICE.md)).

## Governance and privacy

Privacy, data ownership, and publication boundaries are documented under [`legal/`](legal/). Do not include secrets, non-cleared third-party data, or real participant parcel-linked data unless explicitly part of an approved public release.

## Sibling repositories

The runnable Python reference implementation lives in **[oesis-runtime](https://github.com/lumenaut-llc/oesis-runtime)**. The public preview site lives in **[oesis-public-site](https://github.com/lumenaut-llc/oesis-public-site)**. Align cross-repo changes with those checkouts when needed.
