# Data Rights and Participant Controls UX Outline

## Purpose

Define the user-facing control surface for privacy, sharing, visibility, revocation, and participation rights.

## Why this matters

The project's trust model is only real if participants can understand and control it.

Good governance language alone is not enough.
Users need:

- clear controls
- understandable consequences
- easy review and revocation

## UX principles

- private by default
- plain language before policy language
- explain what is shared, not only what is collected
- show consequences of changing a setting
- make exit and revocation realistic

## Core participant rights surfaces

### 1. My data at home

This surface should answer:

- what raw observations stay private
- what home-level outputs are private
- what context is stored for the household

### 2. My sharing mode

This surface should answer:

- am I private-only or contributing to shared intelligence
- what type of shared signals can leave my household boundary
- who can see those shared signals

### 3. My visibility

This surface should answer:

- what other participants can see
- what operators can see
- what no one else can see

### 4. Change or revoke sharing

This surface should let the user:

- reduce sharing scope
- pause participation
- exit the shared layer
- understand persistence and timing effects

## Suggested control states

### Private-only

- private home outputs only
- no shared neighborhood contribution

### Shared derived signals

- contribute bounded neighborhood-safe signals
- receive shared block intelligence

### Expanded pilot sharing

- only for well-governed pilots
- should clearly explain extra visibility and why it exists

## Suggested settings language

Good labels:

- private home only
- share neighborhood-safe signals
- receive shared block intelligence
- pause shared contribution
- leave the shared layer

Avoid:

- abstract privacy jargon without examples
- controls that imply all-or-nothing raw data sharing

## Required explanations

Each sharing mode should explain:

- what stays private
- what may be shared
- whether exact household readings are exposed
- who can see shared results
- how to change the setting later

## Review surfaces

The product should include a review page such as:

- "What I share"
- "What stays private"
- "Who can see my shared signals"
- "My current operator visibility"

## Revocation behavior

When a user revokes sharing, the UX should explain:

- future contributions stop
- some already-derived shared summaries may persist temporarily
- private home outputs continue

## Operator transparency

If an operator role exists, the user should be able to see:

- whether the community has an operator
- what the operator can see
- what the operator cannot see
- how to report misuse or concerns

## Event-time clarity

During stressful events, the product should not hide privacy posture.

Users should still be able to quickly answer:

- am I sharing right now
- who can see shared outputs
- can I pause this later

## Accessibility requirements

Controls should be:

- readable quickly
- low-jargon
- reversible
- available on mobile-first surfaces

## Success criteria

- users can accurately describe their sharing mode
- users know how to pause or revoke sharing
- users do not confuse shared derived signals with raw household exposure
- operator visibility is understandable

## Open questions

- What is the minimum set of privacy controls for phase 1 versus block pilots?
- Should the product expose a simulation view showing what others would see before consent is granted?
