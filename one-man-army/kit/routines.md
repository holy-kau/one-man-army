# Starter routines (ward rounds)

Routines are the team's ward rounds: fixed times when someone checks everything and reports back. Times are in [YOUR_TIMEZONE]. The clock times below are kit defaults. Change the times, not the idea.

Turn on the morning brief in week one. Add the outbox reports once work is actually flowing through `inbox/` and `outbox/`. Add the Saturday digest and Sunday calendar sync in week two.

**How to schedule a routine in your tool:**

| Tool | Where |
|---|---|
| Claude | A scheduled task, with the prompt below as its instructions |
| ChatGPT | A scheduled task in the relevant project |
| Gemini | A Schedule (up to 10 active) |
| Grok Bot | A routine on the owning Bot |
| Muse | Ask Muse to do it every day at that time, then check its plan |
| None of these | A calendar reminder; when it fires, paste the prompt yourself |

Each routine reads `AGENTS.md` and `guardrails.md` before it acts. If usage logging is ON, each routine adds one line to its owner's `usage/log-<role>.md` when it finishes.

## 1. Morning brief — daily 07:00

**Owner:** Chief of Staff. **Usage type:** `morning-brief`

**Purpose:** What matters today, in one short message, before the day runs away.

**Prompt:**

> It is 07:00. Read `AGENTS.md`, `guardrails.md`, `memory.md`, and today's calendar.
> Also check `inbox/` for open tasks, `outbox/` for unread results, and any file named `memory-log/QUESTIONS-*.md`.
> Write me a morning brief:
> 1. Today's calendar in short form.
> 2. The top 3 things that deserve my attention.
> 3. Answer this first: does [YOUR_NAME] need to know anything today? If yes, say it in one line.
> 4. Decisions waiting for me, one item only in this message. If more than one is waiting, name the count and ask the first one.
> 5. Anything broken, overdue or missing.
> Keep it short. Do not invent events. Do not move protected calendar blocks. If you are unsure, say so.

On Mondays, add the top 3 from the latest weekly review in `outbox/`, if one exists.

## 2. Midday outbox report — daily 13:15

**Owner:** Chief of Staff. **Usage type:** `outbox-report`

> It is 13:15. Check `outbox/` for RESULT files that are new or still unreported since this morning.
> For each new item, give me one line: what it is, who filed it, and whether I need to decide anything.
> If I need to decide something, ask only the first decision in this message.
> If there is nothing new, say "Outbox clear at 13:15" and stop.
> Do not rewrite the reports. Do not start new work.

## 3. Evening outbox report — daily 19:15

**Owner:** Chief of Staff. **Usage type:** `outbox-report`

Same prompt as midday, with "since 13:15" and "Outbox clear at 19:15".

## 4. Saturday weekly digest — Saturday 21:30

**Owner:** Chief of Staff, filed for the reasoning agent. **Usage type:** `weekly-digest`

> It is Saturday 21:30. Draft a weekly digest and file it as `inbox/TASK-YYYYMMDD-2130-weekly-digest.md` for the reasoning agent.
> Cover the last seven days from the calendar, `inbox/done/`, `outbox/`, and `memory-log/`.
> Include: what moved, what stalled, decisions still open, and suggested study or deep-work blocks for next week (evenings, none on Saturday, none past 22:00 unless I have said otherwise).
> Do not put money figures in the task file.
> Do not write to the calendar tonight. The Sunday routine does that after I have seen the review.
> End the task with a clear "done when" so the reasoning agent knows what to produce in `outbox/`.

## 5. Sunday calendar sync — Sunday 21:30

**Owner:** Chief of Staff, after the weekly review exists. **Usage type:** `calendar-sync`

> It is Sunday 21:30. Read the latest weekly review in `outbox/`.
> If no review exists yet, say so in one line and stop. Do not invent blocks.
> If the review proposes study or deep-work blocks, show me the list first if I have not already approved it.
> Once I have approved the blocks, add them to the calendar in [YOUR_TIMEZONE], titled clearly, with no overlaps against protected blocks.
> No blocks on Saturday, and none past 22:00, unless I explicitly approved that exception.
> If a block clashes, move it to the next evening at a slightly later start and tell me what you changed.
> Report back with the list of events you wrote.

## Optional, once the core loop is stable

- **Inbox sweep** (reasoning agent, twice on weekdays, for example 12:45 and 18:45). Usage type `inbox-sweep`. Process open `inbox/` files, write results, move finished tasks to `inbox/done/`.
- **Memory merge** (reasoning agent, nightly or in the Sunday sweep). Usage type `memory-merge`. Fold `memory-log/` into `memory.md`, newest statement wins, contradictions into `QUESTIONS-*.md`.
- **Sunday review** (reasoning agent, mid-afternoon). Usage type `weekly-review`. Run `skills/sunday-audit`: sweep stale tasks, collect "Lessons and spec updates" into one short proposal, write the weekly review to `outbox/`.
- **Weekly usage summary** (Chief of Staff, Sunday evening, only if usage logging is ON). Usage type `usage-summary`. Count the lines in `usage/` for the past 7 days and show you the counts. You decide whether to send them.

## Rules for every routine

- Stay in lane. A routine does not send, post, pay, book or delete.
- If a step would change a protected calendar block, or would message someone, draft it and ask.
- If the source file is missing, say so in one line. Do not build a silent replacement.
- Keep the output short enough to read on a phone.

## Monthly privacy check (first Sunday, 10 minutes)

Prompt: "Read guardrails.md. Go through the access register with me one row at a time. For each agent or app, ask whether it still needs that access. List anything to revoke and anything sensitive you found in the shared folder. Change nothing yourself."
