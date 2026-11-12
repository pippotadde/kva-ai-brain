# KVA AI Brain

Team project for the Kakashi Venture Accelerator hackathon **"AI brain for industry"** (Turin, 14 November 2026).

Team: Filippo Taddei, Giorgia Ferraro, Sian Caratelli.

> The project idea, problem and pitch are being finalised. This README will describe the product on the day.

## Repository layout

| Folder | Purpose |
|---|---|
| `docs/` | `AI_ONBOARDING.md` (read first), team brief, `TODO.md`, `PLAN.md` (timeline), `SETUP.md` (environment), `jury.md` |
| `scripts/` | `check_env.sh` (is my machine ready?), `smoke_llm.py` (does my API key work?), `coord.sh` (AI coordination channel on branch `coord`) |
| `research/problems/` | Problem discovery: candidate industry problems, evidence, scoring |
| `research/market/` | Market sizing, competitors, customer profiles |
| `research/data/` | Notes on datasets we can legally use (source, licence) |
| `business/` | Business case and financial validation material |
| `pitch/` | Pitch script and slides |
| `prototype/` | Friday dry-run and throwaway experiments (not the product) |
| `src/` | The product, built on the day |
| `data/` | Small datasets used by the demo (large files stay out of git) |

## Running

```bash
uv sync                      # install Python 3.12 + dependencies
cp .env.example .env         # then paste your API key
bash scripts/check_env.sh    # must end with 0 to fix
```

Full setup guide: `docs/SETUP.md`. Secrets go in `.env`, never in git.

## AI tools used

Declared as required by the rules (section 7): Claude Code, Gemini, ChatGPT; models used inside the product are listed here on the day.
