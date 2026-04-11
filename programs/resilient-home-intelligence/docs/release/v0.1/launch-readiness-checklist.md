# Launch Readiness Checklist

## Purpose

Turn the repo's governance, legal, privacy, and claims rules into a practical release
gate for the current public release, pilot launch, and later product deployment.

## How to use

- assign an owner for each item
- mark status as `not started`, `in progress`, or `done`
- do not treat a document as complete unless the corresponding product or operational surface also exists where required
- use `implementation-status-matrix.md` to separate evidence-backed implementation from docs-only or planned surfaces

## First-pass ownership

Until broader stewardship roles are assigned, Liam is acting as:

- release owner
- legal / IP owner
- governance / privacy owner
- technical maintainer

## Latest dry-run evidence

- Controlled review packet dry run on April 1, 2026 resolved all `18` files listed in the current Packet 2 path from `reviewer-packet-index.md`.
- Operator dry run on April 1, 2026 succeeded for `python3 -m rhi.parcel_platform.reference_pipeline`, `python3 -m rhi.ingest.ingest_packet programs/resilient-home-intelligence/docs/data-model/examples/node-observation.example.json --parcel-id parcel_demo_001`, and release-site HTTP checks returning `200 OK` for `http://127.0.0.1:8000/`.

## Governance and legal gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Data classes are fixed and referenced by product/API work | Liam (technical) | docs, schemas, APIs | in progress | `make rhi-validate` passes and the reference services use the checked-in example contracts, but broader product/API coverage is still incomplete. |
| Sharing modes are defined and aligned with UI and policy docs | Liam (governance/privacy) | parcel settings, docs | not started | Sharing schemas and policy docs exist, but there is no full parcel-settings UI yet. |
| Claims and safety-language standard reviewed against public copy | Liam (release) | site, app, release copy | in progress | The release site and notice were written against the claims doc, but final release-owner review is still pending. |
| Licensing split reviewed for software, hardware, docs, and datasets | Liam (legal/IP) | repo root, legal docs | not started | Licensing materials exist, but this review gate is not yet closed. |
| Dataset release policy applied to all public artifacts | Liam (legal/IP) | repo, releases, pilots | not started | Policy exists, but artifact-by-artifact application is still pending. |
| Trademark and compatibility language reviewed | Liam (release) | release copy, docs, branding | not started | No completed review evidence yet. |

## Product and UX gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Parcel-state labels use condition-estimate language | Liam (technical) | parcel UI, docs, notifications | in progress | Preview docs use condition-estimate language, but fuller parcel UI and notification surfaces remain reference-only. |
| Sharing settings copy matches actual data use | Liam (governance/privacy) | parcel settings UI | in progress | The reference parcel view exposes `sharing_summary`, but a true parcel-settings UI is not implemented yet. |
| Rights request entry points exist for export and deletion | Liam (technical) | parcel settings UI, support flow | in progress | Reference admin export and delete flows exist, but end-user entry points do not. |
| Provenance and freshness are visible in parcel views | Liam (technical) | parcel UI | done | Verified locally on April 1, 2026 from `python3 -m rhi.parcel_platform.reference_pipeline`; `parcel_view` includes `freshness` and `provenance_summary`. |
| Shared-map disclosures explain aggregation and partial coverage | Liam (technical) | shared map UI | in progress | The shared-map API exposes a coverage notice, but the broader shared-map UI is still incomplete. |
| Public map red lines are enforced in product design | Liam (release) | shared map UI, APIs | in progress | The shared-map reference API reports `public_map_supported: false`, but broader product review is still pending. |

## Data and API gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Sharing settings object implemented from schema | Liam (technical) | backend, parcel API | in progress | The reference parcel-view path validates sharing settings and emits a sharing summary, but the broader backend surface is incomplete. |
| Consent record object implemented from schema | Liam (technical) | backend, audit trail | not started | Example and schema exist, but there is no operational consent backend flow yet. |
| Rights request object implemented from schema | Liam (technical) | backend, support/admin flow | in progress | Reference rights-request stores and admin processing routes exist in the parcel-platform tree. |
| Parcel API includes visible data-class and sharing summaries where intended | Liam (technical) | parcel API | in progress | Local reference parcel views expose `data_classes_visible` and `sharing_summary`, but the full API/UI surface is still narrow. |
| Shared-map API suppresses exact parcel identifiers and raw refs | Liam (technical) | shared map API | in progress | The shared-map path is aggregate-first and the public map is disabled, but broader review is still pending. |
| Revocation behavior stops future sharing promptly | Liam (governance/privacy) | backend jobs, map pipeline | not started | Revocation policy is documented, but prompt stop behavior is not yet implemented and verified. |

## Security and operator gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Internal operator access rules are documented and distributed | Liam (governance/privacy) | ops, support, engineering | not started | Internal access policy is documented, but there is no evidence of distribution or operator rollout yet. |
| Parcel-linked access is logged | Liam (technical) | admin tools, backend | in progress | Reference admin flows append operator access events, but broader parcel-linked access coverage is not yet proven. |
| Informal side-copy handling is prohibited operationally | Liam (governance/privacy) | ops practice | not started | Policy direction exists, but there is no operational rollout evidence yet. |
| Incident path exists for privacy, visibility, and output issues | Liam (release) | pilot ops, support | not started | Incident playbook docs exist, but no named active ops path is assigned yet. |
| Production-like demos avoid real household data | Liam (release) | demos, previews | done | Verified locally on April 1, 2026: the reference pipeline and smoke checks use checked-in example JSON rather than real parcel data. |

## Pilot gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Pilot consent checklist completed | Liam (release) | participant onboarding | not started | The checklist exists, but no pilot completion record exists yet. |
| Pilot operator checklist completed | Liam (release) | operator onboarding | not started | The checklist exists, but no operator onboarding run has been completed yet. |
| Pilot incident playbook assigned to named contacts | Liam (release) | pilot operations | not started | The playbook exists, but named contacts are still missing. |
| Pilot participant notice approved | Liam (governance/privacy) | participant materials | not started | Draft materials exist, but there is no completed approval record yet. |
| No pilot result publication exposes exact parcel-linked contributed data | Liam (release) | reports, slides, posts | not started | The red line is documented, but there is no active pilot publication review record yet. |

## Release copy gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Public copy avoids directive safety language | Liam (release) | README, posts, site | in progress | The release site and notice align with the claims-and-safety-language doc, but remaining assets still need owner review. |
| Public copy does not imply complete neighborhood visibility | Liam (release) | site, map copy, posts | in progress | The release site and shared-map coverage language describe partial coverage, but a full asset review is still pending. |
| Public copy distinguishes private, shared, public, and derived information | Liam (governance/privacy) | docs, site, UI | in progress | Core docs and parcel-view fields distinguish major data classes, but broader copy and UI alignment are still incomplete. |
| Release copy stays within current release and publication limits | Liam (legal/IP) | release materials | in progress | The public site stays inside Packet 1 and the reviewer packet isolates deeper material, but formal owner sign-off is still pending. |

## Stop-ship triggers

Do not ship a pilot or broader release if any of the following are true:

- the product still implies emergency authorization or guaranteed safety
- real contributed parcel-linked data is publicly mapped at parcel resolution
- sharing is enabled without a clear matching notice
- revocation does not reliably stop future sharing
- operator access to parcel-linked data is effectively untracked
- public artifacts expose datasets or detail levels not covered by the release and dataset policies
