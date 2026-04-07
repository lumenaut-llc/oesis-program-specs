# Reviewer Packet Index

## Status

Internal handoff index for the April 14, 2026 preview and first controlled review packets.

Do not treat this file itself as a public landing page.

## Purpose

Use one source of truth for what to send to whom so the project does not accidentally mix:

- public preview materials
- controlled implementation review materials
- counsel and filing materials
- pilot and field-operation materials

## Packet selection rule

Choose the narrowest packet that fits the audience.

- Public readers and general launch reviewers get the public preview packet only.
- Trusted implementation reviewers get the controlled review packet only if release owners agree the audience needs it.
- Counsel gets the counsel packet.
- Pilot operators or research partners get the pilot packet.

If a document falls outside the packet lane below, do not attach it by habit.

## Packet 1: Public preview packet

Use for:

- the public website
- social posts
- general reviewers
- anyone who only needs the preview-safe governance and mission materials

Send in this order:

1. `../../../README.md`
2. `NOTICE.md`
3. `../../../legal/public-preview-scope.md`
4. `../../privacy-governance/data-ownership.md`
5. `../../privacy-governance/privacy.md`
6. `../../privacy-governance/claims-and-safety-language.md`
7. `../../../legal/GOVERNANCE.md`
8. `../../../legal/ip.md`
9. `../../../legal/contribution-policy/README.md`

Rules:

- Safe for the public site and preview links.
- Keep the packet non-enabling.
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
3. `../../../technical-architecture/v0.1/README.md`
4. `../../../technical-architecture/v0.1/reference-stack.md`
5. `../../system-overview/integrated-parcel-system-spec.md`
6. `../../data-model/node-registry-schema.md`
7. `../../../software/operator-quickstart.md`
8. `../../build-guides/integrated-parcel-kit-bom.md`
9. `../../build-guides/parcel-kit-procurement-checklist.md`
10. `../../build-guides/parcel-installation-checklist.md`
11. `../../../../../meta/backlog.md`

Rules:

- Treat this lane as controlled review while the filing decision and preview holdback rules remain active.
- Release-owner review is required before sending outside the core team.
- Do not link this packet from the public preview page.

## Packet 3: Counsel and filing packet

Use for:

- patent counsel
- filing review
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
- Keep this lane narrow to parcel-state generation and the current filing candidate.
- Do not mix with general reviewer packets or public preview links.

## Packet 4: Pilot and field packet

Use for:

- pilot operators
- research partners
- participant-material review

Start with Packet 1, then add:

1. `../../../legal/pilot-and-research-data-agreement-template.md`
2. `../../pilot-playbooks/pilot-participant-notice.md`
3. `../../pilot-playbooks/pilot-consent-checklist.md`
4. `../../pilot-playbooks/pilot-operator-checklist.md`
5. `../../pilot-playbooks/pilot-incident-playbook.md`
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
- integrated technical build details that exceed the approved preview scope

## Handoff checklist

Before sending any packet, confirm:

- the packet matches the audience
- the packet stays within `../../../legal/public-preview-scope.md`
- no real homeowner-contributed parcel-linked data is attached
- claims and safety language match `../../privacy-governance/claims-and-safety-language.md`
- the packet does not imply implemented product behavior that the software or hardware still cannot support

## Website rule

The public preview site app in `sites/public-preview/` should only link
materials from Packet 1 and should continue to use the release-owned
publication controls under `docs/release/2026-04-14/site/`.
