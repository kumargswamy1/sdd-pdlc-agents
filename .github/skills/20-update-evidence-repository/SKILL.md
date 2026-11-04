---
name: 20-update-evidence-repository
description: Checks that every pain point, need, job and principle an output cites matches its master register, and lists items that are missing, renamed or copied. Use when a register or a citing output changes. Not for logging or tagging evidence, use 05-organise-the-evidence.
allowed-tools: Read Grep Glob Write Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/check_citations.py *)
---

# 20. Update evidence repository

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 20, CAP-20 Update evidence repository |
| Phase or scope | Cross cutting. Applies to every output that cites a register |
| Work nature mix | Mechanical 1; Judgment 1 (rows in the to-be breakdown). This skill splits the Mechanical row into 5 observable steps and keeps 1 Judgment step |
| Authority level | Checks. It reports. It never edits a register or an output |
| Handoffs in | None. Internal. Run it before any handoff that carries registers or outputs that cite them |
| Handoffs out | None. The consistency report is internal |
| Human gate after | Researcher spot-checks the findings, then the register owner decides which version stands and corrects the source. Approver role: register owner |
| Used by | AG-02 Evidence and insight agent. Information only |
| Version and date | 0.1, 2026-10-12, draft |

## 2. Purpose

Keeps one source for each shared list. When an output repeats, renames or invents an item, the check finds it before the next stage builds on it. It enables the decision about which version of an item stands.

## 3. When to use

Use after a register changes, after any output that cites a register changes, and before a handoff that carries registers or outputs citing them.

Not for: logging, tagging or numbering evidence. Use 05-organise-the-evidence. Not for building the registers, which 05-organise-the-evidence and 06-draw-out-insights-and-needs do. A checker never builds the entries it checks.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Pain point register: registers/pain-point-register.md | None. Internal | Required | Stop and ask |
| User need register: registers/user-need-register.md | None. Internal | Required | Stop and ask |
| Register of experience principles. File name: To verify | None. Internal | Optional | Proceed and list the principles as not checked |
| Outputs that cite registers: folders named in the local config file (personas, empathy maps, jobs matrix, journey blueprints, experience principles) | None. Internal | Required | Stop and ask |
| Local config file: .github/templates/local-config.md (ID prefixes to check, folders to scan, register owner roles, how often to run) | None | Required | Stop and ask |
| Template: templates/consistency-report-template.md | None | Required | Stop and ask |

## 5. Method

1. **Mechanical.** List the registers and the outputs to check, by file name and version. Take the folders and ID prefixes from the local config file. Note any register with no named owner.
2. **Mechanical.** Run `python3 ${CLAUDE_SKILL_DIR}/scripts/check_citations.py --registers <register files> --outputs <folder> --prefixes <prefixes>`. Keep the full output. The script reports four kinds of finding: MISSING (an output cites an ID that no register holds), RENAMED (an output shows an ID with different wording), COPIED (an output repeats a register item's text without its ID) and UNCITED (a register item no output cites). Evidence tag: Evidence.
3. **Mechanical.** Read what the script cannot check. Search the outputs for pain points, needs, jobs and principles named in words with no ID, and for an ID cited alone whose wording you can compare with the register. List each as Other, with file and line.
4. **Mechanical.** Write the consistency report from the template. Sort findings by severity: Critical for MISSING, Warning for RENAMED, COPIED and Other, Info for UNCITED. List what was not checked.
5. **Judgment.** Propose which version stands for each finding. Options to produce: keep the register wording, take the output's wording, merge the two, or add the item to the register (for MISSING). Criteria: which wording the evidence log items support, which version was approved last, whether the register owner has changed it on purpose. The register owner decides, and the owner corrects the source. This skill never corrects a source.
6. **Mechanical.** After the owner reports corrections, run steps 1 to 4 again. Mark each finding that no longer appears as closed. Report a finding that appears in three runs in a row as a structural gap, and escalate it to the register owner.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Consistency report | None. Internal | Markdown | reports/ | consistency-report-<YYYY-MM-DD>.md |
| Corrected sources | None. Made by the register owner, not by this skill | The corrected files | Their own folders | Unchanged file names, new versions |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: which files to scan from the local config file, how to sort findings, how to word a finding.
- Must not decide: which version stands, a change to a register or an output, whether a finding is acceptable, or whether a register owner is right. Must not edit any source.
- Escalate when: a register has no owner, the same finding appears in three runs in a row, an ID appears twice in the registers, a register cannot be read, or no output folder exists.
- Approver role: register owner. Name left blank.

## 8. Quality checks

- [ ] Test 1, Cold start: registers and outputs named by file name and version.
- [ ] Test 3, Traceable: every finding names a file, a line and an ID.
- [ ] Test 4, Single source: every COPIED finding is resolved by citing the register ID.
- [ ] Test 7, Honest about gaps: wording the script cannot compare, and outputs not checked, are listed.
- [ ] Test 8, Versioned and dated: report dated, with register versions listed.
- [ ] Test 10, Checkable: reviewer can tick the checklist in the handoff template.
- [ ] No source file was edited by this skill.
- [ ] Every finding has a proposal and a decision column, and the decision is blank until a person fills it.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Nobody knows how often to check or who owns the registers | Breakdown gap note on G3: "How often does the check run, and who owns the registers it checks against?" | Step 1 reads the schedule and owner roles from the local config file and flags a register with no owner. The frequency is To verify |
| Each output keeps its own pain point list | Breakdown gap note on N5: "Do personas, empathy maps, the blueprint and the jobs matrix cite the register by ID, or does each keep its own pain point list?" | The script finds COPIED text. Step 5 proposes citing the ID |
| Pains drift apart between outputs | Breakdown gap note on E4: "Do these pains feed the same pain point list used by personas and the journey blueprint?" | Steps 2 and 3 compare every output with the register |
| A reworded item the script cannot find | Hypothesis from how the script works: it compares wording only where an ID is followed by its text | Step 3 reads the rest and lists it as Other |
| The checker silently fixes the source | Hypothesis from the roster design check | Authority section: the skill reports and never edits |
| The same finding returns every run | Existing design-lint rule: findings that persist across three or more runs signal a structural gap | Step 6 escalates |

## 10. Principles applied

- Prioritise human control: the skill reports and a person decides, so no source changes without the owner.
- Build trust through visible evidence: every finding shows its file, line, ID and what was found.
- Start simple: one script, one report, one decision step.

## 11. References

- design-lint SKILL.md, read in full (198 lines). Kept: the severity classes, the written report, the rule never to auto-fix, and the escalation of findings that persist for three or more runs. Dropped: project paths, sync scripts, emoji markers, and the checks for migration status, canvas briefs and composition logs, which fall outside this capability.
- design-query SKILL.md, headings only. Not carried: its practice of filing insights back, which needs a person's confirmation and belongs to a later capability.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-20: G3, which is new in the to-be and closes an audit gap.
- Standard practice, not checked against a source: the mapping of finding kinds to severity in step 4.
- Supporting files: templates/consistency-report-template.md, scripts/check_citations.py.
