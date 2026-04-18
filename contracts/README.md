# Contracts

Schemas, examples, and contract prose have moved to [**oesis-contracts**](https://github.com/lumenaut-llc/oesis-contracts).

This directory is a pointer only; it has no canonical content.

## Lane directories in oesis-contracts

- [v0.1](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.1/) — baseline (bench-air, consent, sharing, rights, access)
- [v0.2](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.2/) – [v0.5](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v0.5/) — overlay lanes (inherit v0.1)
- [v1.0](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.0/) — fielded lane (trust scoring, multi-node composition, deployment metadata)
- [v1.5](https://github.com/lumenaut-llc/oesis-contracts/blob/main/v1.5/) — bridge lane (house-state, equipment-state, intervention events, verification outcomes)

## Why the split?

Contracts have their own lifecycle — schemas ship on lane promotions, while the program-specs repo (architecture, governance, release) evolves on a different cadence. See `meta/repo-split-plan.md` Phase 6 for the full rationale.

## Validation

Cross-repo consistency (schemas + examples across `oesis-contracts`, `oesis-runtime`, and this repo) is still checked here:

```bash
make cross-repo-sync
```

This requires both `../oesis-contracts/` and `../oesis-runtime/` as sibling checkouts.
