---
name: 8hack-copilot
description: KVA official 8hack co-pilot (MCP server `hack` + skills): setup, commands, deadlines for 14.11
metadata:
  type: reference
---
KVA hackathon co-pilot "8hack" (slide shown on 2026-11-14). Related: [[hackathon-rules]], [[next-steps]].
- MCP server `hack`: https://c8-hackathon.kakashi.ventures/api/mcp — Filippo's machine: added, auth via `/mcp` -> hack -> Authenticate (login code sent by email).
- Skills installed in ~/.claude/skills: 8hack, hack-economic-model, hack-plain-voice, hack-rubric-check, hack-venture-gates. Install sentence on /me -> Start or /hackathon/skills; if `/8hack` missing -> `/reload-skills`.
- `/8hack start`: after 10:30, team finals idea -> scan -> gate; writes "8hack-start" page.
- `/8hack check`: at every checkpoint, status vs plan + one cut; rewrites "8hack-check".
- `/8hack video`: idea video + abstract, upload by 12:30.
- Both pages go on the jury card. Also: rubric check, economic model (jury reads it for gate 2 financial), venture gates, plain-voice demo script.
**How to apply:** teammates' Claudes need the same MCP + skills; use rubric-check before 16:45 pitch deadline.
