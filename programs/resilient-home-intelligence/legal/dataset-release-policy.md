# Dataset Release Policy

## Purpose

Define what kinds of data may be published, shared, redistributed, or attached to the open-source project without breaking the platform's privacy and trust model.

## Governing rule

Open-source code and open hardware do not require open publication of real homeowner-contributed parcel-linked datasets.

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

### 3. Real homeowner-contributed data

Examples:
- raw sensor observations from parcel devices
- exact parcel-linked derived histories
- precise shared hazard contributions
- account-linked or household-linked telemetry

Release posture:
- must not be published openly by default
- must not be committed to the repository
- must not be relicensed under a generic open-data scheme

### 4. Pilot or research datasets

Examples:
- bounded program exports for validation
- study datasets derived from pilot deployments

Release posture:
- require a separate review, purpose statement, retention rule, and publication decision
- should default to non-public handling unless a documented governance review approves release

## Early-version do-not-release list

- exact parcel geometry tied to real contributed hazard data
- raw time series from real homes
- occupancy, vacancy, reentry, or evacuation-adjacent inferences
- real household identifiers or device identifiers
- neighborhood datasets with low enough participation to enable singling out

## Release checklist

Before any dataset is published or redistributed, confirm:

- the dataset category is identified
- the source terms permit the planned release
- the dataset contains no real parcel-linked homeowner contributions unless explicitly approved
- the release does not undermine opt-in sharing promises
- attribution, provenance, and freshness notes are included where relevant

## MVP recommendation

For early releases, publish only:
- synthetic examples
- schemas
- validators
- benchmark fixtures
- public-source reference manifests

Avoid publishing:
- real-world contributed parcel datasets
- neighborhood hazard maps derived from limited adoption pilots
