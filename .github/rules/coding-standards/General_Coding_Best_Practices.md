# General Coding Best Practices

## Purpose
Establish consistent, maintainable, testable, secure, and production-ready coding practices across engineering teams and technology stacks.

## 1. Readability and Consistency
- Follow the repository's formatter, linter, naming, and folder-structure conventions.
- Use descriptive names for variables, functions, classes, modules, and configuration keys.
- Prefer simple, explicit code over clever or overly compressed implementations.
- Keep formatting, indentation, whitespace, and import ordering consistent.
- Comment the intent and rationale of complex logic rather than restating the code.
- Remove dead code, obsolete comments, debugging statements, and unresolved warnings.

## 2. Modular Design
- Apply separation of concerns and the Single Responsibility Principle.
- Keep functions, classes, components, and modules focused on one responsibility.
- Eliminate duplication by extracting reusable functions, components, and utilities.
- Prefer clear interfaces and dependency injection over hidden coupling and global state.
- Keep files reasonably sized and split large implementations into cohesive modules.

## 3. Error and Edge-Case Handling
- Validate inputs for structure, type, range, format, and business meaning.
- Handle null, empty, invalid, duplicate, timeout, and unavailable-dependency scenarios.
- Catch only exceptions that can be handled meaningfully.
- Preserve diagnostic context when rethrowing errors.
- Return actionable, non-sensitive error messages.
- Use assertions only for developer invariants, not as a substitute for runtime validation.

## 4. Configuration and Dependency Management
- Do not hardcode environment-specific URLs, credentials, thresholds, or feature switches.
- Store configuration in approved configuration providers or environment variables.
- Pin or constrain dependency versions and maintain lock files where supported.
- Remove unused dependencies and regularly review them for vulnerabilities.
- Keep development, test, and production configuration clearly separated.

## 5. Testing and Quality
- Add unit tests for business logic and integration tests for external boundaries.
- Test happy paths, negative scenarios, edge cases, nulls, and malformed inputs.
- Use realistic and diverse test data without exposing production-sensitive data.
- Keep tests deterministic, isolated, readable, and fast.
- Target the project-defined coverage threshold. For application middleware, the source recommends at least 80% coverage.
- Build and run applicable tests locally after synchronizing with the latest branch.
- Treat failing tests, lint errors, security findings, and build warnings according to repository quality gates.

## 6. Logging and Observability
- Use the standard logging framework instead of console or print statements in production.
- Use appropriate log levels such as DEBUG, INFO, WARNING, and ERROR.
- Log key lifecycle events, failures, dependency calls, and relevant performance metrics.
- Include correlation identifiers where available.
- Never log passwords, tokens, secrets, or unnecessary personal or sensitive data.
- Integrate application telemetry with the approved monitoring platform.

## 7. Performance and Scalability
- Choose suitable algorithms and data structures before applying low-level optimization.
- Avoid unnecessary computations, allocations, network calls, and repeated I/O.
- Profile before optimizing and document meaningful performance trade-offs.
- Cache only when justified, with clear invalidation and capacity controls.
- Use asynchronous or streaming processing for suitable I/O and large-data scenarios.
- Design stateless services where possible to support horizontal scaling.

## 8. Version Control
- Use the repository's approved branching strategy.
- Keep commits small, cohesive, and described with meaningful messages.
- Keep pull requests focused on one feature, fix, or logical change.
- Rebase or merge the latest target branch and retest before requesting approval.
- Do not commit generated artifacts, secrets, local settings, or unnecessary binaries.
- Use semantic versioning where appropriate and preserve backward compatibility intentionally.

## 9. Pull Request and Review Checklist
Before raising a pull request:
- The solution builds successfully.
- Automated tests pass and cover the change.
- The PR description explains purpose, implementation, risk, and validation performed.
- Relevant work items are linked.
- Screenshots are included for visible UI changes.
- Formatting, linting, static analysis, and security checks pass.
- Configuration, migration, compatibility, and rollback impacts are documented.
- The change contains no unrelated refactoring.

During review:
- Review the code, not the author.
- Validate correctness, maintainability, test coverage, security, and broader design impact.
- Identify blocking versus non-blocking feedback clearly.
- Respond to every comment and document deferred work.
- Require domain, database, security, or architecture reviewers when applicable.

## 10. Documentation
- Maintain a README with setup, configuration, build, test, run, and contribution steps.
- Document public APIs, modules, functions, and non-obvious architectural decisions.
- Keep environment variables and deployment assumptions documented.
- Update documentation in the same pull request as the related code change.

## 11. CI/CD Quality Gates
A typical build or deployment pipeline should include, as applicable:
1. Dependency restore
2. Formatting and linting
3. Compilation or build
4. Unit tests and coverage validation
5. Integration and performance tests
6. Static code and secret scanning
7. Dependency and container vulnerability scanning
8. Artifact publication
9. Deployment and post-deployment validation

## Definition of Done
Code is complete only when it is implemented, reviewed, tested, documented, observable, secure, backward-compatible where required, and successfully validated by the delivery pipeline.

---
Source basis: `Coding_Standard_V1.0.docx`, especially General Coding Standards, Testing and Debugging, Code Review, Version Control, Documentation, and Deployment sections.
