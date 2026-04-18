# Open Environmental Sensing and Inference System

Open Environmental Sensing and Inference System (`OESIS`) is the canonical flagship
open program described in this repository.

`Resilient Home Intelligence` (`RHI`) remains a legacy compatibility name during
the transition.

Read `../../NOTICE.md` before treating this program as a complete technical open release.

OESIS is **parcel-first** and **multi-scale** by design: it starts at the dwelling and
parcel, and is meant to grow toward route, block, and broader coordination without
giving up private-by-default handling of parcel-linked data. The parcel is the anchor
for decisions; it is not the final boundary of the program's long-term scope.

## Mission

Create dwelling-scale environmental sensing and parcel-level situational intelligence that:
- works for individual homes
- improves with neighborhood participation
- preserves owner control of parcel-linked data, including explicit public-release choices
- uses external public data only inside the platform
- stays modular and open
- aims over the long term to support a grounded information layer for disaster
  preparedness, relief, and infrastructure and climate resilience—combining local
  observations, parcel and public context, and optional shared neighborhood evidence;
  the end goal is useful situational awareness, not accumulating sensors for their own sake
- presents conclusions as evidence-based and uncertainty-aware, and stays useful when
  adoption and coverage are partial
- is designed to complement official alerts and emergency authorities, not replace them

The program is now in its April 14, 2026 open-release period. Approved software,
hardware, documentation, governance materials, and intentionally public datasets may be
released under asset-specific terms, while some materials remain outside release for
privacy, provenance, security, or licensing reasons.

## Long-term direction

The program's long-term arc is **aspirational** and not a commitment about what any
single release ships today:

sensing → inference → functional interpretation → intervention and verification →
route, block, and community lifeline–scale resilience intelligence

Deeper framing of the information-layer target and functional recovery lives in
`../../architecture/system/vision-and-use-cases.md` and related system architecture docs.

## Lane contract

- **Baseline lane**: `v0.1/` program docs describe the active program baseline and
  framing.
- **Additive lanes**: use `../operating-packet/` for narrative packet deltas and
  lane-specific framing that should not silently rewrite baseline claims.
- **Compatibility policy**: when packet paths move, keep redirect stubs or index
  updates so older links still resolve.
- **Canonical mapping**: program labels must remain aligned with
  `../../architecture/system/version-and-promotion-matrix.md`.

## Program phase labels (summary)

These labels describe **program and execution posture**, not interchangeable marketing
tags. They are **not** the same as **capability stages** (`current v1`, `v1.5`, …) or
**deployment maturity** per node family — see `../../architecture/system/version-and-promotion-matrix.md`.

- **Program phase `v0.1`** — narrow executable reference slice; frozen truth in
  `../../architecture/current/`.
- **Program phase `v0.2`** — **next accepted runnable promotion** after `v0.1`: first
  widened parcel-kit slice with stable indoor plus sheltered outdoor operation
  (`bench-air-node` + `mast-lite`), with explicit promotion criteria in
  `../../architecture/current/pre-1.0-version-progression.md`. Not synonymous with “done”
  because docs exist; requires contract/runtime boundary and evidence per that doc.
- **Program phase `v1.0`** — first materially broader fielded system than the first
  narrow slice (see pre-1.0 progression); also used for the **runtime contract lane**
  [`v1.0/`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/) over the frozen `v0.1` baseline; architecture now also exposes an
  explicit `../../architecture/v1.0/` lane beside the transitional `../../architecture/future/`
  path — keep those meanings distinct from marketing “1.0” labels.
- **Capability stage `v1.5`** — measurement-to-intervention **foundation** (house-state,
  action/outcome logs, read-side equipment signals); explicit bridge-stage lanes now
  exist under `../../architecture/v1.5/`, [`v1.5/`](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/), `../../software/v1.5/`, and
  [`v1.5/`](https://github.com/lumenaut-llc/oesis-hardware/blob/main/v1.5/); roadmap and contracts may be draft;
  full **controls-compatibility inventory** is primarily **`v2.5`**.
- **Public or marketing “v1.0”** — website, release, or grant language; do not assume it
  matches program-phase lanes or the runtime `v1.0` contract lane unless release materials say so
  explicitly.

Canonical glossary (`program/operating-packet/`): `../operating-packet/00-version-labels-and-lanes.md`. Full promotion matrix:
`../../architecture/system/version-and-promotion-matrix.md`. Node and evidence taxonomy:
`../../architecture/system/node-taxonomy.md`.

Full phasing narrative: `../operating-packet/09-phasing-v0.1-v1.0-v1.5.md`. Delivery sequence tied to the
current reference stack: `../../architecture/current/milestone-roadmap.md`.

## Program structure

- `../../architecture/` — canonical architecture home for current, future, and system narratives
- [`oesis-hardware`](https://github.com/lumenaut-llc/oesis-hardware) — physical sensor nodes and installation systems
- `../../software/` — ingest, parcel platform, inference, and maps
- `../../contracts/` — contract docs, schemas, and example payloads
- `../../release/` — release packet materials and publication controls
- `../../legal/` — licensing, defensive publication, governance, and contribution policy
- `../../operations/` — pilot playbooks and operational materials
- `../../media/` — diagrams, renders, and images

## Current MVP hazards

- smoke
- pluvial flooding / runoff
- heat

## Current MVP outputs

For each parcel:
- shelter conditions estimate
- reentry conditions estimate
- egress conditions estimate
- asset risk estimate
- confidence
- evidence mode
- reasons

## Principles

- parcel first
- private by default
- shared by choice
- intentionally public datasets must be explicitly designated and licensed
- more nodes improve precision, not basic functionality
- explicit provenance and uncertainty

## Read first

- `../../NOTICE.md`
- `../../architecture/README.md`
- `../../architecture/current/README.md`
- `../../architecture/system/version-and-promotion-matrix.md` — current truth vs next promotion vs capability stages
- `../../architecture/system/node-taxonomy.md` — hardware and v1.5 bridge surfaces
- `../operating-packet/09-phasing-v0.1-v1.0-v1.5.md` — program phase framing (v0.1, v1.0, v1.5)
- `../../release/v1.0/open-source-v1-summary.md`
- `../../release/v1.0/asset-class-license-and-publication-matrix.md`
- `../../legal/ip.md`
- `../../legal/dataset-release-policy.md`
- `../../legal/GOVERNANCE.md`
- `../../legal/privacy/data-ownership.md`
- `../../legal/privacy/privacy.md`
- `../../release/v1.0/NOTICE.md`
