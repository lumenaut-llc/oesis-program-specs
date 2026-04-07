# Privacy

## Purpose

Provide the working privacy notice outline and privacy commitments for the April 14, 2026 public preview.

This file is a policy draft and planning artifact. It is not legal advice and is not yet a final product privacy notice.

## Privacy posture

Open Environmental Sensing and Inference System is designed around a
parcel-first, homeowner-controlled data model.

The working privacy posture is:

- private by default
- shared by choice
- explicit provenance and uncertainty
- no quiet conversion of private parcel data into public data

## Data categories covered

The project uses the following data classes:

- private parcel data
- shared opt-in data
- public context
- derived parcel states
- administrative and governance records

See `data-classification-standard.md`.

## What data the project may collect

Depending on the deployment and enabled features, the project may collect or process:

- raw environmental observations from homeowner-controlled devices
- exact parcel-linked device and deployment metadata
- homeowner-supplied parcel notes or configuration
- sharing settings and consent records
- derived parcel-state outputs such as confidence, evidence mode, freshness, and reasons
- public context used to interpret parcel conditions
- limited service, audit, and security records

## Why data may be processed

The working purposes are:

- provide parcel-level monitoring and interpretation for the homeowner
- maintain product operation, debugging, and security
- apply the homeowner’s selected sharing settings
- generate neighborhood aggregate views only where an opt-in mode permits it
- support bounded research or pilot activity only where separately authorized

## Private-by-default rule

Exact parcel-linked raw data should remain in the private parcel context unless the homeowner affirmatively enables a sharing mode that allows a broader use.

The project should not:

- default users into neighborhood sharing
- expose exact parcel-linked raw streams to other households
- publish exact parcel-linked data in public map layers
- imply anonymization where that claim has not been verified

## Sharing and consent

The project expects sharing to be separated into distinct modes rather than governed by one blanket consent.

Working preview modes include:

- private only
- network assist
- neighborhood aggregate contribution
- research or pilot contribution

Each mode should clearly state:

- what leaves the private parcel context
- who can receive it
- at what precision it is shared
- when it is shared
- why it is shared

See `permissions-matrix.md`.

## Public context and provenance

The system may use public or third-party context such as weather, smoke, flood, terrain, or alert feeds.

When public context is used:

- the source should be distinguished from homeowner-contributed data
- source freshness and provenance should be preserved where practical
- the product should not imply parcel-exact local verification when only broad public context is available

## Derived parcel states

The project may generate parcel-state outputs such as condition estimates, confidence, evidence mode, reasons, and freshness.

Privacy and product language should treat these as inferences, not as guaranteed facts.

Derived parcel-state outputs should:

- remain clearly tied to their evidence sources
- preserve freshness information
- avoid overstating certainty

## Access, export, deletion, and revocation

The project intends to support practical user control over parcel-linked data, including:

- access to key homeowner-contributed records
- export of homeowner-contributed records and major parcel-state history
- deletion of private parcel-linked data subject to stated exceptions
- revocation of future sharing permissions

See `retention-export-deletion-revocation.md`.

## Internal access expectations

The project’s working rule is that parcel-linked data access by operators should be limited and logged.

Current governance direction:

- access should be tied to operational need
- test fixtures should use synthetic data where possible
- deletion or revocation should not be undermined by informal operator copies

## What this preview does not promise

This preview file does not promise that:

- every privacy control is fully implemented today
- every jurisdiction-specific privacy requirement has been fully reviewed
- all shared outputs are anonymous
- the project will retain data indefinitely

## Attorney review triggers

Privacy or data counsel review is strongly recommended before:

- public pilots using real homeowner data
- research data collection beyond ordinary product operation
- any public map release using participant data
- finalizing a public privacy notice or terms of use

## Related docs

- `data-ownership.md`
- `data-classification-standard.md`
- `permissions-matrix.md`
- `retention-export-deletion-revocation.md`
- `claims-and-safety-language.md`
