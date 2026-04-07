# Open Source DIY Tech — Open Environmental Sensing and Inference System

This repository is the program-definition and release home for the Open
Environmental Sensing and Inference System program inside Open Source DIY Tech.

Open Environmental Sensing and Inference System (`OESIS`) is the canonical
system name. `Resilient Home Intelligence` (`RHI`) remains a legacy
compatibility name during the transition.

## Purpose

Open Environmental Sensing and Inference System is a modular, homeowner-owned
environmental sensing and parcel-awareness initiative. It combines:

- physical sensor builds
- parcel-level software
- neighborhood inference
- privacy/governance rules
- documentation and pilot playbooks

The system is designed so each parcel can receive parcel-level condition estimates even with partial sensor adoption. More participating nodes can improve precision and confidence, but they do not unlock basic functionality.

This repository now serves as the canonical home for:

- architecture and system definitions
- schemas, examples, and release packet materials
- governance, privacy, and publication controls
- build and publication support for split-repo workflows

The runnable Python reference services and the public preview site are being
split into standalone sibling repositories:

- `oesis-runtime`
- `oesis-public-site`

During the migration, `oesis/` and `sites/public-preview/` remain as staged
compatibility mirrors so split tooling and verification can complete without
interrupting the current repo workflow.

## Core principles

- Parcel first
- Private by default
- Shared by choice
- Useful as a standalone build
- More powerful as a network
- Explicit uncertainty
- Open and well documented

## Repository map

- `programs/open-environmental-sensing-and-inference-system/` — program docs, architecture, release, legal, and hardware/operator materials
- `oesis_build/` — build and publication support for contracts, release, and split-repo workflows
- `shared/` — shared standards, templates, and glossary
- `meta/` — planning, milestones, operating notes, and repo-split execution docs
- `artifacts/` — generated split artifacts such as contracts, public content, and runtime evidence bundles
- `scripts/repo_split.py` — split automation for syncing runtime assets, building bundles, and extracting sibling repos
- `oesis/` — staged compatibility copy of the runtime while `oesis-runtime` is being cut over
- `sites/public-preview/` — staged compatibility copy of the public site while `oesis-public-site` is being cut over

## Split workflow

Use these commands while the split is in progress:

- `make repo-split-sync-runtime-assets`
- `make repo-split-build-contracts-bundle`
- `make repo-split-build-public-content-bundle`
- `make repo-split-build-runtime-evidence-bundle`
- `make repo-split-extract-site`
- `make repo-split-extract-runtime`

The canonical execution plan lives in `meta/repo-split-plan.md`.

## Start here

1. Read `NOTICE.md`
2. Read `programs/open-environmental-sensing-and-inference-system/README.md`
3. Read `programs/open-environmental-sensing-and-inference-system/docs/release/2026-04-14/open-source-v1-summary.md`
4. Read `programs/open-environmental-sensing-and-inference-system/technical-architecture/README.md`
5. Read `meta/repo-split-plan.md` if you are working on runtime/site extraction or bundle boundaries
6. Use `shared/templates/` when starting a new subsystem or document
