# Non-Release List

## Purpose

Track the materials that should stay out of the v0.1 open release even after the project moved away from the provisional-first path.

This list should be reviewed before any social post, repo publication, talk, demo, diagram release, or media interview.

## Current non-release categories

### 1. Secrets and access material

Do not release:

- API keys
- credentials
- auth tokens
- internal admin endpoints
- operator-only secrets or signing material

Why:

- these create immediate operational and security risk

### 2. Non-cleared third-party material

Do not release:

- third-party datasets whose license does not allow redistribution
- partner or vendor material not cleared for publication
- non-public screenshots, photos, or diagrams borrowed from outside sources
- any material whose provenance is unclear

Why:

- the project cannot open what it does not have authority to release

### 3. Non-public personal or operator data

Do not release:

- personal contact details
- operator-only access records
- internal incident-response notes
- future participant parcel-linked data that is not part of the intentionally published project-controlled v1 dataset

Why:

- the open release should be intentional, not accidental

### 4. Archival filing and counsel materials

Keep internal by default:

- `legal/provisional-*`
- `legal/send-to-counsel-checklist.md`
- `legal/counsel-questions/path-b-counsel-questions.md`

Why:

- these are historical internal planning artifacts, not the current release posture

### 5. Misleading safety or scope claims

Do not release:

- copy that implies official alerts or emergency authority
- copy that implies guaranteed safety
- copy that implies the project has complete neighborhood visibility
- copy that implies all future participant data is public by default

Why:

- the project’s core trust boundary still matters in the open-release posture

## Allowed release substitutes and approved public categories

Use these confidently in the current release:

- technical architecture and implementation docs cleared for release
- hardware build guides and design docs cleared for release
- source code, schemas, packet contracts, and examples selected for the open release
- the project-controlled v1 dataset when it carries explicit dataset terms and provenance
- governance, ownership, and limitation language

## Review workflow

For each item under consideration:

1. Ask whether the project has authority to publish it.
2. Ask whether it contains secrets, non-public personal data, or non-cleared third-party content.
3. Ask whether it is intentionally part of the public v1 dataset or an accidental inclusion.
4. Ask whether it creates misleading safety or scope claims.
5. If any answer is problematic, keep it out of the release until fixed or explicitly approved.

## Status table

Use this table as the live release gate.

| Item | Owner | Status | Public release approved | Safe for v0.1 release | Notes |
| --- | --- | --- | --- | --- | --- |
| Secrets and access material | Technical owner | blocked | no | no | never publish |
| Archival provisional packet docs | Legal/IP owner | internal | no | no | historical planning only |
| Project-controlled v1 dataset | Release owner | in review | yes, if licensed | yes | publish only with explicit dataset terms and provenance |
| Reference code and schemas | Software owner | approved | yes | yes | include with asset-class licensing |
| Hardware build and design docs cleared for release | Hardware owner | approved | yes | yes | keep safety limitations attached |
