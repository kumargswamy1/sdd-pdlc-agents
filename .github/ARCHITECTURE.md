# Copilot Configuration Architecture

## Structure

```text
.github/
├── agents/
├── instructions/
├── prompts/
├── rules/
├── templates/
├── copilot-instructions.md
├── SPEC_DRIVEN_WORKFLOW.md
└── README.md
```

## Design
- Agents define who performs each PDLC role.
- Rules define how work must be done.
- Instructions apply rules to file patterns.
- Templates define canonical artifact shape.
- Prompts provide reusable workflow chains.

## Traceability
All major outputs should map:

```text
CTX -> BRD -> FR/NFR -> US -> SPEC -> TASK -> CODE -> TEST -> REVIEW -> DOC
```

## Banking Domain Scope
The configuration is generic for any software system and supports:
- Customer onboarding.
- KYC and AML.
- Risk profiling.
- Suitability.
- Portfolio view.
- Product catalogue.
- Advisory recommendations.
- Order capture.
- Statements and documents.
- Alerts and servicing.
