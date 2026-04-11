# Open Release V1 Audit Checklist

## Purpose

Use this checklist before calling the April 14, 2026 `v1.0` surface a credible open-source/open-release public release.

## Go / no-go standard

V1 is ready only if an outside reader can understand:

- what is public now
- what is intentionally outside release
- what terms apply to each public asset class
- how contributors should participate safely
- why private homeowner-contributed parcel-linked data is not part of the blanket open story

## Repository and notice checks

- [ ] Root `README.md` points to the current v1 public-release summary.
- [ ] Root `NOTICE.md` points to the current asset-class licensing and release-boundary docs.
- [ ] Program-level `program/README.md` and `program/NOTICE.md` point to the same canonical v1 summary.
- [ ] No top-level README or notice implies one blanket license governs every file.

## Licensing checks

- [ ] `LICENSES.md` still matches the intended asset-class release direction.
- [ ] Public-facing docs describe software, hardware, docs, and data as separate asset classes where applicable.
- [ ] Public-facing docs do not imply that non-release materials are already licensed for public use.
- [ ] Public-facing docs do not imply that future participant-contributed parcel-linked data is open data.
- [ ] Any more specific notices remain consistent with the asset-class matrix.

## Scope and non-release checks

- [ ] Public release pages stay inside `../../legal/public-preview-scope.md`.
- [ ] Non-release materials listed in `../../legal/holdback-list.md` are not linked from public entrypoints.
- [ ] Public materials do not disclose implementation-enabling methods, thresholds, or excluded internals.
- [ ] Public materials do not expose real homeowner-contributed parcel-linked records unless intentionally designated and licensed as a public dataset.

## Governance and contribution checks

- [ ] Contributors can find a short guide explaining ordinary, governance-sensitive, and release-sensitive changes.
- [ ] Governance-sensitive public claims still point back to the privacy and claims policy docs.
- [ ] Release-sensitive changes still route through release-owner and legal or IP review.
- [ ] The public release posture does not weaken private-by-default or shared-by-choice rules.

## Site and publication checks

- [ ] The public site points to the canonical open-release docs rather than improvising licensing claims.
- [ ] Public navigation excludes reviewer/counsel/internal historical planning material.
- [ ] Public routes and source roots match the generated public content bundle.
- [ ] The site does not behave like a raw repository browser or imply access to excluded materials.

## Reviewer clarity checks

- [ ] An outside reviewer can identify the current public release surface in under five minutes.
- [ ] An outside reviewer can identify the intended terms for each public asset class.
- [ ] An outside reviewer can tell that the current release is bounded even though it is openly released.
- [ ] An outside reviewer can find the contribution and review path without private context.

## Related documents

- `open-source-v1-summary.md`
- `asset-class-license-and-publication-matrix.md`
- `contributor-and-review-guide.md`
- `../../LICENSES.md`
- `../../legal/ip.md`
- `../../legal/public-preview-scope.md`
- `../../legal/holdback-list.md`
