---
name: tool-and-model-selection
description: Use when deciding WHICH tool (Codex, Antigravity, Claude Code, etc.) and WHICH model should perform a given task, to make optimal use of the available tools and quotas.
---
# Tool & Model Selection (a Product Owner / orchestration responsibility)

Choosing the right tool+model for each task is part of running the project well. Today the human's
architect (Claude in the browser) makes this call and tells the human exactly who to give each prompt
to and which model to pick. When a Product Owner agent later does this itself, it must follow this skill.

## What we know about each tool (update as this changes)
- **Codex (in VS Code)** — strong, precise coding and git. Has working git push. Good default CODER.
  Model picker includes GPT-5.5 / GPT-5.4 / GPT-5.4-Mini with Reasoning levels (Low→Extra High).
- **Antigravity** — reliable at following rules with citations; working git push. Good PRODUCT OWNER /
  reviewer / git-execution. Model picker includes Gemini 3.x and Claude Sonnet/Opus (Thinking).
- **Claude Code** — strong reasoning, BUT in this setup runs in an isolated sandbox that could NOT push
  to the user's GitHub (persistent 403). Avoid for tasks that must push/merge until that is fixed.

## How to choose
1. **Match the task type to the tool's strength**:
   - Writing/refactoring code, running builds → Coder tool (Codex).
   - Judging, reviewing, merging feature→integration, governance → Product Owner tool (Antigravity).
   - Pure planning/architecture/explanation → the architect (browser Claude); no repo access needed.
2. **Respect role separation** (rule 10): the tool that built a piece must NOT be the one to test,
   review, or merge that same piece. So coder and reviewer/PO should be DIFFERENT tools.
3. **Pick the model by difficulty**:
   - Heavy reasoning (design, tricky bug, judging mission fit) → strongest "thinking" model
     (e.g. Claude Opus Thinking in Antigravity; GPT-5.5 High/Extra-High reasoning in Codex).
   - Routine, mechanical, or cheap-and-fast steps (a simple git merge, a small file copy, a status
     check) → a fast/cheaper model (e.g. Gemini Flash; GPT-5.4-Mini). Don't burn a premium model on
     a `git status`.
4. **Respect quota rotation**: the human rotates tools as paid quotas run out. If a preferred tool is
   unavailable, fall back to the next best that satisfies the role-separation rule, and note it.

## The output of this decision
Whoever assigns a task states, explicitly:
- which TOOL to use, with which MODEL/reasoning level, and WHY (one line),
- ending with the standard `>> HANDOFF:` line so the human knows exactly where to paste the prompt.

## Why this is documented
So that when a Product Owner agent eventually does orchestration itself, it knows tool+model selection
is part of its job — not an afterthought. Optimal tool/model use saves cost and improves quality.
