# Synthesis templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. Every line cites item IDs from evidence/evidence-log.md.

## Persona profile (personas/persona-<segment-slug>.md)

```
# <Segment label>

Status: draft | Version: <n> | Date: <YYYY-MM-DD>
Participants behind this segment: <participant IDs>
Evidence threshold met: <yes or no, per local-config.md>

## Role
<Generic role description. No organisation or unit names.>

## Goals
1. <goal> [<item IDs>] [<Evidence or Inference>]

## Frustrations
1. <frustration> [<item IDs>] [<Evidence or Inference>]

## Context of use
- Environment, time pressure, multitasking, data sensitivity: <each cited>

## Key behaviours
- <behaviour> [<item IDs>]

## Scenario
<One short scenario built from the items. Cite the items.>

## Representative quote
"<verbatim text copied by item ID>" (<participant ID>, <source ID>)
<Or write: No verbatim quote fits.>

## Gaps and open questions
- <list>
```

## Empathy map (empathy-maps/empathy-map-<persona-slug>.md)

```
# Empathy map: <persona label>

Status: draft | Version: <n> | Date: <YYYY-MM-DD>

## Centre
<Persona label, then two sentences: who they are and what they do. No real names.>

| Quadrant | Cluster | Entry | Item IDs | Evidence tag |
|---|---|---|---|---|
| Says | <cluster label> | <one answer: a verbatim quote, or a paraphrase with no quotation marks> | <IDs> | Evidence |
| Does | <cluster label> | <observed action> | <IDs> | Evidence |
| Thinks | <cluster label> | <inferred thought> | <IDs> | Inference |
| Feels | <cluster label> | <inferred feeling> | <IDs> | Inference |

## What the clusters suggest the user needs
- <note, tagged Inference. Not a need statement. Feeds the need statement step>

## Blank areas
- <quadrants with no items or thin items, where the team still needs to learn more>

## Readings that differ
- <entry, the competing readings and the item IDs behind each>

## Playback
- Certain (Evidence entries): <list>
- Gaps (Inference entries and Blank areas): <list>
- Assumptions: <entries that are assumptions>
- Questions for later inquiry or validation: <list>

## Gaps and open questions
- <list>
```

## Pains, gains and contradictions (empathy-maps/pains-gains-contradictions.md)

```
| Kind | Statement | Says item IDs | Does item IDs | Register ID | Evidence tag |
|---|---|---|---|---|---|
| Pain, gain or contradiction | <statement> | <IDs> | <IDs> | <PP-NN, or Not in register> | <tag> |
```

## Need statement

One pattern for every statement. The local config file may replace the wording, never the structure.

```
<User> needs a way to <need> so that they <benefit>.
```

Write the need, not a feature. A word that names the machine, such as a screen element or an action on one, is a clue that the idea is a feature. The word list is in the local config file.

## User need register (registers/user-need-register.md)

The ID is in the first column and the need statement in the second, so 20-update-evidence-repository can check the table.

```
| ID | Need statement | User | Pain point IDs | Evidence tag | Confidence | Owner role |
|---|---|---|---|---|---|---|
| <UN-NN> | <User> needs a way to <need> so that they <benefit>. | <persona label> | <PP-NN, PP-NN> | <tag> | <High, Medium or Low, with one phrase why. Blank until a person confirms> | <role, blank until named> |

## New questions
- <questions the work raised, for the Gaps and open questions section>
```

## Job statement

Default pattern. The local config file may replace it.

```
When <situation>, I want to <motivation>, so I can <outcome wanted>.
```

## Jobs-to-be-done matrix (jobs/jobs-to-be-done-matrix.md)

```
| Job ID | Job statement | Level | Type | Persona | Importance | How well served today | Evidence strength | Item IDs |
|---|---|---|---|---|---|---|---|---|
| <JB-NN> | <statement> | Main or supporting | Functional, emotional or social | <persona label> | <per scale in local-config.md> | <per scale> | <participants behind it> | <IDs> |
```
