# Python Coding Best Practices

## 1. Style and Layout
- Follow PEP 8 and the repository's configured formatter and linter.
- Use four spaces per indentation level and never mix tabs with spaces.
- Keep code lines within 79 characters where practical and docstrings within 72 characters.
- Use two blank lines around top-level functions and classes, and one blank line between class methods.
- Prefer double quotes consistently unless the formatter or project convention specifies otherwise.

## 2. Naming
- Variables and functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Modules and packages: lowercase `snake_case`
- Private implementation details: prefix with a single underscore
- Avoid cryptic abbreviations and names that shadow built-ins.

## 3. Imports
Group imports in this order, separated by blank lines:
1. Standard library
2. Third-party packages
3. Local application imports

Additional rules:
- Put imports on separate lines unless importing selected names from one module.
- Avoid wildcard imports.
- Remove unused imports.
- Avoid circular imports through better module boundaries.

## 4. Functions and Classes
- Keep functions focused and generally small. Refactor long functions into cohesive helpers.
- Avoid excessive parameters. Prefer a typed data object when parameters form a logical unit.
- Follow the Single Responsibility Principle for classes.
- Prefer composition over deep inheritance.
- Avoid global mutable state.
- Use context managers for files, sockets, locks, and other managed resources.

## 5. Type Hints and Documentation
- Add type hints to public functions, methods, and important data structures.
- Use docstrings for public modules, classes, functions, and methods.
- Document behavior, parameters, return values, raised exceptions, and side effects.
- Avoid redundant annotations when inference is clear and project standards allow it.

```python
def process_data(values: list[int]) -> int:
    """Return the sum of the supplied integer values."""
    return sum(values)
```

## 6. Python Idioms
- Prefer built-in functions and standard-library utilities.
- Use `enumerate()` instead of manually maintaining an index.
- Use comprehensions when readable. Use generators for large or streaming datasets.
- Use f-strings for readable string formatting.
- Use `"".join(parts)` for repeated string concatenation.
- Use `is None` for singleton identity checks and `==` for value comparison.
- Use a ternary expression only for simple conditional assignments.

## 7. Mutable Values and State
Never use mutable objects as default argument values.

```python
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    result = [] if items is None else list(items)
    result.append(item)
    return result
```

## 8. Exceptions
- Catch specific exception types.
- Do not silently swallow exceptions.
- Add useful context without leaking sensitive data.
- Use custom exceptions for meaningful domain failures.
- Preserve the original cause with `raise ... from error` when appropriate.
- Use `finally` or context managers for required cleanup.

## 9. Dependencies and Packaging
- Use an isolated virtual environment.
- Declare and constrain dependencies in the project's approved manifest and lock file.
- Keep source code in a clear package structure, preferably a `src` layout for distributable packages.
- Separate runtime and development dependencies.
- Scan dependencies and remove unused packages.

## 10. Testing
- Use `pytest` or the project-approved framework.
- Follow Arrange, Act, Assert.
- Test normal, invalid, boundary, and exception paths.
- Use fixtures for reusable setup and mocks only at true external boundaries.
- Avoid time, network, random, and filesystem nondeterminism unless explicitly controlled.

## 11. Performance
- Profile before optimizing.
- Prefer iterators and generators for large data volumes.
- Avoid unnecessary copies and eager materialization.
- Cache expensive pure computations only when cache size and invalidation are understood.
- Use asynchronous programming for suitable I/O-bound workflows, not as a default.

## 12. Quality Tooling
Recommended categories of tools:
- Formatter: Black or project equivalent
- Linter: Ruff, Flake8, or project equivalent
- Type checker: mypy or Pyright
- Tests and coverage: pytest and coverage.py
- Security: Bandit, dependency scanning, and secret scanning

## Review Checklist
- PEP 8 and repository checks pass.
- Names, types, and docstrings are clear.
- Mutable defaults and broad exception handlers are absent.
- Resources are safely managed.
- Tests cover errors and edge cases.
- No credentials or environment-specific values are embedded.

---
Source basis: `Coding_Standard_V1.0.docx`, Python Coding Standards section.
