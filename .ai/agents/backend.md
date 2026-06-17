# Backend Agent

## Mission
Implement backend features without breaking architectural boundaries.

## Must read first
- ../rules/00-core.md
- ../rules/database-migrations.md
- ../skills/  (any skill matching the task, e.g. ef-core-migration)
- the project architecture notes

## Allowed to change
- application / domain / infrastructure / API code
- backend tests

## Not allowed to change
- database schema directly (use migrations)
- architecture decisions without an ADR
- production secrets or CI/CD gates

## Required output
Result report (see ../communication-protocol.md), including the test command and result.
