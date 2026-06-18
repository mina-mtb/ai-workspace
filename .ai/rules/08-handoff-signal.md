# Rule: Handoff Signal (how agents pass the baton through the human)

Agents cannot wake each other automatically. The human is the wire between them. To make this reliable,
every agent MUST end its turn with ONE explicit, standard handoff line so the human knows exactly what to do.

## Required ending — every agent, every turn
End with a line in this exact shape:

`>> HANDOFF: <my role> is done. NEXT: <next role>. ACTION: <what the human should tell that role>.`

Examples:
- `>> HANDOFF: Backend is done. NEXT: Test/QA. ACTION: tell Test/QA to run unit tests on branch feat/save-cv.`
- `>> HANDOFF: Test/QA is done (PASS). NEXT: Reviewer. ACTION: tell Reviewer to review PR #4.`
- `>> HANDOFF: Reviewer approved. NEXT: Product Owner. ACTION: tell Product Owner to judge PR #4 for merge.`

## When work is blocked or stuck (loop safety)
`>> HANDOFF: <role> is STUCK after 3 attempts. NEXT: human. ACTION: <the exact blocker you need decided>.`

## At a human gate (Product Owner -> human)
`>> GATE: Phase <X> is complete and approved on <integration|staging>. NEXT: human (you).
   ACTION: if you approve, tell me to merge to <develop|production>. Evidence: <tests + why on-mission>.`

## The human's job
The human reads the HANDOFF/GATE line, goes to the named tool/agent, and says "your turn, continue".
The human is the postman, not the decision-maker — except at the two human gates, where the human decides.
