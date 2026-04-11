---
name: lean-directory-audit
description: Audit a repository or directory tree for clutter, unnecessary directories, generated artifacts, duplicate or overlapping files, weak linkage, and blurred separation of concerns. Use when Codex needs to review structure before or after a refactor, trim a repo that feels bloated, decide whether files should be merged, moved, or deleted, or keep a workspace lean without deleting intentional source-of-truth material.
---

# Lean Directory Audit

## Overview

Use this skill to judge whether a tree is intentionally organized rather than merely small. Favor one obvious home per concern, minimal indirection, and clear ownership between source, generated output, docs, templates, and planning artifacts.

## Audit Workflow

1. Read the intent before pruning.
- Open the root `README`, `.gitignore`, contribution guide, and any repo map or manifest.
- Identify whether repeated structures are deliberate subsystem templates rather than accidental duplication.

2. Scan the tree.
- Run `scripts/scan_tree.py <path>` for a first pass.
- Use `--json` if the results need to feed a follow-up script or a structured review.
- Treat the scan as candidate generation, not an automatic delete list.

3. Classify each candidate.
- `delete`: generated artifacts, caches, OS cruft, dead temporary files.
- `ignore`: local build output that may exist on disk but should not be tracked.
- `merge`: two files that serve the same audience with the same content.
- `move`: a file that is valid but lives under the wrong concern boundary.
- `keep`: intentional symmetry, public release mirrors, packaging entrypoints, or audience-specific variants.

4. Verify before editing.
- Search for incoming references with `rg -n "path|filename" <root>`.
- Diff same-named files before deduping them.
- Preserve intentional duplication when it exists for legal, release, packaging, or public-consumption reasons.

5. Recommend the smallest safe diff.
- Remove high-confidence cruft first.
- Merge or move only after the canonical owner is clear.
- Update any repo map or manifest after structure changes if the repository keeps one.

## What To Flag

- Generated directories inside source trees such as `__pycache__`, `.ruff_cache`, `.pytest_cache`, `node_modules`, `dist`, `build`, and `.pio`.
- OS or editor leftovers such as `.DS_Store`.
- Exact duplicate files or repeated code or script basenames that suggest wrapper drift.
- Directories with little semantic value, especially those containing only a single low-value file or child.
- Docs that only redirect to another doc without adding audience-specific context.
- Folders that mix source, generated output, exports, and planning material.

## What Not To Flag Automatically

- Parallel subsystem docs with shared names when the names encode a stable template.
- Packaging or CLI entrypoints that intentionally wrap canonical library code.
- Release artifacts that are intentionally versioned as public deliverables.
- Legal or notice files repeated because policy or distribution boundaries require them.

## Repo Heuristics For This Workspace

Use `references/review-rubric.md` when the answer is not obvious. For this repository in particular:

- Treat `shared/` as the home for cross-cutting templates, standards, glossary material, and reusable skills.
- Treat `meta/` as planning, milestones, manifests, and repo-level decisions rather than product docs.
- Treat repeated filenames under `hardware/*` and `software/*` as structured symmetry until content proves otherwise.
- Treat `programs/resilient-home-intelligence/docs/release/**/site/` with extra care because generated site output and source often live nearby.
- Treat `rhi/` as canonical Python package code; same-named files under `programs/.../software/**/scripts/` may be user-facing wrappers rather than accidental duplicates.

## Resources

- `scripts/scan_tree.py` produces a fast first-pass scan for generated artifacts, duplicate content, repeated basenames, low-signal directories, and symlinks.
- `references/review-rubric.md` provides decision rules for borderline cases where deletion and consolidation would be risky.

## Output Shape

Return findings in this order:

1. `High-confidence cleanup`
2. `Merge or move candidates`
3. `Needs intent confirmation`
4. `Suggested smallest next diff`

Keep each finding concrete: path, reason, confidence, and recommended action.
