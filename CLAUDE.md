# Project rules for Claude Code (all team members)

Goal: WIN the KVA hackathon "AI brain for industry". Judging: fit with challenge (memory/ontologies/AI brains) 25% — also tie-breaker; technical quality of what works on the day 25%; real industry problem & impact 25%; business case 20%; demo clarity 5%.

## Working rules
- Talk to the user in Italian; code, comments, commit messages in English.
- Smallest change that works. A working demo beats a half-working big feature.
- `main` must always run. Pull with `git pull --rebase` before pushing; push small commits every 20-30 minutes.
- Each person owns separate files/folders (agreed at the architecture sync). Do not edit someone else's files without asking them.
- NEVER commit secrets. API keys live only in `.env` (gitignored). The repo becomes public on the day.
- Large data files stay out of git; document their source and licence in `research/data/`.
- Every fact the product shows should carry its provenance (source document, author, date) when possible — it is core to the challenge.

## Ownership
- Giorgia: architecture and tech decisions.
- Filippo: timing, priorities, business case, repo/integration.
- Sian: product idea, demo UI, pitch.
