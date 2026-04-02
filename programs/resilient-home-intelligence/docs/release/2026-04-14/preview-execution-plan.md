# Preview Execution Plan

## Purpose

Turn the existing software, hardware, legal, and release documents into one practical execution sequence for the first credible public preview and first private pilot-ready parcel kit.

## Outcome target

At the end of this plan, the project should have:

- a reproducible software reference path
- a hardware build path that starts simple and scales by parcel tier
- a clear packet of legal and governance docs to send to reviewers or counsel
- a simple public-facing webpage that stays within the preview boundary

## Track 1: Software must run

### Goal

Make the current reference implementation dependable enough that docs, demos, and the first site all point at something that actually works.

### Current reference commands

- `make rhi-validate`
- `make rhi-check`
- `make rhi-http-check`

### Minimum done definition

- example contracts validate
- reference pipeline runs end to end
- local HTTP surfaces start and respond
- canonical package path remains `repo/rhi/`

### Next concrete steps

1. Keep `make rhi-validate`, `make rhi-check`, and `make rhi-http-check` green before any release or pilot demo.
2. Add one short operator README for how to start the reference services from `repo/`.
3. Implement the next observation families after `air.node.snapshot`:
   `flood.low_point.snapshot`, `air.pm_weather.snapshot`, and `thermal.scene.snapshot`.
4. Bind ingest authorization and parcel binding to the new node-registry object before adding more live node classes.

### Stop-ship rule

Do not let the website or legal copy imply a working control surface that the software still cannot demonstrate locally.

## Track 2: Hardware must be easy enough to build

### Goal

Make the physical system feel like a tiered kit, not a maze of unrelated prototypes.

### Recommended parcel tiers

- Tier 1: `bench-air-node`
- Tier 2: `bench-air-node` + `mast-lite`
- Optional hazard module: `flood-node`
- Tier 3 upgrade: `weather-pm-mast`
- Separate R&D lane: `thermal-pod`

### Minimum done definition

- every critical-path node has a build guide, wiring guide, serial contract, and operator runbook
- the integrated parcel BOM is understandable by a non-author
- the parcel node registry explains how multiple nodes belong to one parcel

### Next concrete steps

1. Treat `bench-air-node` plus `mast-lite` as the first integrated parcel kit.
2. Use `../../build-guides/parcel-kit-procurement-checklist.md` as the explicit purchase gate for Tier 1 and Tier 2 builds.
3. Use `../../build-guides/parcel-installation-checklist.md` for:
   indoor reference siting, sheltered outdoor siting, and flood-node low-point documentation.
4. Keep `weather-pm-mast` and `thermal-pod` out of the critical path until their contracts and maintenance overhead are ready.

### Stop-ship rule

Do not describe a node family as part of the first parcel kit if it still lacks a realistic bring-up and maintenance path.

## Track 3: Legal and governance packet must be ready to send

### Goal

Make it trivial to send the correct review packet without improvising which documents matter.

### Core packet for public preview reviewers

- `../../../README.md`
- `NOTICE.md`
- `../../../legal/GOVERNANCE.md`
- `../../../legal/ip.md`
- `../../../legal/public-preview-scope.md`
- `../../privacy-governance/data-ownership.md`
- `../../privacy-governance/privacy.md`
- `../../privacy-governance/claims-and-safety-language.md`
- `../../privacy-governance/permissions-matrix.md`

### Core packet for pilot or counsel preparation

Start with the preview packet, then add:

- `../../../legal/send-to-counsel-checklist.md`
- `../../../legal/pilot-and-research-data-agreement-template.md`
- `../../pilot-playbooks/pilot-consent-checklist.md`
- `../../pilot-playbooks/pilot-operator-checklist.md`
- `../../pilot-playbooks/pilot-participant-notice.md`
- `../../pilot-playbooks/pilot-incident-playbook.md`

### Minimum done definition

- the website only says what the legal packet supports
- the legal packet distinguishes preview policy from implemented product behavior
- a named owner exists for release, legal/IP, and governance/privacy review

### Next concrete steps

1. Use `reviewer-packet-index.md` as the packet selector and cover page.
2. Assign named owners on the launch-readiness checklist before any public announcement.
3. Mark which statements are already implemented in product behavior and which are still policy direction.
4. Use the public-preview-scope doc as the approval filter for every site page, screenshot, and social post.

### Stop-ship rule

Do not send or publish a packet that mixes public-preview material with held-back technical detail.

## Track 4: Website must be simple, compliant, and useful

### Goal

Publish one small page that explains the preview, points people to the right documents, and avoids overclaiming.

### Required content

- project mission
- private-by-default and shared-by-choice rule
- what the preview includes
- what the preview does not include
- claims and limitations summary
- links to governance, privacy, data ownership, and release docs

### Required language rules

- use `condition estimate`, not guarantee language
- do not imply full neighborhood visibility
- do not imply emergency authority
- do not say or imply anonymization unless separately supported

### Minimum done definition

- one page works locally without a build step
- links point to the canonical preview docs
- the page includes limitation language and preview-scope context
- the page avoids technical detail that the public-preview-scope doc treats as yellow or red

### Next concrete steps

1. Use the local static page scaffold in `site/`.
2. Keep the page self-contained and semantic HTML first.
3. Add links only to documents that are safe and intended for preview readers.
4. Review the page against the launch-readiness copy gates before publishing.

## Recommended sequence

1. Keep software checks green.
2. Lock the Tier 1 and Tier 2 parcel-kit hardware path.
3. Freeze the preview legal packet and named owners.
4. Publish the simple preview page.
5. Only after those steps, expand into more node classes or richer public-facing surfaces.

## What to do this week

- confirm the current site scaffold content against governance and claims docs
- use the reviewer packet index to freeze who gets which packet
- use the hardware procurement checklist to freeze the Tier 1 and Tier 2 order set
- decide who owns release, legal/IP, and governance/privacy sign-off
