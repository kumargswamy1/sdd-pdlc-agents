# Check templates

Every output carries status draft, version, date, an evidence table and a Gaps and open questions section, following the handoff standard. The checker reports and never edits a screen or component.

## Check header (top of checks/check-log.md)

```
Information architecture version: <version> | Design language version: <version>
Made by: <executor or role> | Checked by: <executor or role>
Same executor made and checked: <yes or no. If yes, a person reviews the result>
Approver role: <design lead, name blank until signed>
```

## Contrast pairs file (checks/contrast-pairs.csv)

```
id,foreground,background,kind
<CT-NN>,<#RRGGBB>,<#RRGGBB>,<text, large text or ui>
```

Results come from contrast_ratio.py. Each result is a calculation and not an accessibility pass.

## Evidence trace, content and consistency (checks/trace-content-consistency.md)

```
| Finding ID | Check (trace, content or consistency) | Screen or component ID | Detail | Standard or principle ID | Severity (proposed) |
|---|---|---|---|---|---|
| <CK-NN> | <check> | <ID> | <what was found> | <ID> | <High, Medium or Low> |
```

## Principle comparison (checks/principle-comparison.md)

```
| Screen ID | Principle ID | Proposed verdict (meets, breaks or ignores) | Screen feature behind it | Principle text behind it | Verdict decided by a person | Reason |
|---|---|---|---|---|---|---|
```

## Accessibility verification (checks/accessibility-verification.md)

```
Target: <from the accessibility standard>

| Check ID | Applies to | What to look at | Verified by (role) | Result (pass, fail or not checked) | Date |
|---|---|---|---|---|---|
| <AC-NN> | <screens or components> | <focus, keyboard use, alt text, tab order> | <role, blank until verified> | <blank until a person verifies> | <YYYY-MM-DD> |
```

## Breaches and decisions (checks/check-log.md)

```
| Breach ID | Source finding IDs | Options with consequence (accept, fix or escalate) | Decision | Decided by (role) | Fix owner role | Fix logged |
|---|---|---|---|---|---|---|
| <BR-NN> | <CK-NN> | <accept: ...; fix: ...; escalate: ...> | <blank until decided> | <role> | <role> | <yes or no> |

Role that can block a design: <role, blank until named>
```
