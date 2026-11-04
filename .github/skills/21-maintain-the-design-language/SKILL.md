---
name: 21-maintain-the-design-language
description: Prepares who owns the design language system after launch and how changes are requested and approved, then versions and dates each release and keeps the current-version file true. Use when the system is released or a change is requested. Not for building it, use 16-define-the-design-language.
allowed-tools: Read Grep Glob Write
---

# 21. Maintain the design language

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | 21, CAP-21 Maintain the design language |
| Phase or scope | Design |
| Work nature mix | Mechanical 1; Judgment 2 (rows in the to-be breakdown). This skill has 4 Mechanical steps and 2 Judgment steps, because it adds a guard step, a drift check and a final write step |
| Authority level | Prepares. People decide the owner, the change rules and each release. The skill drafts, versions and checks |
| Handoffs in | None. Inputs come from other skills and change requests and are internal |
| Handoffs out | H13, H14 |
| Human gate after | A person decides the owner and the change rules and approves each release. A reviewer checks the drift list. Approver role: design lead |
| Used by | AG-03 Experience agent. Information only |
| Version and date | 0.1, 2026-10-13, draft |

## 2. Purpose

Keeps the design language system current and owned, so every step knows which version it uses and who may change it. It enables the decision to release a change and the decision to say no to one.

## 3. When to use

Use when the design language system is first released, when a change to it is requested, and when a downstream step reports a gap.

Not for: building or extending the system. Use 16-define-the-design-language. Not for checking screens against it, use 17-check-designs-against-principles-and-standards. Not for recording why a change was made, use 22-record-decisions-and-rationale.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| Design language system, final, with its DTCG token files: language/ and tokens/ | None. Internal, from 16-define-the-design-language | Required | Stop and ask |
| Current versions: ia-and-dls-current-version.md | None | Required | Stop and ask |
| Change requests, with the requester role and the screen or step affected | None. People and 12-design-the-detailed-screens (component, token and pattern requests) | Required for steps 3 and 5 | Proceed. Version only what was approved |
| Application gaps: language/application-gaps.md | None. Internal | Optional | Proceed |
| Versions cited by concept testing and detailed design: tests/, screens/ | None. Internal | Required for step 5 | Proceed and mark each step To verify |
| Delivery team feedback | None. People | Optional | Proceed and list under Gaps |
| Local config file: local-config.md (version scheme, approver roles, review period, who may block a release) | None | Required | Stop and ask |
| Templates: templates/release-templates.md | None | Required | Stop and ask |

## 5. Method

Never mark a release approved. Only the approver does. A release changes the version file and the changelog, and nothing else.

1. **Mechanical.** Check the inputs. Confirm the design language system is final and that the current-version file lists it. List any change request, application gap or feedback item waiting for a decision. If the system was inherited from another source, list where the inherited version stands now.
2. **Judgment.** Decide who owns the system after launch. Options to produce: two or three candidate owner roles with the duties each would hold: accepting changes, reviewing breaking changes, publishing, answering questions. Criteria: capacity to keep the system current, knowledge of the principles, independence from the teams that request changes. A person decides and names the owner role. Save in maintenance/ownership.md.
3. **Judgment.** Set how changes are requested and approved. Options to produce: candidate routes for a request, with who reviews it, who approves it, how exceptions are handled, how a breaking change differs from a small one, the version scheme, and how long before a removed item disappears. Criteria: the owner can keep up, a breaking change needs a major version and migration guidance, nothing is changed without a log entry. A person decides. Save in maintenance/change-rules.md.
4. **Mechanical.** Version and date the release. Apply the version scheme from the change rules. When tokens changed, rebuild and validate the DTCG token files with the build script in 16-define-the-design-language, and record the result with the release. When the system was inherited and its source has published a new edition, run steps 3 and 4 of 16-define-the-design-language again before releasing. Write a changelog entry listing each change, its request, its effect and its version. Update ia-and-dls-current-version.md: record the new version, the date, the approver role and what changed, and move the prior row to the history table. Leave the status as draft until the approver approves. Save the entry in maintenance/changelog.md.
5. **Mechanical.** Check which version each step uses. This step is done by a person, or by a separate run whose output a person reviews, and not by the run that wrote the release. List every step or file that cites a version other than the current one, every change with no changelog entry, and every component change with no version change. Report only. Save as maintenance/drift-check.md.
6. **Mechanical.** Write the evidence table, the Gaps and open questions section and a list of what was not checked for every file. Set status draft until the design lead approves.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| Ownership decision | H13, H14 | Markdown | maintenance/ | ownership.md |
| Change rules | H13, H14 | Markdown | maintenance/ | change-rules.md |
| Design language system, final and versioned | H13, H14 | Link to the released version | language/ | the released files, with the version in the file name |
| Changelog | None. Internal | Markdown table | maintenance/ | changelog.md |
| Current-version file | H14 | Markdown | the process folder | ia-and-dls-current-version.md |
| Drift check | None. Internal | Markdown table | maintenance/ | drift-check.md |

Every output follows the handoff standard, carries an evidence table and has status draft until approved.

## 7. Authority and gates

- May decide: how to word a changelog entry, how to lay out the version file, which files to scan for versions.
- Must not decide: the owner, the change rules, whether a change is accepted, a release approval, or whether a breaking change needs migration support. Must not mark a release approved.
- Escalate when: no owner exists, a change breaks existing screens, a step cites an old version, a change has no request, or an inherited system changed upstream.
- Approver role: design lead. Name left blank.

## 8. Quality checks

- [ ] Test 3, Traceable: every changelog entry cites its request.
- [ ] Test 6, Owned and statused: owner role, approver role and status are present.
- [ ] Test 7, Honest about gaps: steps with an old version and unrecorded changes are listed.
- [ ] Test 8, Versioned and dated: every release has a version, a date and what changed.
- [ ] Test 9, Findable and readable: the current-version file names the latest version in one place.
- [ ] The prior row moved to the history table, not deleted.
- [ ] The drift check was done by a person or a reviewed separate run.
- [ ] No release was marked approved by the skill.

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| Nobody owns the system after launch | Breakdown gap note on D1: "Is the design language system built here or inherited? If inherited, where does the team depart from it and who approves that?" | Step 2 names an owner role, and step 1 checks where an inherited system stands |
| Steps use different versions and nobody owns changes | Breakdown gap note on D6: "Who owns changes after release? Steps 6 and 7 both use it, so which version does each use?" | Steps 3 to 5 set the rules, version the release and list which version each step cites |
| Silent changes | Rule in Ch 12 design-governance: every component change is logged, with no silent updates | Step 4 writes a changelog entry for every change, and step 5 finds changes without one |
| Breaking changes without migration help | Rule in Ch 12 design-governance: breaking changes need a major version and migration guidance | Step 3 requires it in the change rules |
| Upkeep after release is not in the as-is process | Hypothesis from the as-is audit: no step covers upkeep | This skill is the only place it lives. A review period is To verify |
| The agent approves its own release | Roster design check | The authority section and step 4 |

## 10. Principles applied

- Prioritise human control: people decide the owner, the rules and each release, and the skill never approves one.
- Build trust through visible evidence: each change cites its request, its version and its date.
- Prevent errors: the version file moves the prior row to history, so no version is lost.

## 11. References

- Ch 12 design-governance SKILL.md, Phase A and the rules read (308 lines): versioning, contribution guide, deprecation policy, changelog, naming authority, approval roles, the rule that every change is logged and that breaking changes need a major version and migration guidance. Kept: the changelog, the version rule and the deprecation timeline. Dropped: Phase B principle synthesis, which belongs to the owner of the design language, and project paths.
- NN/g "Design-System Maturity", read about 70 percent: governance covers who decides whether a component is added, who reviews a breaking change, versioning and how exceptions are handled.
- NN/g "Design Systems vs. Style Guides", read about 60 to 70 percent: a design system needs ongoing maintenance and oversight.
- NN/g "Design Systems 101", read about 70 percent: a system is not a one and done solution and needs a team to keep it current.
- As-is and to-be breakdown workbooks, read in full. To-be rows tagged CAP-21: D1 (step 2) and D6 (steps 3 and 4).
- Standard practice, not checked against a source: the options and criteria in steps 2 and 3, and the use of major, minor and patch versions.
- Supporting file: templates/release-templates.md.
