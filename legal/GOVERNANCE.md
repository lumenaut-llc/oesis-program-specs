# Governance

## Purpose

Define the stewardship, decision-making, and change-control model for the Open
Environmental Sensing and Inference System (`OESIS`) project during the v0.1
open-release period and the transition to broader open release.

This file is a project governance draft, not legal advice.

## Mission

Open Environmental Sensing and Inference System exists to build a modular,
parcel operator-centered environmental sensing and parcel-awareness system that:

- works for a single home
- improves with neighborhood participation
- keeps raw parcel-linked data private by default
- supports opt-in sharing rather than forced centralization
- stays technically honest about evidence, uncertainty, and limitations
- is released in a way that is difficult to enclosure-capture

## Governance principles

- parcel first
- private by default
- shared by choice
- explicit provenance and uncertainty
- openness with clear legal boundaries
- no quiet repurposing of private data
- no overclaiming safety, certainty, or emergency authority

## Current governance phase

The project is in an active open-release phase.

Current priorities are:

- keep release materials aligned with the current commons-protective open posture
- keep intentionally public v1 dataset decisions clearly separated from future participant data
- preserve a coherent open-release structure across software, hardware, docs, and datasets
- keep data-governance claims aligned with actual controls

## Stewardship roles

Until a broader community governance model is adopted, the project should use named stewardship roles.

### Release owner

Responsible for:

- release go / no-go decisions
- publication scope control
- coordination across legal, docs, and engineering workstreams

### Legal / IP owner

Responsible for:

- IP and release position
- non-release list and release-scope enforcement
- attorney escalation where licensing, patent, or trademark review is still needed

### Governance / privacy owner

Responsible for:

- data ownership rules
- privacy posture
- permissions matrix and lifecycle-control policy
- review of new sharing uses

### Technical maintainers

Responsible for:

- correctness of software, hardware, and firmware docs
- maintaining provenance and uncertainty support in technical artifacts
- escalating changes that affect claims, safety, or privacy posture

## Decision classes

### Class 1. Ordinary technical changes

Examples:

- implementation cleanup
- documentation edits that do not change policy
- synthetic examples
- non-sensitive architecture clarifications

Approval rule:

- normal maintainer review

### Class 2. Governance-sensitive changes

Examples:

- new data uses
- new sharing modes
- changes to export, deletion, or revocation behavior
- changes to how provenance or confidence is displayed
- claims-sensitive UI copy

Approval rule:

- technical maintainer review plus governance / privacy owner review

### Class 3. Release-sensitive changes

Examples:

- anything touching non-release materials
- changes to public release scope
- changes to public licensing statements
- changes to IP or patent-related wording
- release of new datasets or public map outputs

Approval rule:

- release owner plus legal / IP owner review
- attorney escalation where required

## Decision class by repository scope

The classes above describe the **type** of change. This table maps each repo (or repo subtree) to its **default class**, so contributors know which approval pattern applies before opening a PR.

| Repo / subtree | Default class | Escalation triggers |
|---|---|---|
| `oesis-contracts/v*/schemas/` | Class 2 | Class 3 if change affects governance objects (consent, sharing, retention, rights-request, operator-access-event) |
| `oesis-contracts/v*/examples/` | Class 1 | Class 2 if example demonstrates new sharing/consent flow |
| `oesis-contracts/bundles/` | Class 2 | Bundle is a downstream-consumer surface |
| `oesis-runtime/oesis/ingest/` | Class 1 | Class 2 if affecting admissibility checks or trust-scoring |
| `oesis-runtime/oesis/inference/` | Class 1 | Class 2 if changing hazard math, calibration, or confidence-degradation rules |
| `oesis-runtime/oesis/parcel_platform/` (governance utilities — `process_rights_requests.py`, `run_retention_cleanup.py`, `export_parcel_bundle.py`) | Class 2 | — |
| `oesis-runtime/oesis/shared_map/` | Class 2 | Class 3 if changing public-map suppression, k-anonymity, or aggregation thresholds |
| `oesis-program-specs/architecture/` | Class 1 | Class 2 if changing public-claim posture (claims-sensitive doctrine) |
| `oesis-program-specs/legal/` | Class 3 | Always |
| `oesis-program-specs/release/` | Class 3 | Always |
| `oesis-program-specs/program/` (operating packet, execution plan) | Class 2 | Class 3 if changing public release-scope or holdback list |
| `oesis-program-specs/meta/` (ADRs, milestones, proposals, plan-of-approach) | Class 1 | Class 2 if ADR changes governance posture; Class 3 if ADR changes release boundary |
| `oesis-hardware/v*/parcel-kit/` | Class 2 | Field-hardening, BOM, install posture all affect deployment trust |
| `oesis-hardware/v*/<node-family>/` (build guide, firmware, calibration) | Class 1 | Class 2 if changing calibration claims or trust posture |
| `oesis-hardware/v*/calibration/` | Class 2 | Cross-cutting calibration policy |
| `oesis-public-site/content/` | Class 3 | Public-facing copy is release-sensitive by definition |
| `oesis-public-site/src/` (frontend code, no content) | Class 1 | Class 3 if changing publication boundary or content-bundle handling |
| `oesis-builds` (non-git vault) | Class 1 | Vault stewardship rules apply (see `oesis-builds/CLAUDE.md`); Class 2 if affecting calibration session logs |
| `oesis-wiki` (non-git vault) | Class 1 | Vault stewardship rules apply (see `oesis-wiki/CLAUDE.md`); wiki content updates go through wiki agent commands |

### Multi-class escalation rule

A change that touches files in multiple class buckets defaults to the **highest applicable class**. Example: a PR that updates an `oesis-runtime/oesis/inference/` admissibility check (Class 2) AND `oesis-program-specs/release/v0.5/` notes (Class 3) requires Class 3 approval (release owner + legal/IP owner) for the entire PR.

### Cross-references

Each repo's `CONTRIBUTING.md` should link to this table when explaining review expectations. Update those alongside any change to this table.

### Out of scope here

- Named approver lists (who currently fills release-owner, legal/IP-owner, governance/privacy-owner roles) — see role-assignment ticket
- Tooling enforcement (CODEOWNERS files, branch-protection rules wiring this table into GitHub) — separate ticket if desired

## Hard governance boundaries

The project should not:

- switch private-by-default behavior to opt-out sharing without explicit governance approval
- publish future participant exact parcel-linked parcel-linked data in public materials without explicit approval
- claim anonymization without a defensible standard
- market parcel-state outputs as guaranteed safety guidance
- publish non-release technical details without the required release check

## Contributor governance expectations

Contributors should:

- respect the current release-scope and non-release rules
- use the applicable policy docs when changing data, privacy, or claims behavior
- use the applicable `architecture/` version when changing system boundaries, architecture posture, or subsystem alignment
- avoid introducing silent new data uses
- avoid weakening provenance, freshness, uncertainty, export, deletion, or revocation posture without explicit review
- use `../release/v1.0/contributor-and-review-guide.md` as the short v1 decision guide for public-facing contribution and review work

See `contribution-policy/README.md`.

## Change control for core governance docs

The following documents should be treated as core governance artifacts:

- `ip.md`
- `dataset-release-policy.md`
- `GOVERNANCE.md`
- `../legal/privacy/data-ownership.md`
- `../legal/privacy/privacy.md`
- `../legal/privacy/permissions-matrix.md`
- `../legal/privacy/retention-export-deletion-revocation.md`
- `../legal/privacy/claims-and-safety-language.md`

Changes to these docs should include:

- the reason for change
- the affected product or release surface
- whether the change affects public claims, privacy controls, or release scope

## Release-scope rule

During the current release period:

- public materials must stay within `public-preview-scope.md`
- non-release materials remain governed by `holdback-list.md`
- intentionally public datasets must be explicitly designated and licensed
- public messaging should point users to canonical docs rather than improvise legal or privacy claims on social media

## Future governance evolution

Later versions may add:

- community charter
- maintainer election or appointment rules
- formal ADR process for governance decisions
- public map publication policy
- pilot and research review committee rules

## Attorney review triggers

Escalate before:

- changing the release posture in a way that affects patent, licensing, or trademark posture
- promising a patent non-assert or trademark permission
- adopting final public terms for future participant-contributed real parcel-linked data
- launching public pilots with real participant data
