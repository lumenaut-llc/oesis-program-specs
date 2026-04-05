# V1 Public Website Standard

## Purpose

Turn the April 14, 2026 public-facing site into something that reads like a serious
open project rather than a vague prototype landing page.

This file is the working website and repo-display standard for v1. It should be read
together with:

- `README.md`
- `NOTICE.md`
- `landing-page-copy.md`
- `launch-checklist.md`
- `launch-readiness-checklist.md`
- `implementation-status-matrix.md`
- `../../../legal/ip.md`
- `../../../legal/dataset-release-policy.md`
- `../../privacy-governance/data-ownership.md`
- `../../privacy-governance/privacy.md`

## Two-minute test

If someone lands on the repo or public site, they should be able to answer within two
minutes:

1. what this project is
2. what parts are actually open
3. what works today
4. how to build one thing
5. how to contribute
6. what not to trust yet

If those six answers are not obvious, the site is still under-explaining.

## Core public promise

For v1, the site should present the project as:

- parcel-first homeowner environmental sensing
- open release with clear asset-class licensing
- private by default and shared by choice
- prototype / experimental rather than safety-authoritative
- serious enough to inspect, build, and critique

The site should not read like:

- a vague future vision
- a patent-preservation teaser
- a blanket open-data release
- a safety product claiming more certainty than the implementation supports

## Homepage structure

The v1 homepage should follow this order:

1. project name
2. one-sentence purpose
3. current v1 status
4. why parcel-first
5. what v1 includes
6. what v1 does not include
7. quickstart
8. hardware modules
9. software modules
10. governance / data ownership
11. license matrix
12. contributing
13. safety / limitation notice
14. roadmap

## What the homepage should say for this project

The front page should communicate, near the top:

- what the project is
- what hazards are currently in scope
- what hardware and software lanes exist now
- what is measured versus inferred
- what is still experimental

Recommended v1 framing:

- mission: parcel-first homeowner environmental sensing and parcel awareness
- current hazard scope: smoke, pluvial flooding / runoff, heat
- current maturity: prototype / experimental / not a substitute for official alerts

## Project-specific maturity rules

The site should not present every hardware or software lane as equally mature.

Use the current implementation matrix as the source of truth:

### Hardware maturity labels

- `bench-air-node` — buildable now
- `mast-lite` — early outdoor prototype
- `flood-node` — experimental field prototype
- `weather-pm-mast` — second-wave / partial
- `thermal-pod` — exploratory / R&D

### Software maturity labels

- ingest API — implemented in the current reference path
- inference API — implemented in the current reference path
- parcel-platform API — implemented in the current reference path
- rights / export / retention admin utilities — partial
- shared-map aggregate API — partial
- public shared map — docs-only / not currently supported

## Measured vs inferred vs planned

The public site must separate:

- measured now
- inferred now
- planned next
- speculative long-term

For this repo, that means:

### Safe to say as current reference support

- measured now: the current `bench-air-node` lineage and checked-in public-context examples
- inferred now: parcel-state outputs from the current reference path
- evidence modes: provenance- and freshness-aware parcel-state explanation in the current reference flow

### Not safe to present as current shipped support

- flood low-point observation support as fully implemented
- weather/PM outdoor observation support as fully implemented
- thermal scene observation support as implemented product behavior
- public parcel-resolution shared map support
- autonomous controls or operational decisioning

If the site wants to mention those areas, label them as:

- planned
- partial
- exploratory

## What is open

The public site should show a license matrix near the top.

Use the current asset-class split:

- platform software — see `../../../../../LICENSES.md`
- node firmware — see `../../../../../LICENSES.md`
- hardware design files — see `../../../../../LICENSES.md`
- documentation — see `../../../../../LICENSES.md`
- datasets / sample data — see `../../../../../LICENSES.md`
- trademarks / branding — reserved unless expressly granted

The site should also make clear:

- the project-controlled v1 dataset may be intentionally public
- future participant parcel-linked data is not public by default

## Hardware page standard

Each hardware module page should show:

- what it is
- why it exists
- current maturity
- BOM
- wiring or connection guidance
- source design files in editable form where available
- enclosure / mounting notes
- firmware link
- calibration or bring-up steps
- known failure modes
- photos
- output packet example

Each hardware module card on the site should also show:

- maturity
- cost range
- build difficulty
- outputs
- standalone value
- network value

## Software page standard

The public software presentation should show:

- architecture diagram
- current software modules
- data model
- API endpoints or entry points
- sample packets
- parcel-state outputs
- explanation / provenance examples
- separation of private, shared, and public data
- install / run instructions

Each software module card should show:

- current state
- inputs
- outputs
- dependencies
- maturity

## Governance and privacy page standard

This should be first-class and linked from the homepage.

It should clearly show:

- homeowners own raw data
- private by default
- sharing is opt-in
- what can be shared
- what precision can be shared
- how provenance is shown
- export / delete expectations
- what the platform may do
- what the platform will not do

## Community health expectation

The public repo experience should visibly include:

- `README.md`
- `LICENSES.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `CHANGELOG.md`
- `ROADMAP.md`
- `GOVERNANCE.md`
- hardware subsystem docs
- data ownership docs

Current repo note:

- `README.md`, `LICENSES.md`, `CONTRIBUTING.md`, and `program-level governance/docs` exist
- `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CHANGELOG.md`, and `ROADMAP.md` should be added or explicitly confirmed if the project wants to meet this v1 standard cleanly

## What not to imply

Do not present:

- prototype outputs as authoritative safety truth
- neighbor inference as certainty
- thermal outputs as high-confidence scene intelligence
- flood sensing as universal flood prediction
- automation concepts as currently shipped capability
- one public dataset as proof that all parcel-linked data is open

## Current website gaps to close

To fully meet this standard, the public site should still add or improve:

- a dedicated hardware modules section with maturity labels
- a dedicated software modules section with current-state labels
- a visible quickstart block for builders and reviewers
- a visible roadmap / what comes next section
- a public sample parcel card showing status, confidence, evidence mode, and reasons
- stronger repo-community-health visibility if the missing standard files are not yet present

## Astro implementation direction

The Astro site should use this file as a content standard for future work.

Practical follow-up components:

- `VersionTimeline`
- `HardwareModuleCard`
- `SoftwareModuleCard`
- `ParcelCardExample`
- `LicenseMatrix`
- `RoadmapSection`

The future animated timeline should only be added after the content distinction is
clear between:

- current
- partial
- planned
- exploratory
