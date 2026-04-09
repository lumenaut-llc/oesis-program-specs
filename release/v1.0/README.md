# Release v1.0 (program packet)

## Purpose

This directory is the **canonical public preview packet root** for the v1.0-aligned cut of program-specs: governance copy, release controls, and pointers to technical acceptance. It supersedes path-based references to `release/2026-04-14/` in build tooling and publication bundles.

The earlier **April preview** materials remain archived under `release/v.0.1/` for history and diff review.

## What v1.0 means here (three lenses)

1. **Architecture** — [`v1.0-scope.md`](v1.0-scope.md) ties this packet to [`architecture/current/pre-1.0-version-progression.md`](../../architecture/current/pre-1.0-version-progression.md): which pre-1.0 slice bars are claimed **now** vs deferred.
2. **Product / PRD** — Same scope doc maps [`architecture/system/product-requirements-phase-1.md`](../../architecture/system/product-requirements-phase-1.md) (current v1 product requirements) to **honest** implementation status; full consumer UX is planned in [`v1.0-product-surface.md`](v1.0-product-surface.md).
3. **Technical lane** — Contracts and runtime carry an additive **v1.0** lane beside frozen v0.1; acceptance commands are documented in [`v1.0-acceptance-spec.md`](v1.0-acceptance-spec.md) (sibling repo `oesis-runtime`).

## Reading order

1. [`v1.0-scope.md`](v1.0-scope.md) — in scope, out of scope, PRD honesty table  
2. [`v1.0-acceptance-spec.md`](v1.0-acceptance-spec.md) — how to verify the reference stack  
3. [`v1.0-product-surface.md`](v1.0-product-surface.md) — planned product surfaces (app, alerts, timeline)  
4. Prior preview context: [`../v.0.1/README.md`](../v.0.1/README.md)  
5. Implementation evidence: [`../v.0.1/implementation-status-matrix.md`](../v.0.1/implementation-status-matrix.md) (refresh or fork when v1.0 rows change)

## Publication

- Machine-readable allowlist roots: `artifacts/public-content-bundle/public-content-bundle.json` (regenerated via `make repo-split-build-public-content-bundle` from program-specs).  
- Public Astro app: sibling workspace `../../oesis-public-site` (`src/data/publicationPolicy.ts`, `src/generated/publicContentBundle.ts`).  
- Human policy: `legal/public-preview-scope.md`.

## Related

- `NOTICE.md` and open-release summaries under `../v.0.1/` until v1.0-specific copies are added  
- `legal/holdback-list.md`
