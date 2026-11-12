# Project rules for Claude Code (all team members)

New here? Read `docs/AI_ONBOARDING.md` first: full context, environment setup, coordination channel.

Goal: WIN the KVA hackathon "AI brain for industry" (Sat 14 Nov 2026). Judging: fit with challenge (memory/ontologies/AI brains) 25% — also tie-breaker; technical quality of what works on the day 25%; real industry problem & impact 25%; business case 20%; demo clarity 5%.

## Roles
- Filippo: team lead, coordination, everything. His Claude is the **director** (keeps `.coord/SITUAZIONE.md` and `.coord/TASKS.md`).
- Giorgia: architecture and product.
- Sian: idea, business, pitch, data.
Everyone contributes everywhere; the area owner decides. Switch fast when a better idea appears.

## Coordination between the three Claudes (mandatory)
- Channel: `.coord/` (git branch `coord`, separate worktree). Rules in `.coord/README.md`.
- Before each task: `bash scripts/coord.sh sync`, read `.coord/SITUAZIONE.md`, `.coord/TASKS.md`, `bash scripts/coord.sh inbox`, other agents' `status.md`.
- One writer per file: write only in `.coord/agents/<me>/`, your own messages/decisions, and `shared/` files you own.
- Update `.coord/agents/<me>/status.md` when you finish, get blocked or change direction, then sync.
- Choices that affect others (problem, names, data formats, architecture, pitch numbers): `coord.sh decide` or message the director. Never decide silently.

## Working rules
- Talk to the user in Italian; code, comments, commit messages in English.
- Smallest change that works. A working demo beats a half-working big feature.
- Before Saturday: research, data, business, throwaway tests in `prototype/` only. The product is written on the day in `src/` (rules §7).
- `main` must always run. `git pull --rebase` before pushing; small commits every 20-30 minutes.
- Touch only the files assigned to you; ask before editing someone else's.
- NEVER commit secrets. API keys live only in `.env` (gitignored). The repo becomes public on the day.
- Dependencies via `uv add`; data registered in `research/data/README.md` with source and licence.
- Every fact the product shows carries its provenance (source document, author, date) — core to the challenge.
- Every number for the pitch has a source link; say so when it does not.
