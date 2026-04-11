# Send-to-Counsel Checklist

## Status

Internal operational checklist for sending the lean parcel-state filing packet to patent counsel.

Do not publish before the filing decision.

## Purpose

Give one practical sequence for getting from internal draft to counsel outreach without forgetting the key gating steps.

## Use this version for

- the lean parcel-state generation candidate
- a fast U.S.-first provisional review
- the April 14, 2026 preview timeline

## Step 1. Confirm the filing scope

Before sending anything, confirm all of these are true:

- the candidate is limited to parcel-state generation using local evidence, parcel priors/context, and optional public context
- shared-neighborhood transforms are excluded from this filing
- hardware design specifics are excluded from this filing
- the filing is not meant to cover the entire platform

Primary reference:

- `provisional-one-page-summary-parcel-state.md`

## Step 2. Fill the remaining blanks

Complete the missing fields in:

- `provisional-inventor-questionnaire-prefill.md`
- `provisional-packet-draft-parcel-state.md`

Minimum blanks to fill:

- inventors
- owner/applicant
- earliest known disclosure
- exact target filing date
- top preserve-at-all-costs details

## Step 3. Check disclosure timing

Before contacting counsel, verify:

- whether any public disclosure has already happened
- whether any post, demo, screenshot, repo change, or social post is scheduled before filing
- whether anything in the preview package exceeds the non-enabling scope

Primary references:

- `public-preview-scope.md`
- `holdback-list.md`
- `docs/release/v0.1/social-posts.md`

## Step 4. Review the packet in order

Read in this order:

1. `provisional-one-page-summary-parcel-state.md`
2. `provisional-packet-draft-parcel-state.md`
3. `provisional-figure-captions-parcel-state.md`
4. `provisional-figures-parcel-state.md`
5. `holdback-list.md`
6. `public-preview-scope.md`

Goal:

- make sure all six docs tell the same narrow story
- make sure none of them quietly reintroduce shared-neighborhood scope

## Step 5. Prepare the attachment set

Recommended attachments for counsel:

- `provisional-one-page-summary-parcel-state.md`
- `provisional-packet-draft-parcel-state.md`
- `provisional-figure-captions-parcel-state.md`
- `provisional-figures-parcel-state.md`
- `holdback-list.md`
- `public-preview-scope.md`
- `provisional-inventor-questionnaire-prefill.md` or the completed questionnaire version

Optional attachment:

- `provisional-counsel-cover-email.md` as the email draft you will send

## Step 6. Sanity-check before sending

Do not send until these are true:

- no real homeowner data is included
- no unnecessary technical detail is attached beyond what you want reviewed
- all files are marked internal if needed
- the packet consistently says U.S.-first and preview-before-open-release
- the packet consistently says shared-neighborhood transforms are outside this filing

## Step 7. Send the email

Use:

- `provisional-counsel-cover-email.md`

Customize:

- counsel name
- your name and role
- contact info
- budget or time constraint if you want a fast answer

## Step 8. Questions to ask for the first reply

If you need a very fast first-pass answer, ask counsel to answer these first:

1. Is this candidate narrow and concrete enough for a fast provisional?
2. What missing detail is most important to add before filing?
3. Do any planned preview materials create disclosure risk before filing?
4. What still needs to stay held back after filing because it goes beyond this packet?

## Step 9. After counsel responds

Update these files first:

- `provisional-packet-draft-parcel-state.md`
- `provisional-figures-parcel-state.md`
- `holdback-list.md`
- `public-preview-scope.md`

Then decide:

- file before April 14
- delay the preview
- or switch from Path B to open defensive publication

## Fast version

If time is extremely tight, do only this:

1. Fill the fast summary box in `provisional-inventor-questionnaire-prefill.md`.
2. Fill inventors, owner/applicant, and target filing date in `provisional-packet-draft-parcel-state.md`.
3. Attach the six core files listed above.
4. Send `provisional-counsel-cover-email.md`.
