# Architecture

## Summary

The parcel platform is the presentation and access layer for a single parcel. It should not recompute hazard logic itself. Instead, it reads parcel-state snapshots from the inference engine, combines them with parcel metadata and safe-to-display provenance details, and renders a parcel operator-readable current view plus limited history.

It is also the primary surface for showing sharing choices, consent state, and parcel operator rights controls without blurring private parcel data, shared data, public context, and derived estimates.

## Core objects

- parcel profile
- current parcel-state snapshot
- parcel-state history item
- explanation payload
- freshness block
- provenance summary
- sharing settings summary
- consent notice version reference
- export/delete request record

## Inputs

- parcel-state snapshots from the inference engine
- parcel metadata and display preferences
- optional user-entered parcel notes or context
- policy constraints on what evidence can be displayed
- current sharing-mode settings
- consent and notice records needed to explain enabled sharing
- structured explanation payload from inference

## Outputs

- dwelling-facing parcel condition-estimate view
- parcel-state history view
- API responses for current state and recent history
- sharing settings and notices view
- export/delete/revocation request entry points
- future alerts or notification candidates

## Internal modules

- parcel-state reader
- explanation formatter
- freshness and confidence presenter
- history query module
- access-control and privacy filter
- consent and sharing-settings presenter
- rights request coordinator

## External dependencies

- inference engine output store or API
- parcel metadata store
- identity and access layer
- privacy and governance policy rules
- consent and audit record store

## Realtime needs

- The current parcel view should update quickly when a new parcel-state snapshot is available.
- History can tolerate slower retrieval as long as the latest state stays responsive.
- The platform should make staleness obvious rather than quietly serving old results.
- Sharing setting changes and revocations should take effect quickly and be visible to the parcel operator without ambiguity.

## Risks

- rebuilding inference logic in the UI layer
- collapsing confidence, freshness, and status into one oversimplified label
- exposing more provenance detail than privacy rules allow
- hiding missing evidence in a way that implies certainty
- hiding enabled sharing modes or making revocation harder than activation
- presenting condition estimates as operational safety instructions
