# IP and Release Position

## Purpose

State the project's current intellectual-property and release posture during the April 14, 2026 Path B preview period.

This file is a project policy draft and release-planning statement. It is not legal advice.

## Current posture

Open Environmental Sensing and Inference System is being prepared for a
commons-protective open release across software, hardware, documentation, and
approved public artifacts.

Before that enabling release, the project is using a short sequencing window to preserve the option to file a narrow U.S. provisional on a limited invention candidate.

The current intended sequencing is:

- non-enabling public preview first only if needed
- narrow U.S. filing first if practical
- broader open publication after the filing decision

## Project IP goals

- keep released materials in the commons under clear open terms
- avoid accidental publication of held-back technical details before the filing decision
- avoid implying that private homeowner data becomes open just because the project is open source
- preserve flexibility to open-release the broader system quickly after the filing step
- avoid overpromising patent grants, non-asserts, or trademark permissions before legal review

## What is public now

During the preview phase, the project may publicly release:

- mission and principles
- governance and privacy posture
- data-ownership position
- high-level architecture
- claims and limitations language
- selected non-enabling media and overview documentation

## What is not public yet

Until the filing decision is complete, some technical materials remain withheld, including categories listed in:

- `holdback-list.md`
- `public-preview-scope.md`

Examples of held-back material may include:

- enabling implementation diagrams
- detailed inference flowcharts
- detailed thresholds or scoring logic
- detailed hardware design files
- other technical materials identified in the holdback list

## Preview-phase rights statement

During the preview phase:

- preview documents are only licensed to the extent their attached license or notice says so
- withheld technical materials are not dedicated to the public merely because the project discusses future openness
- no separate patent license is granted except where a final release license explicitly provides one
- no trademark, trade dress, or branding license is granted except where expressly stated
- rights not expressly granted remain reserved

## Intended open-release direction

Subject to final review, the project intends a split license structure by asset class rather than one blanket license for everything.

Current working direction:

- platform and service software: strong copyleft under a network-aware license
- hardware design files: reciprocal open-hardware license
- documentation and specifications: share-alike documentation license
- approved public datasets or snapshots: dataset-specific terms
- real homeowner-contributed parcel-linked data: not made open by default

See `../../../LICENSES.md` for the current working license matrix.

## Data-rights clarification

Open-source licensing for code, hardware, or documentation does not change the ownership or privacy posture of homeowner-contributed parcel-linked data.

The project’s working rule remains:

- homeowners own their raw parcel-linked data
- sharing outside the private parcel context is opt-in
- public release of datasets requires separate review
- no blanket open-data license applies to real homeowner-contributed parcel-linked data during preview

See:

- `../docs/privacy-governance/data-ownership.md`
- `../docs/privacy-governance/privacy.md`

## Contributor expectations during preview

- Do not contribute confidential third-party material.
- Do not publish withheld technical content externally without release-owner approval.
- Do not assume that contribution to preview materials grants publication approval for separate held-back artifacts.

## What this file does not do

This file does not:

- finalize the permanent project license stack
- promise a project-wide patent non-assert
- promise an Apache-style patent grant
- promise that every future artifact will be released on the same date
- authorize publication of held-back materials

## Release-owner checks before public preview

Before April 14 preview publication, confirm:

- preview materials do not exceed `public-preview-scope.md`
- the current licensing matrix still matches the intended release posture
- no held-back technical detail is attached by accident
- preview language does not imply that private user data is open data
- any patent-sensitive material has been escalated appropriately

## Attorney review triggers

Attorney review is strongly recommended before:

- any provisional filing
- any patent non-assert promise
- any final asset-class license lock
- any release of materials currently marked as held back
- any public statement that could be read as a patent license, trademark license, or irrevocable dedication
