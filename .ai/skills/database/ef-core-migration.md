---
name: ef-core-migration
description: Use when changing the database schema in a .NET / Entity Framework Core project — adding or modifying tables, columns, indexes, or relationships.
---
# EF Core Migration
## When to use
Any entity/model change that must reach the database. Never edit the DB by hand.
## Steps
1. Change the entity / DbContext model.
2. `dotnet ef migrations add <DescriptiveName>` — one logical change per migration.
3. Read the generated migration; confirm Up is correct and a sensible Down exists.
4. `dotnet ef database update` against local/dev.
5. Commit the migration file together with the model change.
## Gotchas
- Don't mix `EnsureCreated()` with migrations. Never run destructive migrations on shared/prod DB without approval + backup. Migrations are version-controlled and CI-tested.
