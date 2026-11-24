---
name: new-skill-from-chat
description: Turn a job that just worked into a reusable skill. Use when a task went well and will repeat, or when [YOUR_NAME] says "make this a skill".
owner: Reasoning agent
---

# New skill from chat (the sanding down loop)

## Steps
1. **Redesign first.** If the job was clumsy by hand, fix the steps before writing them down. Automating a bad process makes it fail faster.
2. Re-read the conversation. Keep the steps that produced the result; drop the false starts.
3. Copy `skills/_template/SKILL.md` to `skills/<short-name>/SKILL.md`.
4. Fill in: description (what and when), inputs, numbered steps, off limits, output, done looks like.
5. Name the owning agent and add the skill to the table in `skills/README.md`.
6. Next time it runs and something goes wrong, add a guardrail and a changelog line. That is sanding down.

## Done looks like
- [ ] A fresh agent could run it with no chat history.
- [ ] Listed in `skills/README.md`.
