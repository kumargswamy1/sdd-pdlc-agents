# User Story Template

## Jira Issue Metadata

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| **Issue Type**     | Story                                              |
| **Project**        | `<PROJECT-KEY>`                                    |
| **Summary**        | `<Feature Area> — <Short Capability Description>`  |
| **Priority**       | `High` / `Medium` / `Low`                          |
| **Labels**         | `backlog` / `in-progress` / `done`                 |
| **Epic Link**      | `<PROJECT-KEY>-<epic-issue-number>`                |
| **Sprint**         | `Sprint <N>`                                       |
| **Story Points**   | `<number>`                                         |
| **Assignee**       | `<user email>`                                     |
| **Reporter**       | `<user email>`                                     |
| **Contributor**    | `<user email(s)>`                                  |
| **Interested Party** | `<user email(s)>`                                |
| **Component/s**    | `<component name>`                                 |
| **Fix Version/s**  | `<version>`                                        |
| **Due Date**       | `YYYY-MM-DD`                                       |
| **Planned Due Date** | `YYYY-MM-DD`                                     |
| **Target Start**   | `YYYY-MM-DD`                                       |
| **Target End**     | `YYYY-MM-DD`                                       |

---

## Description Body (Jira Wiki Markup)

> Paste the block below into the Jira Description field.
> Replace every `<placeholder>` before creating the issue.

---

### h2. User Story Statement

As a _<persona / role>_, I want to `<action>` — so that `<outcome/benefit>`.

---

### h2. Description

`<2–4 sentences describing the overall feature and what it enables for the user.>`

---

### h2. Figma Reference

`[<Figma URL>]`

**Navigation**

* **Entry Points:**
  * `<Screen A>` → Tap `"<Button Label>"` → `<navigate to route>`
  * `<Screen B>` → Tap `"<Button Label>"` → `<navigate to route>`

* **Forward / In-Screen Navigation:**
  * Tap `"<Action>"` → `<navigate to route>`
  * Tap `"<Action>"` → `<navigate to route with id>`

* **Back Navigation:**
  * Tap Back / Close → returns to `<previous screen>`

---

### h2. Business Logic

| # | Rule |
|---|------|
| 1 | `<Business rule 1>` |
| 2 | `<Business rule 2>` |
| 3 | `<Business rule 3>` |
| 4 | `<Add more rows as needed>` |

---

### h2. API

| Endpoint | Description |
|----------|-------------|
| `GET /<resource>` | `<What it returns>` |
| `POST /<resource>` | `<What it creates/initiates>` |
| `PATCH /<resource>/{id}` | `<What it updates>` |
| `DELETE /<resource>/{id}` | `<What it deletes>` |

---

### h2. Exception / Error Handling

| # | Scenario | Expected Behaviour |
|---|----------|--------------------|
| 1 | `<Error scenario 1>` | `<User-facing message or system behaviour>` |
| 2 | `<Error scenario 2>` | `<User-facing message or system behaviour>` |
| 3 | `<Error scenario 3>` | `<User-facing message or system behaviour>` |
| 4 | `<Add more rows as needed>` | |

---

### h2. Acceptance Criteria

| AC ID | Title | Given | When | Then |
|-------|-------|-------|------|------|
| AC-01 | `<AC Title>` | `<Precondition>` | `<Trigger / User action>` | `<Expected observable outcome>` |
| AC-02 | `<AC Title>` | `<Precondition>` | `<Trigger / User action>` | `<Expected observable outcome>` |
| AC-03 | `<AC Title>` | `<Precondition>` | `<Trigger / User action>` | `<Expected observable outcome>` |
| AC-04 | `<Add more rows as needed>` | | | |

---

## Authoring Guidelines

### Story Statement
- Format: **As a** _\<persona / role\>_, **I want to** `<action>` — **so that** `<benefit>`.
- Keep the action and benefit concise and user-centric.

### Description
- 2–4 sentences maximum.
- Focus on *what* the feature does for the user, not *how* it is built.

### Figma Reference
- Always include the direct Figma frame URL (include `node-id` parameter where applicable).
- List all navigation entry points and forward routes.

### Business Logic
- Numbered list of rules the system must enforce.
- Each rule should be independently testable.
- Use concrete values (amounts, counts, time periods) wherever known.

### API
- One row per endpoint.
- Use standard HTTP verbs: `GET`, `POST`, `PATCH`, `DELETE`.
- Parameterise dynamic segments with `{id}` notation.

### Exception / Error Handling
- Cover: empty states, API failures, validation errors, permission/limit errors.
- User-facing messages must be quoted exactly as they will appear in the UI.

### Acceptance Criteria
- Minimum 6–10 AC rows per story.
- Use the strict **Given / When / Then** format.
- Each AC must map directly to a Business Logic rule or a navigation path.
- AC IDs follow the pattern `AC-01`, `AC-02`, …

### Labels
- Use `backlog` for new stories not yet assigned to a sprint.
- Switch to `in-progress` when development begins.
- Switch to `done` only after the Definition of Done checklist is fully met.

---

## Worked Example Excerpt

**Summary:** `Rewards — Points Earning, Balance View & Redemption`

**User Story Statement:**
> As a _logged-in mobile app user_, I want to view my reward points balance and redeem points against eligible options — so that I can track and use the benefits I earn from the app.

**Sample AC row:**

| AC-06 | Points Redemption - Success | The user has points above the minimum threshold and selects a redemption option | The user confirms | Points are deducted and a redemption confirmation is displayed |
|-------|---|---|---|---|
