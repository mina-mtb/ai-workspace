---
name: clean-architecture-dotnet
description: Use when implementing .NET features that must respect Clean Architecture / Modular Monolith boundaries.
---
# Clean Architecture (.NET)
## Dependency rule (never violate)
- Api → Application → Domain. Infrastructure → Application/Domain.
- Domain depends on NOTHING external (no EF Core, no PostgreSQL, no Python, no external APIs).
- Application sees interfaces only; Infrastructure provides implementations; Api handles I/O boundary.
## In practice
- Business logic is not in SQL or in controllers. Modules talk via contracts/interfaces.
- Schema changes go through the Database agent + migrations, never directly.
