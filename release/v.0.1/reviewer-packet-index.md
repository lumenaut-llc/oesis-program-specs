# Reviewer Packet Index

## Status

Internal handoff index for the v0.1 open release and related controlled review
packets.

Do not treat this file itself as a public landing page.

## Purpose

Use one source of truth for what to send to whom so the project does not accidentally mix:

- public release materials
- controlled implementation review materials
- counsel and filing materials
- pilot and field-operation materials

## Packet selection rule

Choose the narrowest packet that fits the audience.

- Public readers and general launch reviewers get the public release packet only.
- Trusted implementation reviewers get the controlled review packet only if release owners agree the audience needs it.
- Counsel gets the counsel packet.
- Pilot operators or research partners get the pilot packet.

If a document falls outside the packet lane below, do not attach it by habit.

## Packet 1: Public release packet

Use for:

- the public website
- social posts
- general reviewers
- anyone who only needs the public governance and mission materials

Send in this order:

1. `../../../README.md`
2. `NOTICE.md`
3. `../../../legal/public-preview-scope.md`
4. `../../../legal/dataset-release-policy.md`
5. `../../legal/privacy/data-ownership.md`
6. `../../legal/privacy/privacy.md`
7. `../../legal/privacy/claims-and-safety-language.md`
8. `../../../legal/GOVERNANCE.md`
9. `../../../legal/ip.md`
10. `../../../legal/contribution-policy/README.md`

Rules:

- Safe for the public site and release links.
- Keep the packet within the approved public release boundary.
- Do not add build guides, registry details, BOM details, pilot ops docs, or filing materials.

## Packet 2: Controlled implementation review packet

Use for:

- trusted technical collaborators
- internal implementation review
- grant, steward, or advisor review where the high-level packet is not enough

This is not a default public packet.

Start with Packet 1, then add:

1. `preview-execution-plan.md`
2. `implementation-status-matrix.md`
3. `../../../architecture/current/README.md`
4. `../../../architecture/current/reference-stack.md`
5. `../../architecture/system/integrated-parcel-system-spec.md`
6. `../../contracts/node-registry-schema.md`
7. `../../../software/operator-quickstart.md`
8. `../../hardware/parcel-kit/integrated-parcel-kit-bom.md`
9. `../../hardware/parcel-kit/parcel-kit-procurement-checklist.md`
10. `../../hardware/parcel-kit/parcel-installation-checklist.md`
11. `../../../../../meta/backlog.md`

Rules:

- Treat this lane as controlled review while non-release controls remain active.
- Release-owner review is required before sending outside the core team.
- Do not link this packet from the public release page.

## Packet 3: Counsel and archival patent packet

Use for:

- patent counsel, if later needed
- archival filing review
- narrow invention-scope sanity checks

Start with Packet 1 only if counsel needs preview context, then add:

1. `../../../legal/send-to-counsel-checklist.md`
2. `../../../legal/provisional-one-page-summary-parcel-state.md`
3. `../../../legal/provisional-packet-draft-parcel-state.md`
4. `../../../legal/provisional-figure-captions-parcel-state.md`
5. `../../../legal/provisional-figures-parcel-state.md`
6. `../../../legal/provisional-inventor-questionnaire-prefill.md`
7. `../../../legal/holdback-list.md`
8. `../../../legal/provisional-counsel-cover-email.md`

Rules:

- Internal or counsel only until release owners decide otherwise.
- Keep this lane narrow to parcel-state generation and the historical filing candidate.
- Do not mix with general reviewer packets or public release links.

## Packet 4: Pilot and field packet

Use for:

- pilot operators
- research partners
- participant-material review

Start with Packet 1, then add:

1. `../../../legal/pilot-and-research-data-agreement-template.md`
2. `../../operations/pilots/pilot-participant-notice.md`
3. `../../operations/pilots/pilot-consent-checklist.md`
4. `../../operations/pilots/pilot-operator-checklist.md`
5. `../../operations/pilots/pilot-incident-playbook.md`
6. `../../../legal/internal-operator-access-policy.md`

Rules:

- Use this packet only when the audience needs pilot or research operations detail.
- Pilot participation should not quietly imply broader data-sharing rights.
- Keep participant-facing and operator-facing documents clearly separated when sending.

## Do not mix these materials

Do not place the following into the public packet or public website:

- filing drafts or counsel email templates
- holdback lists
- pilot operations or internal operator-access documents
- integrated technical build details that exceed the approved release scope

## Handoff checklist

Before sending any packet, confirm:

- the packet matches the audience
- the packet stays within `../../../legal/public-preview-scope.md`
- no future participant-contributed parcel-linked data is attached
- claims and safety language match `../../legal/privacy/claims-and-safety-language.md`
- the packet does not imply implemented product behavior that the software or hardware still cannot support

## Website rule

The public preview site app in the sibling workspace `../../oesis-public-site` should
only link materials from Packet 1. Publication allowlists and anchors live in that
repo (`src/data/publicationPolicy.ts`, backed by `src/generated/publicContentBundle.ts`),
generated from program-specs `../../artifacts/public-content-bundle/public-content-bundle.json`,
and remain bounded by `../../../legal/public-preview-scope.md`.
