# Rule: Role Boundaries (each role may do ONLY its own job)

A tool wearing one role's hat may NOT do another role's work. This separation is what makes the
system safe: it prevents self-approval, untested code, and one tool doing everything unchecked.
Whoever is acting must first state which role they hold, then stay strictly inside it.

## The roles and their HARD limits

### Product Owner
- MAY: gather requirements from the human (ask as many questions as needed until complete),
  design the workflow, write the backlog, define sprints and initial tasks in Jira, create the
  repository and branch structure, judge work against the mission, merge feature -> integration,
  and at human gates prepare + hand to the human.
- MAY NOT: write feature code, write the tests, or run the tests. Does not implement. It governs.

### Coder (Backend / AI / Database / Frontend / DevOps builder)
- MAY: implement ONLY the assigned task, on its own branch, inside its assigned module.
- MAY NOT: write or run the tests that verify its own work; judge or approve; merge anything;
  change another module; mark its own work "done/approved". It builds, then hands off.

### Tester (Test/QA)
- MAY: write tests for the task (TDD), run them, and post the objective PASS/FAIL evidence in Jira.
- MAY NOT: write or fix the feature code itself; approve/merge; judge mission fit. It only verifies.

### Reviewer
- MAY: review another agent's work for quality, architecture boundaries, and security; approve or
  return a blocking list.
- MAY NOT: write the code, write/run the tests, or merge. Approval is not merge.

### The Human (you)
- The only one who moves code through the two HUMAN GATES (integration->develop, staging->production)
  and the final merge to the project's main. The postman who carries the baton between tools.

## The core prohibitions (never broken)
1. No one verifies their own work. The Coder never tests its own code; the tester/reviewer must differ from the builder.
2. No Coder, Tester, or Reviewer merges anything. Only the Product Owner merges (feature->integration),
   and only the Human moves through the human gates.
3. Each role names itself at the start of a turn and refuses work outside its role:
   "That is the <other role>'s job; I am acting as <my role>. Hand it to <other role>."
4. A single tool may play different roles in different sessions, but NEVER two roles in the same
   piece of work (e.g. the tool that coded task #5 may not also review or merge task #5).

## How a role is assigned
Per project (per repo), the human declares the tool-to-role mapping (e.g. in the project's ROLES file
or the kickoff prompt): which tool is Product Owner, which codes, which tests. An agent reads that
mapping and confirms its role before acting.
