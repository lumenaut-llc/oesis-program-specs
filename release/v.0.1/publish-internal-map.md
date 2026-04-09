# Publish / Internal Map

## Purpose

Give one folder-by-folder view of what should be treated as public-release material
versus internal-only material around the April 14, 2026 open release. The **canonical**
public preview packet root in-repo is now `release/v1.0/`; this `release/v.0.1/` tree
holds the prior April preview materials and extended reviewer packet.

This file is a release-control aid. It is not legal advice.

## Public release by default

These areas are part of the intended April 14 public release surface, subject to the
notices and claims/privacy rules:

- `README.md`
- `NOTICE.md`
- `release/v1.0/` (canonical public packet); `release/v.0.1/` (prior April preview / extended packet)
- `legal/privacy/`
- `legal/ip.md`
- `legal/GOVERNANCE.md`
- `legal/public-preview-scope.md`
- `legal/dataset-release-policy.md`
- `legal/licenses/README.md`
- `LICENSES.md`

## Public only after review

These areas may contain public-facing material, but should be checked before external
linking because they can drift into implementation detail or stronger claims:

- `architecture/`
- `contracts/`
- `operations/pilots/`
- `software/README.md`
- `hardware/README.md`
- `architecture/system/README.md`
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
| `README.md`, `NOTICE.md` | publish | core program entry points |
| `release/v1.0/` | publish | canonical public preview set |
| `release/v.0.1/` | publish (archived packet) | April 2026 preview materials; reviewer index and matrices |
| `legal/privacy/` | publish | public governance posture |
| `legal/ip.md` | publish | preview IP position |
| `legal/GOVERNANCE.md` | publish | project governance posture |
| `architecture/` | mixed | versioned architecture canon; review for public-safe scope and implementation detail |
| `legal/provisional-*` | internal | filing and counsel packet |
| `legal/holdback-list.md` | internal | release-control doc |
| `legal/public-preview-scope.md` | internal | release-control doc |
| `software/` | mixed | README / notice can be public, detailed internals need review |
| `hardware/` | mixed | README / notice can be public, design-enabling files need review |
| `architecture/` | mixed | review for public-safe scope, implementation detail, and system narratives |
| `contracts/` | mixed | review for method detail and release scope |

## Practical rule

If a file exists mainly to:

- explain governance, ownership, privacy, release posture, or public limitations, it is likely part of the public release surface
- help you file, help counsel review, or help you avoid disclosing something, it should remain internal

## Related docs

- `launch-checklist.md`
- `NOTICE.md`
- `social-posts.md`
- `../../../legal/ip.md`
