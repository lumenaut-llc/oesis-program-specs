# Architecture

## Summary

The parcel platform is the presentation and access layer for a single parcel. It should not recompute hazard logic itself. Instead, it reads parcel-state snapshots from the inference engine, combines them with parcel metadata and safe-to-display provenance details, and renders a homeowner-readable current view plus limited history.

## Core objects

- parcel profile
- current parcel-state snapshot
- parcel-state history item
- explanation payload
- freshness block
- provenance summary

## Inputs

- parcel-state snapshots from the inference engine
- parcel metadata and display preferences
- optional user-entered parcel notes or context
- policy constraints on what evidence can be displayed

## Outputs

- homeowner-facing parcel status view
- parcel-state history view
- API responses for current state and recent history
- future alerts or notification candidates

## Internal modules

- parcel-state reader
- explanation formatter
- freshness and confidence presenter
- history query module
- access-control and privacy filter

## External dependencies

- inference engine output store or API
- parcel metadata store
- identity and access layer
- privacy and governance policy rules

## Realtime needs

- The current parcel view should update quickly when a new parcel-state snapshot is available.
- History can tolerate slower retrieval as long as the latest state stays responsive.
- The platform should make staleness obvious rather than quietly serving old results.

## Risks

- rebuilding inference logic in the UI layer
- collapsing confidence, freshness, and status into one oversimplified label
- exposing more provenance detail than privacy rules allow
- hiding missing evidence in a way that implies certainty
