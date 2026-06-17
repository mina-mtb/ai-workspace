# Rule: Loop Safety (no infinite loops, no token furnace)

Autonomous retrying is dangerous. Every loop must be able to stop itself and ask a human.

## Hard limits
- **Max 3 attempts** at the same failing task. After the 3rd failure, STOP. Do not try a 4th time.
- **No-progress detection.** If the same error (or essentially the same error) appears twice in a row,
  treat it as "stuck" — do not keep hammering the same approach.
- **Scope cap.** Work at most 3 issues per autonomous run, then pause for human review.

## When a limit is hit — Human Handoff
1. Stop work immediately.
2. Write the current state, what was tried, and the exact blocker into the task (Issue/PR) and into
   `../state/CURRENT.md`.
3. Hand the problem to the human (you). Do not silently continue burning tokens.

## Why
A loop that retries forever, spawns helpers, and never stops is an architectural failure, not autonomy.
The human defines the standards; the loop executes against them and asks for help when stuck.
