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
- Operator dry run on April 1, 2026 succeeded for `python3 -m oesis.parcel_platform.reference_pipeline`, `python3 -m oesis.ingest.ingest_packet oesis/assets/v0.1/examples/node-observation.example.json --parcel-id parcel_demo_001`, and preview-site HTTP checks returning `200 OK` for `http://127.0.0.1:8000/`.

**2026-04-15 refresh:** All six acceptance suites (v0.1–v1.0) pass. Governance, sharing, consent, and revocation gates updated to reflect v0.5 implementation evidence. Licensing gate closed after 4-repo asset-class matrix review. Data-class validation confirmed across v0.1 and v1.0 schema lanes.

## Governance and legal gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Data classes are fixed and referenced by product/API work | Liam (technical) | docs, schemas, APIs | done | `make oesis-validate` and `make oesis-v10-validate` pass; 19 v1.0 example payloads validated. Data classes stable across v0.1–v1.0 lanes. |
| Sharing modes are defined and aligned with UI and policy docs | Liam (governance/privacy) | parcel settings, docs | in progress | v0.5 acceptance validates sharing settings, consent lifecycle, and revocation at API level. Product UI for operator sharing management not yet built. |
| Claims and safety-language standard reviewed against public copy | Liam (release) | site, app, release copy | in progress | The release site and notice were written against the claims doc, but final release-owner review is still pending. |
| Licensing split reviewed for software, hardware, docs, and datasets | Liam (legal/IP) | repo root, legal docs | done | Asset-class license matrix updated for 4-repo structure (specs, runtime, hardware, public-site). GL-4 gate closed 2026-04-15. |
| Dataset release policy applied to all public artifacts | Liam (legal/IP) | repo, releases, pilots | not started | Policy exists, but artifact-by-artifact application is still pending. |
| Trademark and compatibility language reviewed | Liam (release) | release copy, docs, branding | not started | No completed review evidence yet. |

## Product and UX gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Parcel-state labels use condition-estimate language | Liam (technical) | parcel UI, docs, notifications | in progress | Preview docs use condition-estimate language, but fuller parcel UI and notification surfaces remain reference-only. |
| Sharing settings copy matches actual data use | Liam (governance/privacy) | parcel settings UI | in progress | The reference parcel view exposes `sharing_summary`, but a true parcel-settings UI is not implemented yet. |
| Rights request entry points exist for export and deletion | Liam (technical) | parcel settings UI, support flow | in progress | Reference admin export and delete flows exist, but end-user entry points do not. |
| Provenance and freshness are visible in parcel views | Liam (technical) | parcel UI | done | Verified locally on April 1, 2026 from `python3 -m oesis.parcel_platform.reference_pipeline`; `parcel_view` includes `freshness` and `provenance_summary`. |
| Shared-map disclosures explain aggregation and partial coverage | Liam (technical) | shared map UI | in progress | The shared-map API exposes a coverage notice, but the broader shared-map UI is still incomplete. |
| Public map red lines are enforced in product design | Liam (release) | shared map UI, APIs | in progress | The shared-map reference API reports `public_map_supported: false`, but broader product review is still pending. |

## Data and API gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Sharing settings object implemented from schema | Liam (technical) | backend, parcel API | done | v0.5 acceptance validates sharing settings lifecycle: configure, consent, share, revoke. API-level implementation complete. |
| Consent record object implemented from schema | Liam (technical) | backend, audit trail | done | v0.5 acceptance validates consent grant, eligibility check, and structurally-private rejection. Consent store operational. |
| Rights request object implemented from schema | Liam (technical) | backend, support/admin flow | done | Reference rights-request stores and admin processing routes exist and are exercised in v0.5 acceptance. |
| Parcel API includes visible data-class and sharing summaries where intended | Liam (technical) | parcel API | done | Parcel views expose `data_classes_visible` and `sharing_summary`. v0.5 acceptance validates. |
| Shared-map API suppresses exact parcel identifiers and raw refs | Liam (technical) | shared map API | done | Shared-map aggregate-first path tested in v0.5 acceptance; `public_map_supported: false` enforced; revoked parcels suppressed. |
| Revocation behavior stops future sharing promptly | Liam (governance/privacy) | backend jobs, map pipeline | done | v0.5 acceptance proves: `revoked_at` stops future sharing, shared-map suppresses revoked parcels. HTTP-level enforcement not yet tested (Tier B). |

## Security and operator gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Internal operator access rules are documented and distributed | Liam (governance/privacy) | ops, support, engineering | in progress | Internal access policy documented; operator access logging implemented in reference flows (SO-2 closed in v1.0 checklist). Distribution/rollout pending. |
| Parcel-linked access is logged | Liam (technical) | admin tools, backend | done | Reference admin flows append operator access events with timestamps and identity. v0.5 acceptance exercises access logging paths. |
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
