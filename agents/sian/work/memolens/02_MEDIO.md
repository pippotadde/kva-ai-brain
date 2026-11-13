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
