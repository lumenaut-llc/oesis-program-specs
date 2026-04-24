# Directory versioning destination matrix

This matrix is the historical record of the directory-versioning rollout. It documents where each top-level subtree landed, why, and whether further work is expected.

The rollout is **complete at its planned scope**. No further subtrees are being moved to version-first canonical layout (see "Status" column below).

## Conventions

- **Baseline lane**: `v0.1/`
- **Additive lanes**: `v1.0/`, `v1.5/`
- **Two distinct patterns observed**:
  - **`v0.1/` canonical** — canonical content lives under `v0.1/`; later lanes inherit or add (used by oesis-contracts and oesis-hardware sibling repos)
  - **`v0.1/` lane-contract** — canonical content stays at its natural location (e.g., `meta/adr/`, `software/inference-engine/`); `v0.1/README.md` is a thin lane-contract doc that explains the versioning posture for that subtree (used by program-specs subtrees)

## Top-level directory mapping

| Directory | Pattern | Status | Notes |
| --- | --- | --- | --- |
| `contracts/` (sibling repo `oesis-contracts`) | `v0.1/` canonical | ✅ canonical complete | Root stubs (`schemas/`, `examples/`) deleted 2026-04-23 |
| `hardware/` (sibling repo `oesis-hardware`) | `v0.1/` canonical | ✅ canonical complete | Restructure landed 2026-04-23 (PR #8); families and parcel-kit/calibration moved into `v0.1/`; `circuit-monitor` to `v1.5/` |
| `release/` | `v0.1/` canonical | ✅ canonical complete | Was already version-first (release packets are inherently per-slice) |
| `artifacts/` | `v0.1/` lane-contract | ✅ lane-contract in place | `artifacts/v0.1/README.md` documents lane posture; canonical bundles stay at `artifacts/contracts-bundle/` etc. |
| `software/` | `v0.1/` lane-contract | ✅ lane-contract in place | Per-subsystem stubs in `v0.1/<subsystem>/README.md` redirect to canonical `software/<subsystem>/` |
| `operations/` | `v0.1/` lane-contract | ✅ lane-contract in place | `operations/v0.1/README.md` documents lane posture; `pilots/` stays at root |
| `legal/` | `v0.1/` lane-contract | ✅ lane-contract in place | `legal/v0.1/README.md` documents lane posture; per-topic dirs (`privacy/`, etc.) stay at root |
| `meta/` | `v0.1/` lane-contract | ✅ lane-contract in place | `meta/v0.1/README.md` documents lane posture; cross-version artifacts (`adr/`, `milestones/`, `proposals/`) stay at root |
| `program/` | `v0.1/` lane-contract | ✅ lane-contract in place | `program/v0.1/README.md` documents lane posture; `operating-packet/` stays at root |

## Why two patterns

The `v0.1/` canonical pattern (used in contracts and hardware) fits content with **clear per-version product evolution** — schema versions, hardware revisions. Moving the canonical content under `v0.1/` and treating later lanes as deltas/redirects works because the content has a meaningful per-version semantic.

The `v0.1/` lane-contract pattern (used in program-specs subtrees) fits content that is **mostly cross-version** — ADRs, system architecture programs, proposals, current-state docs, legal posture. Forcing this content under `v0.1/` would falsely imply it's version-scoped. The lane-contract stub gives the subtree a documented versioning posture without restructuring its semantics.

## Explicit non-rollouts

- **No further subtrees** in oesis-program-specs are being moved to `v0.1/` canonical. The lane-contract stubs are the endpoint, not a stepping stone.
- **`media/`** was listed in earlier drafts but the directory does not exist; row removed.
- **Subsystem-specific deep content trees** (e.g., `architecture/decisions/`, `software/inference-engine/`, `meta/adr/`) are not version-scoped and stay at their natural location — the lane-contract stubs reference them as canonical.

## Related

- [`meta/oesis-build-decision.md`](oesis-build-decision.md) — sibling decision about a different directory structure question
- [`meta/doc-discipline.md`](doc-discipline.md) — overall doc-organization rules
- [`meta/repo-split-plan.md`](repo-split-plan.md) — historical context for the contracts/hardware extractions
