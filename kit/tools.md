# Choosing your tools

This kit works with any AI assistant that can (a) follow pasted instructions and (b) read and write files in a shared folder. Some tools can also run on a schedule; that is what makes routines like the morning brief automatic.

_Checked 23 Nov 2026. These products change monthly. Before you pay, check the current plan page yourself._

## The short version

- **Already paying for one?** Start there. A kit you actually use in one tool beats a perfect stack you never set up.
- **Simplest start:** one tool, two roles (Chief of Staff and reasoning agent) as two projects or two custom assistants.
- **Mostly on your phone, live in WhatsApp?** Muse or Gemini are the gentlest start.
- **Want things to happen while you sleep?** You need a tool with scheduled tasks (Claude, ChatGPT, Gemini, Grok Bot, Muse all have some form).
- **Doctors:** none of these consumer tools is an approved system for patient information. Use them for your own life, study and admin only.

## What each tool is good and bad at

### Claude (Anthropic)

| Pros | Cons |
|---|---|
| Strong at careful reasoning, long documents and writing. A natural fit for the reasoning agent. | Scheduled tasks and the agent workspace (Cowork) need a paid plan. |
| Projects keep instructions, files and project memory together, which maps neatly onto one role per project. | Fewer "it just does it on its own" features than Grok Bot or Muse; you set things up deliberately. |
| Scheduled tasks run in the cloud even when your computer is asleep. | Connectors to your apps need a little setup the first time. |
| Can be set to always ask before using a connected tool. | |

**Where the role card goes:** a Project's instructions (one project per role), or a scheduled task's instructions for routines.

### ChatGPT (OpenAI)

| Pros | Cons |
|---|---|
| The most familiar app; many people already use it daily. | Scheduled tasks and agent mode are tied to paid tiers and their limits change often. |
| Projects, custom GPTs and scheduled tasks cover most kit roles. | Long-running agent work can drift from instructions over long sessions; keep tasks small. |
| Agent mode (ChatGPT Work) handles multi-step tasks across connected apps and files. | Memory is helpful but can mix contexts between roles if you use one chat for everything. |

**Where the role card goes:** a Project's instructions, or a custom GPT per role.

### Gemini (Google)

| Pros | Cons |
|---|---|
| Lives inside Google: Gmail, Drive, Docs, Calendar. If your life runs on Google, setup is light. | Up to 10 active schedules at a time. |
| Deep Research is a strong research desk and can work over your Drive and Gmail if you connect them. | Scheduled answers are prepared in advance, so fast-changing information may be slightly out of date. |
| Gems let you save a role as a reusable assistant. | Be careful what you connect: a research desk does not need your whole inbox. |

**Where the role card goes:** a Gem per role; a Schedule for routines.

### Grok Bot (SpaceXAI / xAI)

| Pros | Cons |
|---|---|
| Built for a team of named agents. Each Bot has a role and memory, and keeps working on a cloud computer while your laptop is closed. | Paid only: included with the X Subscription from its Premium tier upward. |
| Routines run on a schedule or when something happens; up to 50 per Bot. | Usage is a weekly allowance, so heavy weeks can be hard to predict. |
| Can work on websites that have no proper connection, by using a browser like a person would. | All your Bots share one computer and its logins. A separate Bot is **not** a security wall. |
| You set approvals per action: allow once, always, or deny. | You cannot choose which underlying AI model runs a job, and the product is still changing fast. |

**Where the role card goes:** each Bot's role instructions; routines for the schedule.

### Muse (Meta)

| Pros | Cons |
|---|---|
| Free to start (with a usage limit). Works on phone, desktop, Mac and inside WhatsApp, which makes it the easiest start if you are not technical. | Newer (launched Sept 2026); fewer people have tested it in a structured setup like this. |
| Proactive: it builds a plan, works in the background and comes back with suggestions. | Works best on your own device's files and apps; sharing one folder with other tools needs more thought. |
| Asks before important actions (sending email, buying), with allow once / always / deny. | It is built to take actions; be strict about approvals from day one. |
| Runs on its own secure virtual computer, with your data stored separately. | Check what you share with Meta and switch off model training on your data if you prefer. |

**Where the role card goes:** start a chat with the card as the first message and ask Muse to keep it as its standing instructions; set permissions before connecting anything.

### Also worth knowing

- **Microsoft Copilot.** Worth a look if your work or family already runs on Microsoft 365 (Outlook, OneDrive, Teams). Check current plans before choosing.
- **A local, offline model** (run on your own computer). The most private option and costs nothing per month, but needs a capable laptop, more setup, and usually cannot run schedules or reach your calendar. Good for a private "vault" assistant later, not for a first setup.

## Suggested starting stacks

| If you… | Try this |
|---|---|
| Want the least effort | One tool you already use. Chief of Staff and reasoning agent as two projects or assistants. |
| Live in Google | Gemini for Chief of Staff and research. Add Claude or ChatGPT as the reasoning agent if you want a second opinion. |
| Want a proper team that runs on its own | Grok Bot or Muse for Chief of Staff and specialists, plus Claude as the reasoning agent and sole editor of memory. |
| Are non-technical and mostly on your phone | Muse or Gemini only. One agent, one routine (the morning brief). Grow later. |

## Rules that do not change with the tool

- Every agent reads `AGENTS.md` and `guardrails.md` first.
- One writer per file. Only the reasoning agent edits `memory.md` and `context/`.
- Anything irreversible waits for your yes.
- No patient, client, money or password details anywhere in the folder, in any tool.

## Sources (checked 23 Nov 2026)

1. Anthropic Help Center: Schedule recurring tasks in Claude Cowork. https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
2. Google Gemini Help: Schedules in Gemini Apps. https://support.google.com/gemini/answer/16316416
3. Google blog: Gemini Deep Research can connect to Gmail, Docs and Drive. https://blog.google/products-and-platforms/products/gemini/deep-research-workspace-app-integration/
4. Lindy: Grok Bot explained (pricing, routines, shared computer, approvals). https://www.lindy.ai/blog/grok-bot
5. Meta Newsroom: Introducing Muse. https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/
6. Meta AI: Muse features. https://ai.meta.com/muse/
7. OpenAI Help Center: ChatGPT agent. https://help.openai.com/en/articles/11752874-chatgpt-agent
8. Composio: ChatGPT agent mode explained (ChatGPT Work, limits). https://composio.dev/content/chatgpt-agent-mode-explained-what-it-can-and-cannot-do
