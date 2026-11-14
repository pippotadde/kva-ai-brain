---
name: 8hack-copilot
description: KVA official 8hack co-pilot (MCP server `hack` + skills): setup, commands, deadlines for 14.11
metadata:
  type: reference
---
KVA hackathon co-pilot "8hack" (slide shown on 2026-11-14). Related: [[hackathon-rules]], [[next-steps]].
- MCP server `hack`: https://c8-hackathon.kakashi.ventures/api/mcp — Filippo's machine: added, authenticated OK 2026-11-14 09:5x. Team project slug (pre-10:30): hack-hackathon-tfc05f759e056dec375df657. After team re-formation at 10:30: /mcp -> hack -> Reconnect and re-read slug on /me. Jury card requires: video, abstract, pitch, repo (public), economic model; deck/start/check optional. Pitch deadline 16:45, track choice closes 12:15.
- Skills installed in ~/.claude/skills: 8hack, hack-economic-model, hack-plain-voice, hack-rubric-check, hack-venture-gates. Install sentence on /me -> Start or /hackathon/skills; if `/8hack` missing -> `/reload-skills`.
- `/8hack start`: after 10:30, team finals idea -> scan -> gate; writes "8hack-start" page.
- `/8hack check`: at every checkpoint, status vs plan + one cut; rewrites "8hack-check".
- `/8hack video`: idea video + abstract, upload by 12:30.
- Both pages go on the jury card. Also: rubric check, economic model (jury reads it for gate 2 financial), venture gates, plain-voice demo script.
**How to apply:** teammates' Claudes need the same MCP + skills; use rubric-check before 16:45 pitch deadline.
