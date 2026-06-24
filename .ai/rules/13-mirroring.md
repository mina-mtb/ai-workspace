# Rule: Mirroring / Dual-Write

When we keep the same project knowledge in two systems, both sides must move together. Mirroring is
inside one project only; never mirror content across separate projects.

## Canonical project map
Use `.ai/integrations/PROJECT-LINKS.md` before touching Jira, GitHub, or Confluence. It defines which
repo, Jira project, and Confluence space belong together.

## Mirrored pairs
1. **WorkspaceAI:** WSAI Confluence <-> `ai-workspace` repo.
2. **WorkspaceAI backlog:** AIW Jira <-> `ai-workspace` GitHub Issues.
3. **FindJob:** FJ Confluence space <-> `Find_Job` repo, once the FJ space exists.
4. **FindJob backlog:** FJ Jira <-> `Find_Job` GitHub Issues.

## Rules
1. **Update both sides in the same unit of work.** When one side of a mirrored pair changes, the mirror
   side MUST be updated before the task is reported done.
2. **Whichever side is filled first, the other follows.** Repo-first and Confluence-first are both valid
   when the paired side is brought back into sync immediately.
3. **Report mirror status explicitly.** Every mirrored task report includes: `both sides updated? yes/no`.
   If the answer is no, name the exact blocker.
4. **Keep cross-linked IDs.** Jira items and GitHub Issues must link to each other so future agents can
   verify alignment without guessing.
5. **Resolve conflicts by source of truth.** For rules, skills, and state, the repo wins. Jira and GitHub
   stay aligned through their cross-linked IDs and comments.
6. **Do not mirror across projects.** WSAI never becomes the FindJob space, and AIW never becomes the FJ
   backlog. The only bridge is the continuous-improvement loop in `11-continuous-improvement.md`.
7. **Known limitation:** backlog rank is not currently exposed through the Atlassian MCP tool surface.
   If exact board order matters, rank manually in Jira and record that action in the mirrored item.

## Done means
The report names both updated locations, the cross-links created or preserved, and says
`both sides updated? yes`.
