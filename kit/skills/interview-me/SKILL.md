---
name: interview-me
description: Build or refresh a context file by interviewing [YOUR_NAME] one question at a time. Use on day one for context/me.md, whenever a context file is thin or out of date, or when they say "interview me about X".
owner: Reasoning agent
---

# Interview me

## Purpose
Get what is in your head into a short, true `.md` file, in your words, so every agent stops guessing. You never have to write about yourself from a blank page.

## Steps
1. Read the target file (start with `context/me.md`) and list the gaps: missing facts, stale lines, contradictions.
2. Rank the gaps by how much they matter to `memory.md` aims.
3. Ask **one question at a time**. Prefer specific questions (dates, names, choices). Offer options when it helps.
4. After each answer, restate it in one line. Confirm if it is ambiguous.
5. Stop after about 10 questions, or when they say stop.
6. Write the update: facts only, no advice. Delete anything the answers made untrue.
7. Show a short summary: added, changed, removed.

## Off limits
- Only record what they said. No guesses.
- Never record passwords, ID or account numbers, money figures, or anyone's health or patient details.

## Done looks like
- [ ] Every gap was asked about or skipped on purpose.
- [ ] The file is under about 60 lines and contains nothing untrue.
