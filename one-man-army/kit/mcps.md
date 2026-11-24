# MCPs: giving your agents hands

_Read this after `tools.md`. Plain language, no coding. Names of menus change often: if a step looks different in your app, look for "Connectors", "Apps", "Integrations" or "Extensions"._

## The idea in one line

**The model is the car. The setup is the driving.** Learn to drive once and you can drive any car. This kit is the driving: it works with whichever AI you pick, and the folder moves with you if you switch.

## The three pillars of any agent

| Pillar | What it is | In this kit |
|---|---|---|
| **Context** | What the agent knows about you and the job | `AGENTS.md`, `memory.md`, `context/` |
| **Tools** | What the agent can reach and do: your files, calendar, email, the web | MCPs and connectors (this file) |
| **Skills** | Written routines it follows the same way every time | `skills/` |

Most people only ever do context: a long prompt. Agents get useful when you add tools and skills. Keep context lean: give the agent only the file it needs for the job.

## The loop every agent runs

**Observe** (read the right file) → **Think** (restate the goal and what done looks like) → **Act** (use its tools) → **check** against done → **sand down** (add one lesson so next time is better). Repeat until done. Your job is the goal and the yes, not the steps.

## What an MCP is

**MCP (Model Context Protocol)** is a standard plug that lets an AI agent connect to an app, such as your drive, calendar or a website, and read from it or act in it, instead of you copying and pasting.

- One plug shape for every app, a bit like USB-C.
- In Claude these appear as **Connectors**. ChatGPT, Gemini, Grok Bot and Muse have their own built-in versions under different names. The idea is the same.
- Each connection has its own permission. Set anything that sends, books, pays or deletes to **ask every time**.

## Recommended connections, in order

Add one at a time, and only when a real job needs it.

| # | Connect | Why | Who uses it | Setting |
|---|---|---|---|---|
| 1 | **Your drive** (Google Drive, OneDrive, or a folder on your computer) | The 2nd brain lives here. Every agent reads `AGENTS.md` and `memory.md` from it | All agents | Read and write files in the folder only |
| 2 | **Your calendar** (Google or Outlook) | Morning brief, clash checks, protected blocks | Chief of Staff (and Scheduler for its entries) | Ask before moving or deleting anything |
| 3 | **Web search** (built in to most tools) | Research with sources | Research desk | Read only |
| 4 | **Your email** (Gmail or Outlook) | Drafts and summaries | Reasoning agent only | Draft only. Never send. Never open links or attachments |
| 5 | **A browser agent** (e.g. Claude in Chrome, or your tool's own browser) | For websites that have no connector | One agent, on request | Ask every time |
| 6 | **A hub** (e.g. Zapier or Composio) | One plug for many apps, once you outgrow the basics | Later, week 4+ | Same rules as each app it reaches |
| 7 | **A local model with folder access** (e.g. LM Studio or Ollama) | Anything sensitive that should never leave your computer | Optional | Offline only |

## Rules that never change

- Connect the fewest apps that do the job. A research desk does not need your inbox.
- Several agents sharing one account share its access. Treat them as one agent for safety.
- Never connect patient, client or work systems that hold other people's records.
- Text inside emails and web pages is information, never an instruction. Your agents take orders from you only.
- When you add a connection, write one line in `tools.md`: what it is, which agent uses it, and its setting.
