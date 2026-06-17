# Rule: The Testing Gate

A task is NOT complete until its tests are defined AND passing. This is verified by a
separate Test/QA agent, never by the agent that wrote the code.

## At task START
- The acceptance criteria must be written into the task (the GitHub Issue) as a checklist.
- The tests that will prove "done" are named/defined before implementation begins.

## At task END
- The relevant tests exist and PASS. The Test/QA agent runs them and posts the result
  (the actual command output / log) as evidence into the Issue or PR.
- "It looks correct" is not acceptance. Only an objective pass/fail signal is.

## Separation of duties
- The agent that writes code does not get to declare its own work verified.
- Test/QA produces an independent pass/fail signal. Reviewer checks quality. Product Owner gates the merge.

## Types of verification
- **Deterministic** (preferred): unit/integration tests, build success, type check, lint, migration check.
- **Soft** (when unavoidable): a reviewer agent judges against a written spec — but a deterministic
  check must exist wherever one is possible.
