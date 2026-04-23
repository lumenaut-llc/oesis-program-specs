# Doc discipline

## Purpose

Set house rules for when to add a new document, when to extend an existing one, and how to keep summary docs from drifting from canonical sources. The project's documentation surface is large (hundreds of markdown files across five repos) because the problem is genuinely multi-axis. Entropy is the real risk — docs accumulate faster than they consolidate. This policy slows that.

## Status

House rule. 2026-04-19. If a proposal contradicts a rule here, either the rule needs to evolve (amend this doc and cite the amendment) or the proposal needs to fit the rule. Do not silently bypass.

## Five rules

### Rule 1 — Extend before creating

A new concept goes into an **existing doc** if it fits that doc's scope. Create a new file only when at least one of the following is true:

- The concept is **genuinely cross-cutting** — it touches multiple existing docs and would duplicate into each.
- Adding it in place would **blur the host doc's focus** — the host doc is about X, the concept is about Y, and Y has enough content to stand on its own.
- The concept needs to be **citable as a program-level surface** — other docs will want to link to it by a stable name.

If you can't defend a new file against all three, extend. Examples of the rule working:

- New hazard-formula provenance requirement → **extended** `calibration-program.md` §C rather than creating a new admissibility doc. Correct.
- Adapter-derived Tier 2 trust posture → **created** `adapter-trust-program.md`. Correct — genuinely parallel to calibration-program, needed citable status.
- Per-stage architectural choices → initially drafted as inline additions across 9 stage docs; summary master was **created** as `architectural-choices-by-stage.md`. Correct — the at-a-glance need is cross-cutting.

Examples of the rule being violated:

- Creating `MAP.md` at repo root when the root `README.md` could host the map. That duplicates the landing-page job. Extend the README.

### Rule 2 — Summary docs cite, don't duplicate

Summary docs (`architecture-gaps-by-stage.md`, `architectural-choices-by-stage.md`, per-node part sheets, release scope matrices) are **aggregator surfaces**. They exist to give readers one place to check a cross-cutting question.

They must not restate values that already live in canonical docs. A summary doc cell like "mast-lite IP rating: IP44" must read instead as "IP44 per `deployment-maturity-ladder.md` Deployment-class standards" with the link. The difference:

- **Duplicated value** — both `architectural-choices-by-stage.md` and `deployment-maturity-ladder.md` carry "IP44" as a raw string. Drift risk: if one updates, the other doesn't.
- **Cited value** — the summary says "IP44 per the ladder" with a link. Drift risk: the summary never drifts because the value lives once.

When summary and source disagree, **source wins**. Fix the summary.

### Rule 3 — One canonical home per concept

If a concept appears in ≥ 3 places, declare which is canonical in `meta/markdown-canonical-topic-matrix.md`. Others cite.

This is the authority-map rule. It prevents confusion when two docs describe the same thing differently.

Already in the matrix:
- Program framing (thesis/problem) → `program/operating-packet/01-core-thesis-and-framing.md` canonical; `02`, `03` redirect.
- Target-lane roadmap/spec/taxonomy → `architecture/system/` canonical; `architecture/v1.0/` docs redirect.

Add to the matrix when a new concept earns ≥ 3 locations.

### Rule 4 — Per-version directories require intent

Before creating `foo/v0.X/`, confirm one of:

- **Real per-version content** exists — the directory will hold docs whose meaning is scoped to that version.
- **A redirect shim is genuinely needed** — the path has existing inbound references and cannot be broken.

Avoid empty scaffolding. Several per-version directories today are README-plus-stub patterns that add directory count without adding value. If you're tempted to create `operations/v0.6/README.md` that just says "lane TBD", don't.

Rule of thumb: if the only thing in `foo/v0.X/` would be a README, defer creating the directory until real content exists.

### Rule 5 — Redirect docs self-identify

Any doc that is redirect-only must say so in its **first line**, with the canonical path. Current examples that do this correctly:

- `release/v0.1/v0.1-scope-matrix.md` — opens with "Redirect Notice"
- `architecture/future/README.md` — opens with "Future Architecture Redirect"

Future redirect docs follow the same pattern. The rule prevents a reader from spending time on a redirect doc thinking it's authoritative.

## Checklist before adding a new `.md` file

Five questions. If any answer is "no" or "unsure", reconsider creating the file.

1. **Does the concept fit an existing doc's scope?** If yes, extend the existing doc. Only create if no.
2. **Is the concept genuinely cross-cutting, or self-contained enough to deserve citable status?** If the answer is "it depends on 2 other docs' details", it's not yet ready to stand alone.
3. **Does a summary doc already cover this, or would a new summary duplicate?** Rule 2. Cite, don't duplicate.
4. **Is there a canonical authority question?** If ≥ 3 docs will reference the concept, declare the canonical home in `meta/markdown-canonical-topic-matrix.md` before creating.
5. **Will the file be content or a redirect?** If redirect-only, does its first line say so (rule 5)?

## Signals that content should consolidate, not split

- Two docs describe the same concept from different angles and drift over time.
- A reader needs to read ≥ 3 docs to answer a single cross-cutting question.
- A summary doc's cell values diverge from the canonical source.
- A topic appears in the same form in ≥ 3 place (candidate for rule 3).

When you see these, consolidate rather than add another summary.

## When a rule here is wrong

These rules come from cumulative experience in this repo. If a proposal cannot satisfy a rule but has clear value, amend the rule instead of quietly bypassing. Open-question entry in `architecture/decisions/debate-map.md` is the right place to debate an amendment.

## Related

- `repo-manifest.md` — file-level manifest
- `markdown-canonical-topic-matrix.md` — which lane owns overlapping topics
- `directory-versioning-destination-matrix.md` — destination rules for per-version directory content
- `../README.md` "Navigating this repo" — where readers land; the entry surface this policy protects
- `../architecture/README.md` — architecture-specific lane map
- `proposals/` — pending cross-vault edit proposals (e.g., for oesis-builds, oesis-contracts)
