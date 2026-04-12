# v0.1 Launch Checklist

## Purpose

Provide a dependency-ordered checklist for the v0.1 open release.

This checklist assumes the current open-release posture:

- approved release materials are public now under asset-specific terms
- some materials still remain outside release because of privacy, provenance, licensing, or security constraints
- the project-controlled v1 dataset may be intentionally public, but future participant-contributed parcel-linked data remains private by default

## Phase 1. Lock the release boundary

Complete these first:

- confirm the project is publishing under the current open-release posture
- confirm no non-release files are included in the public release set
- confirm any intentionally public dataset is explicitly designated, licensed, and documented
- confirm release copy does not imply that all future parcel-linked data is public

Primary checks:

- `../../../legal/public-preview-scope.md`
- `../../../legal/holdback-list.md`
- `../../../legal/ip.md`

Do not publish anything until this phase is complete.

## Phase 2. Lock the public-facing governance set

Confirm these files are reviewed together:

- `NOTICE.md`
- `landing-page-copy.md`
- `../../../legal/GOVERNANCE.md`
- `../../../legal/ip.md`
- `../../../legal/dataset-release-policy.md`
- `../../privacy-governance/data-ownership.md`
- `../../privacy-governance/privacy.md`
- `../../privacy-governance/claims-and-safety-language.md`

Check for:

- consistent use of “private by default” and “shared by choice”
- no implication that future participant-contributed private parcel-linked data is open data
- no implication that every repo file is part of the public release
- no safety or emergency overclaims

## Phase 3. Lock social and launch copy

Review:

- `social-posts.md`
- `pinned-post-opener.md`
- `landing-page-copy.md`

Confirm:

- the copy points readers to canonical docs
- the copy does not introduce new legal promises
- the copy does not mention non-release technical specifics
- the copy accurately describes the v1 public-dataset carve-out

## Phase 4. Confirm licensing and dataset status

Confirm:

- whether the release license matrix still matches the intended public asset split
- whether any intentionally public dataset has explicit terms, provenance notes, and scope caveats attached
- whether any wording in `ip.md`, `LICENSES.md`, or the dataset policy needs revision before publication

Primary references:

- `../../../../../LICENSES.md`
- `../../../legal/dataset-release-policy.md`
- `../../../legal/ip.md`

## Phase 5. Final release package check

Make sure the release package contains:

- `README.md`
- `NOTICE.md`
- `landing-page-copy.md`
- `social-posts.md`
- `../../../../../LICENSES.md`
- governance and privacy docs referenced in the reading order

Make sure the release package does not contain:

- secrets, credentials, or operator-only material
- detailed hardware design files not yet cleared
- future participant-contributed parcel-linked data that has not been separately approved
- public claims that exceed the claims-and-safety-language standard

## Phase 6. Publish

Release in this order:

1. publish the repo or release page
2. verify the linked governance and privacy docs render correctly
3. publish the landing page
4. publish the pinned post
5. publish additional social posts only after the canonical page is live

## Phase 7. Immediate post-launch check

After publication, verify:

- links work
- the notice points to the correct docs
- no non-release files are accidentally exposed
- social posts match the canonical page
- no one is summarizing the release as if every repo file is public or safety-certified

## Stop conditions

Pause launch if any of these are true:

- a non-release document is about to be published
- an intentionally public dataset does not yet have explicit license / provenance notes
- the public copy implies guaranteed safety or official-alert replacement
- the privacy docs overstate controls that are not actually available

## Fast version

If you only have a short window, do this:

1. Check `public-preview-scope.md`.
2. Review `NOTICE.md`, `ip.md`, `dataset-release-policy.md`, `data-ownership.md`, and `privacy.md`.
3. Publish the canonical page first.
4. Post the pinned post only after that page is live.
