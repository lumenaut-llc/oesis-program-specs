# IP and Release Position

## Purpose

State the project's current intellectual-property and release posture for the April 14, 2026 open-release period.

This file is a project policy draft and release-planning statement. It is not legal advice.

## Current posture

Resilient Home Intelligence is being released under a commons-protective open-release posture across software, hardware, documentation, and approved public artifacts.

The project is not currently using a provisional-first sequence for v1.

The current intended sequencing is:

- open publication of the current technical release
- deliberate defensive publication of the current reference method through public technical documentation
- later review of whether any future method is specific enough to justify a separate narrow filing

## Project IP goals

- keep released materials in the commons under clear open terms
- make the current release clear enough to function as a real public disclosure
- distinguish intentionally public v1 release artifacts from future participant data that is not automatically public
- avoid implying that future private homeowner data becomes open just because the project is open source
- avoid overpromising patent grants, non-asserts, or trademark permissions before legal review

## What is public now

During the current release period, the project may publicly release:

- mission and principles
- governance and privacy posture
- data-ownership position
- technical architecture
- claims and limitations language
- selected media and overview documentation
- reference software, firmware, hardware documentation, and schemas approved for release
- the project-controlled v1 dataset and related derived artifacts when they are intentionally designated as public release assets and carry an explicit open-data license

## What is not public by default

Even in the open-release posture, some materials may still remain out of public release, including categories listed in:

- `holdback-list.md`
- `public-preview-scope.md`

Examples may include:

- secrets, credentials, or access tokens
- non-cleared third-party data or licensed materials
- personally identifying or operational data not intentionally included in the public v1 dataset
- internal filing and counsel-strategy drafts retained only as historical planning material

## Release-period rights statement

During the current release period:

- released materials are licensed only to the extent their attached license or notice says so
- archival provisional-planning documents do not narrow or expand rights in separately released materials by themselves
- no separate patent license is granted except where a final release license explicitly provides one
- no trademark, trade dress, or branding license is granted except where expressly stated
- rights not expressly granted remain reserved

## Intended open-release direction

Subject to final review, the project intends a split license structure by asset class rather than one blanket license for everything.

Current working direction:

- platform and service software: strong copyleft under a network-aware license
- hardware design files: reciprocal open-hardware license
- documentation and specifications: share-alike documentation license
- project-controlled v1 dataset and approved public snapshots: dataset-specific terms
- future participant-contributed parcel-linked data: not made open by default absent a later explicit policy decision

See `../../../LICENSES.md` for the current working license matrix.

## Data-rights clarification

Open-source licensing for code, hardware, or documentation does not change the ownership or privacy posture of homeowner-contributed parcel-linked data.

The project’s working rule is:

- homeowners own their raw parcel-linked data
- sharing outside the private parcel context is opt-in
- the project-controlled v1 dataset may be intentionally published under explicit open-data terms
- future participant-contributed parcel-linked datasets still require separate review and are not made public by default

See:

- `../docs/privacy-governance/data-ownership.md`
- `../docs/privacy-governance/privacy.md`

## Contributor expectations during open release

- Do not contribute confidential third-party material.
- Do not publish secrets, non-cleared third-party data, or non-public personal data externally without release-owner approval.
- Do not assume that one intentionally public dataset makes all future parcel-linked data public by default.

## What this file does not do

This file does not:

- finalize the permanent project license stack
- promise a project-wide patent non-assert
- promise an Apache-style patent grant
- promise that every future artifact will be released on the same date
- authorize publication of materials that remain outside the current release scope

## Release-owner checks before publication

Before publishing a release artifact, confirm:

- release materials do not exceed `public-preview-scope.md`
- the current licensing matrix still matches the intended release posture
- any intentionally public dataset is clearly identified and carries an explicit dataset license
- no secrets or non-cleared personal data are attached by accident
- release language does not imply that all future private user data is open data

## Attorney review triggers

Attorney review is strongly recommended before:

- any provisional filing
- any patent non-assert promise
- any final asset-class license lock
- any public statement that could be read as a patent license, trademark license, or irrevocable dedication
