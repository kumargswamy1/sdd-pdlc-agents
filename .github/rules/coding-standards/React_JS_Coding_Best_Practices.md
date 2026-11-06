# React.js Coding Best Practices

## 1. Components
- Prefer functional components and Hooks for new development.
- Keep components small, cohesive, and focused on one responsibility.
- Extract reusable UI, behavior, and utilities instead of duplicating logic.
- Generally keep one primary component per file.
- Use fragments instead of unnecessary wrapper elements.
- Give files and components descriptive `PascalCase` names.

## 2. Props and State
- Treat state as immutable and update it through the appropriate setter.
- Do not duplicate props into state unless a synchronization requirement is explicit.
- Keep state as local as possible and lift it only when multiple components must coordinate.
- Derive computed values instead of storing redundant state.
- Destructure props when it improves readability.
- Use TypeScript types or runtime prop validation according to project standards.

## 3. Hooks
- Call Hooks only at the top level of React functions.
- Call Hooks only from React components or custom Hooks.
- Declare complete dependency arrays for effects and memoization Hooks.
- Use effects only for synchronization with external systems, not for ordinary calculations.
- Extract reusable behavior into clearly named custom Hooks.
- Clean up subscriptions, timers, and requests when components unmount or dependencies change.

## 4. Rendering
- Use stable, domain-specific keys for list items. Do not use array indexes when ordering can change.
- Keep conditional rendering simple. Extract large conditional branches into components or helpers.
- Use `map()` for list rendering and handle empty, loading, error, and success states explicitly.
- Avoid expensive work during rendering. Memoize only after measuring a real issue.
- Resolve all React and browser console warnings before requesting review.

## 5. Styling and Accessibility
- Follow the project's approved styling approach and design system.
- Avoid repeated inline styles. Extract reusable styles when multiple properties are involved.
- Use semantic HTML before adding ARIA.
- Ensure keyboard access, visible focus, accessible names, sufficient contrast, and logical heading order.
- Associate form labels and error messages with controls.
- Test keyboard navigation, localization, and at least one language pack where applicable.
- Give reusable controls unique and configurable identifiers only when identifiers are required.

## 6. Imports and File Organization
Recommended import order:
1. React and framework imports
2. Third-party libraries
3. Absolute project imports
4. Relative imports
5. Styles and assets

Additional rules:
- Use folder-level export files only when they improve clarity and do not introduce circular dependencies.
- Keep shared components, hooks, constants, and utilities in clearly named locations.
- Avoid default-exporting anonymous functions.
- Keep components and support files reasonably sized.

## 7. Code Quality
- Use ESLint and Prettier, or the repository's approved alternatives.
- Favor descriptive names over excessive explanatory comments.
- Remove debugging statements, deprecated APIs, dead code, and unused dependencies.
- Do not spread arbitrary props onto DOM elements unless the allowed attributes are controlled.
- Avoid deeply nested JSX and large components.

## 8. Data Access and Errors
- Centralize service calls and API-client behavior.
- Handle loading, empty, error, timeout, cancellation, and retry states.
- Cancel or ignore stale requests to prevent race conditions.
- Validate data received from external boundaries.
- Use error boundaries for unexpected rendering failures where appropriate.
- Never expose tokens, secrets, stack traces, or sensitive server details to the client.

## 9. Security
- Do not render untrusted HTML. Avoid `dangerouslySetInnerHTML`; if unavoidable, sanitize content with an approved library.
- Rely on framework escaping and encode content for the correct output context.
- Protect state-changing requests using the application's CSRF strategy.
- Do not store long-lived sensitive tokens in browser-accessible storage without an approved design.
- Validate authorization on the server. Client-side route guards are not a security boundary.
- Keep dependencies updated and scan for vulnerable packages.

## 10. Testing
- Test behavior from the user's perspective.
- Cover component states, interactions, forms, accessibility, and error conditions.
- Mock network boundaries rather than implementation details.
- Add end-to-end tests for critical user journeys.
- Avoid brittle snapshots as the only validation of meaningful behavior.

## Review Checklist
- Component and Hook responsibilities are clear.
- State is minimal and immutable.
- Hook dependencies and cleanups are correct.
- Lists use stable keys.
- Accessibility and localization are validated.
- Console warnings, lint issues, and formatting errors are resolved.
- Untrusted data is never injected directly into the DOM.

---
Source basis: `Coding_Standard_V1.0.docx`, React.Js section, supplemented by the document's general and secure coding guidance.
