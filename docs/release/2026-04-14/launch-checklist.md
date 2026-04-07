# April 14, 2026 Launch Checklist

## Purpose

Provide a dependency-ordered checklist for the April 14, 2026 public preview launch.

This checklist assumes the current Path B release posture:

- non-enabling public preview
- narrow U.S. filing decision still active or just completed
- broader enabling open release to follow later

## Phase 1. Lock the release boundary

Complete these first:

- confirm the project is still on Path B
- confirm the lean filing candidate excludes shared-neighborhood transforms
- confirm the preview remains non-enabling
- confirm no held-back files are included in the public release set

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
- `../../privacy-governance/data-ownership.md`
- `../../privacy-governance/privacy.md`
- `../../privacy-governance/claims-and-safety-language.md`

Check for:

- consistent use of “private by default” and “shared by choice”
- no implication that private homeowner data is open data
- no implication that the preview is the full technical release
- no safety or emergency overclaims

## Phase 3. Lock social and launch copy

Review:

- `social-posts.md`
- `pinned-post-opener.md`
- `landing-page-copy.md`

Confirm:

- the copy is non-enabling
- the copy points readers to canonical docs
- the copy does not introduce new legal promises
- the copy does not mention unreleased technical specifics

## Phase 4. Confirm filing and counsel status

If counsel is involved, confirm:

- whether the narrow filing is on file, pending, or intentionally skipped
- whether any preview material still needs to stay held back after counsel feedback
- whether any wording in `ip.md` needs revision before publication

Primary references:

- `../../../legal/send-to-counsel-checklist.md`
- `../../../legal/provisional-counsel-cover-email.md`

## Phase 5. Final release package check

Make sure the preview package contains:

- `README.md`
- `NOTICE.md`
- `landing-page-copy.md`
- `social-posts.md`
- governance and privacy docs referenced in the reading order

Make sure the preview package does not contain:

- enabling technical method docs intended to stay held back
- detailed hardware design files not yet cleared
- real homeowner-contributed parcel-linked data
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
- no held-back files are accidentally exposed
- social posts match the canonical page
- no one is summarizing the preview as a complete technical release

## Stop conditions

Pause launch if any of these are true:

- a held-back document is about to be published
- the filing decision is still unresolved and someone wants to post enabling detail
- the public copy implies guaranteed safety or official-alert replacement
- the privacy docs overstate controls that are not actually available

## Fast version

If you only have a short window, do this:

1. Check `public-preview-scope.md`.
2. Review `NOTICE.md`, `ip.md`, `data-ownership.md`, and `privacy.md`.
3. Publish the canonical page first.
4. Post the pinned post only after that page is live.
