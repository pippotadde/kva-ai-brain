# AI ONBOARDING — leggimi per primo

> **Per la persona:** apri Claude Code nella cartella della repo e scrivi:
> *"Leggi docs/AI_ONBOARDING.md, sono <Giorgia|Sian>. Prepara il mio ambiente e collegati al canale di coordinamento."*
> Il resto lo fa Claude, chiedendoti solo le cose che servono (password, login, chiave API).

> **Per Claude:** questo file ti dà tutto il contesto. Seguilo in ordine. Parla con la persona in italiano; codice, commenti e commit in inglese.

---

## 1. Missione

**VINCERE** l'hackathon "AI brain for industry" di Kakashi Venture Accelerator (KVA), **sabato 14 novembre 2026, 09:30–18:30 CET**, online (noi tre lavoriamo insieme a casa di Giorgia). Tutto quello che fai si misura su una domanda: *alza il voto della giuria?*

Il team è di 3 studenti di Ingegneria Informatica al PoliTo. Programmano bene (olimpiadi di informatica, aree IT di Team ASTRA e HKN, CyberChallenge), ma **non conoscono l'AI applicata né un settore industriale**: quando servono concetti di AI, spiegali in modo semplice e concreto.

**Come lavorare con la tua persona:** sta anche studiando per gli esami e non ha orari fissi prima di sabato. Sii efficiente: proponi il prossimo passo più utile, fai tu il lavoro meccanico, chiedi solo quello che serve davvero. Non fissare orari: lavora per **passi in ordine** (sezione 7).

## 2. La gara

- **Tema aperto.** "Scegli un problema reale di AI applicata e risolvilo" con memoria condivisa, ontologie o AI brain su misura. **Nessuno ci assegna un problema**: lo scegliamo noi, prima di sabato.
- **Le domande di KVA** (il cuore del tema):
  - Memoria: come capisce una memoria che una regola è stata superata? Come scrivono più agenti nella stessa memoria senza contraddirsi? Come si registra *perché* è stata presa una decisione?
  - Ontologie: come si costruisce un'ontologia? Come si aggiorna quando l'azienda cambia modo di lavorare? Come la usa un agente per *ragionare* e non solo per cercare?
- **I 7 spunti di KVA** (facoltativi): rendere accessibile a tutti uno strumento da specialisti; pipeline per dataset piccoli e grandi; ontologia da un corpus di documenti; memoria dell'agente visibile e correggibile dalle persone; modelli decisionali integrati con l'agente; anonimizzazione prima della memoria; scatola nera per agenti che compiono azioni critiche.
- **Regole chiave** (fonte: https://github.com/kakashi-ventures/hackathon/blob/main/RULES.md):
  - si possono portare idea, dataset (con diritto d'uso), librerie e modelli open source;
  - il **prodotto va costruito principalmente durante l'evento** → prima di sabato solo ricerca, dati, business e test usa e getta in `prototype/`; il codice del prodotto si scrive sabato in `src/`;
  - vanno **dichiarati gli strumenti AI usati**; il codice va in una **repo pubblica**;
  - consegne obbligatorie prima delle presentazioni delle 12:30 e delle 17:00.
- **Voto della giuria** (1–5 per criterio):

| Criterio | Peso |
|---|---|
| Aderenza al tema (memoria / ontologie / AI brain) — decide anche i pareggi | 25% |
| Qualità tecnica di ciò che funziona il giorno | 25% |
| Problema reale e impatto per un'industria | 25% |
| Business case (verificato alle 16:30) | 20% |
| Chiarezza della demo | 5% |

- **Giuria:** KVA è un venture studio AI che investe in startup (fondatori Federico Bottino e Alberto Trivero; controllato dal Gruppo Excellence, consulenza per banche, assicurazioni e grandi aziende). Pensano da investitori. Davide Lai è un ricercatore: aspettarsi domande tecniche su memoria e ontologie. Dettagli in `docs/jury.md`.

## 3. Team e modello di lavoro

| Persona | Area | Il suo Claude |
|---|---|---|
| Filippo | Organizzazione e business | Tiene il quadro completo (`.coord/SITUAZIONE.md`, `.coord/TASKS.md`) e il business plan |
| Giorgia | Architettura e prodotto | Agente tecnico |
| Sian | Idea, pitch, dati | Agente idea e pitch |

- Ognuno contribuisce a tutto, ma ogni area ha chi la segue: se dopo 5 minuti non c'è accordo, decide lui o lei.
- **Essere dinamici:** se qualcuno porta un'idea migliore, si cambia subito.
- Le persone parlano con il proprio Claude; **i Claude si coordinano tra loro sul canale `.coord/`** (sezione 6).

## 4. Dove trovare le cose

| Percorso | Contenuto |
|---|---|
| `docs/site/generale.html` | Regole, voto, team, **cosa fare entro sabato in ordine**, **sabato minuto per minuto** |
| `docs/site/problemi.html` | Come funziona la scelta, il tema, i 7 ambiti KVA spiegati, come si sceglie, proposte di Claude, business plan, dati e AI |
| `docs/site/lettura.html` | Come si costruisce un AI brain: le 5 parti, esempio di codice funzionante, ontologia in 20 minuti, strumenti, demo, business |
| `research/problems/candidates.md` | Rosa dei problemi con punteggi e fonti |
| `docs/jury.md` | Chi giudica, domande probabili |
| `docs/research-prompts.md` | Prompt per Deep Research (Gemini / ChatGPT) |
| `docs/PLAN.md`, `docs/TODO.md` | Strategia, rischi e piano B; lista completa per persona |
| `docs/SETUP.md` | Guida all'ambiente passo per passo |
| `business/business-plan.md`, `pitch/pitch-script.md` | Modelli da riempire |
| `research/market/`, `research/data/README.md` | Ricerche di mercato; registro dei dati con fonte e licenza |
| `prototype/` | Test usa e getta (prima di sabato) |
| `src/` | Il prodotto (solo sabato) |
| `scripts/check_env.sh`, `scripts/coord.sh` | Verifica dell'ambiente; canale di coordinamento |

Le stesse pagine sono pubblicate per le persone su un link claude.ai privato che Filippo condivide; tu leggi i file in `docs/site/`.

## 5. Prepara l'ambiente (Claude, fallo tu)

Lavora **dentro Linux** (WSL su Windows, Ubuntu nativo per Giorgia), con la repo in `~/kva-ai-brain`, mai in `/mnt/c/...`.

1. Se la repo non c'è ancora: la persona deve aver accettato l'invito (https://github.com/pippotadde/kva-ai-brain/invitations), poi `gh repo clone pippotadde/kva-ai-brain ~/kva-ai-brain`.
2. Controlla gli strumenti: `git --version; gh --version; uv --version; node --version; claude --version`. Installa quello che manca seguendo `docs/SETUP.md`; chiedi la password `sudo` alla persona quando serve.
3. Git: verifica `git config user.name` e `user.email`, chiedili se mancano. Verifica `gh auth status`; se non è loggato, fai lanciare alla persona `! gh auth login` (è interattivo).
4. `uv sync` nella repo.
5. Chiave API: la persona crea una chiave su https://aistudio.google.com/apikey; tu fai `cp .env.example .env` e **lei** la incolla nel file `.env`. Mai scrivere la chiave altrove, nei commit o nei messaggi.
6. `bash scripts/check_env.sh` → deve finire con **0 to fix**. Se qualcosa non va, sistemalo e riprova.

## 6. Collegati al canale di coordinamento

```bash
bash scripts/coord.sh init <giorgia|sian>
```

Leggi `.coord/README.md`, `.coord/SITUAZIONE.md`, `.coord/TASKS.md`; scrivi il primo `.coord/agents/<nome>/status.md`; poi `bash scripts/coord.sh sync`. Suggerisci alla persona di tenere aperto un secondo terminale con `bash scripts/coord.sh watch` (sincronizza ogni 60 secondi).

**Regole del canale (obbligatorie):**
1. **Prima di ogni compito:** `sync`, leggi SITUAZIONE, TASKS, `inbox` e gli status degli altri.
2. **Ogni file ha un solo autore.** Scrivi solo in `agents/<te>/`, nei tuoi messaggi, nelle tue decisioni e nei file `shared/` di cui sei owner. Per cambiare altro, manda un messaggio.
3. **Aggiorna il tuo `status.md`** quando finisci qualcosa, ti blocchi o cambi direzione, poi `sync`.
4. **Le scelte che toccano gli altri** (problema, nomi, formati dei dati, architettura, numeri del pitch) vanno in `coord.sh decide` o in un messaggio a Filippo. Mai decidere in silenzio.
5. **Fonti sempre.** Ogni numero o fatto per il pitch ha un link; se non ce l'ha, scrivilo.

## 7. Cosa fare entro sabato, in ordine (senza orari)

1. **Ambiente e canale** (sezioni 5 e 6).
2. **Due idee a testa (entro venerdì sera):** aiuta la persona a leggere `docs/site/metodo.html` ("Scegliere l'idea": segnali di KVA, 5 strade per trovare idee, scheda, filtro sì/no, business, scheletro tecnico) e a trovare **2 idee**. Puoi partire anche dalle proposte di `docs/site/problemi.html`, ma un'idea propria va benissimo. Scrivi le 2 schede compilate in `.coord/agents/<nome>/idee.md`. Segnali completi di KVA: `research/kva-interests.md`. **Non scegliere l'idea finale:** si decide insieme in call venerdì sera.
3. **Lettura serale:** `docs/site/lettura.html`, con l'esercizio della sezione 3.
4. **Scelta in call** di principale + riserva, registrata con `coord.sh decide`. Dopo la scelta: dati, mappa del settore, prova in `prototype/`, business (anche con un lavoro notturno di Claude su un ramo separato).

Facoltativo: sentire una persona del settore. I passi successivi (dati, business plan, architettura, pitch) verranno definiti dopo la scelta e scritti in `.coord/TASKS.md`.

## 8. Approfondimento dei candidati: cosa guardare

**Giorgia (architettura e prodotto)** — per ogni candidato, un test di 30 minuti in `prototype/<lettera>/`:
- Si trovano documenti veri da usare? (formato, quantità, licenza)
- Un LLM ne estrae entità e relazioni affidabili in JSON, dato l'elenco di classi e relazioni ammesse?
- Si rappresenta "regola X sostituisce regola Y" e si risponde a una domanda seguendo le relazioni?
- Qual è la demo da 90 secondi e cosa serve per costruirla in 2h30?
- Risultato: `prototype/<lettera>/NOTES.md` con "fattibile / rischioso / no" e perché.

**Business (Filippo, aiutato da Sian)** — per ogni candidato:
- Cliente preciso, chi paga, quanto costa oggi il problema (con fonte)?
- Quanti clienti potenziali in Italia ed Europa, quanto pagherebbero, chi sono i concorrenti?
- La storia da 30 secondi per aprire il pitch.
- Chi possiamo sentire (contatti, professori PoliTo, LinkedIn)?
- Risultato: `.coord/agents/filippo/work/<lettera>-business.md`. Struttura del business plan: sezione "Come si costruisce il business plan" in `docs/site/problemi.html`.

**Filippo (organizzazione e business)** — Deep Research, dati disponibili, business, sintesi con i voti sui 5 criteri in `.coord/SITUAZIONE.md`.

**Sian (idea, pitch, dati)** — la storia da 30 secondi, chi possiamo sentire nel settore, dati disponibili.

## 9. Principi del prodotto e della demo

- **L'AI estrae e spiega; le regole decidono.** Le deduzioni importanti ("Mario non è abilitato") vengono da regole nel codice che seguono il grafo, non da un'intuizione del modello.
- **Provenienza ovunque:** ogni fatto mostrato ha documento, autore, data. Le regole superate si chiudono, non si cancellano.
- **Poco ma funzionante:** una demo piccola che funziona dal vivo batte un progetto grande a metà.
- **Stack di base:** Python 3.12 + uv, `networkx` per il grafo, `streamlit` + `pyvis` per l'interfaccia, `google-genai` / `anthropic` per i modelli. Giorgia può cambiarlo.
- **Demo sicura:** stessi dati e stesse domande sempre; i passaggi lenti dell'AI preparati in anticipo; video di riserva.

## 10. Sabato: le regole che contano

- Scaletta completa in `docs/site/generale.html`.
- 09:00 ritrovo da Giorgia; `git pull`, `check_env.sh` verde, `coord.sh watch` acceso. **Un solo computer con l'audio nella call KVA**, gli altri muti.
- 13:00–14:00 pranzo (cucina Giorgia) + architettura definitiva e divisione dei file.
- 14:00–16:00 costruzione; salvataggi su GitHub ogni 20–30 minuti; `main` sempre funzionante.
- **16:00 stop alle funzioni nuove**, video di riserva registrato.
- Consegna finale: README con descrizione, come si avvia e **strumenti AI usati**.

## 11. Regole di lavoro con il codice

- `git pull --rebase` prima di ogni push; commit piccoli e frequenti.
- Ognuno tocca solo i file assegnati.
- Mai committare `.env` o chiavi: sabato la repo diventa pubblica.
- Librerie: `uv add <nome>`, poi commit di `pyproject.toml` e `uv.lock`.
- Dati: prima si registrano in `research/data/README.md` con fonte e licenza.

## 12. Primo messaggio quando hai finito il setup

```bash
bash scripts/coord.sh msg filippo "Setup completato" "Ambiente verde (check_env 0 to fix), canale collegato. Prossimo: opinione sui problemi."
```
