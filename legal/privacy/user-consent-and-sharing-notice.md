# User Consent and Sharing Notice

## Purpose

Provide the MVP baseline for how sharing choices and parcel-linked data use should be explained to parcel operators before data leaves the private parcel context.

## Governing rule

Consent should be specific, understandable, and tied to an actual sharing mode. It should not be bundled into general product access if the user can reasonably use the private parcel product without that sharing.

## Minimum notice elements

Every sharing flow should clearly state:

- what data will leave the private parcel context
- whether the outgoing data is raw, derived, delayed, or aggregated
- who can access it
- what purpose it serves
- whether it can be revoked
- what happens to previously aggregated outputs after revocation

## MVP sharing notice language

Recommended private baseline:

- Your parcel data stays private by default.
- The platform uses your local device data to generate parcel-level condition estimates for your account.

Recommended neighborhood aggregate notice:

- If you turn this on, the platform may contribute delayed and coarsened hazard indicators from your parcel to neighborhood-level condition summaries.
- Other users should not see your exact parcel readings or exact parcel location from this setting alone.
- You can turn this off later to stop future contributions. Previously aggregated neighborhood summaries may remain if they no longer identify your parcel.

Recommended network assist notice:

- If you turn this on, selected parcel signals may be used internally to improve inference quality, calibration, and platform performance.
- This does not make your parcel's exact readings visible to other households.

Recommended research or pilot notice:

- If you join a pilot or research program, your data may be used for the specific program described to you.
- This setting should be separate from ordinary product use and should explain who is operating the program, how long the data is kept, and whether results may be published.

## Consent UX rules

- sharing controls should default to off unless strictly necessary for the requested service
- the control label should match the actual data use
- revocation should be available in the same area as activation
- vague terms like improve the community should not replace concrete descriptions
- if the product uses exact parcel data internally for basic operation, say so directly

## Records

The platform should keep a consent record for:

- the user or account
- the sharing mode enabled
- the effective time
- the notice version shown
- the revocation time if later disabled
