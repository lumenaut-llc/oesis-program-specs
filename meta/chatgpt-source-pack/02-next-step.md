---
title: Next Step
status: canonical-summary
updated: 2026-04-13
sources:
  - architecture/system/version-and-promotion-matrix.md
  - architecture/current/pre-1.0-version-progression.md
  - ../oesis-public-site/src/app/program/page.tsx
  - ../oesis-public-site/src/data/siteContent.ts
---

# Next Step

This file captures the next honest promotion rather than the whole eventual vision.

The core takeaway remains that the next real step is program-phase v0.2: a widened indoor plus sheltered-outdoor parcel kit with explicit promotion evidence, stronger trust and parcel binding, and clearer product-language alignment between specs and public-site messaging.

Conventions for path/label interpretation are defined once in
`README.md` for this source-pack.

## Why This File Exists

This summary is followed by verbatim source-file copies so the synthesized guidance and the underlying canonical text stay together in one markdown.

## Included Source Files

- `architecture/system/version-and-promotion-matrix.md`
- `architecture/current/pre-1.0-version-progression.md`
- `../oesis-public-site/src/app/program/page.tsx`
- `../oesis-public-site/src/data/siteContent.ts`

## Verbatim Source Content

### File: `architecture/system/version-and-promotion-matrix.md`

```md
# Version and Promotion Matrix

## Purpose

Hold a single **non-ambiguous** map between:

- **Public / accepted runnable slices** (`v0.1`, next `v0.2`, …)
- **Capability stages** (`current v1`, `v1.5`, `v2`, `v2.5`, `v3`, `v4`)
- **Deployment maturity** (per node family: `deployment maturity v0.1` … `v2.0`)
- **Implementation status** (`implemented`, `partial`, `docs-only`, `planned`)

Use this document when writing roadmaps, kit language, or marketing so **taxonomy** and **implementation truth** do not collapse into one version number.

## The four axes

| Axis | Question it answers | Examples |
| --- | --- | --- |
| **Accepted runnable slice** | What end-to-end story is **promoted** as the current honest baseline? | `v0.1` today; `v0.2` when bench-air + mast-lite + contracts/runtime meet the promotion bar |
| **Capability stage** | What **class of product behavior** is in scope for architecture and contracts? | `current v1` sensing/inference; `v1.5` intervention bridge objects |
| **Deployment maturity** | Is this **node family** bench-grade or field-hardened? | Per family in `deployment-maturity-ladder.md` |
| **Implementation status** | For each surface, what is actually shipped vs drafted? | Runtime observation table in `integrated-parcel-system-spec.md` |

**Folder note:** `architecture/current/` is the frozen **architecture lane** aligned with program-phase `v0.1`. That is **not** the same label as capability stage `current v1` (see `architecture-gaps-by-stage.md`).

## Product anchor: current truth, next promotion, later staged additions

| | **Current truth** | **Next promotion** | **Later staged additions** |
| --- | --- | --- | --- |
| **Product bar** | One parcel, one bench-air lineage, ingest → inference → parcel view. Frozen working reference slice (`v0.1`). | **Program-phase `v0.2`:** real indoor + sheltered-outdoor parcel kit (`bench-air-node` + `mast-lite`) with explicit architecture scope, contract/runtime boundary updates, acceptance checks, and implementation-status evidence (`../current/pre-1.0-version-progression.md`). Do **not** treat mast-lite as fully proven until that promotion bar is met. | Capability `v1.5` through `v4`: intervention bridge, bounded guidance, controls compatibility, adaptation memory, route/block resilience (`phase-roadmap.md`). |
| **Core purpose** | Prove parcel-first sensing and inference under partial adoption. | Prove the first coherent **field-credible** two-node parcel kit with stronger parcel binding and ops evidence. | Evolve toward bounded adaptation: connect hazard, house state, action, and verified outcome without overclaiming automation. |
| **Hardware in scope** | Bench-air as the proven reference lineage. | Mast-lite as coordinated kit member; optional flood only where parcel-relevant. | `v1.5` bridge families (indoor-response, power-outage, adapters); geography modules (`flood-node`, `weather-pm-mast`, `freeze-node`); `thermal-pod` remains research-gated (`node-taxonomy.md`). |
| **Software / data in scope** | Ingest, normalization, parcel inference, parcel view, confidence, evidence mode, provenance, private/shared/public distinction. | Stronger ingest authorization, parcel binding, field-hardening alignment, clearer evidence summaries in the parcel view. | `v1.5` support objects; `v2` guidance layer; `v2.5` compatibility inventory and bounded controls; `v3` adaptation memory; `v4` route/community layers. |
| **House-state / intervention** | Not part of the current proven reference slice beyond parcel-context optional fields in drafts. | Design and document bridge surfaces; do not describe them as fully implemented in runtime unless status says so. | `v1.5`: indoor response, outage, equipment-state signals, building/site metadata, action log, outcome verification (`architecture-gaps-by-stage.md`). |
| **Controls compatibility** | Not an executed product guarantee in the narrow slice. | Draft or partial docs may exist; keep language honest. | **Primary home for full compatibility inventory and bounded-control execution: `v2.5`**, not `v1.5`. |
| **Governance** | Private-by-default and provenance discipline are part of product framing; several flows remain **partial** or **docs-only**. | Same honesty constraint while kit scope widens. | Stronger export/retention execution, verified revocation, and operational governance UX land in later promotions (see `../current/pre-1.0-version-progression.md` for example `v0.5` governance slice). |

## Pre-1.0 progression (accepted slice ladder)

Canonical detail: `../current/pre-1.0-version-progression.md`.

| Slice | Intent |
| --- | --- |
| `v0.1` | One parcel, one bench-air path, ingest → parcel view |
| `v0.2` | First widened kit: stable indoor + sheltered outdoor |
| `v0.3` | First flood-capable runtime slice with dedicated flood observation family |
| `v0.4` | Stronger multi-node registry and evidence composition |
| `v0.5` | Operational sharing/governance slice with real revocation, retention, export evidence |
| `v1.0` (program sense) | Materially broader system than the first narrow slice — distinct from website marketing labels |

New `v0.x` slices should **only** ship when the runnable system boundary **materially** expands, not when a single schema draft appears.

## Capability stages (summary)

| Stage | Role |
| --- | --- |
| `current v1` | Parcel sensing and inference baseline |
| `v1.5` | Minimum bridge: house-state and intervention **support objects**, equipment-state **read-side** evidence, action/outcome logs, trust/device-operation objects |
| `v2` | Bounded adaptation **guidance** (policy separate from hazard) |
| `v2.5` | **Compatibility inventory**, bounded controls, control verification |
| `v3` | Adaptation memory / learning |
| `v4` | Parcel + route + block resilience |

## Governance honesty

Revocation, sharing/consent execution, and some governance paths may remain **docs-only** or **partial** while the reference slice is narrow. Product copy and architecture claims should say **implemented** only when the runtime and acceptance evidence match.

## Related docs

- `../current/pre-1.0-version-progression.md`
- `node-taxonomy.md`
- `architecture-gaps-by-stage.md`
- `deployment-maturity-ladder.md`
- `integrated-parcel-system-spec.md`
- `phase-roadmap.md`
- `../../contracts/v0.1/README.md`
```

### File: `architecture/current/pre-1.0-version-progression.md`

```md
# Pre-1.0 Version Progression

## Purpose

Define how pre-`1.0` versions should advance without turning every incremental
addition into a new architecture lane.

## Core rule

Use a new `v0.x` only when the accepted runnable reference slice changes in a
way that materially expands what the system is and does.

Do not create a new `v0.x` for:

- every added node or hardware element
- every schema or example addition
- every partial implementation step
- every milestone status change

Use milestones and implementation-status labels for that narrower growth.

## Recommended progression

- `v0.1`
  One parcel, one bench-air node, one accepted ingest-to-parcel-view path.
- `v0.2`
  First widened parcel-kit slice with stable indoor-plus-sheltered-outdoor
  operation.
- `v0.3`
  First accepted flood-capable runtime slice with a dedicated flood observation
  family.
- `v0.4`
  First accepted multi-node parcel slice with stronger registry and evidence
  composition posture.
- `v0.5`
  First accepted operational sharing/governance slice with real revocation,
  retention, export, and boundary enforcement evidence.
- `v1.0`
  First materially broader system that is no longer just the narrow first
  working reference slice.

## Promotion bar for the next slice

Before promoting a new pre-`1.0` version such as `v0.2`, require:

1. explicit architecture scope
2. explicit contract and runtime boundary changes
3. explicit acceptance commands or check updates
4. explicit implementation-status evidence showing what changed

If those conditions are not met, keep the work inside the current accepted lane
and track it through milestones and status posture.

## Related docs

- `../system/version-and-promotion-matrix.md` — how accepted slices relate to capability stages and deployment maturity
- `../system/node-taxonomy.md` — hardware and v1.5 bridge surfaces referenced by widening slices
- `../system/integrated-parcel-system-spec.md` — tiered parcel kit design
```

### File: `../oesis-public-site/src/app/program/page.tsx`

```tsx
import Image from "next/image";
import Link from "next/link";
import { PhaseModel } from "@/components/PhaseModel";
import { ReleaseRoadmap, type RoadmapStage } from "@/components/ReleaseRoadmap";
import { ScopeCallout } from "@/components/ScopeCallout";
import { buildMetadata } from "@/lib/metadata";
import {
  phaseModel,
  programPage,
  releaseStrategy,
  roadmapTldr,
  versionPath
} from "@/data/siteContent";
import { releaseDocLink } from "@/data/releaseContent";
import { withTrailingSlash } from "@/lib/site";

const pageTitle = "Program | Open Environmental Sensing and Inference System";

export const metadata = buildMetadata({
  title: pageTitle,
  description: programPage.description,
  pathname: "/program/"
});

export default function ProgramPage() {
  return (
    <>
      <section className="page-intro">
        <p className="eyebrow">Initiative</p>
        <div className="section-head page-intro-head">
          <div>
            <h1>{programPage.title}</h1>
            <p className="lede">
              {programPage.ledeBeforeHowWeShipLink}
              <Link href="#how-we-ship">{programPage.howWeShipLinkLabel}</Link>
              {programPage.ledeAfterHowWeShipLink}
            </p>
            <div className="action-row program-narrative-links">
              <Link className="button button-secondary" href="/why-it-matters/">
                Why it matters
              </Link>
              <Link className="button button-secondary" href="/how-it-works/">
                How it works
              </Link>
            </div>
          </div>
        </div>
      </section>

      <ScopeCallout />

      <section className="panel" id="how-we-ship" aria-labelledby="how-we-ship-heading">
        <div className="section-head">
          <div>
            <p className="section-kicker">{releaseStrategy.programSectionKicker}</p>
            <h2 id="how-we-ship-heading">{releaseStrategy.programTitle}</h2>
            {releaseStrategy.summary.map((paragraph) => (
              <p key={paragraph}>{paragraph}</p>
            ))}
            <div className="table-wrap">
              <table className="release-strategy-table">
                <thead>
                  <tr>
                    <th scope="col">Label</th>
                    <th scope="col">In plain terms</th>
                    <th scope="col">For implementers</th>
                    <th scope="col">Verify</th>
                  </tr>
                </thead>
                <tbody>
                  {releaseStrategy.rows.map((row) => (
                    <tr key={row.label}>
                      <th scope="row">{row.label}</th>
                      <td>{row.inPlainTerms}</td>
                      <td>{row.forImplementers}</td>
                      <td>
                        {"verify" in row && row.verify ? (
                          row.verify.href.startsWith("http://") ||
                          row.verify.href.startsWith("https://") ? (
                            <a
                              href={row.verify.href}
                              target="_blank"
                              rel="noopener noreferrer"
                            >
                              {row.verify.label}
                            </a>
                          ) : (
                            <Link href={withTrailingSlash(row.verify.href)}>{row.verify.label}</Link>
                          )
                        ) : (
                          <span className="release-strategy-verify-muted">—</span>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </section>

      <section className="panel v10-mockups-panel" id="program-v10-mockups" aria-labelledby="v10-mockups-heading">
        <div className="section-head">
          <div>
            <p className="section-kicker">Program-phase v0.2 next promotion</p>
            <h2 id="v10-mockups-heading">Target experience vs reference stack today</h2>
            <p>
              In program-specs, <strong>v0.2</strong> is the <strong>next accepted parcel-kit promotion</strong>—for
              example indoor <strong>bench-air</strong> plus sheltered-outdoor <strong>mast-lite</strong>, stronger
              trust and history, and more parcel-operator surfaces—without jumping to the v1.5 measurement-to-intervention
              bridge or a full route/block engine. The open-release packet also treats several product surfaces as{" "}
              <strong>partial</strong> or <strong>planned</strong> relative to that target. These are different pictures
              of product maturity: current narrow truth, next promotion target, and later bridge work.
            </p>
          </div>
        </div>
        <div className="v10-mockup-stack">
          <figure className="build-maturity-illustration">
            <Image
              src="/content/publicPages/v10-program-phase-target-mockup.png"
              alt="Concept mockup: one parcel with bench-air indoor node and mast-lite outdoor reference, beside a parcel-view web UI with readiness cards, evidence, history, nodes, and sharing or export."
              width={1376}
              height={768}
              sizes="(max-width: 960px) 100vw, min(1376px, 92vw)"
            />
          </figure>
          <p className="v10-mockup-caption">
            <strong>Program-phase v0.2 target (next promotion).</strong> Illustrative north star for a parcel kit
            and operator experience: two reference nodes on one parcel and a parcel-facing surface with readiness-style
            summaries, evidence legibility, history, node health, and basic sharing or export—not a guarantee that every
            element is live in the reference runtime, and not v1.5 automation, intervention ranking, public
            parcel-resolution maps, or full governance guarantees. See phasing and{" "}
            <Link href="/roadmap/">Roadmap</Link> for how this relates to later work.
          </p>
          <figure className="build-maturity-illustration">
            <Image
              src="/content/publicPages/v10-reference-implementation-today-mockup.png"
              alt="Technical diagram: bench-air node to local ingest API, inference API, parcel platform API, and JSON outputs such as parcel state and evidence summary; mast-lite shown as partial or staged."
              width={1376}
              height={768}
              sizes="(max-width: 960px) 100vw, min(1376px, 92vw)"
            />
          </figure>
          <p className="v10-mockup-caption">
            <strong>Reference implementation today.</strong> The stressed path is a narrow, verifiable pipeline—local
            ingest, inference, and parcel APIs—producing contract-shaped JSON (for example parcel state, parcel view,
            evidence summary). Many consumer-grade surfaces from the v1.0 target remain partial or docs-only; start from{" "}
            <Link href="/open-release/">Open release</Link> and the program-specs{" "}
            <a href={releaseDocLink("v1.0-scope.md")} target="_blank" rel="noopener noreferrer">
              v1.0 scope
            </a>{" "}
            doc for the honest status table.
          </p>
        </div>
      </section>

      <section className="panel" aria-labelledby="why-program-heading">
        <div className="section-head">
          <div>
            <p className="section-kicker">Why this structure</p>
            <h2 id="why-program-heading">Parcel-first, local, community-aligned</h2>
          </div>
        </div>
        <div className="program-why-grid">
          {programPage.whyMatters.map((item) => (
            <article key={item.title} className="program-why-card">
              <h3>{item.title}</h3>
              <p>{item.body}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="panel compact-actions-panel">
        <div className="section-head">
          <div>
            <p className="section-kicker">Explore</p>
            <h2>Related pages</h2>
            <p>
              Systems and components, the phased roadmap, and governance are split out so this page stays narrative.
            </p>
          </div>
        </div>
        <div className="action-row">
          <Link className="button button-primary" href="/systems/">
            Systems
          </Link>
          <Link className="button button-secondary" href="/roadmap/">
            Roadmap
          </Link>
          <Link className="button button-secondary" href="/governance-and-privacy/">
            Governance
          </Link>
        </div>
      </section>

      <section className="panel roadmap-panel">
        <div className="section-head">
          <div>
            <p className="section-kicker">Technical lineage</p>
            <h2>Version arc & capability phases</h2>
            <p>{roadmapTldr}</p>
            <p className="roadmap-note">
              The public nine-phase roadmap lives on <Link href="/roadmap/">Roadmap</Link>. Below is the engineering-style
              version path and intermediate capability model for implementers.
            </p>
          </div>
        </div>
        <ReleaseRoadmap stages={versionPath as RoadmapStage[]} />
        <details className="disclosure roadmap-disclosure">
          <summary className="disclosure-summary">
            <span className="section-kicker">Technical</span>
            <strong>Capability phases between major releases</strong>
            <span className="disclosure-hint">Expand</span>
          </summary>
          <div className="disclosure-body">
            <p className="phase-model-intro">
              Practical product steps between major releases—from an instrumented parcel to interior response, sparse
              shared inference, and federated local systems.
            </p>
            <PhaseModel groups={phaseModel} />
          </div>
        </details>
      </section>
    </>
  );
}
```

### File: `../oesis-public-site/src/data/siteContent.ts`

```ts
import type { PathCardData } from "./pathCard";
import { releaseDocLink, repoLink } from "./releaseContent";

/** Public roadmap (nine phases). Engineering arc: `versionPath` / `phaseModel`. */
export type ProgramPhaseStatus = "complete" | "active" | "next" | "planned";

export const programScope = {
  title: "Program scope",
  body:
    "Open Environmental Sensing and Inference System (OESIS) is a parcel-first environmental sensing and inference program. It combines sensing, parcel inference, governance, neighborhood intelligence, and pilot deployment while keeping parcel-linked data private by default. Long term, it aims to support predictive software for local climate-related conditions and hazards using local observations, parcel context, public data, and optional neighborhood evidence. The parcel remains the anchor for decisions as the program grows. Outputs are meant to complement official alerts and emergency authorities, not replace them.",
  bullets: [
    "Modular hardware and software that scale from one parcel to networks",
    "Explicit governance: private by default, shared by choice",
    "Long-term path from field pilots to broader shared intelligence"
  ]
};

export const currentBuildScope = {
  title: "Current build scope",
  body:
    "The current reference slice is narrow: one parcel, one bench-air lineage, one parcel context, one ingest path, one inference path, and one parcel view. The next planned step is a two-node indoor and sheltered-outdoor kit built from bench-air plus mast-lite. In parallel, the team is focused on the first field pilot, monitoring, documentation, and partnerships.",
  bullets: [
    "v0.1 reference path from bench-air ingest to a parcel view",
    "Single-home and small-site parcel awareness with explicit uncertainty",
    "Partnerships and docs that make deployment repeatable"
  ]
};

/** Home: scannable now vs long-term band (ScopeCallout and Program carry full narrative). */
export const homeImplementationHorizon = {
  kicker: "Implementation horizon",
  title: "Shipping now versus long-term direction",
  intro:
    "Current engineering work is limited to a narrow reference path so contracts, runtime, and the public site stay aligned. That path is smaller than the full program vision. The specs separate current slices such as v0.1 and v0.2 from later capability stages such as v1.5. See the version and promotion matrix for details.",
  timeHorizonNote:
    "This is a long-term effort built through pilots, documentation, and gradual field use.",
  now: {
    badge: "Now",
    phaseLabel: "Program-phase v0.1 reference slice",
    summary:
      "The current slice runs from a bench-air-class node through ingest and inference to one parcel view, with parcel context, confidence, evidence mode, and plain-language reasons. Field pilot prep, operator documentation, governance, and partnerships are being developed alongside that path.",
    detailsLabel: "What this slice is trying to prove",
    details: [
      "One parcel, one sensor lineage, one ingest path, one inference path, and one parcel-facing view",
      "Observed, inferred, and stale states are shown clearly, with provenance the parcel operator can understand",
      "Governance and release boundaries match the open release packet",
      "Documentation and examples support repeatable deployment on the same reference path"
    ],
    chips: [
      "Bench-air-first",
      "Parcel state contract",
      "Open release packet",
      "Pilot + partnerships in parallel"
    ],
    footnote:
      "The home '1.0' label refers to the current public preview, not the full long-term roadmap."
  },
  longTerm: {
    badge: "Long term",
    phaseLabel: "Long-term direction",
    summary:
      "Over time, the program aims to support predictive software for local climate-related conditions and hazards. It combines local observations, parcel context, public data, and optional neighborhood evidence in ways that remain useful under partial adoption.",
    detailsLabel: "What later phases add (direction, not a commitment)",
    details: [
      "More neighborhood and multi-parcel evidence under opt-in sharing rules",
      "Clearer links from measurement to house state, interventions, and verification",
      "Operating models that support shared intelligence without giving up parcel operator control",
      "Outputs that complement official alerts, insurers, and utilities"
    ],
    chips: [
      "Multi-scale networks",
      "v1.0 fielded kit target",
      "v1.5 intervention bridge",
      "Shared by choice",
      "Complements official systems"
    ],
    footnote:
      "The parcel stays the anchor for decisions as scope expands."
  },
  links: [
    { label: "Shipping labels on Program", href: "/program/#how-we-ship" },
    { label: "Phased roadmap", href: "/roadmap/" },
    { label: "Open release hub", href: "/open-release/" }
  ]
};

export const programPhases: {
  order: number;
  name: string;
  goal: string;
  deliverables: string[];
  status: ProgramPhaseStatus;
}[] = [
  {
    order: 1,
    name: "Single-home utility & parcel view",
    goal: "Establish a trustworthy parcel information contract for one home: observed vs inferred, advisory outputs, parcel stewardship.",
    deliverables: [
      "Parcel operator parcel view and release boundary",
      "Core nodes and software path documented in open release",
      "Public preview aligned with governance posture"
    ],
    status: "active"
  },
  {
    order: 2,
    name: "Evidence quality & confidence layer",
    goal: "Make confidence, reason codes, and evidence quality legible in the product—not hidden scores.",
    deliverables: [
      "Stronger confidence framing for parcel state",
      "Reason codes and freshness visible in the parcel view",
      "Tighter alignment between ingest and display semantics"
    ],
    status: "next"
  },
  {
    order: 3,
    name: "Hazard-specific parcel workflows",
    goal: "Move smoke, flood/runoff, and heat from generic status toward clearer parcel workflows.",
    deliverables: [
      "Hazard-specific UX and readiness framing",
      "Parcel-honest messaging where evidence is sparse",
      "Documentation for deployers per hazard"
    ],
    status: "planned"
  },
  {
    order: 4,
    name: "Integrated parcel kit",
    goal: "One coherent parcel kit: unified ingest, stronger evidence, single parcel surface.",
    deliverables: [
      "Kit-level BOM and installation story",
      "Unified evidence path across nodes",
      "Reduced integration friction for builders"
    ],
    status: "planned"
  },
  {
    order: 5,
    name: "Interior response & verification",
    goal: "Relate outdoor forcing to indoor response; close the loop with bounded verification—not assumed success.",
    deliverables: [
      "Interior / critical-room awareness in the model",
      "Manual guidance and soft integrations where appropriate",
      "Did-it-help style verification cues"
    ],
    status: "planned"
  },
  {
    order: 6,
    name: "Block-scale sparse inference",
    goal: "Introduce shared signals derived from parcel-first evidence across nearby parcels.",
    deliverables: [
      "Sparse shared inference with uneven adoption",
      "Route, drainage, and edge dependency modeling",
      "Policy-gated shared outputs"
    ],
    status: "planned"
  },
  {
    order: 7,
    name: "Neighborhood coordination layer",
    goal: "Make neighborhood-scale coordination a first-class product concern.",
    deliverables: [
      "Shared neighborhood priors and context",
      "Operational neighborhood layer distinct from block-only views",
      "Clear upgrade path from parcel to network semantics"
    ],
    status: "planned"
  },
  {
    order: 8,
    name: "Federation & interoperability",
    goal: "Let independent local systems exchange coarse signals and policies without collapsing ownership.",
    deliverables: [
      "Federation patterns and governance boundaries",
      "Interoperability for status layers across communities",
      "Technical contracts for cross-system exchange"
    ],
    status: "planned"
  },
  {
    order: 9,
    name: "City-scale federation",
    goal: "Connect larger areas while preserving local control and parcel-first rules.",
    deliverables: [
      "City-scale coordination narratives and limits",
      "Long-horizon governance and trust models",
      "Optional links to civic and institutional partners"
    ],
    status: "planned"
  }
];

export const pilot = {
  /** One paragraph for the home page pilot teaser (detail stays on /pilot/). */
  homeTeaser:
    "The field pilot moves the program from reference docs to real sites in one defined local geography. It focuses on repeatable installs, structured feedback, and operational learning. Geography, goals, and partner paths are on the pilot page.",
  geography:
    "The first field pilot targets one defined local geography, to be announced with partners. The scope is large enough to test installs, ingest, and support in real conditions.",
  goals: [
    "Prove repeatability: install, operate, and interpret parcel evidence in real homes",
    "Exercise governance in practice: private by default, optional sharing",
    "Collect structured feedback for kit, docs, and product boundaries"
  ],
  audience:
    "Parcel operators and residents who want parcel-level environmental awareness, local partners who can support installs and community trust, and technical contributors who need a real deployment context for software and hardware.",
  siteBenefits: [
    "A pilot parcel-level view of air, heat, water risk, and smoke context aligned to your property, with confidence and evidence limits shown",
    "Participation in shaping the pilot playbook and documentation",
    "Direct line to the team for support, constraints, and governance questions"
  ],
  successCriteria: [
    "Stable operation of the pilot stack across participating sites",
    "Documented lessons for install, inference trust, and parcel operator communication",
    "Credible path from pilot learnings to the next program phases"
  ],
  partnerEngagement:
    "Use the Get involved page to choose a path for pilot sites, community partners, technical contributors, or funding."
};

export const workstreams = [
  {
    id: "hardware",
    title: "Hardware",
    summary:
      "Indoor and outdoor air nodes, flood points, thermal pod work, and future mast-class builds. Specs and build guides live in Docs.",
    links: [
      { label: "Systems overview", href: "/systems/" },
      { label: "Hardware specs (Docs)", href: "/open-release/#hardware-specs" }
    ]
  },
  {
    id: "software",
    title: "Software",
    summary:
      "Parcel platform, ingest, inference, and an optional shared map, with documented interfaces and contracts for implementers.",
    links: [
      { label: "Systems overview", href: "/systems/" },
      { label: "Software specs (Docs)", href: "/open-release/#software-specs" }
    ]
  },
  {
    id: "inference",
    title: "Inference",
    summary:
      "Turning observations into parcel-state estimates with explicit uncertainty and clear observed-versus-inferred framing.",
    links: [
      { label: "Roadmap", href: "/roadmap/" },
      { label: "Governance", href: "/governance-and-privacy/" }
    ]
  },
  {
    id: "governance-privacy",
    title: "Governance & privacy",
    summary:
      "Private by default, shared by choice, dwelling-scale data, and advisory outputs with clear policy and product boundaries.",
    links: [{ label: "Governance", href: "/governance-and-privacy/" }]
  },
  {
    id: "pilot-deployment",
    title: "Pilot deployment",
    summary:
      "Field installs, partner coordination, and the practical bridge from documentation to working sites.",
    links: [
      { label: "Pilot", href: "/pilot/" },
      { label: "Get involved", href: "/get-involved/" }
    ]
  },
  {
    id: "documentation-partnerships",
    title: "Documentation & partnerships",
    summary:
      "Architecture indexes, build guides, and partner paths that support pilots and keep documentation current.",
    links: [
      { label: "Open release hub", href: "/open-release/" },
      { label: "Diagrams", href: "/diagrams/" },
      { label: "Get involved", href: "/get-involved/" }
    ]
  }
] as const;

export const systemsFamily = {
  intro:
    "The system family includes field nodes, software services, and shared-intelligence layers. This page distinguishes what is closest to field deployment from what is still staged or in R&D.",
  /** Near-term vs staged hardware; software panels follow below. */
  buildMaturity: {
    kicker: "Builds",
    title: "What is closest to real sites right now",
    intro:
      "Some modules are documented earlier than they are field-ready. Bench Air is the clearest current slice, mast-lite is the next outdoor step, and flood, richer weather and particulate masts, and thermal remain staged lanes.",
    lanes: [
      {
        label: "Now",
        body:
          "Bench Air Node: current reference build for repeatable indoor or sheltered parcel evidence through the ingest-to-parcel-view stack."
      },
      {
        label: "Next",
        body:
          "Mast-lite outdoor node: next documented outdoor step for weather and air at the parcel edge, following the current bench-class reference path."
      },
      {
        label: "Staged / R&D",
        body:
          "Flood points, richer weather and particulate masts, and privacy-minded thermal pods remain important but are not presented as equally mature field products in this preview."
      }
    ]
  },
  /** Concept rows not duplicated as separate spec sections */
  concepts: [
    {
      id: "weather-pm-mast",
      name: "Weather + PM mast",
      status: "planned" as const,
      tldr: "A richer outdoor mast combining weather and particulate context at parcel edge—successor path beyond mast-lite for full air + weather storytelling.",
      links: [{ label: "Mast-lite (current outdoor step)", href: "/open-release/#hardware-specs" }]
    },
    {
      id: "parcel-engine",
      name: "Parcel engine",
      status: "spec" as const,
      tldr: "Ingest + inference + parcel platform as the coherent ‘engine’ that turns evidence into parcel state and dwelling-facing guidance.",
      links: [
        { label: "Ingest service", href: "/open-release/#software-specs" },
        { label: "Inference engine", href: "/open-release/#software-specs" }
      ]
    },
    {
      id: "shared-neighborhood-intelligence",
      name: "Shared neighborhood intelligence",
      status: "spec" as const,
      tldr: "Policy-gated shared map and future neighborhood layers—downstream of parcel ownership, optional by design.",
      links: [{ label: "Shared map spec", href: "/open-release/#software-specs" }]
    }
  ]
};

export const getInvolvedPaths: readonly PathCardData[] = [
  {
    id: "community",
    title: "Community partners",
    summary:
      "Neighborhood groups, local orgs, and advocates who want parcel-honest environmental awareness without surrendering data rights.",
    timeHint: "Start with pilot framing",
    primaryCta: { label: "Pilot details", href: "/pilot/" },
    secondaryCta: { label: "Get involved", href: "/get-involved/" }
  },
  {
    id: "pilot-sites",
    title: "Pilot sites",
    summary:
      "Homes or small multi-site clusters willing to run early hardware and software and give structured feedback.",
    timeHint: "Ongoing participation",
    primaryCta: { label: "Pilot overview", href: "/pilot/" },
    secondaryCta: { label: "Get involved", href: "/get-involved/" }
  },
  {
    id: "technical",
    title: "Technical contributors",
    summary:
      "Builders, firmware and backend engineers, and integrators implementing against open specs and contracts.",
    timeHint: "Self-paced against specs",
    primaryCta: { label: "Open release hub", href: "/open-release/" },
    secondaryCta: { label: "Diagrams", href: "/diagrams/" }
  },
  {
    id: "research",
    title: "Research collaborators",
    summary:
      "Groups studying environmental inference, human factors, or governance of community sensor networks.",
    primaryCta: { label: "Program", href: "/program/" },
    secondaryCta: { label: "Governance and privacy", href: "/governance-and-privacy/" }
  },
  {
    id: "funding",
    title: "Funding partners",
    summary:
      "Funders who want to support open documentation, pilots, and noncommercial public benefit.",
    primaryCta: { label: "Roadmap", href: "/roadmap/" },
    secondaryCta: { label: "Program", href: "/program/" }
  },
  {
    id: "documentation",
    title: "Documentation contributors",
    summary:
      "Editors and technical writers improving build guides, architecture explanations, and onboarding.",
    primaryCta: { label: "Open release hub", href: "/open-release/" },
    secondaryCta: { label: "How it works", href: "/how-it-works/" }
  }
];

export const homeFeatured = {
  latestProgress: {
    date: "April 2026",
    title: "Public preview & site restructure",
    body:
      "The site now separates program scope from current build scope and routes audiences to Understand, Program, and Build & specs. Next: pilot geography with partners and field milestones as they land.",
    moreLabel: "Project note",
    moreHref: "/note/"
  },
  partnerStrip: {
    title: "Help shape the pilot",
    body:
      "We are organizing community partners, pilot sites, builders, and funders. Pick a path on Get involved—or start with the Pilot page if you represent a site.",
    primaryLabel: "Get involved",
    primaryHref: "/get-involved/",
    secondaryLabel: "Pilot details",
    secondaryHref: "/pilot/"
  }
};

export const programPage = {
  title: "Program",
  description:
    "Open program for parcel-first environmental sensing and inference, modular systems, governance, and a path from pilots to neighborhood-scale intelligence.",
  ledeBeforeHowWeShipLink:
    "OESIS is an open program for parcel-first environmental sensing and inference. It combines modular hardware, explicit uncertainty, and governance that keeps parcel operators in control of parcel-linked data unless they choose to share it. Long-term direction includes preparedness, disaster relief, and climate- and infrastructure-resilience intelligence. For version labels and release scope, see ",
  ledeAfterHowWeShipLink:
    " and the open release packet. For a plain-language overview, start with Why it matters and How it works. This page focuses on scope, shipping labels, and technical lineage.",
  howWeShipLinkLabel: "How we ship",
  whyMatters: [
    {
      title: "Parcel-first, not only regional",
      body: "Forecasts and regional indices miss property-specific risk. Parcel-first systems anchor decisions to what your site actually experiences."
    },
    {
      title: "Local & community-controlled",
      body: "Networks can grow from real places and real stewardship instead of only top-down dashboards—still bounded by opt-in sharing and clear policies."
    },
    {
      title: "Modular and incremental",
      body: "Small nodes and clear contracts let pilots start narrow and expand without rewriting the ownership model."
    }
  ]
};

export const homeVision = {
  headline: "Parcel-first environmental sensing and inference.",
  lede:
    "Home sensors, regional hazard maps, alerts, and community data efforts already exist. OESIS focuses on combining those kinds of inputs around the parcel as the decision point.",
  lede2:
    "The current scope is narrower than the long-term program. This preview focuses on parcel-level interpretation of smoke, heat, and water-related conditions, with uncertainty, provenance, and data boundaries shown clearly. It is meant to complement official alerts and local judgment, not replace them.",
  boundaryLine:
    "This public preview documents direction, boundaries, and contracts. It is not a finished product, live emergency service, or public operational map.",
  timeHorizonLine:
    "Progress depends on pilots, documentation, and field learning over time. Near-term work stays focused on narrow slices that can be tested and published clearly."
};

/** Short phrases surfaced at the top of the home hero (scan-friendly program keywords). */
export const homeKeywordTags = [
  "Parcel-level focus",
  "Combined evidence",
  "Parcel-level interpretation",
  "Partial adoption",
  "Private by default",
  "Shared by choice",
  "Multi-hazard property view",
  "Parcel-relevant vs regional-only",
  "Verification is staged",
  "Complements official systems"
] as const;

/** Canonical home hero diagram (see `public/content/publicPages/hero.png`). */
export const homeHeroDiagram = {
  src: "/content/publicPages/hero.png",
  alt:
    "Conceptual parcel-first overview: one parcel as the anchor, four evidence lanes, a bounded parcel view, and a narrow current public slice rather than a live neighborhood network.",
  caption:
    "Conceptual overview: one parcel, four evidence lanes, and one bounded parcel view. This is intentionally narrower and more truthful than a live neighborhood map or a claim that the full long-range network already exists."
};

export const heroTldr = {
  lede:
    "This preview is a parcel-level environmental read for smoke, heat, air, and water-related conditions. It shows uncertainty and provenance clearly and keeps raw readings with the operator unless they choose to share."
};

export const releaseStrategy = {
  homeKicker: "How we ship",
  homeTitle: "Preview, labels, and where to verify",
  teaserBullets: [
    "The site can move faster than any one documentation tag—use it for orientation, then confirm in the open release packet and spec repos.",
    "Program-phase v0.1 (narrow reference slice), v0.2 (two-node parcel-kit promotion target), v1.0 (materially broader system), and capability v1.5 (measurement-to-intervention bridge) are defined in program-specs—do not assume they match marketing or website “v1.0” unless release materials say so.",
    "The home snapshot label describes the current product slice; the open release packet describes what is published for implementers.",
    "Roadmap phases are narrative; the version arc on Program is the engineering-style lineage.",
    "Durable value—if it comes—will likely compound on a roughly decade-scale horizon (adoption, trust, field proof); near-term work is narrow slices and pilot learning, not the whole payoff at once."
  ],
  programSectionKicker: "Shipping and previews",
  programTitle: "How we ship",
  summary: [
    "This website is a public preview: copy and links may update between tagged documentation drops.",
    "When we say “1.0” on the home snapshot, we mean the current single-home utility slice and hazard focus—not “finished forever,” and not necessarily program-phase v1.0 or the runtime v1.0 asset lane unless the release packet aligns them.",
    "Implementers should treat the open release packet and contract bundles as the canonical boundary for what is published to build against.",
    "Phase and lane vocabulary matches `program/v0.1/README.md` and `architecture/current/` in the program-specs repository—website labels are for orientation only.",
    "The program assumes patient, staged work: the most consequential value—if it materializes—may only be obvious on a roughly decade-scale horizon (adoption, trust, infrastructure fit), while near-term releases stay deliberately narrow."
  ],
  rows: [
    {
      label: "Site preview",
      inPlainTerms: "Narrative pages and cross-links that explain the program and point to deeper docs.",
      forImplementers: "Use for orientation; verify schemas and build guides in program-specs and runtime repos.",
      verify: { label: "Open release", href: "/open-release/" }
    },
    {
      label: "Home snapshot label",
      inPlainTerms:
        "The small card on the home page names the product slice we are emphasizing right now (scope and hazard focus).",
      forImplementers:
        "Aligns with the field pilot and published contracts for that slice—not the entire nine-phase roadmap at once."
    },
    {
      label: "Public packet v1.0",
      inPlainTerms: "The first published open-release boundary: what is licensed, reviewed, and safe to cite.",
      forImplementers: "Start from the v1.0 summary and publication matrix, then follow links into contracts and hardware guides.",
      verify: { label: "Open source v1 summary (repo)", href: releaseDocLink("open-source-v1-summary.md") }
    },
    {
      label: "Version arc and phases",
      inPlainTerms:
        "Accepted slices and capability stages (for example v0.1 → v0.2 → v1.0, with capability v1.5 after the sensing baseline) describe how the product grows over time.",
      forImplementers: "See the arc and capability model on this page; use Roadmap for phase status and milestones.",
      verify: { label: "Roadmap", href: "/roadmap/" }
    }
  ] as const
};

export const projectNoteHome = {
  line: "Curious why this is framed as parcel-first systems work—not “one more sensor shop”?",
  linkText: "Read a short project note",
  href: "/note/"
};

/** Recommended first-time path on the home page. */
export const homeStartHere = {
  kicker: "Start here",
  title: "New to OESIS? Follow this path",
  intro: "Three short stops before you open the full documentation hub.",
  steps: [
    {
      order: 1,
      label: "Why it matters",
      href: "/why-it-matters/",
      blurb: "Why parcel-level interpretation matters and where this fits alongside regional systems."
    },
    {
      order: 2,
      label: "How it works",
      href: "/how-it-works/",
      blurb: "Evidence layers, modes, and advisory outputs in plain language."
    },
    {
      order: 3,
      label: "Governance and privacy",
      href: "/governance-and-privacy/",
      blurb: "Ownership, sharing, privacy, and the boundaries of the current system."
    }
  ] as const
};

export const homePullQuote = {
  quote:
    "Private by default, shared by choice, and explicit about uncertainty. The public site describes the current scope and release boundaries.",
  attribution: "Public preview stance"
};

export const openReleaseAudienceBridge = {
  programLabel: "Program overview",
  programHref: "/program/",
  governanceLabel: "Governance and privacy",
  governanceHref: "/governance-and-privacy/"
};

/** In-page jump row on `/open-release/` (hash targets must match element ids on that page). */
export const openReleaseJumpLinks = [
  { label: "Release packet", hash: "release-packet-heading" },
  { label: "Hardware specs", hash: "hardware-specs" },
  { label: "Software specs", hash: "software-specs" },
  { label: "Spec collections", hash: "released-specs-heading" }
] as const;

/** Shown above outbound GitHub spec links on the open release page. */
export const openReleaseGitHubLinksNote =
  "Specification links open the public GitHub program-specs repository in a new tab.";

/** Scannable trust boundary above the implementer hub (aligned with release packet, not new legal claims). */
export const openReleaseTrustPosture = {
  title: "What is open—and what stays private by default",
  bullets: [
    "The public release surface is intentionally scoped: specs, guides, and architecture indexes published with the preview—not an unfiltered dump of every internal file.",
    "Future participant parcel-linked raw data is not public by default; governance describes ownership, data classes, and opt-in sharing.",
    "Parcel-state style outputs are estimates and inferences for judgment—they do not replace official alerts or emergency authority.",
    "When something is still research, staged, or not yet cleared for publication, the site should not read as if it were already fielded product.",
    "For policy detail, use Governance and privacy; for exact publication boundaries, follow the v1.0 open-release packet and linked contracts."
  ]
};

export const principles = [
  {
    title: "Parcel first",
    tldr: "The product thinks about your whole property, not only a regional forecast.",
    body: "Focus on parcel-level conditions instead of only coarse regional signals."
  },
  {
    title: "Private by default",
    tldr: "Sensors and readings belong to the parcel operator unless you explicitly share.",
    body: "Raw participant-contributed data stays operator-controlled."
  },
  {
    title: "Shared by choice",
    tldr: "Anything broader than your parcel is optional and controlled by policy you can see.",
    body: "Broader sharing is opt-in, bounded, and policy-gated."
  }
] as const;

/** Home: scannable one-liners; full principles copy remains on Program and governance pages. */
export const homePrinciplesSummary = {
  intro:
    "Technical modules and releases change; these ideas stay fixed. Details live on Program and Governance and privacy.",
  bullets: principles.map((p) => ({ title: p.title, line: p.tldr }))
} as const;

export const currentRelease = {
  label: "1.0",
  title: "Single-home utility",
  scope: "Useful parcel awareness for one home.",
  productUnit: "Parcel",
  hazards: ["Smoke", "Flooding / runoff", "Heat"],
  boundary: "Non-enabling public preview",
  nextUnlock: "Integrated parcel kit"
};

export const v1InformationOverview = {
  title: "Why version 1 matters",
  tldr:
    "The first release is about trust: you can tell what was measured, what was estimated, and how confident the system is—without treating any of it as a guarantee or an official alert.",
  body:
    "Version 1 is the first public release that establishes a trustworthy parcel information contract: what is directly observed, what is inferred from evidence, how uncertainty is explained, and what remains advisory rather than authoritative.",
  pillars: [
    {
      label: "Observed",
      title: "Direct parcel and public-context inputs",
      tldr: "Sensors, your site context, and public feeds (like weather or smoke layers) feed the picture.",
      body: "Local nodes, parcel context, and relevant public feeds establish the first evidence base instead of asking the parcel operator to trust a black box."
    },
    {
      label: "Inferred",
      title: "Parcel-state estimates from evidence",
      tldr: "The system turns readings into estimates for your parcel—honest about limits, not pretending to be certainty.",
      body: "The product turns those inputs into parcel-state estimates that stay parcel-first and do not pretend to be certainty or official alerts."
    },
    {
      label: "Explained",
      title: "Confidence, reasons, and evidence framing",
      tldr: "You see why it thinks what it thinks, not just a score or a color.",
      body: "The parcel view is meant to distinguish observed conditions from inferred conditions and show why the system is leaning in a given direction."
    },
    {
      label: "Bounded",
      title: "Advisory outputs inside a clear public boundary",
      tldr: "Outputs are guidance for your judgment, with clear limits on what is claimed in public.",
      body: "Version 1 defines what the system may say publicly, what remains private, and what the product does not claim to know or control."
    }
  ]
};

export const noticeTldr = {
  bullets: [
    "This site is an early public preview, not the full product or a complete technical drop.",
    "Your data stays private by default; wider sharing is always a choice.",
    "Guidance is advisory—not a substitute for official alerts or your own judgment."
  ]
};

/** Dual-register boundary: plain language + implementer verify language (same posture, two readings). */
export const publicBoundaryDual = {
  sectionKicker: "Preview boundary",
  plainTitle: "What this site does and does not do",
  plainIntro:
    "The same posture as Governance and privacy and the open release packet—here in plain language before you click deeper.",
  plainBullets: noticeTldr.bullets,
  implementerTitle: "For implementers—verify, do not infer from marketing copy",
  implementerBullets: [
    "Treat the v1.0 open-release packet and linked contracts as canonical for what is published to build against.",
    "Site copy can move between tagged documentation drops—confirm hashes, bundles, and publication matrices in program-specs before you depend on a path.",
    "Future participant parcel-linked raw data is not public by default; governance and contracts describe sharing lanes, not a blanket public dataset.",
    "Parcel-state style outputs are advisory estimates and inferences—they do not replace official alerts, emergency authority, or your operational judgment."
  ],
  links: [
    { label: "Governance and privacy", href: "/governance-and-privacy/" },
    { label: "Open release hub", href: "/open-release/" },
    { label: "Why it matters", href: "/why-it-matters/" }
  ] as const
} as const;

/** Narrow first path for builders landing on the open release hub. */
export const implementerGoldenPath = {
  title: "First build path",
  intro:
    "Run one slice end to end—bench-air-class hardware through published software contracts—before branching to other modules.",
  steps: [
    {
      label: "Bench Air (hardware hub)",
      href: "/open-release/#hardware-specs",
      note: "Start from the released indoor / sheltered air node on the hub."
    },
    {
      label: "Software specs",
      href: "/open-release/#software-specs",
      note: "Ingest, inference, and parcel platform contracts linked from the hub."
    },
    {
      label: "Diagrams",
      href: "/diagrams/",
      note: "Public-safe architecture flow before you open implementation-heavy repos."
    },
    {
      label: "v1.0 scope (program-specs)",
      href: releaseDocLink("v1.0-scope.md"),
      note: "Honest status table—opens the public repo in a new tab."
    }
  ] as const
} as const;

/** Maintainer’s own integration / publishing state—never conflated with all pilots or partners. */
export const maintainerImplementation = {
  kicker: "From the maintainer",
  title: "What I am running against this preview",
  disclaimer:
    "This reflects the maintainer’s publishing and engineering focus—not a warranty that every pilot site, partner, or contributor matches the same checkout, hardware mix, or timeline.",
  lastUpdated: "April 2026",
  statusLines: [
    "Public site structure and copy kept aligned with the program-specs open release packet and phased roadmap.",
    "Engineering attention on the bench-air-first reference path and parcel-facing read contracts described on the open release hub.",
    "Pilot geography and field milestones are partner-dependent; the site does not claim nationwide or production deployment."
  ],
  primaryCta: { label: "Open release hub", href: "/open-release/" },
  secondaryCta: { label: "Project note", href: "/note/#a-personal-note" }
} as const;

/** One-line human hook on the home hero; full anecdote on the project note. */
export const homeMaintainerTeaser = {
  line:
    "I did not set out to claim empty markets or magic sensors—I wanted parcel-honest sense-making that stays yours unless you share it, with room to grow toward outcomes you can actually verify.",
  linkLabel: "Read the personal note",
  href: "/note/#a-personal-note"
} as const;

export const roadmapTldr =
  "You are here: useful awareness for one home. Next steps tighten the kit, then add careful sharing between nearby properties, neighborhoods, and eventually larger federated networks—without giving up parcel-first ownership.";

export const informationArchitectureTldr =
  "In plain terms: sensors and feeds create evidence, software turns that into a parcel picture, the app shows status and reasons, and sharing sits on top with explicit rules.";

export const howItWorksTldr = {
  intro: "Three ideas behind the diagrams below:",
  bullets: [
    "Your parcel view comes first; anything shared more widely is downstream and optional.",
    "Several small nodes can still feel like one system: one ingest path and one parcel view.",
    "Private data, optional contributions, and public feeds stay in separate lanes."
  ]
};

export const specsSectionTldr = {
  hardware:
    "Open hardware modules cover indoor air, sheltered outdoor reference, optional flood points, and a privacy-minded thermal option. Each has build and firmware docs for makers.",
  software:
    "Software pieces cover the parcel app, ingestion, inference, and optional neighborhood map outputs—each documented for implementers.",
  collections:
    "Indexes for architecture, data contracts, and build guides—jump in here if you are implementing against the open release."
};

export const governanceSectionTldr =
  "Ownership stays with the parcel operator, sharing is opt-in, outputs are estimates, and this preview does not open real contributed data or hidden implementation detail.";

export const diagramsSectionTldr =
  "High-level flowcharts show how nodes, software, and policy fit together. Open a card for audience notes, spec links, and the live diagram render.";

export const openReleaseHub = {
  title: "Open release hub",
  lede:
    "Hardware modules, software services, architecture indexes, data contracts, and build guides published with this public preview. Visual flowcharts live on the Diagrams page.",
  backToHomeLabel: "Back to overview",
  diagramsLinkLabel: "Architecture diagrams"
};

export const audienceEntryPoints: readonly PathCardData[] = [
  {
    id: "operators",
    title: "Parcel operators and neighbors",
    summary:
      "Start with the problem gap and parcel-first framing, then governance for ownership, sharing, and claim limits.",
    timeHint: "Short reads first",
    primaryCta: { label: "Why it matters", href: "/why-it-matters/" },
    secondaryCta: { label: "Governance and privacy", href: "/governance-and-privacy/" }
  },
  {
    id: "builders",
    title: "Builders and integrators",
    summary:
      "Evidence layers, modes, and advisory outputs in plain language—then hardware, software, and schemas on the open release hub.",
    timeHint: "Plain language, then specs",
    primaryCta: { label: "How it works", href: "/how-it-works/" },
    secondaryCta: { label: "Open release hub", href: "/open-release/" }
  },
  {
    id: "partners",
    title: "Partners and pilots",
    summary:
      "Follow the roadmap, pilot scope, and how to plug into deployment—after the short Why it matters / How it works spine so expectations stay aligned.",
    timeHint: "Align expectations, then engage",
    primaryCta: { label: "Get involved", href: "/get-involved/" },
    secondaryCta: { label: "Pilot", href: "/pilot/" }
  }
];

export const openReleaseBridge = {
  title: "Open release documentation",
  body:
    "Hardware specs, software specs, and core spec collections now live on a dedicated hub so this page stays oriented for every audience. Your old links still land here; jump to the matching section on the hub.",
  ctaLabel: "Browse the full open release hub",
  jumpHardware: "Hardware specs (on hub)",
  jumpSoftware: "Software specs (on hub)",
  jumpCollections: "Core spec collections (on hub)"
};

export const hardwareSpecSections = [
  {
    id: "bench-air-node",
    name: "Bench Air Node",
    status: "released",
    tldr: "Indoor or sheltered air reference and the quickest way to get real readings through the full stack.",
    whatItDoes:
      "Produces the first repeatable indoor or sheltered parcel evidence and exercises the full ingest-to-parcel-view path.",
    whyItMatters:
      "It is the fastest hardware route from concept to trustworthy parcel evidence.",
    diagramRelevance: ["System context", "Recommended first integrated prototype"],
    links: [
      { label: "Overview", href: repoLink("hardware/bench-air-node/README.md") },
      { label: "Build guide", href: repoLink("hardware/bench-air-node/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/bench-air-node/firmware/README.md") }
    ]
  },
  {
    id: "mast-lite",
    name: "Mast-Lite Outdoor Node",
    status: "released",
    tldr: "Outdoor reference for weather and air at the edge of the parcel.",
    whatItDoes:
      "Adds sheltered outdoor parcel context without waiting for the richer mast build.",
    whyItMatters:
      "It is the simplest outdoor step that turns a single-home slice into a fuller parcel kit.",
    diagramRelevance: ["Recommended first integrated prototype", "Parcel view surface"],
    links: [
      { label: "Overview", href: repoLink("hardware/mast-lite/README.md") },
      { label: "Build guide", href: repoLink("hardware/mast-lite/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/mast-lite/firmware/README.md") }
    ]
  },
  {
    id: "flood-node",
    name: "Flood Node",
    status: "released",
    tldr: "Depth and rise-rate evidence at meaningful runoff low points.",
    whatItDoes:
      "Measures low-point runoff evidence while staying explicit that one point is not the whole parcel story.",
    whyItMatters:
      "It adds flood-specific evidence without pretending a single sensor point is parcel-wide truth.",
    diagramRelevance: ["Recommended first integrated prototype", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("hardware/flood-node/README.md") },
      { label: "Build guide", href: repoLink("hardware/flood-node/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/flood-node/firmware/README.md") }
    ]
  },
  {
    id: "thermal-pod",
    name: "Thermal Pod",
    status: "released",
    tldr: "Derived thermal scene metrics without raw imagery persistence.",
    whatItDoes:
      "Provides area-level thermal context through privacy-safe derived metrics rather than stored frames.",
    whyItMatters:
      "It opens a path to scene sensing while preserving the project’s privacy posture.",
    diagramRelevance: ["Parcel view surface", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("hardware/thermal-pod/README.md") },
      { label: "Build guide", href: repoLink("hardware/thermal-pod/build-guide.md") },
      { label: "Firmware", href: repoLink("hardware/thermal-pod/firmware/README.md") }
    ]
  }
];

export const softwareSpecSections = [
  {
    id: "parcel-platform",
    name: "Parcel Platform",
    status: "released",
    tldr: "The dwelling-facing app and API surface for parcel status, evidence, and freshness.",
    whatItDoes:
      "Turns parcel-state outputs and evidence summaries into a usable parcel view without hiding uncertainty.",
    whyItMatters:
      "It is the main product surface where parcel awareness becomes usable rather than buried inside pipeline internals.",
    diagramRelevance: ["System context", "Parcel view surface"],
    links: [
      { label: "Overview", href: repoLink("software/parcel-platform/README.md") },
      { label: "Interfaces", href: repoLink("software/parcel-platform/interfaces.md") },
      { label: "Integrated parcel system spec", href: repoLink("docs/system-overview/integrated-parcel-system-spec.md") }
    ]
  },
  {
    id: "ingest-service",
    name: "Ingest Service",
    status: "released",
    tldr: "Validates device packets and external feeds, then normalizes them into canonical observations.",
    whatItDoes:
      "Creates the evidence boundary that turns raw packets into the parcel-first information model.",
    whyItMatters:
      "It is the place where raw measurements become consistent, inspectable evidence for the rest of the system.",
    diagramRelevance: ["System context", "Recommended first integrated prototype"],
    links: [
      { label: "Overview", href: repoLink("software/ingest-service/README.md") },
      { label: "Interfaces", href: repoLink("software/ingest-service/interfaces.md") },
      { label: "Data model index", href: repoLink("docs/data-model/README.md") }
    ]
  },
  {
    id: "inference-engine",
    name: "Inference Engine",
    status: "released",
    tldr: "Combines observations and context into parcel-state outputs with explicit uncertainty.",
    whatItDoes:
      "Turns normalized evidence into parcel-state guidance while keeping reasons, freshness, and confidence visible.",
    whyItMatters:
      "It is where parcel evidence becomes parcel-state guidance without pretending sparse evidence is certainty.",
    diagramRelevance: ["System context", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("software/inference-engine/README.md") },
      { label: "Interfaces", href: repoLink("software/inference-engine/interfaces.md") },
      { label: "Integrated parcel system spec", href: repoLink("docs/system-overview/integrated-parcel-system-spec.md") }
    ]
  },
  {
    id: "shared-map",
    name: "Shared Map",
    status: "released",
    tldr: "Optional coarse neighborhood outputs built from policy-gated shared signals.",
    whatItDoes:
      "Creates a neighborhood condition layer that remains downstream of parcel ownership and sharing controls.",
    whyItMatters:
      "It is the part of the stack where network effects become visible without exposing raw parcel data.",
    diagramRelevance: ["System context", "Data-rights and visibility boundary"],
    links: [
      { label: "Overview", href: repoLink("software/shared-map/README.md") },
      { label: "Architecture", href: repoLink("software/shared-map/architecture.md") },
      { label: "Shared map posture", href: repoLink("docs/system-overview/shared-map-product-posture.md") }
    ]
  }
];

export const releasedSpecCollections = [
  {
    label: "Architecture",
    title: "Versioned architecture and operating model",
    tldr: "How hardware, software, identity, and governance fit together across versions.",
    body:
      "Current technical architecture guidance that explains how hardware, software, parcel identity, governance, and future architecture debate fit together.",
    links: [
      { label: "Architecture index", href: repoLink("architecture/README.md") },
      { label: "Current architecture", href: repoLink("architecture/current/README.md") },
      { label: "Integrated parcel system spec", href: repoLink("docs/system-overview/integrated-parcel-system-spec.md") }
    ]
  },
  {
    label: "Contracts",
    title: "Schemas and canonical contracts",
    tldr: "Formal definitions for parcels, nodes, observations, and sharing behavior.",
    body:
      "Canonical parcel, node, observation, and sharing definitions for the released system surface.",
    links: [
      { label: "Contracts index", href: repoLink("contracts/v0.1/README.md") },
      { label: "v1.0 contracts", href: repoLink("contracts/v1.0/README.md") },
      { label: "Data model index", href: repoLink("docs/data-model/README.md") }
    ]
  },
  {
    label: "Build guides",
    title: "Hardware assembly and deployment guidance",
    tldr: "Cross-subsystem references for building, procuring, and installing the parcel kit.",
    body:
      "BOMs, procurement checklists, installation guidance, and node-specific build references for the current released kit.",
    links: [
      { label: "Build guides index", href: repoLink("docs/build-guides/README.md") },
      { label: "Integrated parcel kit BOM", href: repoLink("docs/build-guides/integrated-parcel-kit-bom.md") },
      { label: "Parcel installation checklist", href: repoLink("docs/build-guides/parcel-installation-checklist.md") }
    ]
  }
];

export const publicBoundary = {
  publicNow: [
    {
      title: "Mission and architecture",
      detail: "The parcel-first system model and high-level architecture are public."
    },
    {
      title: "Ownership and sharing",
      detail: "Ownership, privacy, and opt-in sharing rules are public."
    },
    {
      title: "Claims and limits",
      detail: "Claims, limitations, and public-safe diagrams are part of this release."
    }
  ],
  notPublicNow: [
    {
      title: "Implementation detail",
      detail: "Implementation-enabling technical detail remains out of scope."
    },
    {
      title: "Real contributed data",
      detail: "Real participant-contributed parcel-linked data is not blanket-open."
    },
    {
      title: "Safety authority claims",
      detail: "The project does not claim emergency authority or guaranteed safety."
    }
  ]
};

export const versionPath = [
  {
    label: "1.0",
    title: "Single-home utility",
    body: "First useful parcel awareness for one home.",
    adds: "Establishes the dwelling parcel view, ownership controls, and the first truthful public release boundary.",
    releaseWindow: "Current preview",
    status: "current"
  },
  {
    label: "1.5",
    title: "Integrated parcel kit",
    body: "One coherent parcel kit instead of separate nodes.",
    adds: "Unifies ingest, strengthens parcel evidence, and turns the first release into a more complete parcel view surface.",
    releaseWindow: "Next build target",
    status: "next"
  },
  {
    label: "2.0",
    title: "Block intelligence",
    body: "First sparse shared intelligence across nearby parcels.",
    adds: "Introduces block-scale derived intelligence without abandoning parcel ownership rules or the parcel-first operating model.",
    releaseWindow: "Future direction",
    status: "future"
  },
  {
    label: "3.0",
    title: "Neighborhood network",
    body: "Neighborhood coordination becomes a first-class product layer.",
    adds: "Extends from block-scale inference to broader neighborhood coordination, richer shared signals, and clearer network behavior.",
    releaseWindow: "Future direction",
    status: "future"
  },
  {
    label: "4.0",
    title: "City federation",
    body: "Federated local systems connect at city scale.",
    adds: "Connects larger areas without collapsing local control, parcel ownership, or neighborhood-level governance.",
    releaseWindow: "Long-range direction",
    status: "future"
  }
];

export const phaseModel = [
  {
    bridge: "Between 1.0 and 1.5",
    title: "From instrumented parcel to integrated parcel kit",
    outcome:
      "The house stops looking like a few evidence points and starts behaving like one coherent parcel system.",
    phases: [
      {
        label: "1.1",
        title: "Evidence quality and confidence layer",
        body: "Observed vs inferred parcel state becomes clearer, with stronger confidence framing and reason codes for the parcel view."
      },
      {
        label: "1.2",
        title: "Hazard-specific parcel workflows",
        body: "Smoke, flood / runoff, and heat move from one generic status model toward clearer parcel workflows and more truthful readiness framing."
      },
      {
        label: "1.6",
        title: "Interior response awareness",
        body: "The product begins relating outdoor forcing to indoor response and critical-room conditions instead of treating the parcel as exterior-only."
      },
      {
        label: "1.7",
        title: "Bounded action and verification loop",
        body: "Manual guidance and limited soft integrations are judged by did-it-help verification rather than assumed success."
      }
    ]
  },
  {
    bridge: "Between 1.5 and 2.0",
    title: "From one parcel kit to sparse local intelligence",
    outcome:
      "Shared awareness begins, but it still grows from parcel-first evidence rather than replacing it.",
    phases: [
      {
        label: "2.1",
        title: "Sparse shared inference",
        body: "A partially instrumented local area can support shared signals without requiring every house to look identical or participate at the same depth."
      },
      {
        label: "2.x",
        title: "Route, drainage, and edge dependency modeling",
        body: "Parcels are understood in relation to route vulnerability, low points, drainage edges, and other block-level dependencies."
      }
    ]
  },
  {
    bridge: "Between 2.0 and 3.0",
    title: "From block signals to neighborhood coordination",
    outcome:
      "The system matures from local inference into a broader shared layer that can support neighborhood-scale coordination.",
    phases: [
      {
        label: "2.5",
        title: "Shared neighborhood priors",
        body: "Block-scale evidence starts informing parcel priors, neighborhood context, and broader situational framing even where adoption is uneven."
      },
      {
        label: "2.8",
        title: "Operational neighborhood layer",
        body: "Neighborhood coordination becomes a distinct product concern instead of a loose extension of block intelligence."
      }
    ]
  },
  {
    bridge: "Between 3.0 and 4.0",
    title: "From neighborhood network to city federation",
    outcome:
      "The network scales outward by federation and interoperability rather than by collapsing local control into one central system.",
    phases: [
      {
        label: "3.5",
        title: "Federated interoperability and governance",
        body: "Independent local systems learn how to exchange signals, policies, and coarse status layers while preserving local ownership and governance boundaries."
      }
    ]
  }
];

export const informationInfrastructure = [
  {
    label: "Layer 1",
    title: "Observation layer",
    body: "Outdoor nodes, indoor monitors, parcel / site context, and public feeds provide the raw evidence that starts the parcel picture."
  },
  {
    label: "Layer 2",
    title: "Inference layer",
    body: "Observed signals are interpreted into parcel-state estimates, hazard framing, and later shared intelligence without collapsing the parcel-first model."
  },
  {
    label: "Layer 3",
    title: "Confidence and evidence layer",
    body: "The system needs to show why it thinks what it thinks: observed vs inferred framing, evidence quality, uncertainty, and confidence-bearing context."
  },
  {
    label: "Layer 4",
    title: "Decision surface",
    body: "The parcel operator sees parcel status, reasons, recommended actions, and verification cues rather than hidden scores or unexplained outputs."
  },
  {
    label: "Layer 5",
    title: "Rights and sharing layer",
    body: "Private parcel-linked data stays operator-controlled, while any broader sharing remains opt-in, bounded, and policy-gated."
  }
];
```
