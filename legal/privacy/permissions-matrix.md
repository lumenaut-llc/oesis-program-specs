# Permissions Matrix

## Purpose

Turn privacy principles into concrete MVP sharing modes that software policy enforcement and UI controls can implement.

## Governing rule

No parcel-linked data should leave the private parcel context unless a defined sharing mode, purpose, precision, and recipient scope all permit it.

Sharing permission does not grant control permission.

## Core dimensions

- what is shared
- where it is shared at what precision
- when it is shared
- who can access it
- why it is being shared

## Data classes covered

- private parcel data
- shared data
- public context
- derived parcel states

This includes later-stage private parcel data such as:
- house-state telemetry
- house capability and control compatibility records
- intervention history
- verification history

## MVP sharing modes

### Mode 1. Private only

Purpose:
- parcel operator monitoring and parcel-local interpretation

Allowed:
- raw parcel observations visible to the parcel operator
- exact parcel-state history visible to the parcel operator
- public context used inside the parcel product

Not allowed:
- neighbor visibility into parcel-linked data
- public map exposure
- research reuse without separate opt-in

### Mode 2. Network assist

Purpose:
- improve the platform's internal parcel inference or neighborhood trend logic without exposing parcel-attributed raw values to other users

Allowed:
- selected private signals used internally by platform services
- model-quality and calibration use tied to service operation

Required constraints:
- separate opt-in from basic product use
- no user-facing parcel attribution to other households
- no repurposing into marketing, insurance, or unrelated analytics

### Mode 3. Neighborhood aggregate contribution

Purpose:
- contribute to a neighborhood condition layer that works under partial adoption without exposing exact parcel conditions

Allowed:
- delayed and coarsened hazard indicators
- thresholded trend summaries
- neighborhood-cell or block-level aggregates

Required constraints:
- minimum participation threshold before display
- no exact parcel marker for another home's contribution
- no raw stream exposure
- no exact timestamps that enable singling out

### Mode 4. Research or pilot contribution

Purpose:
- bounded evaluation, pilot, or research work beyond normal product operation

Allowed:
- only under a separate, explicit opt-in
- only for a documented purpose and retention period
- only for approved recipients or program operators

Required constraints:
- narrower scope than general product terms
- publication and redistribution rules stated up front
- no assumption that research data becomes open data

## MVP control matrix

| Mode | Default | Data leaving private parcel context | Precision | Recipients | Timing | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Private only | on | none beyond service operation | exact parcel, owner view only | parcel operator and approved household roles | near-current | baseline mode |
| Network assist | off | selected internal-use signals | internal service scope only | platform operator only | near-current or batch | no cross-household visibility |
| Neighborhood aggregate contribution | off | delayed derived indicators, coarse summaries | neighborhood cell, block, or similar coarse unit | participating users via shared layer | delayed or batched | requires thresholding |
| Research or pilot contribution | off | documented subset only | least detailed level that meets study need | named pilot or research operators | batch or bounded event window | separate consent required |

## Prohibited early-version sharing

- public parcel-by-parcel hazard map
- public listing of which homes are contributing
- default-on sharing for model improvement
- exact address or exact parcel geometry in shared neighborhood views
- raw sensor feed sharing across households
- occupancy, vacancy, evacuation, or reentry status published per parcel

## UI and API requirements

- every control must show what leaves the parcel context
- every control must state who can see the shared output
- every control must be revocable
- every API carrying shared data must identify the applicable sharing mode
- any future automation or bounded-control feature must use a separate permission surface from these sharing modes
