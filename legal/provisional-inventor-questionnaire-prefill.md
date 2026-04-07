# Provisional Inventor Questionnaire Prefill

## Status

Internal working draft based on current repo materials and planning assumptions.

Do not publish before the filing decision.

This draft is meant to reduce blank-page friction. Replace any assumption that is wrong.

## Current assumptions used in this prefill

- filing path: narrow U.S. provisional before the April 14, 2026 public preview if possible
- candidate scope: parcel-state generation using local evidence, parcel priors/context, and optional public context
- excluded from this filing: shared-neighborhood transforms, hardware design specifics, and the full platform as a whole
- release path after filing decision: move quickly toward a broader open release

## Section 1. Inventor identity

1. Full legal name of each person who contributed to the claimed parcel-state generation idea:
   - Liam Reckziegel `[confirm legal name and add others if any]`

2. For each person above, what did they specifically contribute?
   - Liam Reckziegel: current assumed contribution is the parcel-level evidence assembly and state-generation concept, including evidence mode, confidence degradation, provenance-aware output structure, and the project-level framing of parcel-specific interpretation. `[confirm]`
   - Additional contributors: `[fill if any]`

3. Did anyone outside the project contribute to this idea, even informally?
   - Current assumption: no outside inventor-level contributor identified. `[confirm]`

4. Is any employer, client, school, grant program, or accelerator likely to claim ownership rights?
   - Current assumption: uncertain. `[fill explicitly]`

## Section 2. Candidate scope confirmation

5. Confirm the lean candidate is:
   - parcel-state generation using local evidence, parcel priors/context, and public context, with evidence mode and confidence handling.
   - Current assumption: yes. `[confirm]`

6. Confirm that shared-neighborhood transforms are excluded from this filing:
   - yes `[current assumed answer]`

7. Confirm that hardware design specifics are excluded from this filing:
   - yes `[current assumed answer]`

8. Confirm that this filing is not intended to cover the full platform:
   - yes `[current assumed answer]`

## Section 3. Earliest conception and disclosure

9. When did you first write down or explain this candidate idea in a concrete way?
   - Current assumption: no exact date pinned yet; likely reflected in the March 2026 repo drafting cycle. `[fill exact earliest known date]`

10. Where is the earliest written record?
   - likely repo documents covering parcel-state schema, inference-engine architecture, and governance/privacy framing
   - likely candidates:
     - `repo/docs/data-model/parcel-state-schema.md`
     - `repo/software/inference-engine/architecture.md`
     - `governance-and-privacy.md`
   - `[confirm earliest specific artifact]`

11. Has any part of this candidate already been publicly disclosed?
   - Current assumption: uncertain / not confirmed in this workspace. `[fill explicitly]`

12. If yes, list the date, place, and what was disclosed.
   - `[fill only if applicable]`

13. Are any public posts, talks, repos, screenshots, or demos scheduled before filing?
   - yes: April 14, 2026 public preview is planned
   - current assumption: preview is intended to remain non-enabling until filing decision is complete

## Section 4. Materials to include before filing

14. Which details would you be upset to lose if they were not covered by the filing?
   - evidence-mode output tied to source classes
   - confidence degradation and `unknown` handling under weak evidence
   - parcel-state snapshot structure with provenance-aware outputs
   - use of parcel priors/context in parcel-level status generation
   - `[add or delete items based on what matters most]`

15. Are there any formulas, thresholds, scoring rules, or fallback rules that matter enough to preserve now?
   - Current assumption: maybe, but not yet specified in the repo at formula level
   - likely candidates to consider:
     - non-`unknown` minimum support rule
     - freshness downgrade rule
     - conflict downgrade rule
     - evidence-mode assignment rule
   - `[confirm which ones matter]`

16. Are there any specific parcel priors or context types that should be mentioned explicitly?
   - structure type
   - topography
   - drainage characteristics
   - node placement context
   - microclimate-related parcel context
   - `[edit list if needed]`

17. Which hazards must be covered in the filing examples:
   - current recommendation: all three
   - smoke
   - flood-runoff
   - heat

## Section 5. Ownership and release sequencing

18. Who should be the applicant or owner named for filing purposes?
   - Current assumption: uncertain. `[fill explicitly]`

19. What is the target filing date?
   - current recommendation: before April 14, 2026 public preview
   - working target: `[fill exact date]`

20. What public materials must stay held back until filing is complete?
   - parcel-inference flowchart
   - detailed evidence weighting notes
   - detailed calibration and threshold rules tied to the candidate
   - any enabling method diagrams beyond the approved preview scope
   - shared-neighborhood transform details, even though excluded from this filing

21. After filing, do you want to move quickly to open publication of the broader system?
   - current assumption: yes

22. If yes, what should remain held back even after this filing because it may become a separate candidate?
   - neighborhood-sharing transform methods
   - privacy-preserving aggregation specifics
   - possibly hardware-to-platform interaction details if later treated as a separate candidate
   - `[trim if you do not want any second candidate]`

## Section 6. Counsel priorities

23. What are the top three questions you want patent counsel to answer first?
   - Is this candidate narrow and concrete enough for a quick provisional?
   - What additional details are most important for written-description support?
   - Which planned preview materials still create disclosure risk before filing?

24. What budget or time limit should counsel assume?
   - Current assumption: fast review needed before April 14, 2026
   - budget: `[fill]`

25. Do you want a fast-file recommendation, a stronger drafting pass, or both?
   - current recommendation: both, with fast-file recommendation first

## Fast summary box

Fill this first if time is tight:

- inventors: Liam Reckziegel `[confirm and add others if any]`
- owner/applicant: `[fill]`
- target filing date: before April 14, 2026 `[fill exact date]`
- earliest known disclosure: `[fill]`
- shared-neighborhood transforms excluded: yes
- top three details to preserve:
  - evidence-mode output tied to source classes
  - confidence degradation / `unknown` behavior
  - parcel-state snapshot generation using local evidence, parcel priors, and public context

## Suggested next edits

- replace all `[confirm]` and `[fill]` markers
- if anyone else contributed to the claimed idea, add them now rather than later
- if there was any public disclosure already, write down the exact date and what was shown
