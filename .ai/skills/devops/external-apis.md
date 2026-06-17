---
name: external-apis
description: Use when integrating or securing third-party services and external APIs (job boards, LLM providers, email, etc.).
---
# External APIs / Services
## Rules
- All keys via secrets manager / env; never committed.
- Wrap each external API behind an interface (so it's swappable and testable with mocks).
- Add rate-limit handling, retries with backoff, and timeouts. Validate all responses (untrusted input).
- Log calls (without secrets/PII) for tracing and cost.
