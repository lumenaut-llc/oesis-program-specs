# Governance

## Purpose

Define the stewardship, decision-making, and change-control model for the Open
Environmental Sensing and Inference System project during the April 14, 2026
preview phase and the transition to broader open release.

This file is a project governance draft, not legal advice.

## Mission

Open Environmental Sensing and Inference System exists to build a modular,
homeowner-centered environmental sensing and parcel-awareness system that:

- works for a single home
- improves with neighborhood participation
- keeps raw homeowner data private by default
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

The project is in a preview-to-open-release transition phase.

Current priorities are:

- maintain safe release sequencing during Path B
- keep preview publication non-enabling where required
- preserve a coherent open-release structure across software, hardware, docs, and datasets
- keep data-governance claims aligned with actual controls

## Stewardship roles

Until a broader community governance model is adopted, the project should use named stewardship roles.

### Release owner

Responsible for:

- preview and release go / no-go decisions
- publication scope control
- coordination across legal, docs, and engineering workstreams

### Legal / IP owner

Responsible for:

- IP and release position
- holdback list and preview-scope enforcement
- attorney escalation and filing coordination

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

- anything touching held-back materials
- changes to public preview scope
- changes to public licensing statements
- changes to IP or patent-related wording
- release of new datasets or public map outputs

Approval rule:

- release owner plus legal / IP owner review
- attorney escalation where required

## Hard governance boundaries

The project should not:

- switch private-by-default behavior to opt-out sharing without explicit governance approval
- publish exact parcel-linked homeowner data in public materials
- claim anonymization without a defensible standard
- market parcel-state outputs as guaranteed safety guidance
- publish held-back technical details during preview without the required release check

## Contributor governance expectations

Contributors should:

- respect the current preview holdback rules
- use the applicable policy docs when changing data, privacy, or claims behavior
- use the applicable `technical-architecture/` version when changing system boundaries, architecture posture, or subsystem alignment
- avoid introducing silent new data uses
- avoid weakening provenance, freshness, uncertainty, export, deletion, or revocation posture without explicit review
- use `../docs/release/2026-04-14/contributor-and-review-guide.md` as the short v1 decision guide for public-facing contribution and review work

See `contribution-policy/README.md`.

## Change control for core governance docs

The following documents should be treated as core governance artifacts:

- `ip.md`
- `GOVERNANCE.md`
- `../docs/privacy-governance/data-ownership.md`
- `../docs/privacy-governance/privacy.md`
- `../docs/privacy-governance/permissions-matrix.md`
- `../docs/privacy-governance/retention-export-deletion-revocation.md`
- `../docs/privacy-governance/claims-and-safety-language.md`

Changes to these docs should include:

- the reason for change
- the affected product or release surface
- whether the change affects public claims, privacy controls, or release scope

## Path B preview rule

During the preview period:

- public materials must stay within `public-preview-scope.md`
- held-back materials remain governed by `holdback-list.md`
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

- changing the release sequencing in a way that affects patent posture
- promising a patent non-assert or trademark permission
- adopting final public terms for real homeowner data
- launching public pilots with real participant data
