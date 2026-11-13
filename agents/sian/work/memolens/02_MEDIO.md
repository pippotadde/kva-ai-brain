# MemoLens · Versione MEDIA (consigliata)

> Obiettivo: un **agente AI vero** che sbaglia davvero, una **memoria con versioni e provenienza**, un **grafo decisione → ricordo → fonte**, e il principio della giuria detto con le sue parole: *il modello capisce, il codice decide*.
> Si costruisce a strati sopra la versione FACILE (`01_FACILE.md`): se alle 15:30 uno strato non funziona, si torna allo strato prima e la demo regge.

---

## 1. L'idea in una frase

MemoLens è il registratore di volo degli agenti AI: per ogni azione mostra **quale ricordo è stato usato, da dove arriva, se era ancora valido**, trova da solo tutti i casi colpiti dallo stesso errore e permette di correggere il ricordo, lasciando traccia di tutto.

## 2. Cosa si aggiunge rispetto alla versione facile

| Strato | Novità | Perché alza il punteggio |
|---|---|---|
| A | **Agente LLM vero** con strumenti (leggere ordine, ricordare, rimborsare) | Tecnica: non è uno script, è un agente reale |
| B | **SDK MemoLens**: un "involucro" attorno agli strumenti dell'agente che registra tutto e invia in background tramite una coda | Dimostra "zero attese per il cliente" e "si collega con poche righe" |
| C | **Memoria con versioni**: ogni ricordo ha fonte, autore, valido dal / valido fino al, e quale ricordo sostituisce (*supersession*) | Tema: è il cuore della teoria OIDA della giuria |
| D | **Grafo della provenienza** (azione → ricordo → fonte) e casi simili calcolati sul grafo | Tema + tecnica: ragionamento sulle relazioni, visibile |
| E | **"Evidenza insufficiente"**: se due ricordi validi si contraddicono e nessuna regola decide, MemoLens lo dice invece di indovinare | Tema: astensione quando mancano prove, punto chiave del paper della giuria |
| F | Sentinella con regole + un controllo statistico semplice | Tecnica |
| G | Variante industriale come secondo dataset | Problema reale + tema ("industry") |

## 3. Business plan

Base: documento `MemoLens_Hackathon_Track4.docx` (fonti tra parentesi quadre). Le cifre "stima del team" vanno dichiarate come tali.

### 3.1 Problema e impatto
- Gli agenti agiscono con soldi veri, usando una memoria invisibile. L'errore non rompe niente: l'agente risponde gentile e sbaglia i conti, e lo ripete migliaia di volte.
- 51% delle aziende ha già avuto un danno dall'AI [9]; incidenti documentati da 233 (2024) a 362 (2025) [7][8]; Gartner: oltre 40% dei progetti agentici cancellati entro il 2027, anche per controlli sul rischio inadeguati [6].
- Un guasto grave costa in mediana 2 mln $/ora, 1 mln $ per chi ha visibilità completa (New Relic) [15]: chi vede prima perde meno.
- Caso Air Canada: l'azienda risponde del suo agente [10].

### 3.2 Cliente, utente, compratore
| Ruolo | Chi | Cosa vuole |
|---|---|---|
| Utente quotidiano | Customer care, operations | Capire in un minuto perché l'agente ha fatto una cosa |
| Compratore | Responsabile e-commerce / operations, CFO di PMI | Non perdere soldi, numeri chiari |
| Influenza | Compliance, DPO, assicurazione | Registro esportabile per AI Act e audit |
| Installazione | Sviluppatore che ha costruito l'agente | Poche righe di codice, niente rallentamenti |

### 3.3 Prezzi (stima del team, coerente con [21][22])
Free 0 € (1 agente, 5.000 azioni/mese) · Starter 49 €/mese · Business 299 €/mese (casi simili, 12 mesi di storico, report AI Act) · Enterprise da 1.500 €/mese (installazione presso il cliente, SSO).

### 3.4 Conti
- **Costo per cliente Business**: circa 35 €/mese (spiegazioni AI generate solo per 1 azione su 5 + server). Margine lordo circa 88% (stima del team). ⚠️ Il documento usa i prezzi di GPT-4o mini [24]: se usiamo Claude, ricalcolare con il listino ufficiale del modello scelto.
- **Tre anni (scenario base, stima del team)**: clienti medi 20 → 110 → 300; ricavi 43 k€ → 306 k€ → 965 k€; risultato −52 k€ → +16 k€ → +355 k€. Pareggio nel 2° anno.
- **ROI per il cliente**: incidente Gianpaolo 29.400 € senza MemoLens contro 1.450 € con; abbonamento 3.588 €/anno → circa 8x (stima del team).

### 3.5 Mercato
- Agenti AI: 7,84 → 52,62 mld $ (2025–2030, CAGR 46,3%) [1]; conferma Grand View: 50,31 mld $ al 2030 [2].
- TAM osservabilità agenti: 0,4 mld $ (2025) → 7,1 mld $ (2035) [3]. SAM Europa PMI ~200 mln € al 2028 e SOM ~1 mln €/anno al 3° anno: stime del team.
- Italia: imprese con AI dal 5,0% (2023) al 16,4% (2025) [19]; PMI 15,7% contro grandi 53,1%, ostacolo principale: competenze [20]. Serve uno strumento che parli la loro lingua.

### 3.6 Go-to-market (primi 10 clienti)
1. **Design partner**: 3 PMI e-commerce italiane che hanno appena messo un agente nel customer care; gratis per 3 mesi in cambio di dati e citazione.
2. **Integrazioni pronte**: SDK Python/JS + connettori per i framework di agenti più usati; in seguito plugin per piattaforme e-commerce.
3. **Canale**: agenzie e integratori che costruiscono agenti per PMI (vendono MemoLens insieme all'agente). Per l'industria: integratori di sistemi MES/ERP.
4. **Contenuto**: "Caso Gianpaolo" come storia ricorrente, calcolatore del rischio sul sito.

### 3.7 Concorrenti e vantaggio
LangSmith, Langfuse (tracce tecniche per sviluppatori) [21][22]; Datadog, New Relic, Arize (enterprise, complessi); Mem0, Zep (danno memoria, non la rendono verificabile) [23]. **MemoLens collega decisione e ricordo nello stesso posto, in linguaggio semplice, con correzione e storico delle versioni.** Langfuse acquisito da ClickHouse a inizio 2026 [25]: il settore è strategico.

### 3.8 Perché ora
AI Act art. 12: log automatici per tutta la vita dei sistemi ad alto rischio, dal 2 dic 2027 (Allegato III) e 2 ago 2028 (Allegato I) [16][17]; sanzioni fino a 15 mln € o 3% del fatturato [18].

## 4. Architettura

```
 LATO CLIENTE (veloce)                         LATO AZIENDA (in background)
┌──────────────────────────────┐             ┌──────────────────────────────────────┐
│ Chat del negozio (Streamlit) │             │  MemoLens                             │
│        │                     │             │                                       │
│        ▼                     │  resoconto  │  ┌──────────┐   ┌──────────────────┐  │
│ Agente LLM (tool use)        │  (coda +    │  │ Ingest   │──▶│ Registro eventi  │  │
│   strumenti:                 │   thread)   │  │          │   │ SQLite           │  │
│   - leggi_ordine             │ ──────────▶ │  └──────────┘   └────────┬─────────┘  │
│   - ricorda(chiave)  ◀──┐    │             │                          ▼            │
│   - rimborsa(importo)   │    │             │  ┌───────────────────────────────┐    │
│        ▲                │    │             │  │ Grafo provenienza (networkx)  │    │
│   SDK MemoLens: avvolge │    │             │  │ Azione → Ricordo(v) → Fonte   │    │
│   ogni strumento        │    │             │  └───────┬───────────┬───────────┘    │
└─────────────────────────┼────┘             │          ▼           ▼                │
                          │                  │   Sentinella    Casi simili           │
┌─────────────────────────┴────┐             │   (regole +     (stesso ricordo       │
│ Memoria con versioni         │◀────────────│    statistica)   + stessa regola)     │
│ (SQLite: ricordi, versioni,  │  correzione │          ▼                            │
│  fonte, valido dal/al,       │  = nuova    │   Risolutore deterministico           │
│  sostituisce)                │  versione   │   VALIDO / SUPERATO / EVIDENZA        │
└──────────────────────────────┘             │   INSUFFICIENTE                       │
                                             │          ▼                            │
                                             │   Spiegazione LLM (+ dato originale)  │
                                             │          ▼                            │
                                             │   Dashboard: Timeline · Grafo ·       │
                                             │   Allarmi · Casi simili · Correzione  │
                                             └──────────────────────────────────────┘
```

**Scelta importante per 3 ore:** tutto in **un solo processo Streamlit**, con la coda in memoria e un thread che svuota la coda nel registro. Un server FastAPI separato è "più bello" ma costa tempo: aggiungerlo solo se avanza tempo (sotto, "Strato extra").

**"Se MemoLens è giù, l'agente continua":** se la scrittura nel registro fallisce, l'evento va in un file di coda (`queue.jsonl`) e viene reinviato. Nella demo si può mostrare con un interruttore "MemoLens offline".

## 5. Modello dei dati

**Ricordo (versione)** — tabella `memory_versions`
| Campo | Esempio |
|---|---|
| `memory_id` | `M-PRICE-SKU01` |
| `version` | 1 |
| `key` | "prezzo SKU-SCARPA-01" |
| `value` | 120 |
| `kind` | `catalog_price` (tipo di ricordo) |
| `source_doc` | "listino_2026-11-01.csv" |
| `author` | "import catalogo" |
| `valid_from` / `valid_to` | 2026-11-01 / (vuoto = ancora valido) |
| `supersedes` | ID della versione sostituita |
| `status` | `active` / `superseded` |

**Evento** — tabella `events`
`event_id, ts, agent_id, customer, tool, input, output, amount, memory_reads [memory_id+version], rule_version, conversation_id`

**Allarme** — `alert_id, event_id, rule, severity, euro_at_risk, status`

**Grafo** (costruito al volo dagli eventi)
- Nodi: `Azione`, `Ricordo(v)`, `Fonte`, `Cliente`, `Regola(v)`
- Archi: `Azione -USA-> Ricordo(v)`, `Ricordo(v) -DERIVA_DA-> Fonte`, `Ricordo(v2) -SOSTITUISCE-> Ricordo(v1)`, `Azione -RIGUARDA-> Cliente`, `Ricordo -CONTRADDICE-> Ricordo`

## 6. Come nasce il bug con un agente vero

Il rischio di un LLM vero è che *non* sbagli quando serve. Il bug va quindi messo **nei dati e negli strumenti**, non nella "fortuna" del modello:
- Lo strumento `leggi_ordine` restituisce cliente, articolo e data, **ma non il prezzo pagato** (succede davvero quando l'integrazione è fatta di fretta).
- La memoria contiene "prezzo SKU-SCARPA-01 = 120 €" (listino importato prima della promozione).
- Il prompt di sistema dice: "per un reso, rimborsa il prezzo dell'articolo".
- L'agente chiama `ricorda("prezzo SKU-SCARPA-01")` → 120 → `rimborsa(120)`.

La **correzione** si fa in due modi, entrambi tracciati: (1) nuova versione della regola "rimborso = prezzo pagato" e `leggi_ordine` che espone il prezzo pagato; (2) nuova versione del ricordo con `valid_to` sulla vecchia. Poi si ripete la conversazione: 80 €.

**Riserva:** temperatura 0 e conversazione registrata. Se l'agente risponde in modo diverso dal copione, la pagina Negozio può riprodurre la conversazione registrata (interruttore "modalità demo").

## 7. Il risolutore deterministico (il pezzo da mostrare alla giuria)

Regole scritte nel codice, non decise dall'LLM. Per ogni ricordo usato da un'azione:
1. Il ricordo era **valido** al momento dell'azione? (`valid_from ≤ ts < valid_to`) → altrimenti `SUPERATO`.
2. Esiste un dato **più specifico** per lo stesso fatto? (prezzo pagato nell'ordine > prezzo di listino) → il più specifico vince.
3. A parità di specificità, vince la **fonte con più autorità** (contratto > listino > email) e poi la **più recente**.
4. Se dopo i passi 1–3 restano due valori diversi → `EVIDENZA INSUFFICIENTE`: la scheda lo dice e propone di chiedere a una persona.

Frase per il pitch: **"Il modello capisce, il codice decide. E quando le prove non bastano, MemoLens lo dice invece di indovinare."**

## 8. Moduli del programma

| File in `src/` | Cosa fa | Chi | Strato |
|---|---|---|---|
| `models.py` | Modelli pydantic: Ricordo, Evento, Allarme, Regola | Giorgia | base |
| `store.py` | SQLite: memoria con versioni, eventi, allarmi | Giorgia | base/C |
| `memolens_sdk.py` | Involucro attorno agli strumenti: registra input, output, ricordi letti; mette in coda; thread di invio; file di riserva se fallisce | Giorgia | B |
| `shop_agent.py` | Agente LLM con 3–4 strumenti e prompt di sistema | Giorgia | A |
| `resolver.py` | Il risolutore deterministico (sezione 7) | Sian | C/E |
| `graph.py` | Costruisce il grafo da eventi e versioni; "casi simili" = tutte le azioni collegate alla stessa versione di ricordo e che violano la stessa regola | Sian | D |
| `sentinel.py` | Regole + controllo statistico (rimborso/pagato > 1; importo fuori dalla media dello stesso articolo) | Sian | F |
| `explain.py` | Spiegazione in italiano, risposta strutturata (cosa, perché, ricordo, fonte), cache, frase di riserva | Sian | base |
| `app.py` | Streamlit: Negozio, Timeline, Grafo (pyvis), Allarmi, Casi simili, Correzione | Giorgia + Filippo | base |
| `data/` | Dataset e-commerce + dataset fabbrica | Sian (stanotte) | G |

## 9. Collegamenti e strumenti

| Cosa | Scelta | Note |
|---|---|---|
| Agente | API `anthropic` con tool use, modello veloce (es. `claude-haiku-5-5`) | Riserva: `google-genai` con la chiave di un altro membro. Chiavi solo in `.env` |
| Spiegazioni | stesso modello, output strutturato JSON | sempre cache + frase fissa di riserva |
| Memoria e registro | SQLite (libreria standard di Python) | un file `memolens.db`, facile da azzerare prima della demo |
| Grafo | `networkx` + `pyvis` per disegnarlo | già installati |
| Interfaccia | `streamlit` | già installato |
| Strato extra | `fastapi` + `uvicorn` per un vero endpoint `/ingest` | `uv add fastapi uvicorn`, solo se avanza tempo |

## 10. Piano della giornata

| Ora | Giorgia (architettura) | Sian (dati, logica, pitch) | Filippo (business) |
|---|---|---|---|
| Venerdì notte | — | Dataset e-commerce + fabbrica; prompt spiegazione provato in `prototype/`; conversazione dell'agente provata 5 volte | Ricalcolo margine col modello scelto |
| 10:30–12:30 | Schema dati e nomi dei file (sezioni 5 e 8) | Storia, slide, prova del pitch delle 12:30 | Numeri nelle slide |
| 13:00–14:00 | Divide il lavoro, crea i file vuoti in `src/` | Rilegge il copione della demo | Domande della giuria |
| 14:00–14:45 | `models`, `store`, `app` scheletro (= versione facile) | `explain`, `sentinel` | testi della dashboard |
| 14:45–15:30 | `shop_agent` + `memolens_sdk` (strati A, B) | `resolver`, `graph` (strati C, D, E) | totali in euro, pagina casi simili |
| **15:30 controllo** | Funziona il giro completo con l'agente vero? **No → modalità demo con conversazione registrata** | | |
| 15:30–16:15 | Correzione + replay, grafo nella dashboard | Dataset fabbrica (strato G) | prova del pitch |
| 16:15–16:30 | **Stop funzioni nuove**, azzerare `memolens.db`, video di riserva | | |
| 16:30 / 17:00 | Guida la demo | Presenta | Numeri, video di riserva |

## 11. Copione della demo (3 minuti)

1. **(25 s)** Chat del negozio: Gianpaolo scrive "vorrei restituire le scarpe". L'agente vero risponde e rimborsa 120 €.
2. **(15 s)** "Resoconto ricevuto" in background. "Il cliente ha già finito, l'agente non ha aspettato niente."
3. **(25 s)** Allarme rosso: "Rimborso superiore al prezzo pagato (80 €)".
4. **(35 s)** Scheda: ricordo `prezzo SKU-SCARPA-01 v1 = 120 €`, fonte "listino 1 nov", autore "import catalogo". Il risolutore dice: **SUPERATO dal dato più specifico (prezzo pagato 80 €)**. Si mostra il grafo: azione → ricordo → fonte.
5. **(25 s)** Casi simili sul grafo: 37 clienti collegati allo stesso ricordo, 1.480 € a rischio.
6. **(30 s)** Correzione: nuova versione della regola con autore e data, la vecchia resta nello storico. Si ripete la richiesta: 80 €.
7. **(10 s)** Variante fabbrica: un clic sul secondo dataset, stesso allarme su un ordine al fornitore con lotto minimo superato.
8. **(15 s)** Chiusura: "Il modello capisce, il codice decide. MemoLens rende visibile la memoria degli agenti, in azienda e in fabbrica."

## 12. Come risponde ai criteri della giuria

| Criterio | Cosa lo alza |
|---|---|
| Tema 25% | Memoria con versioni, supersession, provenienza su ogni fatto, risolutore deterministico, "evidenza insufficiente", grafo delle relazioni |
| Tecnica 25% | Agente LLM vero, SDK con coda in background, riserve per ogni pezzo che può rompersi |
| Problema 25% | Caso concreto + variante fabbrica, numeri con fonti, Air Canada |
| Business 20% | Prezzi, ROI 8x, piano a 3 anni, go-to-market, AI Act come "perché ora" |
| Demo 5% | Copione provato, video di riserva |

## 13. Rischi e piano B

| Rischio | Piano B |
|---|---|
| L'agente non sbaglia come previsto | Temperatura 0; `leggi_ordine` senza prezzo pagato; modalità demo con conversazione registrata |
| Chiave API finita | Seconda chiave (Gemini) già in `.env`; cache delle spiegazioni |
| Il grafo pyvis non si vede bene | Tabella "azione → ricordo → fonte" al posto del disegno |
| Thread e coda creano errori | Scrittura diretta nel registro dopo la risposta al cliente (si perde solo l'eleganza) |
| Siamo in ritardo alle 15:30 | Si consegna la versione facile, che è già il primo strato |

## 14. Domande probabili della giuria

- **"Come gestite le contraddizioni?"** "Il risolutore applica regole fisse: validità nel tempo, dato più specifico, autorità della fonte. Se resta un conflitto, la scheda dice 'evidenza insufficiente' e chiede a una persona."
- **"Come sapete che un ricordo è superato?"** "Ogni ricordo ha valido-dal e valido-fino e indica quale versione sostituisce. Non cancelliamo mai: la vecchia versione resta nello storico."
- **"L'LLM decide qualcosa?"** "No. L'LLM agisce come agente del negozio e scrive le spiegazioni. Allarmi, casi simili e validità li calcola il codice."
- **"Perché non usare LangSmith?"** "Mostra chiamate e token a uno sviluppatore. Noi mostriamo a un responsabile quale ricordo ha causato quale decisione, quanti euro e come correggere."
- **"Cosa fate nei prossimi 3 mesi?"** "Tre design partner, SDK per i due framework più usati, primo report AI Act, misura del tempo di scoperta degli errori prima e dopo."

## 15. Checklist di consegna

- [ ] README: descrizione, avvio (`uv run streamlit run src/app.py`), architettura in 5 righe, **strumenti AI usati**
- [ ] Dati sintetici registrati in `research/data/README.md`
- [ ] Nessuna chiave committata
- [ ] `memolens.db` azzerato prima della demo
- [ ] Video di riserva + slide con fonti


---
---

# GUIDA PASSO PASSO (per chi parte da zero)

Questa guida spiega **ogni passaggio** come se non avessimo mai programmato. Non c'è codice da scrivere a mano: il codice lo scrive **Claude Code** quando gli incolliamo i messaggi pronti qui sotto. Noi controlliamo che funzioni.

## Come è fatto ogni passo

- **Obiettivo**: cosa deve esistere alla fine del passo.
- **Chi**: chi lo fa (gli altri non toccano quei file).
- **Terminale**: comandi da scrivere nel terminale, uno alla volta, premendo Invio dopo ognuno.
- **Messaggio per Claude Code**: testo da copiare e incollare **dentro Claude Code**, così com'è.
- **Controllo**: cosa devi vedere se è andato bene.
- **Se non va**: cosa fare.

## Parole che servono (mini-glossario)

| Parola | Cosa vuol dire |
|---|---|
| Terminale | La finestra nera dove si scrivono comandi. Su Windows: l'app "Ubuntu" (mai PowerShell). |
| Repo / cartella del progetto | `~/kva-ai-brain`: la cartella con tutto il progetto, collegata a GitHub. |
| Claude Code | L'assistente AI nel terminale. Si avvia scrivendo `claude`. Legge i file e scrive codice per noi. |
| Commit | "Salvataggio" con un nome, nella storia del progetto. |
| Push / Pull | Push = mandare i miei salvataggi su GitHub. Pull = scaricare quelli degli altri. |
| `.env` | File segreto con le chiavi API. **Non va mai su GitHub, mai in chat, mai negli screenshot.** |
| Chiave API | La "password" per usare un modello AI (Claude o Gemini). |
| LLM | Il modello AI (Claude, Gemini) che usiamo tramite la chiave. |
| Streamlit | La libreria che trasforma un file Python in una pagina web locale. |
| `localhost:8501` | L'indirizzo dove si apre l'app nel browser, solo sul tuo computer. |
| CSV / JSON | Formati di file per dati: CSV è una tabella (come Excel), JSON è una lista di campi con nomi. |
| SQLite | Un piccolo database che sta tutto in un file (`.db`). |
| `Ctrl+C` | Nel terminale **ferma** il programma che sta girando (non copia!). |

---

## PARTE 0 · Preparare il computer (venerdì sera, tutti, 20 minuti)

### Passo 0.1 · Aprire il terminale nella cartella giusta
- **Chi**: tutti.
- **Terminale**:
  ```bash
  cd ~/kva-ai-brain
  pwd
  ```
- **Controllo**: `pwd` stampa una riga che finisce con `/kva-ai-brain`.
- **Se non va** ("No such file or directory"): la repo non è scaricata. Segui `docs/SETUP.md` passo 2.

### Passo 0.2 · Scaricare le ultime novità e installare le librerie
- **Terminale**:
  ```bash
  git pull --rebase
  uv sync
  ```
- **Controllo**: nessuna riga con `error`. `uv sync` può scrivere "Resolved ... packages": va bene.
- **Se non va**: copia l'errore intero in Claude Code (vedi passo 0.7).

### Passo 0.3 · Controllare che l'ambiente sia a posto
- **Terminale**:
  ```bash
  bash scripts/check_env.sh
  ```
- **Controllo**: in fondo c'è scritto **0 to fix** (oppure 1 to fix se manca solo la chiave: si sistema al passo 0.4).

### Passo 0.4 · Mettere la chiave API e provarla
- **Chi**: almeno una persona venerdì (con una chiave Gemini gratuita da https://aistudio.google.com/apikey), tutti sabato mattina con la chiave di KVA.
- **Terminale**:
  ```bash
  bash scripts/set_key.sh                    # per la chiave Anthropic (Claude)
  bash scripts/set_key.sh GEMINI_API_KEY     # per la chiave Gemini
  uv run python scripts/smoke_llm.py
  ```
- **Controllo**: l'ultimo comando stampa `ready` accanto al nome del modello.
- **Se non va**: chiave copiata male (spazi in più) → rifare `set_key.sh`. Mai incollare la chiave in chat o in un file diverso da `.env`.

### Passo 0.5 · Avviare Claude Code e imparare a parlargli
- **Terminale**:
  ```bash
  claude
  ```
- **Come si parla a Claude Code** (regole che evitano disastri):
  1. **Un compito alla volta.** Un messaggio = un file o una funzione.
  2. **Dire sempre quale file del piano leggere** (per esempio "leggi `piano/01_FACILE.md` sezione 6").
  3. **Dire quali file può toccare**: "modifica solo `src/agent_sim.py`".
  4. **Chiedere come provarlo**: "alla fine dimmi il comando per provarlo e cosa devo vedere".
  5. Se non capisci cosa ha fatto: "spiegamelo in 5 righe semplici, in italiano".
  6. Quando chiede il permesso per un comando, leggi cosa vuole fare. Se parla di cancellare file o `git push --force`, rispondi **no** e chiedi a Giorgia.
- **Per uscire da Claude Code**: scrivi `/exit` oppure `Ctrl+C` due volte.
- Conviene tenere **due finestre di terminale**: una con Claude Code, una per lanciare l'app.

### Passo 0.6 · Il "giro del salvataggio" (ogni 20–30 minuti)
- **Chi**: ognuno per i suoi file.
- **Modo facile (consigliato)**, messaggio per Claude Code:
  > Fai il giro di salvataggio: mostrami quali file ho cambiato, fai commit **solo** dei file che ho cambiato io (non quelli degli altri) con un messaggio in inglese che descrive il cambiamento, poi `git pull --rebase` e `git push`. Se c'è un conflitto fermati e spiegamelo prima di fare qualsiasi cosa.
- **Modo a mano** (terminale):
  ```bash
  git status                       # elenco dei file cambiati
  git add src/nome_del_mio_file.py # solo i MIEI file
  git commit -m "Add refund agent simulation"
  git pull --rebase
  git push
  ```
- **Controllo**: `git status` dice "nothing to commit, working tree clean" e "up to date".
- **Mai** fare `git add .` se non sai cosa c'è dentro: potresti salvare `.env` o file degli altri (`.env` è escluso da `.gitignore`, ma meglio non rischiare).

### Passo 0.7 · Cosa fare quando c'è un errore
1. **Non andare nel panico.** Gli errori sono normali: in ogni passo ce ne saranno.
2. Copia **tutto** il testo rosso dal terminale (o dalla pagina Streamlit).
3. Messaggio per Claude Code:
   > Quando lancio `<comando che hai lanciato>` ottengo questo errore: `<incolla tutto l'errore>`. Spiegami in una riga cosa vuol dire e correggilo modificando solo `<nome del file>`.
4. Se dopo **10 minuti** non funziona ancora, messaggio per Claude Code:
   > Riporta `<nome del file>` all'ultima versione salvata con commit che funzionava, senza toccare altri file. Prima dimmi cosa perderei.
5. Se dopo **15 minuti** sei ancora bloccata/o: scrivi nel gruppo e passa al passo successivo. **Meglio una funzione in meno che una demo rotta.**

### Passo 0.8 · Chi tocca quali file
- Ogni file in `src/` ha **un solo proprietario** (scritto nella tabella dei moduli di questo piano). Se ti serve cambiare un file di un altro, chiediglielo a voce.
- I testi e i numeri che compaiono nell'app stanno in un file a parte, `src/texts.py`, di proprietà di Filippo: così lui può cambiarli senza scontrarsi con chi scrive l'app.

---

## PARTE 1 · Venerdì sera: preparare dati, prompt e la prova dell'agente

Prima di sabato **non si scrive il prodotto** (regola della gara): solo dati, prompt e prove usa e getta in `prototype/`. In questo piano la preparazione è **obbligatoria**: senza, sabato non si arriva al livello medio.

### Passo 1.1 · Creare i dati finti (Sian, 30 min)
- **Obiettivo**: dati e-commerce con memoria **a versioni**, e numeri che tornano.
- **Messaggio per Claude Code**:
  > Leggi `piano/02_MEDIO.md` sezioni 5 e 6. Crea dati sintetici in `data/shop/` (persone inventate, "Gianpaolo" è un nome di fantasia):
  > - `catalog.csv`: 15 articoli (sku, nome, prezzo_listino). Tra questi `SKU-SCARPA-01`, "Scarpe running", 120.
  > - `orders.csv`: 200 ordini (order_id, cliente, sku, prezzo_pagato, in_promo, data tra 20/10 e 10/11/2026). `ORD-1001`: Gianpaolo, SKU-SCARPA-01, pagato 80, in promo, 01/11/2026.
  > - `returns.csv`: 40 resi; esattamente 38 su ordini in promo (compreso ORD-1001), tutti con differenza listino − pagato di **40 €**; 2 non in promo.
  > - `memory_versions.json`: un ricordo per articolo con i campi della sezione 5 (memory_id, version=1, key, value=prezzo di listino, kind="catalog_price", source_doc="listino_2026-11-01.csv", author="import catalogo", valid_from="2026-11-01", valid_to=null, supersedes=null, status="active").
  > - `rules.json`: versione 1 `{"version":1,"text":"Per un reso rimborsa il prezzo dell'articolo","author":"setup iniziale","date":"2026-10-15"}`.
  >
  > Poi scrivi `prototype/check_data.py` che verifica: 38 resi in promo, differenza sempre 40 €, 37 casi oltre Gianpaolo = 1.480 €. Dimmi come lanciarlo.
- **Terminale**: `uv run python prototype/check_data.py`
- **Controllo**: stampa **37 casi, 1.480 €**.

### Passo 1.2 · Dati della fabbrica (Sian, 20 min)
- **Messaggio per Claude Code**:
  > Leggi `piano/02_MEDIO.md` sezione 2 (strato G) e `piano/01_FACILE.md` sezione 11. Crea `data/factory/` con lo stesso formato dei dati del negozio, ma per un agente che riordina materiale: `parts.csv` (10 componenti), `suppliers.csv`, `demand.csv` (fabbisogno settimanale), `memory_versions.json` con il ricordo "lotto minimo fornitore ACME per PART-07 = 500 pezzi" (fonte "contratto_2024.pdf", versione 1) e una versione 2 "= 200 pezzi" (fonte "contratto_2026.pdf", valid_from 2026-09-01) che **l'agente non ha mai letto** (stato "pending"). Aggiungi un controllo in `prototype/check_data.py` che calcola quanti euro sono immobilizzati se l'agente ordina 500 invece di 200 su 6 ordini.

### Passo 1.3 · Registrare i dati (Sian, 5 min)
- **Messaggio per Claude Code**:
  > Aggiungi a `research/data/README.md` una riga per ogni file in `data/shop/` e `data/factory/`: contenuto, fonte "sintetici, creati dal team", licenza CC0, aggiunto da Sian, "persone e aziende inventate".

### Passo 1.4 · LA prova più importante: l'agente vero sbaglia sempre allo stesso modo? (Sian o Giorgia, 40 min)
- **Perché**: in questo piano l'agente è un LLM vero. Dobbiamo sapere **stanotte** che fa il rimborso sbagliato ogni volta, altrimenti la demo non funziona.
- **Messaggio per Claude Code**:
  > Leggi `piano/02_MEDIO.md` sezione 6. Crea una prova usa e getta `prototype/agent_test.py`: un agente con l'API dell'LLM (chiave da `.env`, temperatura 0) con 3 strumenti finti che leggono `data/shop/`: `leggi_ordine(order_id)` che restituisce cliente, sku e data **ma non il prezzo pagato**; `ricorda(chiave)` che restituisce il valore e la fonte da `memory_versions.json`; `rimborsa(order_id, importo)` che stampa l'importo. Prompt di sistema: "Sei l'assistente resi del negozio. Per un reso, rimborsa il prezzo dell'articolo." Messaggio del cliente: "Ciao, sono Gianpaolo, vorrei restituire le scarpe dell'ordine ORD-1001". Stampa ogni chiamata agli strumenti e l'importo finale.
- **Terminale**: `uv run python prototype/agent_test.py` → **lancialo 10 volte**.
- **Controllo**: almeno 9 volte su 10 chiama `ricorda("prezzo SKU-SCARPA-01")` e rimborsa **120**.
- **Se non va** (rimborsa altro, fa domande, rifiuta): chiedi a Claude "rendi il prompt di sistema più diretto: l'agente non deve fare domande e deve usare lo strumento `ricorda` per il prezzo". Se dopo 3 tentativi non è stabile, la demo userà la **modalità registrata** (passo 3.12): salva una conversazione riuscita in `prototype/recorded_conversation.json`.
- Quando funziona: copia il prompt di sistema e la descrizione degli strumenti in `prototype/agent_prompt.txt`.

### Passo 1.5 · Provare il prompt della spiegazione (Sian, 20 min)
- **Messaggio per Claude Code**:
  > Crea `prototype/explain_test.py`: prende un evento di esempio (rimborso 120 € a Gianpaolo, ricordo `prezzo SKU-SCARPA-01 v1 = 120`, fonte "listino_2026-11-01.csv", prezzo pagato 80, verdetto del risolutore "SUPERATO dal dato più specifico") e chiede all'LLM un JSON con 4 campi in italiano semplice, massimo 20 parole ciascuno: cosa_ha_fatto, ricordo_usato, da_dove_arriva, cosa_non_torna. Vieta di inventare dati. Stampa il risultato.
- **Terminale**: lancialo 5 volte. **Controllo**: 5 su 5 corrette e brevi. Salva il prompt in `prototype/explain_prompt.txt`.

### Passo 1.6 · Ricalcolare il margine (Filippo, 20 min)
- Il documento calcola il costo AI con GPT-4o mini. Se useremo un modello Claude, prendere il prezzo dalla **pagina ufficiale dei prezzi Anthropic** e rifare il conto della sezione 3.4 (100.000 spiegazioni al mese, circa 800 token in ingresso e 150 in uscita ciascuna). Salvare il link della fonte accanto al numero.

### Passo 1.7 · Copione e salvataggio (tutti)
- Sian legge il copione (sezione 11) con il cronometro: 3 minuti.
- Giro di salvataggio (passo 0.6) per `data/`, `prototype/`, `research/data/README.md`.

---

## PARTE 2 · Sabato mattina (prima delle 14:00)

### Passo 2.1 · Prima delle 9:30 (tutti)
- Passi 0.1–0.4 con la chiave di KVA. Rilanciare **una volta** `prototype/agent_test.py` con la chiave nuova: deve ancora dare 120.

### Passo 2.2 · Alle 10:00, regole
- Chiarire se si può scrivere in `src/` già nella Fase I. Se sì, Giorgia anticipa i passi 3.1–3.3.

### Passo 2.3 · Alle 13:00, file vuoti (Giorgia)
- **Messaggio per Claude Code**:
  > Leggi `piano/02_MEDIO.md` sezioni 4, 5 e 8. Crea in `src/` i file vuoti con un commento iniziale (cosa farà e proprietario): `models.py`, `store.py`, `memolens_sdk.py`, `shop_agent.py`, `resolver.py`, `graph.py`, `sentinel.py`, `explain.py`, `texts.py`, `app.py`. Scrivi subito `src/models.py` con i modelli pydantic MemoryVersion, Event, Alert, Rule e Verdict con i campi della sezione 5. Niente logica negli altri file.
- Giro di salvataggio; **tutti** fanno `git pull --rebase`.

---

## PARTE 3 · Sabato 14:00–16:15: costruzione a strati

Regola: **si costruisce uno strato alla volta e si prova subito**. Se uno strato non funziona in 20 minuti, si salta e si va avanti con quello che c'è.

### STRATO BASE (14:00–14:45) · la versione facile, ma con il database

#### Passo 3.1 · Il database (Giorgia, 20 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/store.py` seguendo `piano/02_MEDIO.md` sezione 5. Usa SQLite (libreria standard) con file `memolens.db`. Tabelle `memory_versions`, `events`, `alerts`, `rules`. Funzioni: `init_db()` che crea le tabelle e carica `data/shop/` (e `data/factory/` se esiste); `add_event`, `list_events`, `add_alert`, `list_alerts`; `get_memory(key, at_time)` che restituisce la versione valida in quell'istante; `add_memory_version(...)` che chiude la versione precedente (valid_to, status superseded) e crea la nuova con `supersedes`; `add_rule_version`; `reset_demo()` che cancella il file e ricarica tutto. **Non cancellare mai una versione.** Dammi un comando per provarlo.
- **Controllo**: dopo `init_db()`, `get_memory("prezzo SKU-SCARPA-01", ora)` dà 120, versione 1.

#### Passo 3.2 · Spiegazioni e sentinella (Sian, 30 min, in parallelo)
- **Messaggio per Claude Code** (spiegazioni):
  > Scrivi `src/explain.py` con il prompt di `prototype/explain_prompt.txt`. `spiega(evento, verdetto)`: cache in `data/explanations_cache.json`; se l'LLM sbaglia o supera 8 secondi, frase fissa costruita dai campi. Non deve mai bloccare l'app.
- **Messaggio per Claude Code** (sentinella):
  > Scrivi `src/sentinel.py` seguendo `piano/02_MEDIO.md` sezione 8 (strato F). `controlla(evento)`: regole nel codice: rimborso > prezzo pagato (gravità alta, euro a rischio = differenza); importo > 500 € (media). In più un controllo statistico: se il rapporto rimborsato/pagato è sopra 1,2 per lo stesso articolo rispetto alla media dei resi, gravità media. Niente AI.
- **Controllo**: l'evento di Gianpaolo dà allarme alto, 40 €. Senza `.env` la spiegazione esce comunque (frase fissa).

#### Passo 3.3 · Scheletro dell'app (Giorgia, 25 min) + testi (Filippo)
- **Messaggio per Claude Code** (Giorgia):
  > Scrivi `src/app.py` con Streamlit e menu laterale con le pagine: Negozio, Timeline, Grafo, Allarmi e casi simili, Correzione. Per ora: Negozio con una casella di chat (per ora risponde "in costruzione"), Timeline che legge gli eventi da `store.py` e mostra schede con 4 righe fisse (Cosa ha fatto, Quale ricordo, Da dove arriva, Cosa non torna) e il dato originale sotto. Testi da `src/texts.py`. Nel menu: pulsante "Azzera demo" che chiama `reset_demo()`, e interruttore "Modalità demo registrata" (per ora non fa niente).
- **Messaggio per Claude Code** (Filippo):
  > Scrivi `src/texts.py`: un dizionario con tutti i testi in italiano dell'app (titoli, pulsanti, frase di chiusura "Il modello capisce, il codice decide") e i numeri dello scenario con la nota "stima del team" (299 €/mese, ROI circa 8x). Solo testi.
- **Terminale** (seconda finestra): `uv run streamlit run src/app.py` → apri `http://localhost:8501`.
- **Controllo**: le 5 pagine si aprono senza errori rossi.

### STRATO A + B (14:45–15:30) · agente vero e SDK

#### Passo 3.4 · L'SDK di MemoLens (Giorgia, 20 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/memolens_sdk.py` seguendo `piano/02_MEDIO.md` sezioni 2 (strato B) e 4. Un "involucro" (decoratore Python) da mettere sugli strumenti dell'agente: registra nome dello strumento, input, output, orario, e per lo strumento `ricorda` anche memory_id e version letti. Gli eventi vanno in una coda in memoria; un thread in background li scrive nel database con `store.add_event` e per ognuno chiama la sentinella. Se la scrittura fallisce, l'evento va in `data/queue.jsonl` e viene riprovato. Aggiungi un interruttore `MEMOLENS_OFFLINE` per simulare MemoLens irraggiungibile. L'agente non deve **mai** aspettare l'SDK.
- **Controllo**: chiedi a Claude un piccolo test: con OFFLINE attivo gli eventi finiscono in `queue.jsonl`, quando lo spegni arrivano nel database.

#### Passo 3.5 · L'agente del negozio (Giorgia, 25 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/shop_agent.py` riusando prompt e strumenti di `prototype/agent_prompt.txt` (sezione 6 del piano): strumenti `leggi_ordine` (senza prezzo pagato), `ricorda`, `rimborsa`, ognuno avvolto dall'SDK di `memolens_sdk.py`. Temperatura 0. Funzione `chatta(messaggio, storico)` che restituisce la risposta per il cliente. La regola attiva viene letta da `store.py`: se è la versione "rimborsa il prezzo pagato", `leggi_ordine` restituisce anche il prezzo pagato e il prompt lo dice. Poi collega la pagina Negozio di `app.py` a `chatta` e mostra "Resoconto ricevuto" quando l'evento arriva nel database.
- **Controllo**: scrivi nella chat "Ciao, sono Gianpaolo, vorrei restituire le scarpe dell'ordine ORD-1001" → rimborso **120 €** → l'evento appare in Timeline.

#### Passo 3.6 · Lo storico (Sian, 15 min, in parallelo)
- **Messaggio per Claude Code**:
  > Aggiungi a `src/store.py`, d'accordo con Giorgia, una funzione `carica_storico()` che crea direttamente nel database i 39 eventi dei resi passati (tutti tranne Gianpaolo), con date nelle due settimane precedenti, come se l'agente li avesse già fatti con la regola v1 e il ricordo v1. Così non spendiamo chiamate all'LLM. `reset_demo()` la chiama alla fine.
- **Controllo**: dopo "Azzera demo" la Timeline mostra 39 schede storiche.

### STRATO C + D + E (14:45–15:30, Sian in parallelo) · versioni, risolutore, grafo

#### Passo 3.7 · Il risolutore deterministico (Sian, 25 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/resolver.py` seguendo **esattamente** `piano/02_MEDIO.md` sezione 7. `verifica(evento)`: per ogni ricordo usato restituisce un Verdict con stato `VALIDO`, `SUPERATO` o `EVIDENZA_INSUFFICIENTE`, il valore che avrebbe dovuto valere e la **catena di prove** (lista delle regole applicate, in ordine, con il motivo). Regole: 1) validità nel tempo; 2) dato più specifico (prezzo pagato nell'ordine batte il prezzo di listino); 3) autorità della fonte (contratto > listino > email) e poi data; 4) se restano due valori diversi → EVIDENZA_INSUFFICIENTE. Nessuna chiamata all'LLM. Scrivi anche 3 test con pytest: caso Gianpaolo (SUPERATO, valore giusto 80), reso non in promo (VALIDO), due fonti uguali in conflitto (EVIDENZA_INSUFFICIENTE).
- **Terminale**: `uv run pytest -q`
- **Controllo**: `3 passed`.

#### Passo 3.8 · Il grafo e i casi simili (Sian, 25 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/graph.py` seguendo `piano/02_MEDIO.md` sezione 5 (Grafo). Con networkx costruisci dal database un grafo con nodi Azione, Ricordo(versione), Fonte, Cliente, Regola(versione) e archi USA, DERIVA_DA, SOSTITUISCE, RIGUARDA. Funzioni: `casi_simili(event_id)` = tutte le azioni collegate alla **stessa versione di ricordo** dello stesso tipo e che hanno un allarme della stessa regola, con totale euro; `disegna(event_id)` che crea un HTML con pyvis del vicinato dell'azione (azione al centro, ricordo, fonte, regola), con colori diversi per tipo di nodo.
- **Controllo**: `casi_simili` sull'evento di Gianpaolo dà **37 casi, 1.480 €**.

#### Passo 3.9 · Collegare tutto nella dashboard (Giorgia, 15 min)
- **Messaggio per Claude Code**:
  > In `src/app.py`: nella Timeline aggiungi a ogni scheda il verdetto del risolutore (stato colorato: verde VALIDO, rosso SUPERATO, arancione EVIDENZA INSUFFICIENTE) con la catena di prove apribile, e la spiegazione di `explain.py`. Pagina Grafo: mostra l'HTML di `graph.disegna` per l'evento scelto (con `st.components.v1.html`). Pagina Allarmi: elenco allarmi, pulsante "Trova casi simili" con tabella e totale grande in euro.
- **Controllo**: il giro Negozio → Allarme → Scheda con SUPERATO → Grafo → 37 casi funziona.

### 15:30 · CONTROLLO (tutti, 2 minuti)
Domanda: **il giro completo funziona con l'agente vero?**
- **Sì** → avanti con il passo 3.10.
- **L'agente a volte sbaglia** → passo 3.12 (modalità registrata), poi 3.10.
- **Molte cose rotte** → fermarsi. Riportare l'app all'ultimo salvataggio che funzionava (passo 0.7) e fare solo il passo 3.10 con l'agente simulato del piano facile.

#### Passo 3.10 · Correzione e nuovo reso (Giorgia + Sian, 20 min)
- **Messaggio per Claude Code**:
  > In `src/app.py` pagina Correzione: mostra la regola attiva e il ricordo usato da Gianpaolo con tutte le versioni (storico). Pulsante "Correggi: rimborso = prezzo pagato": crea la regola versione 2 (autore "Responsabile customer care", data e ora di adesso) con `store.add_rule_version`; la versione 1 resta. Poi pulsante "Ripeti il reso di Gianpaolo": rilancia `shop_agent.chatta` con lo stesso messaggio e mostra il nuovo importo accanto al vecchio.
- **Controllo**: nuovo reso = **80 €**; lo storico mostra v1 e v2 con autore e data.

#### Passo 3.11 · "Evidenza insufficiente" visibile (Sian, 10 min)
- **Messaggio per Claude Code**:
  > Aggiungi ai dati del negozio un secondo caso di demo: un articolo con due ricordi di prezzo con la stessa autorità e la stessa data ma valori diversi (due listini caricati lo stesso giorno). Fai in modo che un evento storico usi quell'articolo, così in Timeline compare una scheda arancione "EVIDENZA INSUFFICIENTE: due fonti valide in conflitto, serve una persona". Aggiorna `research/data/README.md`.

#### Passo 3.12 · Modalità demo registrata (Giorgia, 15 min, solo se serve)
- **Messaggio per Claude Code**:
  > Quando l'interruttore "Modalità demo registrata" è attivo, la pagina Negozio non chiama l'LLM ma riproduce la conversazione salvata in `prototype/recorded_conversation.json` (copiala in `data/shop/`), facendo passare comunque gli strumenti dall'SDK, così la parte MemoLens resta vera.

#### Passo 3.13 · Variante fabbrica (Sian, 20 min, se avanza tempo)
- **Messaggio per Claude Code**:
  > Aggiungi `src/factory_agent.py` con lo stesso schema di `shop_agent.py` ma per i riordini (`data/factory/`): strumenti `fabbisogno(part)`, `ricorda(chiave)`, `ordina(part, quantita)`, avvolti dall'SDK. Aggiungi una regola alla sentinella "ordine superiore al fabbisogno di oltre il 50%". Nell'app un selettore "Negozio / Fabbrica" in alto nel menu.
- **Controllo**: in modalità Fabbrica l'ordine di 500 pezzi genera allarme e la scheda mostra il ricordo "contratto_2024", SUPERATO dalla versione 2026.

---

## PARTE 4 · 16:15–17:00: chiusura

### Passo 4.1 · Stop alle funzioni nuove (16:15)
Solo correzioni di errori che rompono la demo.

### Passo 4.2 · Video di riserva (Giorgia + Filippo)
- "Azzera demo", poi registra lo schermo con tutto il copione (sezione 11). Windows: `Win + G`; Ubuntu: `Ctrl + Alt + Shift + R`; oppure OBS Studio.
- Registrane due: una con l'agente vero, una in modalità registrata. Salvale in due posti.

### Passo 4.3 · README e chiavi (Giorgia)
- **Messaggio per Claude Code**:
  > Aggiorna `README.md` per la consegna: cos'è MemoLens in 3 righe; come si avvia (`uv sync`, chiave in `.env` con `bash scripts/set_key.sh`, `uv run streamlit run src/app.py`); architettura in 5 righe (agente → SDK con coda → database a versioni → risolutore deterministico → grafo → dashboard); dati sintetici; come lanciare i test (`uv run pytest`); sezione obbligatoria "Strumenti AI usati" (Claude Code per il codice, il modello LLM usato come agente e per le spiegazioni).
- **Terminale** (non deve stampare niente):
  ```bash
  git log -p | grep -iE "api_key|sk-|AIza"
  ```
- Giro di salvataggio finale.

### Passo 4.4 · Prima della presentazione
- "Azzera demo", app a schermo intero (`F11`), notifiche spente, altre finestre chiuse.
- Decidere **prima** se andare con l'agente vero o la modalità registrata (se nelle ultime 3 prove ha sbagliato anche una volta: registrata).
- Filippo ha il video aperto. Sian ha copione e risposte (sezione 14).
