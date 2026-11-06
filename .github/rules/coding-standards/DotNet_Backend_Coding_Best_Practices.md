# .NET Backend Coding Best Practices

## 1. Architecture and Design
- Apply SOLID principles pragmatically.
- Separate API, application, domain, and infrastructure concerns.
- Use dependency injection and depend on abstractions at external boundaries.
- Prefer composition over inheritance.
- Keep controllers and endpoints thin. Move business rules into testable services or domain objects.
- Use explicit contracts for requests, responses, and integration messages.

## 2. Naming and Style
- Follow Microsoft's C# naming conventions and the repository's `.editorconfig`.
- Use `PascalCase` for public types and members, and `camelCase` for parameters and local variables.
- Prefix interfaces with `I` where that is the project convention.
- Use meaningful names and avoid unclear abbreviations.
- Enable analyzers, nullable reference types, and formatting checks where supported.

## 3. Dependency Injection
- Register services with the narrowest correct lifetime.
- Do not inject scoped services into singletons.
- Avoid the service locator anti-pattern.
- Keep constructors focused. Excessive dependencies often indicate mixed responsibilities.
- Inject typed clients and configuration abstractions rather than creating dependencies directly.

## 4. Asynchronous Programming
- Use `async` and `await` for I/O-bound operations.
- Avoid `.Result`, `.Wait()`, and blocking waits that can cause thread starvation or deadlocks.
- Propagate `CancellationToken` through request and dependency calls.
- Use `Task.WhenAll` for independent operations only when concurrency is safe and bounded.
- Do not wrap naturally synchronous CPU work in `Task.Run` inside request handling without a clear reason.

## 5. API Design
- Use consistent routes, status codes, validation responses, pagination, and error contracts.
- Version APIs intentionally and preserve backward compatibility where required.
- Validate request models and business invariants.
- Use a standardized error format such as Problem Details.
- Enforce payload size, timeout, and rate limits according to risk and operational needs.
- Generate and maintain API documentation.

## 6. Data Access
- Use parameterized queries or framework-supported query APIs.
- Avoid string concatenation for SQL commands.
- Keep transactions short and explicitly scoped.
- Choose tracking behavior intentionally in ORMs.
- Avoid N+1 queries and unbounded result sets.
- Use pagination and project only required columns.
- Manage schema changes through reviewed, backward-compatible migrations.

## 7. Exception Handling and Logging
- Use centralized exception handling middleware.
- Catch exceptions only when adding value, translating domain errors, or performing recovery.
- Preserve stack traces and original exception context.
- Use structured logging with named properties.
- Include correlation and trace identifiers.
- Do not log secrets, tokens, connection strings, or unnecessary personal data.

## 8. Performance and Caching
- Measure with profiling and telemetry before optimizing.
- Use caching for stable, frequently requested data with documented expiration and invalidation.
- Prevent cache stampedes and uncontrolled cache growth.
- Pool and reuse expensive external clients through approved factory patterns.
- Stream large payloads and avoid unnecessary buffering.
- Use efficient serialization and compression only when measurement supports it.

## 9. Security
- Enforce authentication and authorization at the server boundary.
- Use policy-based authorization for business permissions.
- Validate and encode untrusted data for its output context.
- Use HTTPS and secure transport configuration.
- Store secrets in an approved secret manager; prefer managed identity where available.
- Protect endpoints against injection, request forgery, over-posting, insecure deserialization, and excessive resource consumption.
- Keep framework and NuGet dependencies patched and scanned.

## 10. Resilience and Scalability
- Design services to be stateless where possible.
- Add timeouts, retries with backoff and jitter, and circuit breakers only where semantically safe.
- Ensure write operations are idempotent when retries are possible.
- Use health checks for dependencies and readiness.
- Avoid in-memory coordination when multiple application instances must share state.
- Apply load balancing and distributed-system patterns based on actual scale and availability needs.

## 11. Testing
- Unit-test domain and application logic.
- Add integration tests for HTTP endpoints, persistence, authentication, and external adapters.
- Cover authorization failures, validation errors, cancellation, timeouts, and concurrency behavior.
- Use test doubles at external boundaries, not for internal implementation details.
- Keep tests deterministic and independent.

## Review Checklist
- SOLID boundaries and dependency lifetimes are appropriate.
- Async calls remain asynchronous and cancellation is propagated.
- Inputs, authorization, and errors are handled consistently.
- Queries are parameterized and bounded.
- Logging is structured and excludes sensitive values.
- Tests cover business rules and security-critical paths.

---
Source basis: `Coding_Standard_V1.0.docx`, .Net Backend section, supplemented by general, testing, API versioning, and security sections.
