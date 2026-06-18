# Rule: Module Boundaries (so fixing one place doesn't break another)

The project is a Modular Monolith with separate AI microservices. The whole point of these boundaries
is blast-radius containment: work inside one module must not silently break another.

## Rules for every agent
- **Stay inside the assigned module.** A task targets a specific module (e.g. Jobs, Documents,
  Identity, AiOrchestration). Do not modify files in another module to make your change "work".
- **Cross-module communication only through contracts/interfaces.** Never reach into another module's
  internals. If you need something from another module, use its public contract; if the contract is
  missing, that's a task for the Architect, not a workaround.
- **Respect the dependency rule** (see ../skills/backend/clean-architecture-dotnet.md):
  Domain depends on nothing external; Application sees interfaces; Infrastructure implements; Api is the boundary.
- **Python AI services never bypass contracts** and never touch the main database directly.
- **Changing a shared contract is a bigger deal.** It needs contract tests and Architect awareness,
  because it can affect every consumer. Flag it; don't change a shared contract quietly.

## Why
If modules are properly separated, the Backend agent working on Jobs physically cannot corrupt the
Documents module — they only meet at a versioned contract. This is what keeps the system safe to change
as it grows, and what makes it cleanly splittable into real microservices later.

## When a change would cross a boundary
Stop and route it: the Orchestrator sequences a multi-module change as separate tasks (one module at a
time, default sequential), each with its own branch, tests, and review. Never one giant cross-module commit.
