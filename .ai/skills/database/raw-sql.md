---
name: raw-sql
description: Use when a query genuinely cannot be expressed via EF Core and raw SQL is required.
---
# Raw SQL (use sparingly)
## When to use
Only for performance-critical or complex queries EF can't express well. Document why.
## Rules
- Never put business logic in SQL. Parameterize everything (no string concatenation → no injection).
- Keep it in the Infrastructure layer behind an interface. Application sees the interface only.
- Add an integration test that runs it against a temporary PostgreSQL.
