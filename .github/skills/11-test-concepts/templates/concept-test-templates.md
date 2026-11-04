# Concept test templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. Participants appear by ID only. Names and contact details live in one restricted file named in the local config file.

## Test scope and hypotheses (tests/test-scope.md)

```
| Assumption ID | Risk | Features that carry it | Hypothesis | Result that would confirm it | Result that would reject it | Decided by (role) | Date |
|---|---|---|---|---|---|---|---|
| <AS-NN> | <High, Medium or Low> | <FT-NN> | <hypothesis> | <result> | <result> | <role> | <YYYY-MM-DD> |

Written before the first session: <yes or no>
```

## Test plan (tests/test-plan.md)

```
# Concept test plan: <round>

Status: draft until signed | Version: <n> | Date: <YYYY-MM-DD>
Signer role: <role, blank until signed> | Signed on: <YYYY-MM-DD, blank until signed>
Dated before first session: <yes or no>

## Goals
<List.>

## Success criteria
Outcome levels: <for example accepted, changed, not accepted>
| Feature ID | Threshold for accepted | Source of the threshold |
|---|---|---|

## Participants
| Group | Matches persona | How many | Inclusion | Exclusion |
|---|---|---|---|---|

## Method, tasks and questions
| Task or scenario (in the user's words) | Hypothesis or assumption ID | Questions |
|---|---|---|

## Keeping reactions on the concept
| Item | Decision |
|---|---|
| What the participant is told at the start (a concept with simulated content, the idea is tested) | <wording> |
| Order of questions (task and idea before the look) | <order> |
| Tag for comments on appearance, kept apart from concept reactions | appearance |

## Roles in the session
| Role | Held by (role) | Rule for intervening |
|---|---|---|
| Facilitator | | |
| Observer | | |
```

## Concept proposals and alignment (tests/concept-proposals.md)

The ID is in the first column and the idea in the second.

```
| ID | Concept idea (plain words) | Feature IDs | User need or pain point IDs | Hypothesis it tests | What a participant must be able to do | Evidence tag | Decision (approve, revise, hold or drop) | Decided by (role) | Date |
|---|---|---|---|---|---|---|---|---|---|
| <CN-NN> | <idea> | <FT-NN> | <UN-NN, PP-NN> | <hypothesis> | <task> | Inference | <blank until a person decides> | <role> | <YYYY-MM-DD> |
```

## Instruction to prototype (tests/prototype-instruction.md)

Written by the person leading the work, in their own words. No prototype is made without it.

```
Given by (role): <role> | Date: <YYYY-MM-DD>
Concepts to prototype: <CN-NN list>
For each concept, what the prototype must let a participant do: <list>
Concepts held or sent back: <CN-NN list>
Test plan and success criteria signed: <yes or no, with date>
```

## Concept prototype brief for 12-design-the-detailed-screens (tests/concept-prototype-brief.md)

```
Written from the signed instruction. Starts 12-design-the-detailed-screens in concept prototype mode.
| Concept ID | Feature IDs | Principle IDs | Tasks from the test plan | Screens or flows needed | States the test needs |
|---|---|---|---|---|---|

Design system version to use: <from ia-and-dls-current-version.md>
Concept prototype returned: <link and version, blank until returned> | Date: <YYYY-MM-DD>
```

## Concept to feature map (tests/concept-feature-map.md)

```
| Concept ID | Feature ID | Version of the concept prototype | Made by | Mapped by (a person, or a separate run a person reviewed) |
|---|---|---|---|---|
| <CN-NN> | <FT-NN> | <n> | <executor> | <executor> |

Concepts with no feature: <list>
Features with no concept: <list>
Prototype screens not in an approved proposal: <list>
```

## Pilot and kit (tests/test-ready-kit.md)

```
Pilot confirmed by (role): <role> | Date and time: <YYYY-MM-DD HH:MM>
| Issue found | Where | Fix | Fixed |
|---|---|---|---|
| <unclear task or breakage> | <task or concept> | <fix> | <yes or no> |

Kit contents: <test plan, concepts, discussion guide, consent form, recording set-up>
```

## Booking preparation (shown to the person before they confirm)

```
Recipients: <participant IDs, not names>
Content: <invitation, consent form>
Timing: <dates and sessions>
Contact details held in: <restricted file, not shown here>
Confirm: <blank until a person confirms>
```

## Participants and schedule (tests/participants-and-schedule.md)

```
| Participant ID | Group | Matches persona | Session date and time | Status |
|---|---|---|---|---|
| <P-NN> | <group> | <persona label> | <YYYY-MM-DD HH:MM> | <booked, completed or withdrawn> |
```
