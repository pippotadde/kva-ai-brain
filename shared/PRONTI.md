# PRONTI A PARTIRE — condizione perfetta (14.11)
Owner: Claude di Filippo. Ognuno spunta i propri punti nel proprio `agents/<nome>/status.md` (riga `PRONTI: x/7`).
Fonte: skill ufficiale 8hack (`~/.claude/skills/8hack/references/event-2026-11-14.md`), che vince sul RULES.md.

## A. Ogni persona (Filippo, Giorgia, Sian) — entro le 10:30
Comandi da lanciare nel terminale (Linux/WSL):

```bash
# 1. Server MCP della piattaforma KVA
claude mcp add --scope user --transport http hack https://c8-hackathon.kakashi.ventures/api/mcp
# 2. Skill ufficiale 8hack (+ 4 skill compagne) in ~/.claude/skills
curl -fsSL https://c8-hackathon.kakashi.ventures/hackathon/8hack/install.sh | HACK_CLIENT=claude-code sh
# 3. Verifica: deve dare 5e0879b2...c431006 e 38851
sha256sum ~/.claude/skills/8hack/SKILL.md && wc -c < ~/.claude/skills/8hack/SKILL.md
# 4. Aggiorna repo e canale
cd <repo> && git pull --rebase && bash scripts/coord.sh sync
```

Poi, a mano:
5. Riavviare Claude Code → `/mcp` → `hack` → Authenticate → codice via email (invito PERSONALE, non quello di un altro).
6. Sulla pagina `/me` della piattaforma: leggere lo slug del progetto (`hack-...`), premere «Show the key», mettere in `.env` la riga `AI_GATEWAY_API_KEY=...` (MAI nel repo; `.env` è già in `.gitignore`). Questa chiave risolve il problema "chiave Gemini": è del team, solo per il PRODOTTO, non per Claude Code.
7. Nel proprio Claude: «8hack self-check» → tutti `ok` (o `not yet` prima delle 10:30).

Dopo le 10:30 (i team vengono rifatti): `/mcp → hack → Reconnect`, rileggere lo slug e la chiave su `/me`.

## B. Team — condizione perfetta per partire alle 10:30
- [ ] 3/3 persone con `hack` collegato e self-check ok
- [ ] Repo `pippotadde/kva-ai-brain` PUBBLICO (Filippo, dopo controllo segreti) e registrato con `set_team_repo`
- [ ] Idea scelta + riserva, track deciso (o progetto libero) — scadenza track 12:15
- [ ] Ruoli della mattina assegnati: video 50s (chi gira/monta), abstract 1200 caratteri, pagina `8hack-start`
- [ ] NIENTE creato sulla piattaforma prima delle 10:30 (`8hack-start` prima delle 10:30 = segnato "early")

## C. Scadenze della giornata
| Ora | Cosa | Chi |
|---|---|---|
| 10:30 | Team fissati, si parte; `8hack-start` | tutti / Sian |
| 12:15 | Track scelto o cambiato (su `/me`) | Filippo |
| **12:30** | **Video MP4 ≤50s ≤25MB + abstract ≤1200 caratteri.** Gate 1: decide chi passa alle 13:30 | Sian |
| 13:30 | Fase II solo per i team scelti | — |
| 14:00–16:30 | Build | Giorgia (+ tutti) |
| 16:30 | Validazione finanziaria — modello economico salvato (`update_economic_model`) | Filippo |
| **16:45** | **Artifact genere `pitch` + deck + repo pubblico + modello economico**: dopo, tutto chiuso | tutti |
| 17:05 | Show-off 5:00 a team. Gate 2 = classifica finale | tutti |

Valutazione: criteri 1–7 con pesi per track (non i 5 criteri 1–5 di RULES.md). Pitch: pubblicarne uno presto e ripubblicarlo con lo stesso titolo. Dichiarare modelli e strumenti AI usati (§7).
