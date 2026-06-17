---
name: git-merge-flow
description: Use ONLY when the Product Owner has approved a branch for merge. Step-by-step git commands to merge a feature branch up to a higher branch and push. Mechanical execution of an already-made decision — never a substitute for the merge decision itself.
---
# Git Merge Flow (execution only)

> This skill is the MECHANICAL part of a merge. The DECISION to merge belongs to the Product Owner
> (see ../../agents/product-owner.md and ../../rules/04-merge-authority.md). Never run these commands
> unless the merge has been authorized. The builder of the work must never run these on its own work.

## Preconditions (all must be true before running anything)
1. Test/QA posted a PASS with evidence.
2. Reviewer approved (quality, architecture, security).
3. Product Owner confirmed the change fits the mission in ../../state/PROJECT.md.
4. The human gave the go-ahead (until the Product Owner role is itself a trusted agent).

If any precondition is missing, STOP and ask. Do not merge.

## Steps (replace <branch> and <target> accordingly; <target> is usually main)
```
# 1. make sure the working tree is clean first
git status            # if not clean: stop, report, do not proceed

# 2. go to the target branch and update it
git checkout <target>

# 3. merge the approved branch
git merge <branch>

# 4. delete the merged branch (local)
git branch -d <branch>

# 5. publish to the backup/remote
git push origin <target>
```

## After merging
- Update ../../state/CURRENT.md: what merged, and the new "where we are / next step".
- Append a line to ../../state/DECISIONS.md if the change was notable.
- Comment the result + evidence on the related GitHub Issue, and close it if done.

## If something goes wrong
- Merge conflict → do NOT force anything. Stop, report the conflicting files, ask the human.
- `git push` asks for credentials / fails → stop and report; never paste a token into a file.
- `git checkout` complains about uncommitted changes → stop; report what is uncommitted.

## Hard limits
- Never `git push --force` to a shared branch. Never rewrite history on main.
- This skill does not grant merge AUTHORITY; it only documents the commands once authority is granted.
