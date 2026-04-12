# ADR 0005: Open Code and Hardware, but Not Open Real Parcel-Contributed Data

- Status: Superseded in part by ADR 0006
- Date: 2026-03-30
- Owners: program maintainers
- Related workstreams: legal, licensing, dataset release, contribution policy

## Context

The project aims to be open-source and commons-oriented, but real participant-contributed parcel-linked sensing data carries privacy, singling-out, and downstream misuse risk. A blanket open-data posture would conflict with the project's private-by-default and opt-in-sharing commitments.

The repo needs an explicit decision separating openness of code and hardware from openness of real-world household data.

## Decision

The project will keep software, hardware designs, documentation, schemas, and synthetic examples open, while not treating real participant-contributed parcel-linked datasets as open by default.

Working posture:
- software source and service components: open license
- hardware design files: open hardware license
- documentation, governance text, and schemas: open documentation license
- synthetic examples and fixtures: open dataset terms
- real participant-contributed parcel-linked data: governed separately and not published under a blanket repository-wide open-data license

## Consequences

Positive:
- preserves openness where it supports trust, auditability, and ecosystem growth
- avoids overcommitting real household data to irreversible public reuse
- aligns licensing with the privacy model

Costs:
- some open-data advocates may view this as insufficiently open
- additional governance is required for any future pilot or research dataset release

## Alternatives considered

- blanket open-data license for shared database outputs
  Rejected because it conflicts with revocation, privacy, and household trust expectations.
- fully closed product stack
  Rejected because it would weaken auditability and commons-oriented collaboration goals.

## Follow-up work

- maintain a dataset release policy with explicit do-not-release categories
- require separate review for any research or pilot dataset publication
- add source notices and release metadata for redistributed public reference datasets
