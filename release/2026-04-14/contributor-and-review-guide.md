# Contributor And Review Guide

## Purpose

Give contributors, maintainers, and outside reviewers one short v1 guide for deciding what can be merged, what needs escalation, and what must stay out of the public release surface.

This guide is a release and governance aid, not legal advice.

## Baseline rule

The repository is open by asset class and by approved release surface, not by assumption.

That means:

- public code, docs, and hardware will use clear open terms by asset class
- some technical materials remain held back during the preview phase
- real homeowner-contributed parcel-linked data is not a normal contribution target
- privacy, claims, and release-scope controls still apply to open contributions

## Ordinary contributions

These usually follow normal maintainer review:

- implementation cleanup
- documentation edits that do not change policy or claims
- synthetic examples and fixtures
- non-sensitive architecture clarifications
- housekeeping around public-facing notices, links, and consistency

Contributor expectations:

- use DCO-style signoff or equivalent attestation
- confirm you have the right to submit the work
- identify material third-party code, data, or design inputs
- preserve provenance and avoid overclaiming capabilities

## Governance-sensitive contributions

These require maintainer review plus governance or privacy review:

- new data uses or new data classes
- changes to sharing, export, deletion, or revocation behavior
- claims-sensitive UI copy or public messaging
- changes to how uncertainty, freshness, or provenance is presented
- dataset handling or release-category changes

Required references:

- `../../privacy-governance/data-ownership.md`
- `../../privacy-governance/privacy.md`
- `../../privacy-governance/permissions-matrix.md`
- `../../privacy-governance/retention-export-deletion-revocation.md`
- `../../privacy-governance/claims-and-safety-language.md`

## Release-sensitive contributions

These require release-owner review and legal or IP review before merge or publication:

- anything touching held-back technical materials
- changes to public preview scope
- changes to public licensing statements
- new public dataset releases or public map outputs
- changes that could be read as a patent grant, trademark permission, or publication approval for withheld materials

Required references:

- `../../../legal/ip.md`
- `../../../legal/public-preview-scope.md`
- `../../../legal/holdback-list.md`
- `../../../legal/GOVERNANCE.md`

## Hard red lines

Do not merge or publish these through normal contribution paths:

- real homeowner-contributed parcel-linked hazard data
- exact household locations, secrets, or live credentials
- held-back source code, formulas, thresholds, packet contracts, or reproducible internals
- marketing or UI claims that imply guaranteed safety, certainty, or emergency authority
- changes that flip private-by-default behavior into opt-out sharing
- third-party datasets or scrape-derived data with unclear rights

## Fast review decision tree

1. Is the contribution public-facing or release-facing?
2. Does it touch data rights, privacy, claims, or sharing defaults?
3. Does it expose any held-back method detail?
4. Does it introduce third-party rights or dataset obligations?
5. Does it stay consistent with the current asset-class licensing plan?

If the answer to questions 2 through 4 is yes, escalate beyond ordinary maintainer review.

## Outside reviewer checklist

Outside reviewers should be able to verify:

- the project uses a visible asset-class licensing model
- the preview surface is intentionally defined
- held-back materials are explicitly called out rather than silently omitted
- data rights are separated from source-code openness
- contributor expectations are understandable without private context

## Related documents

- `open-source-v1-summary.md`
- `asset-class-license-and-publication-matrix.md`
- `open-release-v1-audit-checklist.md`
- `../../../legal/contribution-policy/README.md`
- `../../../legal/GOVERNANCE.md`
