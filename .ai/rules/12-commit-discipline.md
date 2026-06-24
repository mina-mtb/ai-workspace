# Rule: Commit Discipline

Keep repo history usable. A task is easier to review, resume, and recover when state changes are
committed in clear units instead of piling up in the working tree.

## Rules
1. **Checkpoint pending state before new work.** If `.ai/state/` has pending changes from the last
   session, commit and push that checkpoint before starting a new task.
2. **One clear commit per meaningful unit of work.** Do not bundle unrelated edits into one commit.
3. **Use standard message prefixes.** Prefer `docs:`, `feat:`, `fix:`, and `chore:` unless the repo
   establishes a narrower convention.
4. **Do not let uncommitted work pile up.** At the end of every session, update `.ai/state/CURRENT.md`
   and commit the state change when the task changed project state.
5. **Push after each significant commit.** Shared memory only helps rotating agents if the remote has
   the latest checkpoint.
6. **Never commit temporary artifacts.** `scratch/`, local audit dumps, generated throwaway logs, and
   other temp files stay ignored and out of commits.
7. **Respect the branch rule.** Checkpoint commits for task work happen on the task branch; no direct
   pushes to `main` unless the human explicitly approved repo housekeeping for the current phase.

## Done means
The final report names the commit(s), push status, and whether the working tree is clean except for
intentionally ignored files.
