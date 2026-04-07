# Publish / Internal Map

## Purpose

Give one folder-by-folder view of what should be treated as public-preview material versus internal-only material for the April 14, 2026 Path B release.

This file is a release-control aid. It is not legal advice.

## Public preview by default

These areas are part of the intended April 14 preview surface, subject to the notices and claims/privacy rules:

- `README.md`
- `NOTICE.md`
- `docs/release/2026-04-14/`
- `docs/privacy-governance/`
- `legal/ip.md`
- `legal/GOVERNANCE.md`
- `legal/licenses/README.md`
- `LICENSES.md`

## Public preview only after review

These areas may contain public-facing material, but should be checked before external linking because they can drift into implementation detail or stronger claims:

- `technical-architecture/`
- `docs/system-overview/`
- `docs/data-model/`
- `docs/pilot-playbooks/`
- `software/README.md`
- `hardware/README.md`
- `docs/README.md`
- `legal/contribution-policy/README.md`
- `legal/dataset-release-policy.md`
- `legal/trademark-and-certification-policy.md`

## Internal by default during Path B

These areas should stay internal unless you deliberately change the release decision:

- `legal/provisional-*`
- `legal/send-to-counsel-checklist.md`
- `legal/holdback-list.md`
- `legal/public-preview-scope.md`
- `legal/counsel-questions/`

## Internal until separately cleared

These areas may eventually become public, but should not be assumed public in the April 14 preview:

- detailed hardware design files not yet cleared for release
- detailed inference logic, thresholds, and scoring materials
- implementation-specific protocol details tied to the filing candidate
- real homeowner-contributed parcel-linked data
- any demos, figures, or screenshots that teach the held-back method

## Folder summary

| Folder or file set | Default status for April 14 preview | Notes |
| --- | --- | --- |
| `repo/README.md`, `repo/NOTICE.md`, `repo/LICENSES.md` | publish | core entry points |
| `programs/open-environmental-sensing-and-inference-system/README.md`, `NOTICE.md` | publish | core program entry points |
| `programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/` | publish | canonical preview set |
| `programs/open-environmental-sensing-and-inference-system/docs/privacy-governance/` | publish | public governance posture |
| `programs/open-environmental-sensing-and-inference-system/legal/ip.md` | publish | preview IP position |
| `programs/open-environmental-sensing-and-inference-system/legal/GOVERNANCE.md` | publish | project governance posture |
| `programs/open-environmental-sensing-and-inference-system/technical-architecture/` | mixed | versioned architecture canon; review for public-safe scope and implementation detail |
| `programs/open-environmental-sensing-and-inference-system/legal/provisional-*` | internal | filing and counsel packet |
| `programs/open-environmental-sensing-and-inference-system/legal/holdback-list.md` | internal | release-control doc |
| `programs/open-environmental-sensing-and-inference-system/legal/public-preview-scope.md` | internal | release-control doc |
| `programs/open-environmental-sensing-and-inference-system/software/` | mixed | README / notice can be public, detailed internals need review |
| `programs/open-environmental-sensing-and-inference-system/hardware/` | mixed | README / notice can be public, design-enabling files need review |
| `programs/open-environmental-sensing-and-inference-system/docs/system-overview/` | mixed | review for claims and enabling detail |
| `programs/open-environmental-sensing-and-inference-system/docs/data-model/` | mixed | review for method detail and release scope |

## Practical rule

If a file exists mainly to:

- explain governance, ownership, privacy, release posture, or public limitations, it is likely part of the preview surface
- help you file, help counsel review, or help you avoid disclosing something, it should remain internal

## Related docs

- `launch-checklist.md`
- `NOTICE.md`
- `social-posts.md`
- `../../../legal/ip.md`
