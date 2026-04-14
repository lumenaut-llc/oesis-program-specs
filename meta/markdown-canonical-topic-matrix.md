# Markdown canonical topic matrix

This matrix records where overlapping topics should be maintained as canonical
content versus redirect-only pointers.

## Lane intent summary

- `architecture/current/` = frozen `v0.1` current-truth architecture.
- `architecture/system/` = cross-version architecture and operating-model
  narratives.
- `architecture/v1.0/` = debated target-lane framing and deltas.
- `architecture/future/` = compatibility redirects for old `v1.0` paths.
- `program/operating-packet/` = narrative packet for framing/phasing context.

## Topic matrix

| Topic | Existing locations | Canonical location | Secondary location policy |
| --- | --- | --- | --- |
| Program framing (thesis/problem/positioning) | `program/operating-packet/01`, `02`, `03` | `program/operating-packet/01-core-thesis-and-framing.md` | Keep `02` and `03` as redirect stubs |
| Version labels and phasing packet | `program/operating-packet/00`, `09` | Keep both (different roles) | No merge; cross-link |
| Hazard/functional/response bridge | `program/operating-packet/functional-state-and-response-model.md` | Same file | Keep separate from `05` and `09` |
| Target-lane roadmap/spec/taxonomy/gaps/requirements | `architecture/v1.0/{phase-roadmap,integrated-parcel-system-spec,node-taxonomy,architecture-gaps-by-stage,product-requirements-phase-1}.md` and `architecture/system/` counterparts | `architecture/system/` files for shared, cross-version canonical bodies | Convert overlapping `v1.0` files to redirect stubs to `../system/*` |
| Debated target-lane strategy/proposals | `architecture/v1.0/goals-and-deltas.md`, `proposed-architecture.md`, `open-questions.md`, `decision-log.md` | `architecture/v1.0/` | Keep as full target-lane docs |
| Legacy debated-lane paths | `architecture/future/*.md` | `architecture/v1.0/*.md` | Keep future files as redirect-only compatibility stubs |

## Execution notes

- For topic surfaces that are intentionally lane-specific, do not merge bodies.
- For duplicate cross-version surfaces, prefer one canonical body plus redirect
  files to preserve inbound links.
