# Public Content Allowlist

## Purpose

Define which materials belong on the public preview site, which routes they should map to, and which materials must stay out of the public navigation during the April 14, 2026 preview.

This file is the site-facing publication control for the preview packet.

## Routing model

If the site is rebuilt in Astro, use these route classes:

- `/` for the primary one-page public experience
- `/governance-and-privacy` for a secondary focused view of ownership, sharing, and claims
- `/diagrams` for a secondary focused view of public-safe diagrams

Do not create routes for internal packet-assembly or counsel materials.
Do not assume every canonical repository document should become a first-class website route.

## Approved public landing-page links

The landing page may link directly to anchored sections such as:

- `/#snapshot`
- `/#roadmap`
- `/#how-it-works`
- `/#hardware-specs`
- `/#software-specs`
- `/#governance`
- `/#diagrams`

## Approved public sections

These folders may feed the public site as source material if individual files stay inside preview scope:

- `../../`
- `../../../privacy-governance/`
- `../../../../technical-architecture/`
- `../../../system-overview/`
- `../../../../legal/`

## Excluded from public site navigation

Do not link these from the public preview site without a deliberate release decision:

- `../reviewer-packet-index.md`
- `../publish-internal-map.md`
- `../preview-execution-plan.md`
- `../launch-readiness-checklist.md`
- `../../../pilot-playbooks/`
- `../../../../legal/counsel-questions/`
- `../../../../legal/provisional-*`
- `../../../../legal/send-to-counsel-checklist.md`
- any held-back technical artifact listed in `../../../../legal/holdback-list.md`

## Content metadata model

If the site is rebuilt, each routed document should declare or derive:

- title
- description
- public status
- section
- order
- canonical path
- release tag if the page is preview-specific

Recommended public gate:

- `public: true`
- `release: 2026-04-14` for preview-specific materials

## Publication rules

Before exposing a document on the site:

1. Confirm it is inside `../../../../legal/public-preview-scope.md`.
2. Confirm it does not contain held-back technical detail.
3. Confirm it does not expose real homeowner-contributed parcel-linked data.
4. Confirm it matches the asset-class licensing posture.
5. Confirm it belongs in the public packet rather than reviewer or counsel workflows.

## Navigation guidance

The public site should emphasize:

- mission and principles
- the public boundary and release limits
- released hardware and software spec access
- governance and privacy posture
- data ownership and sharing rules
- claims and limitations
- open release, with boundaries
- public-safe diagrams that explain the system visually without exposing implementation detail

The homepage should function as a complete guided story on its own, with deeper sections expandable in place rather than requiring route changes.

The site should avoid acting like a raw repository browser or a link dump.
It should not treat more technical release artifacts as first-stop website reading unless the site is intentionally pulling selected portions from them.
Canonical repository docs may be cited as source material for website pages without becoming direct public navigation targets.

## Related documents

- `../open-source-v1-summary.md`
- `../asset-class-license-and-publication-matrix.md`
- `../contributor-and-review-guide.md`
- `public-preview-guide.md`
- `README.md`
- `../../../../legal/public-preview-scope.md`
- `../../../../legal/holdback-list.md`
