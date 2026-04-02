# Preview Site Scaffold

## Purpose

Provide a simple local landing page for the public preview that stays within the current release boundary and points readers to the canonical docs.

## Files

- `index.html`
- `styles.css`

## Local use

Open `index.html` directly in a browser, or from this folder run:

```bash
python3 -m http.server 8000
```

Then visit `http://127.0.0.1:8000/`.

## Content rule

This page is intentionally high-level and non-enabling.
Before publishing it externally, review it against:

- `../../../../legal/public-preview-scope.md`
- `../../../privacy-governance/claims-and-safety-language.md`
- `../launch-readiness-checklist.md`

Only link documents that belong in the public preview packet.
Do not link `../reviewer-packet-index.md` or pilot/counsel materials from the public page.
