# V1 Patent Decision Memo

## Status

Internal decision memo for the current v1 release posture.

This is planning support only. It is not legal advice.

Date: April 2, 2026

## Purpose

Give the project a practical answer to three questions:

1. Does the current v1 appear to contain a specific technical method that may justify patent work?
2. Does the project appear to want exclusion rights strongly enough to justify that work?
3. Is patenting a better use of time and money than open publication?

## Short answer

Current recommendation:

- do not treat a patent as necessary for v1
- prefer open release plus deliberate defensive publication over a provisional filing
- only revisit a narrow provisional if the project later decides it wants temporary exclusion leverage around a clearly stated neighborhood-transformation method

## Scope reviewed

This memo is based on the current v1 documentation and reference implementation, especially:

- `ip.md`
- `public-preview-scope.md`
- `holdback-list.md`
- `provisional-one-page-summary-parcel-state.md`
- `software/inference-engine/architecture.md`
- `docs/data-model/parcel-state-schema.md`
- `repo/rhi/inference/infer_parcel_state.py`
- `docs/system-overview/neighborhood-signal-transformation-overview.md`
- `repo/rhi/shared_map/aggregate_shared_map.py`

## What looks potentially inventive

### Candidate A: parcel-state generation

The strongest narrow candidate in the existing filing drafts is the parcel-state generation method:

- combine local observations, parcel context, and optional public context
- emit parcel-level status outputs
- include confidence, freshness, reasons, and evidence mode
- degrade to `unknown` when evidence is weak

Why it may matter:

- it is a real method, not just a dashboard
- it tries to preserve source distinctions and uncertainty
- it is framed as useful under partial adoption

Why it does not currently look like a must-file candidate:

- the implemented v1 logic is mostly threshold/config/rule based
- the current code reads as a clean reference heuristic system, not an obviously unique technical breakthrough
- the repo itself repeatedly treats this as a possible narrow filing, not an already compelling one

### Candidate B: neighborhood signal transformation

The more distinctive concept in the repo is the transformation of private parcel signals into privacy-scoped shared neighborhood intelligence.

Why it may matter:

- the repo describes this as the neighborhood moat
- it tries to preserve household control while still producing useful shared outputs
- it may be the most differentiated part of the long-term system

Why it is still weak as an immediate patent target:

- the strongest public differentiation still lives more in architecture than in one sharply bounded claimed method
- the current implementation is only a partial aggregation path
- the strongest details are still emerging and not yet expressed as one clear claim-sized method

## What does not look like a strong patent target

The following look important, but not especially patent-driven on their own:

- generic sensor hardware choices
- packet validation and normalization
- ordinary API structure
- status labels and explanation payload structure by themselves
- governance, privacy, contribution, and rights-control surfaces

These feel more like product design, trust architecture, and open-system discipline than core exclusion assets.

## Option review

### Option 1: Patent

What this means:

- prepare a narrow U.S. provisional now
- continue withholding enabling details until filing
- decide later whether to continue prosecution or open-release after filing

Pros:

- preserves a short window of exclusion leverage
- may feel safer if the project wants optional commercial control later
- may help if the neighborhood-transformation method becomes a genuine moat

Cons:

- costs money and attention now
- requires sharper inventorship, applicant, and disclosure sequencing work
- feels somewhat misaligned with the repo's commons-protective posture
- the current implemented v1 does not obviously justify the spend

Best fit if:

- the project wants the right to stop others from using one narrow method
- that method can be stated clearly in one claim-sized sentence
- the team is willing to keep some technical details held back a bit longer

### Option 2: Defensive publication

What this means:

- publish the technical method clearly enough to function as prior art
- stop preserving the patent-first sequencing window
- rely on open licenses and public disclosure instead of exclusion

Pros:

- fits the repo's current commons-oriented direction
- reduces ambiguity about what is intentionally being opened
- avoids paying for a weak or uncertain provisional
- directly supports the goal of making the work harder to enclosure-capture

Cons:

- gives up the main value of filing first
- requires a real technical disclosure, not just high-level architecture
- may require revising current release-control docs

Best fit if:

- the project cares more about keeping the method in the commons than about exclusivity
- the team is comfortable publishing the key logic clearly
- the goal is "open and hard to privatize," not "reserve leverage first"

### Option 3: Open now

What this means:

- publish code, docs, and data under clear open terms now
- stop treating the April release as patent-sequencing sensitive

Pros:

- fastest path
- best fit if openness is the real goal
- avoids spending time on patent logistics

Cons:

- if done without a deliberate defensive-publication step, it may still be less clean than an intentional prior-art package
- does not by itself answer how to handle real parcel-linked v1 data
- requires immediate policy updates if the project truly wants public v1 data rather than private-by-default data

Best fit if:

- the project no longer wants to preserve any patent option
- the team is prepared to update the data and release policies now

## Comparison

| Option | Cost now | Preserves exclusion | Fits commons goals | Fits current v1 maturity | Recommended |
| --- | --- | --- | --- | --- | --- |
| Patent | medium to high | yes | only partially | weak to moderate | no |
| Defensive publication | low to medium | no | yes | strong | yes |
| Open now | low | no | yes | strong, but policy work needed | yes, if paired with clear publication and licensing |

## Recommendation

Choose Option 2 as the main IP strategy:

- deliberate defensive publication

Operationally, that likely means:

- open the code, documentation, schemas, and non-sensitive technical logic
- publish the important method details clearly enough to count as a real technical disclosure
- rely on open licenses, timestamps, public mirrors, and broad publication instead of a provisional filing

If the team wants the fastest practical framing, it can be described as:

- "open now, using defensive publication rather than patenting"

## Why this is the recommendation

1. The current v1 does not look like a case where a patent is obviously required.
2. The current reference implementation looks more like a credible open reference system than a sharply bounded patent asset.
3. The project's written goals repeatedly prioritize commons protection and later broad open release over long-term exclusion.
3. The project's written goals repeatedly prioritize commons protection and broad open release over long-term exclusion.
4. The most distinctive future method appears to be the neighborhood-transformation layer, but that layer is still early enough that filing now looks premature unless the project strongly wants exclusion.

## Trigger to revisit a patent later

Revisit a narrow provisional only if all of these become true:

- the team can name one concrete method in one sentence
- that method is central to the project's real moat
- the team actually wants temporary exclusion rights
- the implemented details are specific enough to support a real filing

If any of those remain false, stay with open publication.

## Immediate next steps if this memo is accepted

1. Keep the repo aligned with the current open-publication posture.
2. Complete `legal/defensive-publication/core-system-spec.md` so it functions as a real technical disclosure.
3. Publish the code and non-sensitive technical materials under the intended open licenses.
4. Make a separate, explicit decision on whether v1 data includes any real parcel-linked or household-identifiable data, because future participant data is still not open by default.

## Data note

This memo is only about patent strategy.

It does not conclude that all v1 data should be public without qualification.

If the project wants to publish all v1 data, it must make an explicit policy decision that supersedes the current private-by-default dataset posture and choose a real open-data license for the dataset release.
