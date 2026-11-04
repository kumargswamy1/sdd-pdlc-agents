# Backlog and decisions templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard.

## Backlog (backlog/backlog.md)

One backlog. Fixes, wishlist ideas and deferred items are kept together, with the type as a column. The ID is in the first column and the item text in the second, so 20-update-evidence-repository can check the table.

```
| ID | Item | Type | Finding ID | Severity | Rank | Evidence item IDs | Status | Owner role |
|---|---|---|---|---|---|---|---|---|
| <BL-NN> | <item text> | <fix, wishlist or defer> | <RF-NNN> | <0 to 4, from 19-analyse-test-results> | <rank, from 19-analyse-test-results> | <IDs> | <blank until a person sets it> | <role, blank until named> |
```

## Decision per issue (analysis/loop-back-decisions.md)

```
| Backlog ID | Pass criteria result | Options with consequence | Proposed action | Decision (fix now, hand to the product team or accept) | Decided by (role) | Date |
|---|---|---|---|---|---|---|
| <BL-NN> | <met or not met, from the comparison file> | <fix now: ...; hand over: ...; accept: ...> | <proposal> | <blank until a person decides> | <role> | <YYYY-MM-DD> |
```

## Design brief for rework (analysis/design-brief-for-rework.md)

```
# Design brief for rework: <round>

Status: draft | Version: <n> | Date: <YYYY-MM-DD>
Briefed by: <person role, blank until the conversation has happened>

| Backlog ID | What to change | Where the rework goes (prototype for the next sessions, or design file for development) | Reviewed before it goes live | Evidence item IDs |
|---|---|---|---|---|
| <BL-NN> | <specific change> | <place> | <yes, no or to decide> | <IDs> |

## Open question for the person
Rework made directly in the design file for development may skip the formal design review. Decide whether a review is needed: <blank until decided>.

## Gaps and open questions
- <list>
```

## Findings report (reports/usability-findings-report.md)

```
# Usability findings report: <round>

Status: draft | Version: <n> | Date: <YYYY-MM-DD>
For: <product team and detailed design, by role>

## Summary (150 words or fewer)
<What was tested, what met the pass criteria, what did not, and the decisions asked of the reader.>

## Pass criteria comparison
<Paste analysis/pass-criteria-comparison.md.>

## Benchmark
<Paste analysis/usability-benchmark.md.>

## Decisions
<Paste analysis/loop-back-decisions.md.>

## Evidence
| Item ID | Claim | Source | Evidence tag | Confidence |
|---|---|---|---|---|

## Gaps and open questions
- <list>

## Not checked
- <list>
```
