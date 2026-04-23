# ADR 0011: Doc Discipline — Extend Before Creating

- Status: Accepted
- Date: 2026-04-19
- Owners: Open Environmental Sensing and Inference System (meta)
- Related workstreams:
  - meta/doc-discipline
  - meta/markdown-canonical-topic-matrix
  - README.md (root navigation)

## Context

The OESIS program-specs repository contains ~200 markdown files across 6 top-level directories with per-version subdirectories under multiple roots (`legal/v0.x/`, `meta/v0.x/`, `operations/v0.x/`, `program/v0.x/`, `release/v0.x/`, `software/v0.x/`). A single week of architectural work can add 2–4 new canonical docs, 2–3 summary docs, and inline extensions to 10+ existing docs. Each addition is locally correct; cumulatively, three problems emerge:

1. **Discoverability.** A new reader or session cannot tell where to start; the repo's own README assumes familiarity.
2. **Entropy.** New concepts get new files faster than existing files get extended. No rule limits proliferation.
3. **Consistency.** The same concept (e.g., a node's deployment posture) can live in 9 docs simultaneously with no mechanism to verify they agree.

Existing guidance (`architecture/README.md` reading order, `meta/markdown-canonical-topic-matrix.md`, `meta/repo-manifest.md`) addresses narrow aspects but not the behavioral rule that keeps proliferation in check.

## Decision

Establish **doc discipline** as a house rule in [`../doc-discipline.md`](../doc-discipline.md). Five rules plus a 5-question new-doc checklist plus consolidation signals:

1. **Extend before creating.** New concept goes into an existing doc unless genuinely cross-cutting, would blur host-doc focus, or needs citable program-level status.
2. **Summary docs cite, don't duplicate.** Aggregator surfaces (architectural-choices-by-stage, architecture-gaps-by-stage, part sheets, release scope matrices) reference canonical values; they do not restate them. When summary and source disagree, source wins.
3. **One canonical home per concept.** If a concept appears in ≥ 3 places, declare canonical home in `meta/markdown-canonical-topic-matrix.md`.
4. **Per-version directories require intent.** Confirm real per-version content or real redirect need exists before creating `foo/v0.X/`.
5. **Redirect docs self-identify** in their first line, with the canonical path.

Doc discipline is complemented by:
- Root `README.md` "Navigating this repo" section (extends existing README rather than creating `MAP.md`).
- Per-node part sheets under `architecture/system/parts/` — aggregators that cite, not duplicate.

## Consequences

Positive:
- **Proliferation slows.** Any new doc must pass the 5-question checklist; most proposed new docs become extensions.
- **Aggregators have a pattern.** Part sheets, summary tables, and future consolidators follow rule 2 — cite upstream, don't restate — so they cannot drift.
- **Authority is declared, not implicit.** Rule 3 means canonical ownership of overlapping topics is visible in the canonical-topic-matrix, not discovered by reader spelunking.
- **Discipline is amendable.** Any proposal that cannot satisfy a rule goes to `architecture/decisions/debate-map.md` for amendment rather than quietly bypassing.

Negative:
- **One more thing to read.** New contributors must read doc-discipline before adding content. Mitigated by brevity (~120 lines) and the checklist being the most-cited surface.
- **Judgment calls remain.** "Genuinely cross-cutting" is not crisp; reasonable reviewers can disagree. The checklist narrows the disagreement space but does not eliminate it.
- **Back-compat.** Docs created before this rule may not meet rule 5 (redirect self-identification). Grandfathered — rule applies to new docs only.

## Alternatives considered

**No rule; rely on reviewer judgment.**
Rejected because the rate of accumulation exceeds the rate of judgment application. Rules 2 and 3 in particular address failure modes (aggregator drift, authority confusion) that emerge only after several docs accumulate.

**Automated enforcement (CI check that blocks new markdown files without a discipline-rule citation).**
Rejected as premature. The rules are 24 hours old. Codifying them in CI locks in shape before the rules have been stress-tested. Revisit once doc-discipline has survived at least one month of use.

**Stronger rule: "no new markdown files without ADR."**
Rejected as too coarse. Part sheets and per-stage scope documents are legitimate new files that don't warrant an ADR each.

## Follow-up work

- Monitor discipline-rule uptake in subsequent sessions. If proposals still create files that should have extended existing docs, consider tightening rule 1.
- Amend doc-discipline as rules prove insufficient or overly restrictive. Amendments go through `architecture/decisions/debate-map.md`.
- Periodically audit the repo for rule-5 compliance (redirect-only docs identifying themselves in first line). Flag violations as low-severity cleanup items.
- Consider codifying rule 1 in CI after 1–3 months if the qualitative judgment calls are stable.
