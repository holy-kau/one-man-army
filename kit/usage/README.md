# usage/ — opt-in usage counts

**Off by default.** Nothing in this folder is collected, sent or shared unless you choose to. Turning it on or off is one line in `AGENTS.md`: `Usage logging: ON` or `Usage logging: OFF`.

## Why it exists

The kit's author wants to learn which routines and lanes people actually use, so v2 can be simpler and more useful. Counts are enough for that. Content is never needed.

## What an agent writes (and only this)

After each routine or task, the agent that did it appends **one line** to its own file, `usage/log-<role>.md`:

```
YYYY-MM-DD | type | role | tool | outcome
```

Example:

```
2026-12-02 | morning-brief | chief-of-staff | gemini | done
2026-12-02 | task-learning | learning | claude | needs-approval
```

- **type**, from this fixed list only: `morning-brief`, `outbox-report`, `weekly-digest`, `calendar-sync`, `inbox-sweep`, `memory-merge`, `weekly-review`, `usage-summary`, `task-schedule`, `task-learning`, `task-health`, `task-lifestyle`, `task-research`, `task-writing`, `task-other`
- **role**: `chief-of-staff`, `reasoning-agent`, `research-desk`, `scheduler`, `learning`, `health`, `lifestyle`
- **tool**: `claude`, `chatgpt`, `gemini`, `grok-bot`, `muse`, `copilot`, `local`, `other`
- **outcome**: `done`, `needs-approval`, `skipped`, `failed`

## What is never written

- What the task was about, its title, or any words from it.
- Names of people, patients, clients, places, workplaces.
- Health, money, or any figures other than the date.
- Message text, file contents, links, or the time of day.

If a line would need any of these, the agent writes `task-other` and nothing else.

## What happens to the log

- It stays in **your** folder. Nobody else can see it.
- If you also opted in to the weekly check-in, once a week you (or Chief of Staff) count the lines, **you look at the counts**, and you decide whether to send them through the check-in form. The primer page can do the counting for you in your browser.
- You can read, edit or delete any line at any time.

## How to turn it off

1. Change `Usage logging: ON` to `Usage logging: OFF` in `AGENTS.md` (and in `memory.md`).
2. Optionally delete the `usage/` files.
3. Stop sending the weekly check-in. That is all. Nothing else needs undoing.
