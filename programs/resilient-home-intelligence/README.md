# Resilient Home Intelligence

Resilient Home Intelligence is a flagship program inside Open Source DIY Tech.

Read `NOTICE.md` before treating every file in this program as a public release asset.

## Mission

Create homeowner-owned environmental sensing and parcel-level situational intelligence that:
- works for individual homes
- improves with neighborhood participation
- preserves owner control of parcel-linked data, including explicit public-release choices
- uses external public data only inside the platform
- stays modular and open

The program is now in its v0.1 open-release period. Approved software,
hardware, documentation, governance materials, and intentionally public datasets may be
released under asset-specific terms, while some materials remain outside release for
privacy, provenance, security, or licensing reasons.

## Version framing

Keep these labels separate:

- `v0.1` = the current public release label
- `current v1`, `v1.5`, `v2`, `v2.5`, `v3`, `v4` = capability stages
- `deployment maturity v0.1`, `v1.0`, `v1.5`, `v2.0` = hardware and operations maturity

For the tracked architecture and roadmap docs inside this repo, start with:

- `docs/system-overview/README.md`
- `docs/system-overview/phase-roadmap.md`
- `docs/system-overview/architecture-gaps-by-stage.md`
- `docs/system-overview/deployment-maturity-ladder.md`

## Program structure

- `hardware/` — physical sensor nodes and installation systems
- `software/` — ingest, parcel platform, inference, and maps
- `docs/` — system docs, guides, schemas, calibration, and pilot playbooks
- `legal/` — licensing, defensive publication, governance, and contribution policy
- `media/` — diagrams, renders, and images

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

- `NOTICE.md`
- `legal/ip.md`
- `legal/dataset-release-policy.md`
- `legal/GOVERNANCE.md`
- `docs/privacy-governance/data-ownership.md`
- `docs/privacy-governance/privacy.md`
- `docs/release/v0.1/NOTICE.md`
