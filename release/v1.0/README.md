# Release v1.0 (program packet)

## Purpose

This directory is the **canonical v1.0 public release packet root** for the current cut of program-specs: governance copy, release controls, open-release summaries, and pointers to technical acceptance. It supersedes path-based references to `release/2026-04-14/` in build tooling and publication bundles.

The earlier **April preview** materials remain archived under `release/v.0.1/`
(release label **`v0.1`**) for history and diff review.

## What v1.0 means here (three lenses)

1. **Architecture** — [`v1.0-scope.md`](v1.0-scope.md) ties this packet to [`architecture/current/pre-1.0-version-progression.md`](../../architecture/current/pre-1.0-version-progression.md): which pre-1.0 slice bars are claimed **now** vs deferred.
2. **Product / PRD** — Same scope doc maps [`architecture/system/product-requirements-phase-1.md`](../../architecture/system/product-requirements-phase-1.md) (current v1 product requirements) to **honest** implementation status; full consumer UX is planned in [`v1.0-product-surface.md`](v1.0-product-surface.md).
3. **Technical lane** — Contracts and runtime carry an additive **v1.0** lane beside frozen v0.1; acceptance commands are documented in [`v1.0-acceptance-spec.md`](v1.0-acceptance-spec.md) (sibling repo `oesis-runtime`).

## Reading order

1. [`v1.0-scope.md`](v1.0-scope.md) — in scope, out of scope, PRD honesty table
2. [`v1.0-scope-matrix.md`](v1.0-scope-matrix.md) — surface-by-surface scope breakdown against PRD and non-goals
3. [`v1.0-acceptance-spec.md`](v1.0-acceptance-spec.md) — how to verify the reference stack
4. [`v1.0-product-surface.md`](v1.0-product-surface.md) — planned product surfaces (app, alerts, timeline)
5. [`v1.0-gap-register.md`](v1.0-gap-register.md) — gaps between current state and v1.0 readiness, classified by severity
6. [`v1.0-launch-checklist.md`](v1.0-launch-checklist.md) — comprehensive launch gates (Tier A internal / Tier B external pilot)
7. [`v1.0-pilot-minimum-subset.md`](v1.0-pilot-minimum-subset.md) — tiered minimum subset for internal reference and external pilot
8. [`open-source-v1-summary.md`](open-source-v1-summary.md) — canonical v1 open-release explanation
9. [`asset-class-license-and-publication-matrix.md`](asset-class-license-and-publication-matrix.md) — asset-class licensing and publication map
10. [`contributor-and-review-guide.md`](contributor-and-review-guide.md) — contribution and review path
11. [`open-release-v1-audit-checklist.md`](open-release-v1-audit-checklist.md) — readiness checklist
12. Prior preview context (label **`v0.1`**, path `v.0.1/`):
    [`../v.0.1/README.md`](../v.0.1/README.md)
13. Implementation evidence (same lane):
    [`../v.0.1/implementation-status-matrix.md`](../v.0.1/implementation-status-matrix.md)
    (refresh or fork when v1.0 rows change)

## Publication

- Machine-readable allowlist roots: `artifacts/public-content-bundle/public-content-bundle.json` (regenerated via `make repo-split-build-public-content-bundle` from program-specs).  
- Public Next.js app: sibling workspace `../../oesis-public-site` (`src/data/publicationPolicy.ts`, `src/generated/publicContentBundle.ts`).  
- Human policy: `legal/public-preview-scope.md`.
- Human release-readiness checklist: `open-release-v1-audit-checklist.md`.

## Related

- `NOTICE.md`
- `open-source-v1-summary.md`
- `asset-class-license-and-publication-matrix.md`
- `contributor-and-review-guide.md`
- `open-release-v1-audit-checklist.md`
- `legal/holdback-list.md`
