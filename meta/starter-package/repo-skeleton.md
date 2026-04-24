# Repo Skeleton

Suggested starting structure:

```text
open-source-diy-tech/
  programs/
    resilient-home-intelligence/
      README.md
      roadmap.md
      system-overview.md
      glossary.md
      architecture-index.md
      governance-and-privacy.md
      procurement-and-bom.csv
      project-instructions.md
      chat-prompts.md

      hardware/
        bench-air-node/
        mast-lite/
        weather-pm-mast/
        flood-node/
        thermal-pod/

      software/
        parcel-platform/
        ingest/
        inference/
        shared-map/
        dashboard/

      docs/
        build-guides/
        calibration/
        data-model/
        api/
        pilot-playbooks/

      legal/
        licensing/
        defensive-publication/
        contribution-policy/

      media/
        diagrams/
        renders/
        photos/
```

Suggested next additions:

- one markdown file per hardware subsystem
- one markdown file per hazard model
- one shared data dictionary
- one packet schema file for nodes
- one installation checklist per node type
