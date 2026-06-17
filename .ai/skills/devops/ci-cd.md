---
name: ci-cd
description: Use when building or changing the CI/CD pipeline (GitHub Actions) — build, test, eval, security scan, deploy.
---
# CI/CD (GitHub Actions)
## On Pull Request
build + unit/integration tests (.NET & Python), contract tests, EF migration check, architecture tests,
lint/format, security scan, dependency check, Docker build test; LLM/RAG evals if AI files changed.
## On main after approval
build & push images → deploy staging → smoke tests → migration rehearsal → approval → prod deploy → health checks → rollback available.
## Hard rule
No code reaches main without passing checks AND Product Owner approval.
