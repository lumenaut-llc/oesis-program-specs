# Pilot Incident Playbook

## Purpose

Define a minimum response structure for incidents during a pilot involving parcel-linked sensing, shared outputs, or user trust.

## Incident categories

- data exposure or unauthorized access
- incorrect or misleading parcel output
- incorrect or over-revealing shared-map output
- broken revocation, export, or deletion handling
- device compromise or suspicious data tampering
- participant complaint about notice, consent, or public visibility

## Immediate response steps

- identify the affected pilot scope, parcels, and systems
- stop or suppress the affected output if continued display increases harm
- preserve logs and decision records
- notify the responsible operator or escalation contact
- document whether the incident affects private parcel data, shared data, public context, derived outputs, or administrative records

## Containment examples

- disable a shared layer if thresholds failed or singling-out risk appears
- suppress a parcel estimate if stale or corrupted inputs are driving misleading outputs
- pause non-essential operator access while the issue is reviewed

## Participant communication

When participants need to be informed:

- describe what happened in plain language
- describe what data or outputs were affected
- describe what actions were taken
- avoid overconfident statements until the facts are known

## Post-incident review

- record root cause and affected controls
- record whether governance docs or product behavior failed
- record what policy, UI, schema, or access-control changes are needed
- review whether any pilot publication or dataset release should be paused

## Escalation rule

If an incident materially affects parcel privacy, sharing commitments, or public visibility, treat it as a governance incident and not just a routine bug.
