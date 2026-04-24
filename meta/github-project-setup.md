# GitHub Project v2 — cross-repo gaps setup

## Purpose

Set up a single organization-level Project v2 at [github.com/orgs/lumenaut-llc](https://github.com/orgs/lumenaut-llc) that pulls gap-tracking issues from every OESIS repo into one cross-repo board with views grouped by program-phase, node family, owner, and critical path.

## Why a Project v2

The gap register ([`release/v.0.1/v0.1-gap-register.md`](../release/v.0.1/v0.1-gap-register.md)) is the canonical summary index with pivot views for release review. Each tracked gap (G11–G24) now has a GitHub Issue on the repo where the work actually happens. A cross-repo Project layers views over those issues without moving the canonical summary out of the docs.

Per [`doc-discipline.md`](doc-discipline.md) rule 2: summary docs cite, they don't duplicate. The gap register stays canonical; the Project is a navigational surface over existing issues.

## Prerequisites

The user executing this setup needs:

1. GitHub account with admin access to the `lumenaut-llc` organization
2. `gh` CLI installed and authenticated
3. `project` scope added to the gh token:

```bash
gh auth refresh -s project
```

After refresh, verify:

```bash
gh auth status
# Token scopes should now include: project
```

## Setup — web UI (recommended first time)

Step-by-step through the GitHub web UI, since Project v2 field configuration is easier point-and-click than via API:

### 1. Create the Project

1. Navigate to <https://github.com/orgs/lumenaut-llc/projects>
2. Click **New project**
3. Select **Board** template (we'll add views later)
4. Title: **OESIS cross-repo gaps**
5. Description: *Tracks every gap from v0.1-gap-register.md (G1–G24+) across all OESIS repos. Canonical summary lives in oesis-program-specs/release/v.0.1/v0.1-gap-register.md. This Project is a navigational view only.*
6. Click **Create project**

### 2. Configure custom fields

Click **Settings** (top right) → **+ New field** for each:

**Phase** (Single select)

- v0.1
- v0.2
- v0.3
- v0.4
- v0.5
- v1.0
- v1.5
- v2 / v2.5 / v3 / v4 (defer)

**Node family** (Single select)

- bench-air
- mast-lite
- flood-node
- weather-pm-mast
- thermal-pod
- circuit-monitor
- platform

**Owner area** (Single select)

- hardware
- technical
- governance
- product
- operations

**Severity** (Single select)

- blocker
- important
- defer
- PRD-only

**Program** (Single select — which platform program the gap belongs to)

- calibration
- adapter-trust
- hazard-formula-v1
- none

**Promotion bar item** (Single select — which of the 5 items in `pre-1.0-version-progression.md` item 5 this blocks)

- item 1 (architecture scope)
- item 2 (contract/runtime boundary)
- item 3 (acceptance commands)
- item 4 (implementation-status evidence)
- item 5 (calibration-program compliance)

**Gap ID** (Text — record the G## for cross-reference with v0.1-gap-register.md)

### 3. Add the repos as sources

Settings → **Manage access** → enable Project workflows for each repo:

- lumenaut-llc/oesis-program-specs
- lumenaut-llc/oesis-hardware
- lumenaut-llc/oesis_runtime
- lumenaut-llc/oesis-contracts
- lumenaut-llc/oesis-public-site

### 4. Auto-add issues with `gap` label

Settings → **Workflows** → **Auto-add to project**:

Filter: `is:issue label:gap`

Repos: all 5 above.

Every new issue labeled `gap` in any of the 5 repos now auto-appears in the Project.

### 5. Add existing issues

Click **+ Add item** → search for each of the 14 issues filed:

- oesis-hardware#2, #3, #4, #5, #6
- oesis_runtime#3, #4, #5
- oesis-contracts#2
- oesis-program-specs#12, #13, #14, #15, #16

Alternatively, use gh CLI (after `gh auth refresh -s project`):

```bash
# Get project ID
gh project list --owner lumenaut-llc --format json

# Batch add issues (replace <PROJECT_ID>)
for issue in "oesis-hardware/2" "oesis-hardware/3" "oesis-hardware/4" \
             "oesis-hardware/5" "oesis-hardware/6" \
             "oesis_runtime/3" "oesis_runtime/4" "oesis_runtime/5" \
             "oesis-contracts/2" \
             "oesis-program-specs/12" "oesis-program-specs/13" \
             "oesis-program-specs/14" "oesis-program-specs/15" \
             "oesis-program-specs/16"; do
  gh project item-add <PROJECT_ID> --owner lumenaut-llc \
    --url "https://github.com/lumenaut-llc/$issue"
done
```

### 6. Populate custom field values

For each added issue, set:

- **Phase** — from the label or issue body
- **Node family** — from the label
- **Owner area** — from the label
- **Severity** — from the label
- **Program** — from the label
- **Gap ID** — `G##` from the issue title

The field values should match labels; the fields exist because Project views can group by field values (labels cannot be grouped in the same way).

### 7. Create views

**View 1 — By phase** (default board)

- Layout: Board
- Group by: Phase
- Sort: Severity (blocker first)

**View 2 — By node family**

- Layout: Board
- Group by: Node family

**View 3 — By owner**

- Layout: Board
- Group by: Owner area

**View 4 — Critical path** (v1 hazard formula chain)

- Layout: Table
- Filter: `Program = hazard-formula-v1 OR Program = calibration`
- Sort: Phase, then Severity
- Shows the dependency chain G13 → G14 → G16/G17 → G15 → G11 in a readable row

**View 5 — Open blockers**

- Layout: Table
- Filter: `Status != Done AND Severity = blocker`
- Sort: Phase

**View 6 — Good first issue**

- Layout: Table
- Filter: `label = "good first issue"`
- For drive-by contributors landing at the Project for the first time

## Setup — API-only alternative

If you prefer full-automation, the full setup can be scripted via `gh project` and `gh api graphql`. However:

- Project v2 custom-field configuration via API is verbose (each field needs a separate GraphQL mutation)
- Views cannot be created via API today — view configuration is web-UI only

For a first-time setup, the web UI is faster. For ongoing operations (adding new issues, updating field values), `gh project` commands work well.

## Contributor-facing view

Once the Project is live, add a link to it from each repo's CONTRIBUTING.md or README.md:

```markdown
## How to help

See [`OESIS cross-repo gaps`](https://github.com/orgs/lumenaut-llc/projects/<NUMBER>)
for all currently-tracked work across repos. Filter by:

- **Phase** to see what blocks a given promotion (v0.2, v1.0, v1.5)
- **Node family** to see everything for a specific sensor node
- **good first issue** label for drive-by-friendly work
```

Canonical authority remains in the gap register. The Project is a navigational view.

## Maintenance

The Project is low-maintenance if two disciplines hold:

1. **Every new tracked gap gets filed as an issue labeled `gap`** (auto-ingested into Project via workflow)
2. **Gap register updates** — when a gap resolves, close the issue and update the `v0.1-gap-register.md` entry. The Project reflects closure automatically.

Per [`doc-discipline.md`](doc-discipline.md) rule 2, the gap register is canonical and the Project cites it. If they disagree, fix the Project to match the register (not the other way around).

## Related

- [`doc-discipline.md`](doc-discipline.md) rule 2 — summary docs cite canonical sources
- [`../release/v.0.1/v0.1-gap-register.md`](../release/v.0.1/v0.1-gap-register.md) — canonical gap register
- [`repo-manifest.md`](repo-manifest.md) — file-level manifest
- [`../architecture/decisions/debate-map.md`](../architecture/decisions/debate-map.md) — frontier debates (not tracked in Project; live in the doctrine doc)
