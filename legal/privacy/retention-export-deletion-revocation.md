# Retention, Export, Deletion, and Revocation

## Purpose

Define the minimum lifecycle rules for participant-contributed data and parcel-linked outputs in the MVP.

## Governing rule

If the platform promises parcel stewardship and sharing by choice, it must support practical exit, review, and control mechanisms rather than treating those ideas as branding language.

## Retention baseline

The MVP should adopt category-based retention rather than indefinite storage.

### Private parcel data

Default rule:

- retain fine-grained raw observations only as long as needed for product operation, troubleshooting, calibration review, and parcel operator history features

MVP policy target:

- define a default retention window for high-resolution raw observations
- allow the parcel operator to keep a longer private history only through an explicit setting
- avoid indefinite retention of raw packets by default

### Shared data

Default rule:

- retain only the minimum fields needed for the selected sharing mode
- prefer aggregated or transformed records over persistent raw contributions

MVP policy target:

- keep future-facing shared contributions revocable at the mode boundary
- document whether previously aggregated neighborhood outputs can remain after revocation

### Public context

Default rule:

- retain according to source license, operational need, and reproducibility requirements

### Derived parcel states

Default rule:

- retain a parcel operator-visible recent history
- do not imply a permanent safety record unless the product actually supports it

### Administrative and governance records

Default rule:

- retain long enough to demonstrate consent, revocation, access review, and policy compliance

## Export rules

Parcel operators should be able to export:

- their raw participant-contributed observations
- parcel metadata they supplied
- major derived parcel-state history tied to their account
- current sharing settings and recent settings history

Export requirements:

- machine-readable format
- understandable field labels
- timestamps preserved
- provenance references included where practical

The MVP does not need perfect export breadth on day one, but it should not lock users into opaque data custody.

## Deletion rules

Deletion should cover:

- account profile data tied to the parcel operator
- private parcel-linked raw data stored by the service
- parcel associations controlled by that account
- future access to household-facing parcel-state history for the deleted account

Deletion exceptions may apply for:

- security logs
- fraud or abuse prevention records
- legal hold scenarios
- irreversibly aggregated statistics

Deletion policy requirements:

- explain what is deleted versus retained
- define expected completion timing
- prevent continued routine use of deleted data in normal product flows

## Revocation rules

Revocation applies to sharing permissions and should be distinct from full account deletion.

Minimum revocation behavior:

- stop future shared contributions immediately after the change takes effect
- stop new neighborhood or research use under that sharing mode
- record the effective time of revocation

Revocation notice requirements:

- explain whether older aggregated outputs remain
- explain whether already-exported research snapshots can be recalled or only barred from future use

## Internal access limits

- deletion or revocation must not be undermined by informal operator copies
- support and engineering access to parcel-linked data must be logged
- internal test fixtures should use synthetic data whenever possible

## Open implementation questions

- exact retention windows by data class
- offline or on-device deletion behavior for local-first deployments
- how much parcel-state history is operationally useful versus unnecessarily risky
