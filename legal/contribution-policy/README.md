# Contribution Policy

## Purpose

Define how outside contributors can help with code, docs, hardware, and examples without creating hidden IP, privacy, or safety-governance risk.

For the April 14, 2026 public preview, use `../../release/2026-04-14/contributor-and-review-guide.md` as the short contributor and reviewer entrypoint.

## MVP contribution rules

- contributors may submit code, documentation, hardware designs, test fixtures, schemas, and synthetic examples
- contributors should not submit real homeowner-contributed parcel-linked data through normal repository contribution paths
- contributors should not include secrets, exact household locations, live credentials, or unreviewed third-party datasets
- safety, privacy, and claims-sensitive changes require maintainer review before merge

## Inbound rights model

Recommended MVP approach:
- use a Developer Certificate of Origin-style signoff or equivalent attestation for ordinary contributions
- require contributors to represent that they have the right to submit the work
- require contributors to identify material third-party code, data, or design inputs
- avoid a heavyweight bespoke CLA unless the project later needs centralized relicensing flexibility

Patent posture:
- rely on the patent terms of the applicable outbound licenses for normal contributions
- require maintainers to flag any contribution that appears to include patent-sensitive methods, proprietary calibration logic, or external encumbrances

## Review standards

- privacy-sensitive changes must reference the applicable privacy-governance doc
- claims-sensitive UI or copy changes must reference the claims-and-safety-language standard
- data-model changes must identify whether they affect private, shared, public, derived, or administrative data classes
- dataset-related contributions must identify source terms and release category
- architecture-sensitive changes should identify the target `architecture/` version and any affected subsystem `architecture.md`
- maintainers should reject contributions that create silent new data uses

## Contribution paths

- code / docs / hardware contribution paths
- code contributions should update interfaces, schemas, examples, and versioned architecture references when relevant
- hardware contributions should include calibration and safety notes where relevant
- docs contributions should preserve provenance and avoid overclaiming capabilities
- example data contributions should be synthetic unless explicitly approved otherwise

## Contribution red lines

- no pull request should add public parcel-level hazard data from real homes
- no pull request should add marketing claims that imply guaranteed safety or emergency-grade guidance
- no pull request should change sharing defaults from opt-in to opt-out without explicit governance approval
- no pull request should add undisclosed third-party datasets or scrape-derived data with unclear rights
- no pull request should weaken provenance, auditability, or deletion/revocation controls without explicit review
