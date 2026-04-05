# Publish / Internal Map

## Purpose

Give one folder-by-folder view of what should be treated as public-release material
versus internal-only material for the April 14, 2026 open release.

This file is a release-control aid. It is not legal advice.

## Public release by default

These areas are part of the intended April 14 public release surface, subject to the
notices and claims/privacy rules:

- `README.md`
- `NOTICE.md`
- `docs/release/2026-04-14/`
- `docs/privacy-governance/`
- `legal/ip.md`
- `legal/GOVERNANCE.md`
- `legal/public-preview-scope.md`
- `legal/dataset-release-policy.md`
- `legal/licenses/README.md`
- `LICENSES.md`

## Public only after review

These areas may contain public-facing material, but should be checked before external
linking because they can drift into implementation detail or stronger claims:

- `docs/system-overview/`
- `docs/data-model/`
- `docs/pilot-playbooks/`
- `software/README.md`
- `hardware/README.md`
- `docs/README.md`
- `legal/contribution-policy/README.md`
- `legal/trademark-and-certification-policy.md`

## Internal or archival by default

These areas should stay internal unless you deliberately restart a separate counsel or
filing process:

- `legal/provisional-*`
- `legal/send-to-counsel-checklist.md`
- `legal/counsel-questions/`

## Internal until separately cleared

These areas may eventually become public, but should not be assumed public in the
April 14 release:

- detailed hardware design files not yet cleared for release
- detailed inference logic, thresholds, and scoring materials
- implementation-specific protocol details not yet cleared for release
- future participant-contributed parcel-linked data
- any demos, figures, or screenshots that reveal non-release material

## Folder summary

| Folder or file set | Default status for April 14 release | Notes |
| --- | --- | --- |
| `repo/README.md`, `repo/NOTICE.md`, `repo/LICENSES.md` | publish | core entry points |
| `programs/resilient-home-intelligence/README.md`, `NOTICE.md` | publish | core program entry points |
| `programs/resilient-home-intelligence/docs/release/2026-04-14/` | publish | canonical release set |
| `programs/resilient-home-intelligence/docs/privacy-governance/` | publish | public governance posture |
| `programs/resilient-home-intelligence/legal/ip.md` | publish | current IP position |
| `programs/resilient-home-intelligence/legal/GOVERNANCE.md` | publish | project governance posture |
| `programs/resilient-home-intelligence/legal/public-preview-scope.md` | publish | release-scope control doc |
| `programs/resilient-home-intelligence/legal/dataset-release-policy.md` | publish | public data boundary |
| `programs/resilient-home-intelligence/legal/provisional-*` | internal | filing and counsel packet |
| `programs/resilient-home-intelligence/legal/holdback-list.md` | internal review | release-control doc with non-release categories |
| `programs/resilient-home-intelligence/software/` | mixed | README / notice can be public, detailed internals need review |
| `programs/resilient-home-intelligence/hardware/` | mixed | README / notice can be public, design-enabling files need review |
| `programs/resilient-home-intelligence/docs/system-overview/` | mixed | review for claims and enabling detail |
| `programs/resilient-home-intelligence/docs/data-model/` | mixed | review for method detail and release scope |

## Practical rule

If a file exists mainly to:

- explain governance, ownership, privacy, release posture, or public limitations, it is likely part of the public release surface
- help you file, help counsel review, or help you avoid disclosing something, it should remain internal

## Related docs

- `launch-checklist.md`
- `NOTICE.md`
- `social-posts.md`
- `../../../legal/ip.md`
