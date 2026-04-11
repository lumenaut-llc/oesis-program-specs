# Open Release Site

## Purpose

Provide the Astro source for the current open-release website while keeping the site
within the approved public release boundary.

## Structure

- `src/pages/` — route-level Astro pages
- `src/layouts/` — page shell and metadata handling
- `src/components/` — reusable hero and future site components
- `src/styles/global.css` — shared site styling
- `package.json` — Astro scripts and dependency entry point
- `astro.config.mjs` — static output configuration

## Local use

From this folder run:

```bash
npm install
npm run dev
```

Then visit the local Astro dev server shown in the terminal.

For a production build run:

```bash
npm run build
```

That writes the static site to `dist/`.

## Why Astro here

- gives the release site layouts, components, and routing instead of one-off HTML files
- keeps the output static and easy to deploy
- makes it much easier to add richer storytelling later, including an animated version timeline
- keeps future design work from turning into copy-paste page maintenance

## Content rule

These pages are intentionally high-level and should stay within the approved public
release boundary. Before publishing externally, review them against:

- `../v1-public-website-standard.md`
- `../../../../legal/public-preview-scope.md`
- `../../../../legal/dataset-release-policy.md`
- `../../../privacy-governance/claims-and-safety-language.md`
- `../launch-readiness-checklist.md`

Only link documents that belong in the public release packet.
Do not link `../reviewer-packet-index.md` or pilot/counsel materials from the public
pages.
