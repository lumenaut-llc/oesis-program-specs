# Open Release V1 Audit Checklist

## Purpose

Use this checklist before calling the April 14, 2026 preview a credible open-source/open-release v1 surface.

## Go / no-go standard

V1 is ready only if an outside reader can understand:

- what is public now
- what is intentionally held back
- what terms apply to each public asset class
- how contributors should participate safely
- why private homeowner-contributed parcel-linked data is not part of the blanket open story

## Repository and notice checks

- [ ] Root `README.md` points to the current v1 public-release summary.
- [ ] Root `NOTICE.md` points to the current asset-class licensing and release-boundary docs.
- [ ] Program-level `README.md` and `NOTICE.md` point to the same canonical v1 summary.
- [ ] No top-level README or notice implies one blanket license governs every file.

## Licensing checks

- [ ] `LICENSES.md` still matches the intended asset-class release direction.
- [ ] Public-facing docs describe software, hardware, docs, and data as separate asset classes where applicable.
- [ ] Public-facing docs do not imply that held-back materials are already licensed for public use.
- [ ] Public-facing docs do not imply that private homeowner-contributed data is open data.
- [ ] Any more specific notices remain consistent with the asset-class matrix.

## Scope and holdback checks

- [ ] Public preview pages stay inside `../../../legal/public-preview-scope.md`.
- [ ] Held-back materials listed in `../../../legal/holdback-list.md` are not linked from public entrypoints.
- [ ] Public materials do not disclose implementation-enabling methods, thresholds, or withheld internals.
- [ ] Public materials do not expose real homeowner-contributed parcel-linked records.

## Governance and contribution checks

- [ ] Contributors can find a short guide explaining ordinary, governance-sensitive, and release-sensitive changes.
- [ ] Governance-sensitive public claims still point back to the privacy and claims policy docs.
- [ ] Release-sensitive changes still route through release-owner and legal or IP review.
- [ ] The public release posture does not weaken private-by-default or shared-by-choice rules.

## Site checks

- [ ] The landing page links to the canonical v1 summary.
- [ ] The landing page does not act as a raw Markdown dump without guidance.
- [ ] Public navigation distinguishes approved public docs from internal or reviewer-only materials.
- [ ] The site content allowlist matches the actual links exposed on the page.

## Reviewer clarity checks

- [ ] An outside reviewer can identify the current public surface in under five minutes.
- [ ] An outside reviewer can identify the intended terms for each public asset class.
- [ ] An outside reviewer can tell that the preview is not yet the full enabling technical release.
- [ ] An outside reviewer can find the contribution and review path without private context.

## Related documents

- `open-source-v1-summary.md`
- `asset-class-license-and-publication-matrix.md`
- `contributor-and-review-guide.md`
- `site/public-content-allowlist.md`
- `../../../legal/public-preview-scope.md`
- `../../../legal/holdback-list.md`
