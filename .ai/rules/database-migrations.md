# Database & Migrations

> This is the concrete example rule. Edit it to match YOUR stack. The principle is the same
> whether you use EF Core, Prisma, Alembic, Flyway, Django, or raw SQL migration files.

## Rule
- **Never change the database schema directly** (no manual `ALTER TABLE`, no editing the DB by hand,
  no `EnsureCreated` against a real database).
- All schema changes happen through **migrations**, checked into version control.
- A migration must be reversible (have a `Down` / rollback) unless explicitly approved otherwise.
- Never run a destructive migration against a shared or production database without human approval.

## Why
Direct edits cause "state drift": the code's model and the real database disagree, and the next
person (or agent) cannot reproduce the environment. Migrations keep schema history auditable and repeatable.

## Example (EF Core / .NET)
- To change schema: edit the entity/model, then generate a migration, then apply it.
  ```
  dotnet ef migrations add <DescriptiveName>
  dotnet ef database update
  ```
- Review the generated migration before applying. Commit the migration file with the code change.

## See also
The how-to steps live in `../skills/ef-core-migration.md`.
