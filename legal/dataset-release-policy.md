# Dataset Release Policy

## Purpose

Define what kinds of data may be published, shared, redistributed, or attached to the open-source project without breaking the platform's privacy and trust model.

## Governing rule

Open-source code and open hardware do not require open publication of all future parcel-linked datasets.

The project may, however, intentionally publish the project-controlled v1 dataset under explicit open-data terms.

## Dataset categories

### 1. Synthetic examples and test fixtures

Examples:

- hand-authored example payloads
- simulated hazard runs
- generated benchmark data

Release posture:

- may be published in the repository
- preferred open dataset category for early versions

### 2. Public reference datasets

Examples:

- weather or hydrology layers obtained from public agencies
- public parcel basemap references where source terms allow redistribution
- public topography or land-cover context

Release posture:

- only redistribute when the upstream license allows it
- preserve attribution, notices, and source metadata
- keep source-specific terms attached

### 3. Project-controlled v1 field dataset

Examples:

- raw sensor observations from parcel devices
- exact parcel-linked derived histories
- parcel-linked hazard contributions intentionally designated for the public release
- derived parcel-state outputs tied to the v1 release

Release posture:

- may be published openly when the project has clear authority to release it
- may be committed to the repository or mirrored externally when it is intentionally part of the public release
- should carry explicit dataset terms, provenance notes, date range, and any caveats about representativeness
- current recommended public dataset license: `CDLA-Sharing-1.0`

### 4. Future participant-contributed parcel-linked data

Examples:

- raw sensor observations from other households
- exact parcel-linked derived histories from future participants
- account-linked or household-linked telemetry from future deployments

Release posture:

- not public by default
- require explicit publication authority and a separate documented decision
- must not be assumed public merely because the project-controlled v1 dataset is public

### 5. Pilot or research datasets

Examples:

- bounded program exports for validation
- study datasets derived from pilot deployments

Release posture:

- require a separate review, purpose statement, retention rule, and publication decision
- should default to non-public handling unless a documented governance review approves release

## Early-version do-not-release list

- future participant parcel-linked data not explicitly designated for public release
- household identifiers or account identifiers outside the intentionally released v1 dataset scope
- neighborhood datasets with low enough participation to enable singling out
- secrets, credentials, or operator-only records accidentally embedded in dataset exports

## Release checklist

Before any dataset is published or redistributed, confirm:

- the dataset category is identified
- the source terms permit the planned release
- the project has clear authority to publish the dataset
- if the dataset is parcel-linked, it is either the intentionally public project-controlled v1 dataset or a separately approved later release
- the release does not undermine future opt-in sharing promises for later participants
- attribution, provenance, and freshness notes are included where relevant
- an explicit dataset license is attached

## MVP recommendation

For early releases, publish only:

- synthetic examples
- schemas
- validators
- benchmark fixtures
- public-source reference manifests
- the project-controlled v1 dataset when intentionally included in the public release package

Avoid publishing:

- future participant-contributed parcel datasets without a separate explicit decision
- neighborhood hazard maps derived from limited adoption pilots unless the project intentionally publishes them with clear scope, provenance, and owner authority
