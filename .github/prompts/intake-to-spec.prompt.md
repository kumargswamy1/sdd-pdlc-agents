---
description: "Consolidate existing requirement docs and generate a technical spec."
---

# Intake To Spec Workflow

Use this prompt when the user provides a source requirement folder and project name.

Arguments expected from the user:
- Source folder, for example `requirement/legacy/`
- Project name, for example `MyApp_v1`
- Optional GitHub issue URL or number

Run this workflow:

1. Act as `Requirement Intake Consolidator`.
2. Read all source Markdown documents in the source folder.
3. Generate:
   - `requirement/Context_{ProjectName}.md`
   - `requirement/BRD_{ProjectName}.md`
   - `requirement/{ProjectName}_Requirements.md`
   - `requirement/Intake_Gap_Report_{ProjectName}.md`
   - `requirement/Traceability_Matrix.md`
4. Stop if Critical gaps block specification.
5. Act as `Traceability Manager` and validate `requirement/Traceability_Matrix.md`.
6. Act as `Technical Specifier` and generate `output/{RUN_ID}/specify/spec.md`.
7. Act as `Compliance Reviewer` and review the generated spec.
8. Report generated files, Run ID, Critical/High gaps, and whether the spec is ready for planning.

Follow `.github/copilot-instructions.md`.
