# Results templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard.

## Data file for task or feature outcomes (tests/task-results.csv)

One row per participant per task or feature. Participants appear by ID only.

```
group,participant,level
<task or feature>,<participant ID>,<level from the test plan>
```

Levels for a usability task: success, success with issues, failure. Levels for concept acceptance: accepted, changed, not accepted. The test plan defines each level before the sessions.

## Data file for SUS (tests/sus-responses.csv)

One row per participant. Each answer is a whole number from 1 to 5.

```
participant,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10
<participant ID>,<1 to 5>,<1 to 5>,<1 to 5>,<1 to 5>,<1 to 5>,<1 to 5>,<1 to 5>,<1 to 5>,<1 to 5>,<1 to 5>
```

## Concept test analysis (analysis/concept-test-analysis.md)

```
# Concept test analysis: <round>

Status: draft | Version: <n> | Date: <YYYY-MM-DD>
Test plan used: <file name and version>. Dated before the sessions: <yes or no>

## Criteria compared with results
| Criterion | Result from rate_levels.py | Met, not met or not comparable |
|---|---|---|

## Acceptance by feature
<Paste the rate_levels.py table.>

## Patterns and surprises proposed for a person to decide
| Proposal | Participants | Item IDs | Options | Criteria used |
|---|---|---|---|---|

## Assumptions proposed for a person to decide
| Assumption ID | Proposed status (confirmed, rejected, still open) | Item IDs | Criteria used |
|---|---|---|---|

## Gaps found
- <list>

## Outputs affected by rejected assumptions
- <file name and item ID, for 20-update-evidence-repository>

## Gaps and open questions
- <list>
```

## Usability findings (analysis/usability-findings.md)

Finding IDs follow the RF-NNN convention of the existing research skill. IDs are stable and never reused. A retired finding keeps its ID and is marked [RETIRED].

```
| Finding ID | Finding | Root cause or symptom | Frequency | Impact | Persistence | Severity 0 to 4 | Item IDs | Second rater agrees |
|---|---|---|---|---|---|---|---|---|
| <RF-NNN> | <specific, observable> | <root cause or symptom> | <n of n participants> | <description> | <one-off or recurring> | <proposed> | <IDs> | <yes, no or blank> |
```

## Usability benchmark (analysis/usability-benchmark.md)

```
# Usability benchmark: <round>

Status: draft | Version: <n> | Date: <YYYY-MM-DD>

| Field | Value |
|---|---|
| Measures | <success rate, SUS, other> |
| Method | <moderated or unmoderated, task set, version of prototype> |
| Participants | <n, recruitment criteria, segment> |
| Conditions | <where, device, date> |
| Earlier round compared | <file name, or none> |
| Target compared | <source of target, or none> |
| Method matches earlier round | <yes or no, and what differs> |

## Results
<Paste the rate_levels.py and score_sus.py output.>

## Comparison
| Measure | This round | Earlier round | Target | Difference |
|---|---|---|---|---|

## Gaps and open questions
- <list>
```

## Pass criteria comparison (analysis/pass-criteria-comparison.md)

```
| Criterion | Pass criterion (source file, version) | Result | Met or not met |
|---|---|---|---|
```

A comparison states met or not met. It never states what to do. A person decides.

## Ranked findings (analysis/ranked-findings.md)

```
| Finding ID | Type (fix, wishlist or defer) | Severity | Reach | Effort | Rank | Item IDs |
|---|---|---|---|---|---|---|
```

All types go into one backlog, with the type kept as a column. The backlog is assembled by 14-share-and-align-with-stakeholders.
