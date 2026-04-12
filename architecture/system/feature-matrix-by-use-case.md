# Feature Matrix by Use Case

## Purpose

Map major use cases to likely sensors, core outputs, likely deployment scale, and major technical or product constraints.

## Reading guide

- `home-first` means the use case is valuable to one household without network participation
- `network-amplified` means nearby participation materially improves usefulness
- `block-native` means the use case becomes much more compelling at shared block scale
- `city-federated` means the use case benefits from aggregation across many neighborhoods

## Matrix

| Use case | Primary scale | Likely sensors and context | Core outputs | Product strength | Main constraints |
| --- | --- | --- | --- | --- | --- |
| Wildfire smoke | home-first, network-amplified | PM, temperature, humidity, wind, public smoke context, home envelope context | indoor and outdoor smoke burden, ventilation guidance, shelter readiness, plume trend | very strong | low-cost sensor calibration, indoor/outdoor placement quality |
| Urban wildfire readiness | network-amplified, block-native | smoke, heat, wind, public fire perimeter context, parcel vulnerability context | readiness degradation, route risk, directional worsening, asset-risk posture | moderate to strong | irregular ember-driven spread, cannot claim exact flame front |
| Flooding and runoff | home-first, block-native | rain, water level, low-point sensors, parcel slope, drainage context | low-point flooding, route passability, intrusion risk, trouble-spot alerts | very strong | placement matters, block geometry strongly affects truth |
| Extreme heat | home-first, network-amplified | indoor and outdoor temperature, humidity, shade and exposure context, outage context | heat burden, overnight recovery failure, room or parcel shelter stress | very strong | indoor and outdoor representativeness must stay explicit |
| Freeze and winter storm | home-first, network-amplified | temperature, humidity, pipe temp, outage context, route context | freeze risk, cold burden, pipe protection guidance, icing risk | strong | some effects are inside-wall or structure-specific |
| Windstorm | network-amplified | wind, pressure, outage context, tree and street context | gust exposure, debris risk, route degradation, local corridor stress | moderate | many outcomes are indirect or inferred |
| Landslide and debris flow | home-first in the right terrain, network-amplified | soil moisture, rainfall, tilt, runoff, terrain and slope context | slope instability risk, route avoidance, low-confidence early warning | moderate | terrain-specific, high false-confidence risk if under-instrumented |
| Drought and chronic dryness | home-first, city-federated | soil moisture, rainfall, vegetation context, heat | vegetation stress, watering guidance, chronic dryness trends | moderate | slower-moving, less urgent for many users |
| Indoor air health | home-first | PM, CO2, VOC proxies, humidity, occupancy context | ventilation windows, filtration effectiveness, indoor burden | very strong | interpretation must avoid medical overclaiming |
| Water intrusion and leaks | home-first | leak sensors, sump state, humidity, temperature | leak detection, mold-promoting conditions, urgent check prompts | very strong | often requires dedicated hardware beyond climate sensors |
| Backup power and utility resilience | home-first, network-amplified | line voltage status, battery state, connectivity, indoor temp | outage readiness, backup runtime posture, load-shed prompts | strong | utility integrations and hardware diversity |
| Route readiness | block-native | flood, smoke, wind, outage, public closures, neighborhood signals | route degradation, safer local paths, egress confidence | strong | requires careful claims discipline and context freshness |
| Elder-care resilience | home-first | heat, air, outage, caregiver context | caregiver alerts, elevated risk prompts, simplified readiness | strong | privacy, accessibility, and medical-adjacent caution |
| Disability and mobility support | home-first, block-native | route context, outage context, elevator/building context, weather | accessibility degradation, route readiness, shelter stress | moderate to strong | requires better accessibility-specific modeling |
| Mutual aid coordination | block-native | derived readiness states, voluntary flags, incident context | block check-ins, support prioritization, shared alerts | strong | social and governance design matter as much as tech |
| Environmental justice evidence | city-federated | chronic air, heat, runoff, outage patterns, burden overlays | resident-owned evidence, burden maps, adaptation support | strong | governance, policy, and sustained participation |
| Insurance and property evidence | home-first | time-stamped household conditions and history | event history, recurring issue evidence, hardening priorities | moderate | legal review, evidence quality, downstream acceptance |
| Recovery and reentry | home-first, network-amplified | smoke, moisture, heat, outage recovery, neighborhood normalization | habitability trend, reentry posture, secondary-risk prompts | strong | high need for conservative claims language |
| Multi-unit building resilience | block-native | unit sensors, shared-system context, power, air, heat | building readiness, floor-level conditions, shared-system failures | strong long-term | different governance and installation model |
| Resilience hubs | neighborhood, city-federated | hub sensors, occupancy context, power, air, water, cooling | hub readiness, community refuge status, operating constraints | strong long-term | institutional workflows and liability |
| Chronic neighborhood livability | block-native, city-federated | air, heat, noise, pollution context, traffic context | daily quality-of-life map, walking and play windows, chronic burden trends | strong | risk of scope creep beyond core resilience mission |

## Recommended phase-1 feature cluster

These use cases have the best mix of parcel operator value, technical feasibility, and long-term network upside:

- wildfire smoke
- indoor air health
- extreme heat
- flooding and runoff
- outage readiness
- recovery and reentry

## Recommended phase-2 block cluster

These use cases best demonstrate why neighborhood participation matters:

- smoke plume movement
- runoff trouble spots
- route readiness
- outage clustering
- mutual aid coordination
- chronic environmental burden mapping

## Recommended phase-3 expansion cluster

- multi-unit buildings
- resilience hubs
- environmental justice evidence
- neighborhood planning and adaptation support

## Major watchouts

- do not promise exact disaster-front tracking where only indirect evidence exists
- keep indoor versus outdoor representativeness explicit
- avoid drifting into generalized surveillance
- treat recommendation language and safety language as a product surface, not only a legal surface
