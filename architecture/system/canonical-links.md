# Canonical Links

Some project-level starter-package files still live one directory above the git
repo, in the workspace package root.

Those outer files are useful for chat/bootstrap context, but they are not
tracked by this repo.

Tracked equivalents and deeper in-repo sources of truth live here:

- `README.md` for the program-level entry point
- `README.md` in this folder for the tracked system-overview index
- `phase-roadmap.md` for the capability-stage roadmap
- `deployment-maturity-ladder.md` for the hardware and operations overlay
- `architecture-gaps-by-stage.md` for stage placement of operational architecture gaps
- `../../../../meta/starter-package/` for tracked bootstrap and prompt files that used to exist only in the outer workspace package

The outer starter-package files currently include:

- system-overview.md
- glossary.md
- roadmap.md
- architecture/README.md
- architecture/current/README.md
- governance-and-privacy.md
- procurement-and-bom.csv

When there is a conflict between outer bootstrap notes and tracked implementation
docs, prefer the tracked docs in this repo.
