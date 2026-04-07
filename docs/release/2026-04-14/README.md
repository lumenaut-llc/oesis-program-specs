# April 14, 2026 Open Release

## Status

This release is a public preview of the legal, governance, and documentation
foundation for Open Environmental Sensing and Inference System.

It publishes the current governance, privacy, documentation, and approved technical
release materials under the project's current commons-protective release posture.

## What this release is for

- explain the project mission and architecture at a high level
- make the homeowner-ownership and private-by-default model public
- document the intended open-source and open-hardware direction
- document the intentionally public v1 dataset carve-out and its boundaries
- show the system scope for smoke, pluvial flooding/runoff, and heat
- publish the release claims and limitations posture

## What is intentionally not included

This release still does not make every file in the repo a public release asset.

Some materials remain outside release because they include secrets, non-cleared
third-party content, unintended personal or operational data, or internal historical
planning artifacts.

See:

- `../../../legal/public-preview-scope.md`
- `../../../legal/holdback-list.md`

## Current release posture

- homeowner-owned raw data remains a core rule
- private by default and shared by choice remains a core rule
- the project-controlled v1 dataset may be intentionally public when explicitly licensed and designated
- future participant-contributed parcel-linked data is still not public by default
- public release materials should not overclaim safety, certainty, or emergency authority
- approved release materials are public now under the applicable asset-specific terms

## Reading order

Start here:

1. `../../../README.md`
2. `NOTICE.md`
3. `open-source-v1-summary.md`
4. `asset-class-license-and-publication-matrix.md`
5. `contributor-and-review-guide.md`
6. `../../../technical-architecture/v0.1/README.md`
7. `../../privacy-governance/README.md`
8. `../../privacy-governance/claims-and-safety-language.md`
9. `../../../legal/GOVERNANCE.md`
10. `../../../legal/dataset-release-policy.md`
11. `../../../legal/ip.md`
12. `../../../legal/contribution-policy/README.md`
13. `../../../LICENSES.md`

## Release assets

- `NOTICE.md`
- `open-source-v1-summary.md`
- `asset-class-license-and-publication-matrix.md`
- `contributor-and-review-guide.md`
- `open-release-v1-audit-checklist.md`
- `social-posts.md`
- `landing-page-copy.md`
- `../../../technical-architecture/`
- `preview-execution-plan.md`
- `implementation-status-matrix.md`
- `../../../technical-architecture/`
- `site/` (release-owned publication controls)
- sibling repo `../oesis-public-site` (stable Astro app)
- `pinned-post-opener.md`
- `launch-checklist.md`
- `publish-internal-map.md`

## For contributors and reviewers

If you are assembling a review packet, start with:

- `reviewer-packet-index.md`

That file is an internal handoff map for packet assembly.
It should not be treated as a public-site asset or linked from public social surfaces
by default.

Do not assume every repo artifact is approved for external publication merely because
it exists in the repo.

Before publishing or linking any new file externally, check the current release-control
documents in `legal/`.
