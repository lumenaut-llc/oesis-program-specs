# Public Preview Site

## Purpose

Provide the stable Astro app for the Open Environmental Sensing and Inference
System public preview site while keeping release-owned source material in the
program release and governance directories.

## App ownership

This directory owns:

- Astro pages, layouts, components, and styles
- local app content collections and public assets
- curated site-side data modules and adapter files
- build and dev configuration

Canonical release, privacy, and legal source material remains outside this app under:

- `programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/`
- `programs/open-environmental-sensing-and-inference-system/docs/privacy-governance/`
- `programs/open-environmental-sensing-and-inference-system/legal/`

The adapter/data layer in `src/data/` and `src/lib/` is the only place that should know about external source roots.

Current public routes:

- `/`
- `/governance-and-privacy`
- `/diagrams`

The homepage is now intended to be the primary public experience.
The governance and diagrams routes may still exist as secondary views, but the
main site story should work without route-hopping.

The homepage now also acts as the guided entrypoint for released hardware and
software specs, with subsystem summaries and links out to the released source
artifacts.

## Local use

From this folder run:

```bash
npm install
npm run dev
```

Then visit the local Astro dev URL shown in the terminal.

For a production build:

```bash
npm run build
```

## Publication rule

This site must remain intentionally high-level and non-enabling. Before publishing it externally, review it against the canonical release-owned controls:

- `programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/open-source-v1-summary.md`
- `programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/site/public-content-allowlist.md`
- `programs/open-environmental-sensing-and-inference-system/legal/public-preview-scope.md`
- `programs/open-environmental-sensing-and-inference-system/docs/privacy-governance/claims-and-safety-language.md`
- `programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/launch-readiness-checklist.md`

Only link documents that belong in the approved public preview packet. Do not link reviewer, pilot, counsel, or other controlled materials from the public site.
