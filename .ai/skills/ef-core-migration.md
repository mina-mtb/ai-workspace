---
name: ef-core-migration
description: Use this skill when you need to change the database schema in a .NET / Entity Framework Core project — adding or modifying tables, columns, indexes, or relationships. Use whenever a model/entity change requires a database change.
---

# EF Core Migration

## When to use
Any time an entity/model change needs to be reflected in the database. Never edit the DB by hand.

## Steps
1. Make the change to the entity / `DbContext` model in code.
2. Generate a migration with a descriptive name:
   ```
   dotnet ef migrations add AddUserEmailIndex
   ```
3. **Read the generated migration file.** Confirm the `Up` does what you intend and a sensible
   `Down` exists (reversible).
4. Apply it to your local/dev database:
   ```
   dotnet ef database update
   ```
5. Commit the migration file together with the model change in the same commit.

## Example
```
dotnet ef migrations add AddOrderStatusColumn
dotnet ef database update
```

## Gotchas
- Do NOT use `EnsureCreated()` against a database you also migrate — they conflict.
- Never apply a destructive migration (dropping a column/table with data) to a shared or
  production database without human approval and a backup.
- If a migration is wrong, create a new corrective migration; don't hand-edit an applied one.
- Keep one logical schema change per migration so it's easy to review and roll back.
