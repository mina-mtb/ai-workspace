# Workflow: Review a Pull Request

Run by the Reviewer Agent. The reviewer does not write the feature — it audits it.

1. Read the PR summary and the diff.
2. Check against EVERY file in `.ai/rules/`.
3. Run the tests yourself; don't trust "tests pass" — verify.
4. Security pass: secrets, injection, auth, least privilege.
5. Confirm the handoff/summary is complete (`.ai/communication-protocol.md`).
6. Output: PASS, or a numbered list of blocking issues, each with a concrete fix.
