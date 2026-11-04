---
name: <skill-name, lowercase kebab-case, equals the folder name>
description: <What the skill does. Use when <trigger>. Not for <neighbouring capability>, use <neighbouring-skill-name>. 300 characters or fewer, third person.>
when_to_use: <optional extra trigger wording>
disable-model-invocation: <optional, true only if the skill has side effects>
user-invocable: <optional, false only for background knowledge>
allowed-tools: <optional, the minimum tools needed>
model: <optional, only if the capability needs an override>
effort: <optional, only if the capability needs an override>
---

# <Skill no.>. <Capability name>

## 1. Skill card

| Field | Value |
|---|---|
| Skill no. and capability | <NN, CAP-NN and name. Shared skills use S1, S2> |
| Phase or scope | <stage, or cross cutting> |
| Work nature mix | <Mechanical n; Judgment n> |
| Authority level | <Does, Drafts, Prepares or Checks> |
| Handoffs in | <handoff IDs from the register, or None> |
| Handoffs out | <handoff IDs from the register, or None> |
| Human gate after | <what is reviewed or decided, and the approver role> |
| Used by | <agent names. Information only> |
| Version and date | <version, YYYY-MM-DD, status> |

## 2. Purpose

<Two sentences at most: what good output achieves, and the decision it enables.>

## 3. When to use

<The trigger.>

Not for: <what the neighbouring capability does>. Use <neighbouring-skill-name>.

## 4. Inputs

| Input | Source handoff ID | Required or optional | If missing |
|---|---|---|---|
| <input, named by handoff ID and file name> | <ID or None> | <Required or Optional> | <Stop and ask, or proceed and mark To verify> |
| Local config file: .github/templates/local-config.md | None | Required | Stop and ask |

## 5. Method

1. **<Mechanical, Judgment or Relational>.** <Observable step. Name inputs and outputs by handoff ID and file name.>
2. **Judgment.** <Step.> Options to produce: <list>. Criteria: <list>. A person decides.
3. **Relational.** Prepare for the human: <material>. Do not hold the conversation.

## 6. Outputs

| Output | Handoff ID | Format | Location | File name |
|---|---|---|---|---|
| <output> | <ID or None> | <format> | <folder> | <file name> |

Every output follows the handoff standard, carries an evidence table and has status draft.

## 7. Authority and gates

- May decide: <list>
- Must not decide: <list>
- Escalate when: <list>
- Approver role: <role. Person's name left blank>

## 8. Quality checks

- [ ] <Handoff test that applies, by number and name>
- [ ] <Check specific to this capability>

## 9. Failure modes

| Failure mode | Source | What the skill does about it |
|---|---|---|
| <way this goes wrong> | <audit gap note, or hypothesis> | <step or rule that guards against it> |

## 10. Principles applied

- <Principle>: <what it requires in this skill>

## 11. References

- <Source actually read, with how much was read, or "Standard practice, not checked against a source">
- <Link to a supporting file>
