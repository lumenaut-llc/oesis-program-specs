# Architecture

## Summary

The shared map is the neighborhood condition layer, not a public parcel surveillance tool. It should present coarse, delayed, thresholded shared conditions without revealing which specific parcel contributed a real hazard signal.

## Core objects

- neighborhood cell summary
- aggregate hazard indicator
- participation threshold state
- public-context overlay
- provenance class summary

## Inputs

- shared-mode contributions permitted by active sharing settings
- public context layers suitable for map display
- map publication policy constraints

## Outputs

- coarse shared neighborhood condition view
- map-ready aggregate summaries for participating users
- coverage or participation disclaimer metadata

## Internal modules

- aggregation and thresholding module
- spatial coarsening module
- provenance labeler
- publication policy filter

## External dependencies

- shared-data store
- public-context store
- policy rules from privacy governance and legal docs

## Realtime needs

- neighborhood updates should prefer delay and safety over apparent real-time precision
- publication should be suppressible when participation is too low or data is too sparse

## Risks

- revealing the likely identity of a contributing parcel
- implying full neighborhood visibility under partial adoption
- mixing public context and participant-contributed signals without distinction
- exposing map timestamps or counts that enable singling out
