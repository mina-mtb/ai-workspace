# Rule: Branch Flow & Human Gates

The path from a worker's code to production has layered tests and TWO human gates. The human and the
agents are not the same; the two most dangerous transitions require the human's explicit approval.

## The flow (low, fast tests at the bottom; few, heavy tests at the top)
```
feature/*        workers build here, one branch per task
   | (1) unit tests (TDD) by a DIFFERENT agent than the builder  -> must PASS
   | Product Owner approves + merges            <- AGENT, automatic
integration      several pieces combined for one operation
   | (2) integration tests on the combination   -> must PASS
   | Product Owner checks: closer to the goal? nothing else broken? (regression)
   | >>> HUMAN GATE 1 <<<  Product Owner hands to the human; human approves
develop          official development line
   | (3) E2E / system tests: whole system, all parts together, real user scenarios
staging          production-like
   | high-level test group approves
   | >>> HUMAN GATE 2 <<<  hands to the human; human approves
main / production real users
```

## Rules
- Workers branch from `develop` (or from `integration` for a multi-piece operation), never from `main`.
- A builder NEVER runs the tests that verify its own work; a different agent (Test/QA) does.
- Product Owner may merge feature -> integration automatically (it did not build the code).
- Product Owner may NOT push to `develop` or to `production` on its own. Those are HUMAN GATES:
  the Product Owner prepares and approves, then HANDS TO THE HUMAN with the exact sentence in
  `08-handoff-signal.md`. Only the human moves code through a human gate.
- Each gate requires evidence: which tests ran, results, and a one-line "why this is safe / on-mission".

## Why two gates (not one)
Gate 1: agent work entering the official dev line — the human confirms direction before it becomes "real".
Gate 2: before production — even the tests were written/run by agents, so a human signs off before real users.
