# One Man Army

A starter kit for running your life with a small team of AI agents. One shared folder, one rulebook, a Chief of Staff, a few specialists with one job each, and a weekly rhythm. Agents draft, research, remind and file. You keep the pen.

**Try it:** [kaushikilango.com/tools/one-man-army](https://kaushikilango.com/tools/one-man-army/). The interactive primer asks a few questions and builds a copy of this kit made for you.

## What's here

| Path | What it is |
|---|---|
| `kit/` | The kit itself: rulebook (`AGENTS.md`), guardrails, routines, agents, skills, MCP guide. Start with `kit/README.md`. |
| `primer/primer.template.html` | The single page web primer, with the kit injected at build time. |
| `primer/build.py` | Builds the primer from the kit. |

## Build the primer

```bash
python3 primer/build.py kit primer/primer.template.html dist/index.html
```

Open `dist/index.html` in a browser. No server, no dependencies.

## Principles

- One agent, one job.
- Agents draft; you approve anything that sends, pays, books, posts or deletes.
- The folder is the asset. The tools are replaceable.
- No patient, client, money or password details anywhere in the folder.

Not a clinical tool, not a medical device, not professional advice.

## Licence

MIT. Use it, fork it, make it yours.
