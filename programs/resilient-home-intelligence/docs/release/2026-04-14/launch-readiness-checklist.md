# Launch Readiness Checklist

## Purpose

Turn the repo's governance, legal, privacy, and claims rules into a practical release gate for public preview, pilot launch, and later product deployment.

## How to use

- assign an owner for each item
- mark status as `not started`, `in progress`, or `done`
- do not treat a document as complete unless the corresponding product or operational surface also exists where required

## Governance and legal gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Data classes are fixed and referenced by product/API work | | docs, schemas, APIs | not started | |
| Sharing modes are defined and aligned with UI and policy docs | | parcel settings, docs | not started | |
| Claims and safety-language standard reviewed against public copy | | site, app, release copy | not started | |
| Licensing split reviewed for software, hardware, docs, and datasets | | repo root, legal docs | not started | |
| Dataset release policy applied to all public artifacts | | repo, releases, pilots | not started | |
| Trademark and compatibility language reviewed | | release copy, docs, branding | not started | |

## Product and UX gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Parcel-state labels use condition-estimate language | | parcel UI, docs, notifications | not started | |
| Sharing settings copy matches actual data use | | parcel settings UI | not started | |
| Rights request entry points exist for export and deletion | | parcel settings UI, support flow | not started | |
| Provenance and freshness are visible in parcel views | | parcel UI | not started | |
| Shared-map disclosures explain aggregation and partial coverage | | shared map UI | not started | |
| Public map red lines are enforced in product design | | shared map UI, APIs | not started | |

## Data and API gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Sharing settings object implemented from schema | | backend, parcel API | not started | |
| Consent record object implemented from schema | | backend, audit trail | not started | |
| Rights request object implemented from schema | | backend, support/admin flow | not started | |
| Parcel API includes visible data-class and sharing summaries where intended | | parcel API | not started | |
| Shared-map API suppresses exact parcel identifiers and raw refs | | shared map API | not started | |
| Revocation behavior stops future sharing promptly | | backend jobs, map pipeline | not started | |

## Security and operator gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Internal operator access rules are documented and distributed | | ops, support, engineering | not started | |
| Parcel-linked access is logged | | admin tools, backend | not started | |
| Informal side-copy handling is prohibited operationally | | ops practice | not started | |
| Incident path exists for privacy, visibility, and output issues | | pilot ops, support | not started | |
| Production-like demos avoid real household data | | demos, previews | not started | |

## Pilot gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Pilot consent checklist completed | | participant onboarding | not started | |
| Pilot operator checklist completed | | operator onboarding | not started | |
| Pilot incident playbook assigned to named contacts | | pilot operations | not started | |
| Pilot participant notice approved | | participant materials | not started | |
| No pilot result publication exposes exact parcel-linked contributed data | | reports, slides, posts | not started | |

## Release copy gates

| Item | Owner | Surface | Status | Notes |
| --- | --- | --- | --- | --- |
| Public copy avoids directive safety language | | README, posts, site | not started | |
| Public copy does not imply complete neighborhood visibility | | site, map copy, posts | not started | |
| Public copy distinguishes private, shared, public, and derived information | | docs, site, UI | not started | |
| Preview copy stays within holdback and publication limits | | release materials | not started | |

## Stop-ship triggers

Do not ship a pilot or broader release if any of the following are true:

- the product still implies emergency authorization or guaranteed safety
- real contributed parcel-linked data is publicly mapped at parcel resolution
- sharing is enabled without a clear matching notice
- revocation does not reliably stop future sharing
- operator access to parcel-linked data is effectively untracked
- public artifacts expose datasets or detail levels not covered by the release and dataset policies
