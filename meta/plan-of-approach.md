# OESIS — Plan of Approach

## Purpose

Operational guide for executing against [Project 5 "OESIS cross-repo gaps"](https://github.com/orgs/lumenaut-llc/projects/5). After the April 2026 decomposition pass, Project 5 has **202 items across 25 programs**; this document sequences them into an actionable plan without duplicating the strategic framing already captured in `program/execution-plan.md` and `architecture/current/milestone-roadmap.md`.

Read this when you need to answer: **"what do I do first, second, third, and what can wait?"**

## Status

Drafted 2026-04-23 after the six-round decomposition session that expanded Project 5 from 21 → 202 items. Re-verify the blocker graph against current ticket state before starting each phase.

## Relationship to existing plans

| Document | Role | Relationship to this doc |
|---|---|---|
| [`program/execution-plan.md`](../program/execution-plan.md) | Canonical "where are we, what's next" | Upstream strategic source — this doc is downstream tactical detail |
| [`architecture/current/milestone-roadmap.md`](../architecture/current/milestone-roadmap.md) | Milestone-by-milestone delivery | Upstream — milestones M1–M5 are the phase containers here |
| [`architecture/current/pre-1.0-version-progression.md`](../architecture/current/pre-1.0-version-progression.md) | Slice promotion bar | Referenced at each phase exit |
| [`release/v.0.1/v0.1-gap-register.md`](../release/v.0.1/v0.1-gap-register.md) | G1–G24 gaps | Source for Phase 1 blockers |
| [`release/v1.0/v1.0-launch-checklist.md`](../release/v1.0/v1.0-launch-checklist.md) | Tier A/B launch gates | Source for Phase 3 blockers |
| [`meta/backlog.md`](backlog.md) | Flat soon-term items | Subset of Project 5 `program: backlog` |

## The governing insight

The 202 items are not equal. They cluster around **three hard gate clusters** and one **slow-burn design thread**:

1. **v0.2 / Milestone 2 promotion** — 13 blockers with a single-dependency chain.
2. **v1.0 Tier-A internal reference** — partial surfaces that need operational completion.
3. **v1.0 Tier-B external pilot** — 17 blockers gating real-participant enrollment.
4. **Design threads** — UA1–UA5, U1–U3, U8–U17 each produce design docs on their own cadence; most don't block the gate clusters.

**Attack the gate clusters in order; treat design threads as parallel background work.** A year with the gate-cluster arc cleared but no debate-decomposition PRs is success. A year with 30 shallow design docs and no live pilot is not.

## Project 5 distribution (as of 2026-04-23)

| Axis | Distribution |
|---|---|
| Severity | 30 blockers · 123 important · 48 defer · 1 PRD-only |
| Phase | 24 v0.2 · 1 v0.5 · 130 v1.0 · 33 v1.5 · 14 later |
| Umbrellas | 17 trackers (U1–U17) plus G11 promoted |

---

## Phase 1 — Clear v0.2 / Milestone 2 promotion

**Goal:** Promote the first widened kit slice (bench-air + mast-lite) with hazard formula v1 running in shadow mode. See `milestone-roadmap.md` §Milestone 2 for the canonical scope.

### Critical-path chain (13 blockers, partly sequential)

```
G13 (reference instruments)        ──┐
   ↓                                  │
G14 (burn-in gate, hw + runtime)   ──┼─→ G15 (admissibility tooling)
   ↓                                  │          ↓
G17 (observation-schema facts)     ──┘   G11 replay harness prototype
                                                  ↓
                                          v1_1/ shadow scaffold
                                                  ↓
                                          Brier / ECE reporting + incident-log schema
                                                  ↓
                                          coefficient fitting + promotion criteria
                                                  ↓
                                             v0.2 PROMOTION
```

**Hardware parallel track** (independent of the software chain):

- G12 mast-lite build spec + radiation-shield design
- G16 bench-air §F block (already applied 2026-04-19)
- G20 bring-up gates (addressed in part by `meta/proposals/oesis-builds-calibration-program-integration.md`)
- G23 provenance slots in v0 config

### Phase 1 tickets (linked)

Software:
- [G11 (#12)](https://github.com/lumenaut-llc/oesis-program-specs/issues/12) — umbrella, stays open through all children
- [G17 (oesis-contracts#2)](https://github.com/lumenaut-llc/oesis-contracts/issues/2)
- [G15 (oesis_runtime#4)](https://github.com/lumenaut-llc/oesis_runtime/issues/4)
- [G14 runtime (oesis_runtime#3)](https://github.com/lumenaut-llc/oesis_runtime/issues/3)
- [G23 (oesis_runtime#5)](https://github.com/lumenaut-llc/oesis_runtime/issues/5)
- G11 children: [replay harness (oesis_runtime#8)](https://github.com/lumenaut-llc/oesis_runtime/issues/8), [v1_1 scaffold (oesis_runtime#10)](https://github.com/lumenaut-llc/oesis_runtime/issues/10), [Brier/ECE (oesis_runtime#9)](https://github.com/lumenaut-llc/oesis_runtime/issues/9), [incident-log schema (#33)](https://github.com/lumenaut-llc/oesis-program-specs/issues/33), [NCEI preload (#32)](https://github.com/lumenaut-llc/oesis-program-specs/issues/32), [coefficient fitting (#34)](https://github.com/lumenaut-llc/oesis-program-specs/issues/34), [promotion criteria (oesis_runtime#11)](https://github.com/lumenaut-llc/oesis_runtime/issues/11)

Hardware:
- [G12 mast-lite (oesis-hardware#2)](https://github.com/lumenaut-llc/oesis-hardware/issues/2)
- [G13 reference instruments (oesis-hardware#3)](https://github.com/lumenaut-llc/oesis-hardware/issues/3)
- [G14 hardware (oesis-hardware#4)](https://github.com/lumenaut-llc/oesis-hardware/issues/4)
- [G16 bench-air §F (oesis-hardware#5)](https://github.com/lumenaut-llc/oesis-hardware/issues/5)

### Phase 1 exit criteria

Per `milestone-roadmap.md` §Milestone 2 acceptance criteria:

- All 13 critical-path blockers closed
- v1_1 shadow module beats v0_1 on Brier AND ECE on at least one pilot-incident slice
- Mast-lite independently reproduced once
- §F build-spec blocks present on both bench-air and mast-lite
- Admissibility tooling active on ingest

---

## Phase 2 — v1.0 Tier-A internal reference (parallelizes with Phase 1)

**Goal:** Internal reference stack is operationally mature — reviewers can exercise it without surprises.

Tier-A is largely already complete (17 of 44 launch-checklist gates done, per `v1.0-launch-checklist.md` 2026-04-15 status). Remaining Tier-A work is **infrastructure foundations** that the existing runtime + contracts don't cover.

### Pick a minimum set; don't attempt everything

From U11 engineering infrastructure — pick **3–4 of 7**:

- [Test strategy doc (#170)](https://github.com/lumenaut-llc/oesis-program-specs/issues/170) — gates every other test work
- [Monitoring / observability framework (#173)](https://github.com/lumenaut-llc/oesis-program-specs/issues/173) — required before pilots run blind
- [CI philosophy doc (#171)](https://github.com/lumenaut-llc/oesis-program-specs/issues/171) — cheap, unblocks branch-protection
- [Cloud infrastructure / IaC (#175)](https://github.com/lumenaut-llc/oesis-program-specs/issues/175) — repeatable deploys for pilots
- [Backup / disaster recovery (#174)](https://github.com/lumenaut-llc/oesis-program-specs/issues/174) — must exist before real participant data

From U8 security hygiene — pick **2 of 7**:

- [Dependabot + triage SLA (#135)](https://github.com/lumenaut-llc/oesis-program-specs/issues/135) — cheap, high leverage
- [Secrets-management pattern (#136)](https://github.com/lumenaut-llc/oesis-program-specs/issues/136) — blocks DA-3 ingest auth

From U7 bridge endpoints — pick **2 of 6**:

- [`intervention-event` endpoint (#123)](https://github.com/lumenaut-llc/oesis-program-specs/issues/123) — enables closed-loop participant actions
- [`house-state` endpoint (#122)](https://github.com/lumenaut-llc/oesis-program-specs/issues/122) — enables participant-entered state

Other U8 children, other bridge endpoints, and U11 release-automation can wait until specific triggers.

### Phase 2 exit criteria

- Observability + backup + IaC in place
- Dependabot enabled + triage cycle exercised once
- Test-strategy doc exists
- At least 2 bridge endpoints live
- `make oesis-v*-accept` still all pass

---

## Phase 3 — v1.0 Tier-B external pilot

**Goal:** Enroll real participants. Stop-ship rules from `v1.0-launch-checklist.md` apply.

**Hardest work in the plan.** Legal + governance + pilot-readiness + hardware field validation must all clear before first external participant.

### Proposed nine-week sequence

| Week | Track | Tickets |
|---|---|---|
| 1–2 | **Legal starts** (lawyer roundtrip is the biggest wall-clock risk) | [Participant ToS (#179)](https://github.com/lumenaut-llc/oesis-program-specs/issues/179), [privacy-policy audit (#180)](https://github.com/lumenaut-llc/oesis-program-specs/issues/180), [research-ethics review (#196)](https://github.com/lumenaut-llc/oesis-program-specs/issues/196) |
| 1–2 | **Pilot governance framework** (parallel with legal) | [UA5 tracker (#65)](https://github.com/lumenaut-llc/oesis-program-specs/issues/65) + children [(#92–97)](https://github.com/lumenaut-llc/oesis-program-specs/issues/92) |
| 3–4 | **Launch-checklist signoffs** (parallelize — mostly review work) | [GL-3 claims review (#117)](https://github.com/lumenaut-llc/oesis-program-specs/issues/117), [GL-5 holdback audit (#118)](https://github.com/lumenaut-llc/oesis-program-specs/issues/118), [SO-3 data-publication audit (#124)](https://github.com/lumenaut-llc/oesis-program-specs/issues/124), [PI-1 consent checklist (#125)](https://github.com/lumenaut-llc/oesis-program-specs/issues/125), [PI-2 operator checklist (#126)](https://github.com/lumenaut-llc/oesis-program-specs/issues/126), [PI-4 participant notice (#128)](https://github.com/lumenaut-llc/oesis-program-specs/issues/128) |
| 3–4 | **Product-surface completion** | [PU-3 evidence view (#119)](https://github.com/lumenaut-llc/oesis-program-specs/issues/119), [PU-5 metadata capture (#120)](https://github.com/lumenaut-llc/oesis-program-specs/issues/120), [PU-6 deployment-quality flags (#121)](https://github.com/lumenaut-llc/oesis-program-specs/issues/121), [PU-7 sharing settings UI (#131)](https://github.com/lumenaut-llc/oesis-program-specs/issues/131), [PI-5 notice-matching enforcement (#127)](https://github.com/lumenaut-llc/oesis-program-specs/issues/127) |
| 5–6 | **Hardware field validation** | [HR-3 mast-lite field-hardening (#132)](https://github.com/lumenaut-llc/oesis-program-specs/issues/132), [HR-6 flood-node install (#133)](https://github.com/lumenaut-llc/oesis-program-specs/issues/133), [HR-10 protective-fixture tests (#134)](https://github.com/lumenaut-llc/oesis-program-specs/issues/134) |
| 7–8 | **Pilot-ops tooling** | Cross-cutting ops parallels: [dashboard scope (#44)](https://github.com/lumenaut-llc/oesis-program-specs/issues/44), [incident escalation (#45)](https://github.com/lumenaut-llc/oesis-program-specs/issues/45), [offboarding (#46)](https://github.com/lumenaut-llc/oesis-program-specs/issues/46) |
| 9 | **First pilot launches** against cleared gate set | — |

### Phase 3 exit criteria

Per `v1.0-launch-checklist.md` §Stop-ship triggers:

- Every Tier-B launch-checklist blocker `complete` (not `in progress`)
- First participant onboarded under reviewed ToS + signed consent + approved notice
- Incident escalation flow + named contacts in place
- Pilot dashboard operational
- No stop-ship triggers outstanding

---

## Phase 4 — v1.5 horizon (post-external-pilot)

Activates per trigger. Don't schedule work before trigger fires.

| Cluster | Trigger |
|---|---|
| [U1 IoT integration (#21)](https://github.com/lumenaut-llc/oesis-program-specs/issues/21) (18 children) | First Matter/HomeKit/ecosystem-adopting pilot; prioritize one ecosystem |
| [U2 Climate roadmap (#22)](https://github.com/lumenaut-llc/oesis-program-specs/issues/22) (7 children) | Climate-planning use case emerges |
| [U10 i18n (#146)](https://github.com/lumenaut-llc/oesis-program-specs/issues/146) (5 children) | First non-US deployment |
| [U16 HW-ops (#169)](https://github.com/lumenaut-llc/oesis-program-specs/issues/169) (3 children) | BME680 EOL announcement OR fleet scale >50 nodes |
| [U7 bridge endpoints (#116)](https://github.com/lumenaut-llc/oesis-program-specs/issues/116) (remaining 4 of 6) | Per-endpoint use case appears; don't build all upfront |
| [U3 cross-cutting-ops (#23)](https://github.com/lumenaut-llc/oesis-program-specs/issues/23) (9 children, all `defer`) | Each child has an explicit trigger annotated in its body |

---

## Slow-burn design threads (ongoing background)

These produce design docs, not shipped product. Realistic cadence: **~1 doc per month across all threads**, not per-thread.

| Thread | Output | Activation |
|---|---|---|
| [UA1 local-first (#61)](https://github.com/lumenaut-llc/oesis-program-specs/issues/61) | Processing-boundary + offline-runtime specs | Steady; not gating |
| [UA2 contribution schema (#62)](https://github.com/lumenaut-llc/oesis-program-specs/issues/62) | Derived-contribution schema + shared-layer rules | Steady |
| [UA3 hazard-engine interface (#63)](https://github.com/lumenaut-llc/oesis-program-specs/issues/63) | Plugin interface spec | Bundle into one PR if possible |
| [UA4 route safety (#64)](https://github.com/lumenaut-llc/oesis-program-specs/issues/64) | Route + segment schemas + inference | After v1.0 Tier-A |
| [UA5 pilot governance (#65)](https://github.com/lumenaut-llc/oesis-program-specs/issues/65) | Framework + standards + roles | **Required for Phase 3** |
| [U8 security hygiene (#144)](https://github.com/lumenaut-llc/oesis-program-specs/issues/144) | SBOMs, signed releases, hardware provenance, firmware security | 1 per quarter after Phase 2 minimums |
| [U9 accessibility (#145)](https://github.com/lumenaut-llc/oesis-program-specs/issues/145) | Baseline, audit, plain-language, per-surface criteria | Baseline first; others with UI work |
| [U11 eng-infra (#164)](https://github.com/lumenaut-llc/oesis-program-specs/issues/164) | Versioning policy, release automation | Versioning-policy soon; others triggered |
| [U12 testing (#165)](https://github.com/lumenaut-llc/oesis-program-specs/issues/165) | Load + chaos + regression | Chaos with UA1; regression with first v0.2→v0.3 promotion |
| [U13 research (#166)](https://github.com/lumenaut-llc/oesis-program-specs/issues/166) | Reproducibility, ADR 0006 impl, citation, peer review | Reproducibility + citation near-term; peer review with first paper |
| [U14 legal (#167)](https://github.com/lumenaut-llc/oesis-program-specs/issues/167) | ToS, privacy-audit, export-control | **ToS + privacy-audit required for Phase 3** |
| [U15 sustainability (#168)](https://github.com/lumenaut-llc/oesis-program-specs/issues/168) | Funding, non-code contribution, comms policy | Funding near-term |
| [U17 ethics/equity (#193)](https://github.com/lumenaut-llc/oesis-program-specs/issues/193) | Equity audit, vulnerable-pop UX, IRB, e-waste | **IRB required for Phase 3**; others ongoing |

---

## Parallel workstreams by contributor type

| Track | Approx ticket volume | Representative tickets |
|---|---|---|
| **Hardware (physical)** | 10–12 | G12, G13, G14-hw, G16, G20, HR-3, HR-6, HR-10, FMEA (U16), firmware security |
| **Runtime (Python)** | 20+ | G11 children, G14-runtime, G15, G23, bridge endpoints, observability, backup, IaC |
| **Design / architecture docs** | 50+ | UA1–UA5, U8–U17 children — each is a spec doc |
| **Governance / legal** | 10–12 | U14 children, PI signoffs, UA5 framework, GOVERNANCE extensions |
| **Operations** | 8–10 | Docker packaging, backup drills, monitoring setup, pilot dashboards |
| **Research / publication** | 5–6 | U13 children, dataset publication per ADR 0006 |

### Capacity-bound scenarios

**Single contributor:** plan compresses to Phase 1 → legal+security prep → Phase 3. Drop design threads entirely until Tier-B pilot is running.

**Multiple contributors:** tracks parallelize well. Design threads become steady output at ~1 doc/month each.

---

## Project 5 view configuration

With 202 items, view setup is load-bearing. Configure these saved views in [Project 5](https://github.com/orgs/lumenaut-llc/projects/5):

| View | Filter | Approx count |
|---|---|---|
| **Active now** (default) | `Severity: blocker AND Status != Done` | ~30 |
| **v0.2 critical path** | `Phase: v0.2 AND Severity: blocker` | 13 |
| **Tier-B launch gates** | `Program: v1.0-launch-gates` | 20 |
| **Design-thread backlog** | `Program in (local-first, contribution-schema, hazard-engine, route-safety, pilot-governance, iot-integration, climate-roadmap, ethics-equity)` | ~75 |
| **Deferred / triggered** | `Severity: defer` | 48 |
| **By node family** | Group-by Node field | — |

Default on open should be **Active now**. The 150 non-blocker items should not dominate the first impression.

---

## Review and governance cadences

| Cadence | What | Why |
|---|---|---|
| Weekly | Triage new items; advance in-progress | Prevents ticket graveyard |
| Per-milestone | Slice-promotion review per `pre-1.0-version-progression.md` | Required by doctrine |
| Per-release | SBOM regeneration, Dependabot triage, CHANGELOG | Release hygiene once U8 + U11 release-automation land |
| Quarterly | Close obviously-dead deferred tickets | Prevents tracker bloat |
| Annually | Equity audit (U17 #194); accessibility audit (U9 #148) | Calendar-driven, not triggered |

---

## Risks and their mitigations

| Risk | Mitigation |
|---|---|
| ToS lawyer-review roundtrip delays Phase 3 | Start legal track at Week 1 of Phase 3 (before launch-checklist signoffs) |
| Design-thread work crowds out gate-cluster work | Hard rule: no design-thread PR lands without a blocker-track PR also landing that week |
| G11 chain stalls at one step (e.g., G17 schema debate) | Escalate to ADR after 2 weeks of debate; design-decision bias toward shipping shadow mode |
| Hardware track blocks software | Software can proceed against fixtures until mast-lite reproducible; fixture → live swap is a late-phase task |
| Deferred items accumulate past usefulness | Quarterly triage sweep closes dead tickets |
| Project 5 becomes unreadable at 200+ items | View configuration above; re-run view audit each quarter |

---

## Definition of success

**This plan succeeds** when:

1. v0.2 slice is promoted per `pre-1.0-version-progression.md`.
2. v1.0 Tier-A internal reference is operationally mature.
3. First Tier-B external pilot runs with real participants under reviewed ToS + IRB-equivalent review + live incident-escalation path.
4. Design-thread docs land at steady cadence without blocking gate clusters.

**This plan fails** when:

- A year passes with 30 design-decomposition PRs merged but no live Tier-B pilot.
- Project 5 balloons past 300 items without triage sweeps.
- Launch-checklist Tier-B blockers drift in "in progress" state indefinitely because no one owns them.
- G11 hazard-formula-v1 stays in shadow without Brier/ECE comparison against v0 on real pilot labels.

---

## Related

- [`program/execution-plan.md`](../program/execution-plan.md)
- [`architecture/current/milestone-roadmap.md`](../architecture/current/milestone-roadmap.md)
- [`architecture/current/pre-1.0-version-progression.md`](../architecture/current/pre-1.0-version-progression.md)
- [`release/v.0.1/v0.1-gap-register.md`](../release/v.0.1/v0.1-gap-register.md)
- [`release/v1.0/v1.0-launch-checklist.md`](../release/v1.0/v1.0-launch-checklist.md)
- [`meta/backlog.md`](backlog.md)
- [`meta/milestones/phase-0-foundation.md`](milestones/phase-0-foundation.md)
- [`meta/milestones/phase-1-pilot-readiness.md`](milestones/phase-1-pilot-readiness.md)
- [Project 5 on GitHub](https://github.com/orgs/lumenaut-llc/projects/5)
