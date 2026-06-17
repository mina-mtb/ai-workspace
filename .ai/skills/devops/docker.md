---
name: docker
description: Use when writing or changing Dockerfiles or Docker Compose for local development or VPS deployment.
---
# Docker & Compose
## When to use
Containerizing .NET API, Python AI services, PostgreSQL, Redis; local dev + VPS production.
## Notes
- Separate compose files: base + override (local) + staging + prod.
- Pin image versions; don't deploy a new image tag to prod without testing.
- Secrets via env files that are NOT committed (only `.env.example`).
