# AI ONBOARDING — leggimi per primo

> **Per la persona:** apri Claude Code nella cartella della repo e scrivi:
> *"Leggi docs/AI_ONBOARDING.md, sono <Giorgia|Sian>. Prepara il mio ambiente e collegati al canale di coordinamento."*
> Il resto lo fa Claude, chiedendoti solo le cose che servono (login, chiave API).

> **Per Claude:** questo file ti dà tutto il contesto. Seguilo in ordine. Parla con la persona in italiano; codice, commenti e commit in inglese.

---

## 1. Missione

**VINCERE** l'hackathon "AI brain for industry" di Kakashi Venture Accelerator (KVA), **sabato 14 novembre 2026, 09:30–18:30 CET**, online. Tutto quello che fai si misura su una domanda: *alza il voto della giuria?*

Il team è di 3 persone, studenti di Ingegneria Informatica al PoliTo. Tutti sanno programmare bene (olimpiadi di informatica, aree IT di Team ASTRA e HKN, CyberChallenge), ma **non conoscono l'AI applicata né un settore industriale**: spiega i concetti AI in modo semplice e concreto quando servono.

## 2. La gara in breve

- **Tema aperto:** "scegli un problema reale di AI applicata e risolvilo" con memoria condivisa, ontologie o AI brain su misura. **Nessuno ci assegna un problema**: lo scegliamo noi. KVA ha suggerito 7 spunti (in `research/problems/candidates.md` e nella pagina del team).
- **Regole chiave** (fonte: https://github.com/kakashi-ventures/hackathon/blob/main/RULES.md):
  - si possono portare idea, dataset (con diritto d'uso), librerie e modelli open source;
  - il **prodotto va costruito principalmente durante l'evento** → prima di sabato si fanno solo ricerca, dati, business e test usa e getta in `prototype/`; il codice del prodotto si scrive sabato in `src/`;
  - vanno **dichiarati gli strumenti AI usati**; il codice va in una **repo pubblica**;
  - checkpoint obbligatori prima delle presentazioni delle 12:30 e delle 17:00.
- **Voto della giuria** (1–5 per criterio):

| Criterio | Peso |
|---|---|
| Aderenza al tema (memoria / ontologie / AI brain) — decide anche i pareggi | 25% |
| Qualità tecnica di ciò che funziona il giorno | 25% |
| Problema reale e impatto per un'industria | 25% |
| Business case (verificato alle 16:30) | 20% |
| Chiarezza della demo | 5% |

- **Sabato:** 10:15 talk, 10:30–12:30 ideazione, 12:30 prima presentazione, **14:00–16:30 costruzione (solo 2h30)**, 16:30 verifica finanziaria, 17:00 demo finale, 18:30 premiazione.
- **Giuria:** KVA è un venture studio AI che investe in startup (fondatori Federico Bottino e Alberto Trivero; controllato dal Gruppo Excellence, consulenza per banche, assicurazioni, grandi aziende). Pensano da investitori. Dettagli in `docs/jury.md`.

## 3. Team, ruoli e modello di lavoro

| Persona | Ruolo | Il suo Claude |
|---|---|---|
| Filippo | Team leader, coordinamento, tutto | **Regista**: quadro completo, compiti, decisioni globali |
| Giorgia | Architettura e prodotto | Agente tecnico |
| Sian | Idea, business, pitch, dati | Agente idea/business |

- Ognuno contribuisce a tutto, ma **ogni area ha un responsabile che decide**. Se dopo 5 minuti non c'è accordo, decide il responsabile.
- **Essere dinamici:** se qualcuno porta un'idea migliore, si cambia subito.
- Le persone parlano con il proprio Claude. **I Claude si coordinano tra loro sul canale `.coord/`** (sezione 6).

## 4. Mappa della repo

| Percorso | Contenuto |
|---|---|
| `CLAUDE.md` | Regole permanenti per tutti i Claude |
| `docs/PLAN.md` | Piano ora per ora fino a sabato, rischi, piano B |
| `docs/TODO.md` | Lista completa delle cose da fare, per persona |
| `docs/SETUP.md` | Guida all'ambiente (per la persona) |
| `docs/jury.md` | Chi giudica e domande probabili |
| `docs/research-prompts.md` | Prompt per Deep Research (Gemini / ChatGPT) |
| `research/problems/candidates.md` | Rosa dei problemi con punteggi |
| `research/market/`, `research/data/` | Ricerche di mercato, registro dei dati |
| `business/business-plan.md` | Modello del business plan |
| `pitch/pitch-script.md` | Copione del pitch da 3 minuti |
| `prototype/` | Test usa e getta (prima di sabato) |
| `src/` | Il prodotto (solo sabato) |
| `scripts/check_env.sh` | Verifica dell'ambiente |
| `scripts/coord.sh` | Canale di coordinamento tra AI |
| `.coord/` | Il canale (ramo git `coord`, cartella separata dal codice) |

## 5. Prepara l'ambiente (Claude, fallo tu)

Lavora **dentro Linux** (WSL su Windows, Ubuntu nativo per Giorgia), con la repo in `~/kva-ai-brain`, mai in `/mnt/c/...`.

1. Controlla cosa c'è: `git --version; gh --version; uv --version; node --version; claude --version`.
2. Installa quello che manca seguendo `docs/SETUP.md` (sezione 1). Chiedi la password `sudo` alla persona quando serve.
3. Git: verifica `git config user.name` e `user.email`; se mancano chiedili. Verifica `gh auth status`; se non è loggato, fai lanciare alla persona `gh auth login` (è interattivo: suggerisci di scrivere `! gh auth login`).
4. `uv sync` nella cartella della repo.
5. Chiave API: chiedi alla persona di creare una chiave su https://aistudio.google.com/apikey, poi `cp .env.example .env` e falla incollare **da lei** nel file `.env`. Non scrivere mai la chiave in altri file, nei commit o nei messaggi.
6. `bash scripts/check_env.sh` → deve finire con **0 to fix**. Se qualcosa non va, sistemalo e riprova.

## 6. Collegati al canale di coordinamento

```bash
bash scripts/coord.sh init <giorgia|sian>
```

Poi leggi `.coord/README.md` (regole del canale), `.coord/SITUAZIONE.md` e `.coord/TASKS.md`, e scrivi il primo `.coord/agents/<nome>/status.md`. Infine `bash scripts/coord.sh sync`.

Suggerisci alla persona di tenere aperto un secondo terminale con `bash scripts/coord.sh watch` (sincronizza ogni 60 secondi).

**Regole del canale (obbligatorie):**
1. **Prima di ogni compito:** `sync`, leggi SITUAZIONE, TASKS, `inbox` e gli status degli altri.
2. **Ogni file ha un solo autore.** Scrivi solo in `agents/<te>/`, nei tuoi messaggi, nelle tue decisioni e nei file `shared/` di cui sei owner. Per cambiare altro, manda un messaggio.
3. **Aggiorna il tuo `status.md`** quando finisci qualcosa, ti blocchi o cambi direzione, poi `sync`.
4. **Le scelte che toccano gli altri** (problema, nomi, formati dei dati, architettura, numeri del pitch) vanno in `coord.sh decide` o in un messaggio al regista. Mai decidere in silenzio.
5. **Fonti sempre.** Ogni numero o fatto da usare nel pitch ha un link. Se non ce l'ha, scrivilo.

## 7. Il calendario

| Quando | Cosa |
|---|---|
| **Giovedì sera** | Setup + canale. Lettura della rosa dei problemi. Opinione personale scritta in `.coord/agents/<nome>/work/opinione-problemi.md`. Studio del PDF di teoria (in arrivo in `docs/`). |
| **Venerdì 09:00–12:30** | Ricerca e test sui 2–3 candidati migliori (sezione 8). Trovare una persona del settore da sentire per 10 minuti. |
| **Venerdì 13:30–14:00** | **Decisione:** problema principale + riserva, votando sui criteri della giuria. |
| **Venerdì pomeriggio** | Sul problema scelto: dati, business plan, test di fattibilità più serio, ambiente. |
| **Venerdì sera** | Architettura e divisione dei file; 2 prove del pitch; a letto presto. |
| **Sabato** | Scaletta nella pagina del team e in `docs/PLAN.md`. |

## 8. Venerdì mattina: cosa approfondire

**Giorgia (architettura e prodotto)** — per ogni candidato, un test di 30 minuti in `prototype/<lettera>/`:
- Si trovano documenti veri da usare? (formato, quantità, licenza)
- Un LLM riesce a estrarne entità e relazioni affidabili in JSON?
- Riusciamo a rappresentare "regola X sostituisce regola Y" e a fare una domanda che segue le relazioni?
- Quale sarebbe la demo da 90 secondi e cosa serve per costruirla in 2h30?
- Risultato: `prototype/<lettera>/NOTES.md` con "fattibile / rischioso / no" e perché.

**Sian (idea, business, pitch, dati)** — per ogni candidato:
- Chi è il cliente preciso, chi paga, quanto costa oggi il problema (con fonte)?
- Quanti clienti potenziali in Italia ed Europa, quanto pagherebbero, chi sono i concorrenti?
- Qual è la storia da 30 secondi per aprire il pitch?
- Chi possiamo sentire oggi (contatti, professori, LinkedIn)?
- Risultato: `.coord/agents/sian/work/<lettera>-business.md`.

**Filippo (regia)** — sintesi per la decisione delle 13:30: tabella con i voti sui 5 criteri, basata su ricerche e test, in `.coord/SITUAZIONE.md`.

## 9. Regole di lavoro con il codice

- `main` deve sempre funzionare. `git pull --rebase` prima di ogni push; commit piccoli ogni 20–30 minuti.
- Ognuno tocca solo i file assegnati (si decide venerdì sera).
- Mai committare `.env` o chiavi: sabato la repo diventa pubblica.
- Librerie: `uv add <nome>`, poi commit di `pyproject.toml` e `uv.lock`.
- Dati: prima si registrano in `research/data/README.md` con fonte e licenza.
- Nel prodotto, ogni fatto mostrato deve avere la sua **provenienza** (documento, autore, data): è il cuore del tema.

## 10. Primo messaggio da mandare quando hai finito

```bash
bash scripts/coord.sh msg filippo "Setup completato" "Ambiente verde (check_env 0 to fix), canale collegato. Prossimo: opinione sui problemi."
```
