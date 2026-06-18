# Rule: Layered Testing (which test runs where)

Follow the testing pyramid: many fast tests low, few heavy tests high. Each layer runs at a specific
stage and gates the next. A builder never verifies its own work — a different agent does.

## Layer 1 — Unit tests (TDD)  [on every feature branch]
- Scope: one function/component in isolation; mock external deps (DB, services).
- Who: written test-first by the Test/QA agent (or a builder different from the one being tested).
- When: on every change, before the piece is accepted. Fast (seconds).
- Gate: a piece is not "done" until its unit tests PASS with evidence.

## Layer 2 — Integration tests  [when pieces are combined / before entering develop]
- Scope: do the combined pieces work together? DB calls, API contracts, service-to-service, migrations.
- Use a temporary/real PostgreSQL, not mocks, where it matters.
- When: after units pass, on the integration branch, before HUMAN GATE 1.
- Gate: integration tests PASS + regression check (nothing previously working is broken).

## Layer 3 — E2E / System tests  [on develop -> staging, before HUMAN GATE 2]
- Scope: the whole application as a user experiences it — real user journeys end to end.
- Keep these THIN and deliberate: only business-critical journeys (e.g. "upload CV", "match CV to job").
- When: at milestones, before a release. Slow; do not run on every commit.
- Gate: critical journeys PASS in a production-like (staging) environment.

## Project-specific test types (from the architecture plan)
Also apply where relevant: contract tests (.NET<->Python boundaries), EF Core migration checks,
architecture tests (Clean Architecture boundaries), security scans (OWASP LLM Top 10),
and AI evals (prompt/RAG/model) whenever AI behaviour changes.

## Anti-pattern to avoid
Do NOT pile up E2E tests to "be safe" (the inverted "ice-cream-cone"). It makes the pipeline slow and
flaky. Push coverage DOWN: prefer many unit tests, a moderate number of integration tests, few E2E tests.
