# Workflow: Add a Feature
1. Orchestrator turns the goal into an "Agent Ready" Issue with acceptance criteria + named tests.
2. Architect confirms it fits existing modules (new module → ADR).
3. Builder (Backend/AI/Database/Frontend) implements ONLY its part on its own branch.
4. Test/QA runs the named tests; posts evidence; PASS required.
5. Reviewer checks quality, architecture, security.
6. Product Owner confirms mission fit and authorizes the merge.
7. Update state/CURRENT.md + DECISIONS.md; comment the Issue with evidence.
8. If something reusable emerged, add a rule/skill.
