# Contracts Bundle

The contracts bundle has moved to [**oesis-contracts/bundles/contracts-bundle/**](https://github.com/lumenaut-llc/oesis-contracts/blob/main/bundles/contracts-bundle/).

It is a published snapshot of the canonical schemas and examples, generated from `oesis-contracts/` at a known commit.

## Consumers

The bundle is consumed by downstream projects that need a single versioned drop rather than tracking the contracts repo directly:

- `oesis-runtime` — mirrors bundle schemas under `oesis/assets/v*/` and verifies parity
- `oesis-public-site` — consumes public-safe portions via `public-content-bundle`

## Manifest

See [bundles/contracts-bundle/manifest.json](https://github.com/lumenaut-llc/oesis-contracts/blob/main/bundles/contracts-bundle/manifest.json) for the latest bundle version, lane, and schema inventory.
