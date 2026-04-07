# Contracts Bundle Spec

## Purpose

Define the first cross-repo artifact that allows `oesis-runtime` to stop reading examples and contract materials directly from the monorepo docs tree.

The bundle should be simple enough to hand-assemble at first and strict enough to automate later.

## Producer and consumers

Producer:

- `oesis-program-specs`

Primary consumers:

- `oesis-runtime`
- `oesis-public-site` when public-safe contract metadata is needed

## Bundle contents

Minimum contents:

- checked JSON schemas
- checked example payloads
- bundle metadata

Optional contents:

- release notes for the bundle
- compatibility notes
- public-safe derived summaries for the site

## Suggested directory shape

```text
contracts-bundle/
  manifest.json
  schemas/
    consent-record.schema.json
    export-bundle.schema.json
    node-observation.schema.json
    node-registry.schema.json
    operator-access-event.schema.json
    parcel-state.schema.json
    retention-cleanup-report.schema.json
    rights-request-store.schema.json
    rights-request.schema.json
    shared-neighborhood-signal.schema.json
    sharing-settings.schema.json
    sharing-store.schema.json
  examples/
    consent-record.example.json
    evidence-summary.example.json
    export-bundle.example.json
    node-observation.example.json
    node-registry.example.json
    normalized-observation.example.json
    operator-access-event.example.json
    parcel-context.example.json
    parcel-state.example.json
    public-context.example.json
    raw-public-smoke.example.json
    raw-public-weather.example.json
    retention-cleanup-report.example.json
    rights-request-store.example.json
    rights-request.example.json
    shared-neighborhood-signal.example.json
    sharing-settings.example.json
    sharing-store.example.json
```

## Manifest shape

Suggested `manifest.json` fields:

- `bundle_version`
- `generated_at`
- `source_repo`
- `source_commit`
- `schema_version_set`
- `examples`
- `schemas`
- `compatibility`

Suggested example:

```json
{
  "bundle_version": "2026.04.0",
  "generated_at": "2026-04-07T00:00:00Z",
  "source_repo": "oesis-program-specs",
  "source_commit": "<git-sha>",
  "schema_version_set": [
    "oesis.bench-air.v1"
  ],
  "schemas": {
    "node-observation": "schemas/node-observation.schema.json",
    "parcel-state": "schemas/parcel-state.schema.json"
  },
  "examples": {
    "node-observation": "examples/node-observation.example.json",
    "parcel-context": "examples/parcel-context.example.json",
    "parcel-state": "examples/parcel-state.example.json"
  },
  "compatibility": {
    "runtime_min_version": "0.1.0",
    "runtime_max_version": null
  }
}
```

## Runtime integration expectations

`oesis-runtime` should consume the bundle through one boundary only.

Suggested behavior:

- default to packaged runtime fixtures for local development
- allow `OESIS_CONTRACTS_BUNDLE_DIR` to override fixture lookup
- prefer explicit bundle input in CI and release checks

This keeps local development simple while making the split path real.

## Publication rules

The bundle should be:

- versioned
- immutable once published
- validated before release
- safe to consume without internal-only review materials

The bundle should not contain:

- controlled-review notes
- counsel-only materials
- unpublished policy drafts

## Initial release rule

For the first split iteration:

- hand-assembled bundles are acceptable
- runtime may still carry a packaged default fixture set
- the important change is the boundary, not immediate automation perfection

## Future automation

Later, `oesis_build/` can assemble the bundle by:

- copying approved schemas and examples
- generating `manifest.json`
- validating file completeness against a declared list
- publishing the bundle as a release artifact
