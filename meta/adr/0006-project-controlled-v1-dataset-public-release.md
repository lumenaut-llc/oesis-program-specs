# ADR 0006: Project-Controlled V1 Dataset Public Release

- Status: Accepted
- Date: 2026-04-02
- Owners: program maintainers
- Related workstreams: legal, licensing, dataset release, public release

## Context

ADR 0005 established the right default boundary for the project: open code, open
hardware, and open documentation do not automatically require a blanket open-data
release of real parcel-linked household data.

That rule still makes sense for future participant-contributed parcel-linked data.
However, the current v1 dataset is project-controlled and is being intentionally
considered as part of the public April 14, 2026 release.

The repo needs an explicit decision that preserves the private-by-default posture for
future participants while allowing the project-controlled v1 dataset to be published
openly under clear dataset-specific terms.

## Decision

The project may publish the project-controlled v1 dataset openly when it is:

- intentionally designated as a public release artifact
- released under explicit open-data terms
- accompanied by provenance, scope, and caveat notes appropriate to the dataset

The current recommended public dataset license for that v1 release is:

- `CDLA-Sharing-1.0`

Future participant-contributed parcel-linked data remains private by default and is
not made public merely because the project-controlled v1 dataset is public.

## Consequences

Positive:
- allows the project to publish the v1 dataset clearly and intentionally
- preserves the project's private-by-default promise for later participants
- reduces ambiguity about whether one public dataset changes the policy for all future data

Costs:
- requires careful designation of which dataset artifacts are actually part of the public release
- requires provenance, scope, and licensing notes to travel with the released dataset
- may disappoint people who expected either a blanket open-data posture or a blanket no-open-data posture

## Alternatives considered

- keep all parcel-linked datasets non-public, including the project-controlled v1 dataset
  Rejected because it conflicts with the current decision to make the v1 release genuinely public.
- make all future parcel-linked datasets open by default
  Rejected because it would overrule private-by-default expectations for future participants.

## Follow-up work

- keep `dataset-release-policy.md` aligned with this carve-out
- keep public release notices explicit that one public v1 dataset does not open all future parcel-linked data
- include the chosen dataset license, provenance notes, and scope caveats with the v1 public release package
