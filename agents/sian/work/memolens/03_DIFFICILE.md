# MemoLens · Versione DIFFICILE ("per vincere il tema")

> Obiettivo: parlare **la lingua esatta della giuria**. KVA ha costruito Project OIDA (registro governato di decisioni con supersession, contraddizioni, provenienza, risolutore deterministico, astensione, esposto via MCP) e ha scritto il paper *"Retrieval Is Not Enough"* (vedi `research/kva-company.md`). Questa versione applica quei principi alla **memoria degli agenti che agiscono**, un posto dove OIDA non c'è ancora, e la porta in fabbrica.
>
> ⚠️ **Realismo:** in 3 ore di costruzione non si fa tutto. Questa versione è il MEDIO (`02_MEDIO.md`) + strati in ordine di valore. Si aggiungono solo se il medio funziona. Senza preparazione stanotte, puntare al massimo a uno strato (il server MCP).

---

## 1. L'idea in una frase

MemoLens è **l'infrastruttura epistemica per gli agenti che agiscono**: ogni azione di un agente è collegata ai ricordi che l'hanno causata, ogni ricordo ha tipo, fonte, validità nel tempo e storia; un risolutore deterministico dice quale ricordo valeva in quel momento, trova contraddizioni e tutti i casi colpiti, e chiunque (persona o altra AI via MCP) può chiedere "perché?".

## 2. Cosa si aggiunge rispetto al medio (in ordine di valore per la giuria)

| # | Strato | Cosa si vede | Tempo stimato | Valore |
|---|---|---|---|---|
| H1 | **Server MCP di MemoLens** | In Claude Desktop o Claude Code si chiede "perché Gianpaolo ha ricevuto 120 €?" e Claude risponde con ricordo, fonte e casi simili, leggendo da MemoLens | 30–40 min | ⭐⭐⭐ La giuria espone OIDA via MCP: è il segnale più forte |
| H2 | **Oggetti di conoscenza tipizzati** (stile OIDA) | Ogni elemento è *Decisione, Evidenza, Osservazione, Assunzione, Contraddizione, Domanda aperta*; il tipo cambia peso e colore nella timeline | 30 min | ⭐⭐⭐ Tema |
| H3 | **Memoria bitemporale + "macchina del tempo"** | Cursore: "cosa sapeva l'agente alle 10:42" contro "cosa era vero alle 10:42" | 30 min | ⭐⭐ Tema, molto chiaro da vedere |
| H4 | **Replay controfattuale** | "Se il ricordo fosse stato giusto": ricalcolo deterministico delle 38 decisioni → euro recuperabili, cliente per cliente | 20 min | ⭐⭐ Business + tecnica |
| H5 | **Valutazione misurata** | "Su 50 bug iniettati in dati sintetici MemoLens ne trova X, in media in Y secondi" | preparato stanotte | ⭐⭐ Davide Lai (ricercatore) la chiederà |
| H6 | **Export AI Act** | Pulsante "Registro per auditor": JSON + PDF con eventi, versioni, autori | 20 min | ⭐ Business |
| H7 | **Mascheramento dati personali** prima del salvataggio | Nomi ed email sostituiti da codici nel registro | 15 min | ⭐ Rischio GDPR coperto |
| H8 | **Ingresso standard OpenTelemetry** (convenzioni GenAI) | "Si collega anche ad agenti già tracciati con Langfuse o simili" | 45 min+ | ⭐ Solo a parole se manca tempo |
| H9 | **Due agenti, due settori** | Agente resi (negozio) + agente riordini (fabbrica) sullo stesso MemoLens | 30 min | ⭐⭐ "Industry" |

**Ordine consigliato sabato:** H1 → H2 → H4 → H3 → H9. H5 si prepara stanotte (è solo un numero e uno script in `prototype/`). H6–H8 si dicono nel pitch come "già progettati" se non c'è tempo.

## 3. Business plan (versione da investitore)

La giuria ragiona da venture studio (il premio B è un investimento). Oltre ai numeri del documento serve far vedere **un'azienda possibile**.

### 3.1 Tesi d'investimento in 4 righe
1. Gli agenti stanno passando da "rispondere" ad "agire con soldi veri" (commercio agentico USA: 190–385 mld $ al 2030 secondo Morgan Stanley [12], 300–500 secondo Bain [13]).
2. Chi agisce deve poter spiegare perché: tribunali (Air Canada [10]), auditor e AI Act (art. 12, dal 2 dic 2027 [16][17]) lo pretendono.
3. Gli strumenti attuali sono per sviluppatori (LangSmith, Langfuse [21][22]) o danno memoria senza verificabilità (Mem0, 24 mln $ raccolti [23]).
4. MemoLens è lo strato che manca: **memoria verificabile + decisione + impatto in euro**, per chi risponde del business.

### 3.2 Numeri chiave (dal documento; "stima del team" dove indicato)
| Voce | Valore | Fonte |
|---|---|---|
| Mercato agenti AI | 7,84 → 52,62 mld $ (2025–2030) | [1] |
| TAM osservabilità agenti | 0,4 → 7,1 mld $ (2025–2035) | [3] |
| SAM Europa PMI/mid | ~200 mln € al 2028 | stima del team |
| SOM 3° anno | ~1 mln €/anno (300 clienti × 268 €/mese) | stima del team |
| Margine lordo Business | ~88% | stima del team ⚠️ ricalcolare col modello effettivo |
| Pareggio | nel 2° anno | stima del team |
| ROI cliente | ~8x (un incidente evitato) | stima del team, ipotesi in sezione 3.4 del documento |

### 3.3 Difendibilità (domanda certa da un investitore)
- **Dati di incidenti**: ogni cliente arricchisce una libreria di "schemi di errore degli agenti" (rimborso > pagato, promozione scaduta, lotto superato). Più clienti → sentinelle migliori per tutti (con dati anonimizzati).
- **Ontologia di settore**: tipi di ricordo e regole di validità per e-commerce, assicurazioni, manifattura. Costruirla richiede esperti di dominio, non solo codice.
- **Posizione nel flusso**: MemoLens è dove si correggono i ricordi. Diventa il registro ufficiale della memoria dell'agente (sistema di record), difficile da sostituire.
- **Europa e AI Act by design**: dati in UE, registro conforme, mascheramento dati personali.

### 3.4 Roadmap
| Quando | Cosa | Misura di successo |
|---|---|---|
| 0–3 mesi | 3 design partner (2 e-commerce, 1 manifatturiero), SDK Python + JS, server MCP pubblico | tempo medio di scoperta errore: da settimane a < 1 giorno sui partner |
| 3–6 mesi | Ingresso OpenTelemetry, connettori a 2 framework di agenti, primo report AI Act | 10 clienti paganti |
| 6–12 mesi | Libreria di sentinelle per settore, versione installabile presso il cliente | 50 clienti, primo contratto Enterprise |

### 3.5 Legame con il portafoglio KVA (da dire con tatto)
- **OIDA** governa le decisioni delle persone; **MemoLens** governa la memoria degli agenti che agiscono. Complementari, non concorrenti.
- **Gergo** (cobot a voce, "il modello capisce, il codice decide") registra cosa fa il cobot; MemoLens è lo strato che spiega *perché*, con quale ricordo, e quante volte.
- **Clienti di Excellence** (banche, assicurazioni): il caso "pratica di sinistro calcolata su dati vecchi" è lo stesso motore.

### 3.6 Prezzi e go-to-market
Come nel medio: Free / 49 € / 299 € / da 1.500 € (stima del team). Canale principale: integratori che costruiscono agenti per PMI e system integrator industriali (MES/ERP). Server MCP gratuito come porta d'ingresso per gli sviluppatori.

## 4. Architettura

```
                         ┌───────────────────────────────────────────────┐
  AGENTI (lato cliente)  │                 MEMOLENS (lato azienda)         │
┌───────────────────┐    │                                                 │
│ Agente resi (LLM) │─┐  │  ┌──────────┐  ┌───────────┐  ┌──────────────┐  │
└───────────────────┘ │  │  │ Ingest   │─▶│ Mascherare│─▶│ Registro     │  │
┌───────────────────┐ ├─▶│  │ SDK/OTel │  │ dati pers.│  │ bitemporale  │  │
│ Agente riordini   │─┘  │  └──────────┘  └───────────┘  │ (SQLite)     │  │
│ fabbrica (LLM)    │    │      ▲ coda in background     └──────┬───────┘  │
└───────────────────┘    │      │ (il cliente non aspetta)      ▼          │
        ▲                │                    ┌───────────────────────────┐│
        │ legge          │                    │ Grafo di conoscenza        ││
┌───────┴────────────┐   │                    │ oggetti tipizzati:         ││
│ Memoria governata  │◀──┼── correzione ──────│ Decisione · Evidenza ·     ││
│ versioni, validità,│   │   (nuova versione, │ Osservazione · Assunzione ·││
│ autore, fonte      │   │    mai cancellare) │ Contraddizione · Domanda   ││
└────────────────────┘   │                    └─────────────┬─────────────┘│
                         │                                  ▼              │
                         │  ┌──────────────────────────────────────────┐   │
                         │  │ Risolutore deterministico                 │   │
                         │  │ validità · specificità · autorità · data  │   │
                         │  │ → VALIDO / SUPERATO / CONTRADDIZIONE /    │   │
                         │  │   EVIDENZA INSUFFICIENTE                  │   │
                         │  └───┬──────────────┬───────────────┬────────┘   │
                         │      ▼              ▼               ▼            │
                         │  Sentinella    Casi simili     Replay            │
                         │                + euro          controfattuale    │
                         │      └──────────────┼───────────────┘            │
                         │                     ▼                            │
                         │  ┌──────────────┐  ┌─────────────┐  ┌──────────┐ │
                         │  │ Dashboard    │  │ Server MCP  │  │ Export   │ │
                         │  │ Streamlit    │  │ (per Claude │  │ AI Act   │ │
                         │  │ + macchina   │  │  e altre AI)│  │ JSON/PDF │ │
                         │  │ del tempo    │  └─────────────┘  └──────────┘ │
                         │  └──────────────┘                                │
                         └──────────────────────────────────────────────────┘
```

**Regola d'oro:** l'LLM fa solo due cose (essere l'agente del negozio/fabbrica e scrivere le spiegazioni). **Tutto il resto è deterministico e ripetibile.** È esattamente il messaggio del paper della giuria: importanza, validità e contraddizioni "calcolate con formule, non dall'umore di un LLM".

## 5. Modello dei dati (oltre al medio)

### 5.1 Oggetti di conoscenza tipizzati
| Tipo | Nel caso Gianpaolo | Comportamento |
|---|---|---|
| **Evidenza** | Listino del 1 nov (120 €); ricevuta d'ordine (80 €) | Ha una fonte documentale; peso alto |
| **Osservazione** | "Gianpaolo ha pagato 80 € il 01/11" | Fatto specifico su un caso; batte le regole generali |
| **Assunzione** | "Il prezzo dell'articolo è il prezzo da rimborsare" | Implicita nel prompt dell'agente; va resa visibile |
| **Decisione** | "Rimborsati 120 € a Gianpaolo" (presa dall'agente) | Collegata alle evidenze/assunzioni usate |
| **Contraddizione** | 120 € (listino) contro 80 € (pagato) per lo stesso fatto | Arco con segno tra due oggetti; genera l'allarme |
| **Domanda aperta** | "Quale prezzo vale per i resi in promo?" quando nessuna regola decide | Prodotta dall'astensione: va a una persona |

### 5.2 Bitemporalità (due orologi)
- **Tempo di validità**: quando il fatto è vero nel mondo (`valid_from`, `valid_to`).
- **Tempo di registrazione**: quando il sistema l'ha saputo (`recorded_at`, `retracted_at`).
- Domande che diventano possibili: "cosa sapeva l'agente quando ha deciso?" (per giudicare l'agente in modo equo) e "cosa era vero?" (per calcolare il danno).

### 5.3 Risolutore: stati di uscita
`VALIDO` · `SUPERATO` (da una versione più recente o più specifica) · `CONTRADDIZIONE` (due valori validi e incompatibili) · `EVIDENZA_INSUFFICIENTE` (nessuna regola li separa → Domanda aperta). Ogni uscita porta con sé la **catena di prove**: quali regole sono state applicate e in che ordine.

## 6. Server MCP (strato H1, il più importante)

Un piccolo server con la libreria ufficiale `mcp` per Python (`uv add mcp`), avviato in locale e collegato a Claude Desktop o Claude Code. Strumenti esposti (solo lettura, tranne l'ultimo):

| Strumento MCP | Domanda a cui risponde | Risposta |
|---|---|---|
| `perche(azione)` | "Perché l'agente ha fatto questo?" | ricordi usati, fonte, autore, stato del risolutore, catena di prove |
| `casi_simili(azione)` | "Chi altro è colpito?" | elenco + euro a rischio |
| `memoria_al(chiave, istante)` | "Cosa sapeva l'agente alle 10:42?" | versione valida e versione registrata in quell'istante |
| `contraddizioni_aperte()` | "Cosa non sappiamo?" | Domande aperte e contraddizioni non risolte |
| `proponi_correzione(...)` | "Correggi questo ricordo" | crea una **proposta**, non la applica: serve l'approvazione di una persona nella dashboard |

Momento demo: si apre Claude, si chiede in italiano "Perché Gianpaolo ha ricevuto 120 € e quanti altri clienti sono nella stessa situazione?" → risposta con fonti, presa da MemoLens. Frase: **"La memoria dei vostri agenti diventa interrogabile da qualsiasi altra AI, con le prove."**

Riserva: se il collegamento MCP non funziona dal vivo, screenshot/video registrato alle 16:15.

## 7. Valutazione misurata (strato H5, da preparare stanotte)

- Script in `prototype/` che genera 50 scenari sintetici con bug iniettati di 5 tipi (rimborso > pagato, promozione scaduta applicata, sconto doppio, lotto minimo superato, ricordo di un altro cliente) + 50 scenari puliti.
- Si misura: quanti bug trova la sentinella (richiamo), quanti falsi allarmi (precisione), quanti casi simili trova rispetto a quelli veri.
- Sabato si riscrive in `src/eval.py` (le regole lo impongono) e si mostra il risultato in una slide: "richiamo X%, precisione Y% su 100 scenari sintetici". **Dichiarare che sono dati sintetici.**
- Risposta pronta a "come sapete che funziona?" e coerente con il metodo KVA ("validato su benchmark e con clienti").

## 8. Moduli del programma (oltre al medio)

| File in `src/` | Cosa fa | Chi | Strato |
|---|---|---|---|
| `knowledge.py` | Tipi di oggetti di conoscenza e loro regole (peso, sensibilità alle contraddizioni) | Sian | H2 |
| `temporal.py` | Domande bitemporali: valido a / registrato a | Giorgia | H3 |
| `resolver.py` | Esteso: stati CONTRADDIZIONE e EVIDENZA_INSUFFICIENTE, catena di prove | Sian | H2 |
| `counterfactual.py` | Ricalcola le decisioni con il ricordo corretto, euro recuperabili | Sian | H4 |
| `mcp_server.py` | Server MCP con gli strumenti della sezione 6 | Giorgia | H1 |
| `redact.py` | Maschera nomi ed email prima del salvataggio | Giorgia | H7 |
| `export.py` | Registro per auditor (JSON; PDF se c'è tempo) | Filippo con Claude | H6 |
| `factory_agent.py` | Agente riordini con il suo dataset | Giorgia | H9 |
| `eval.py` | Valutazione sui 100 scenari | Sian | H5 |

## 9. Collegamenti e strumenti

| Cosa | Scelta | Installazione |
|---|---|---|
| Base | tutto il medio (anthropic, streamlit, networkx, pyvis, pydantic, SQLite) | già presente |
| MCP | SDK ufficiale `mcp` (Python), trasporto locale stdio | `uv add mcp` · configurazione nel client Claude (Claude Desktop o `claude mcp add`) |
| PDF | `reportlab` o semplice HTML stampabile | `uv add reportlab` solo se serve |
| OpenTelemetry | `opentelemetry-sdk` con le convenzioni GenAI | solo come roadmap se manca tempo |
| Modelli | agente e spiegazioni con un modello veloce (es. `claude-haiku-5-5`); riserva Gemini | chiavi in `.env` |

Provare **stanotte** in `prototype/` che il server MCP si colleghi a Claude sul computer di Giorgia: è l'unico pezzo con configurazione esterna.

## 10. Piano della giornata

| Ora | Giorgia | Sian | Filippo |
|---|---|---|---|
| Venerdì notte | Prova MCP in `prototype/` | Dataset 2 settori, 100 scenari di valutazione, prompt | Slide investitore (sezione 3), ricalcolo margine |
| 10:30–12:30 | Schema dati completo (sezioni 5 e 8) | Storia e pitch delle 12:30 | Numeri |
| 13:00–14:00 | File vuoti in `src/`, divisione lavoro | Copione | Domande giuria |
| 14:00–15:15 | **Medio, strati A–D** (vedi `02_MEDIO.md`) | resolver, graph, explain, sentinel | testi dashboard, euro |
| **15:15 controllo** | Il medio fa il giro completo? **No → fermarsi al medio** | | |
| 15:15–15:55 | H1 server MCP | H2 tipi + H4 controfattuale | slide valutazione (H5) |
| 15:55–16:15 | H9 agente fabbrica *o* H3 macchina del tempo (uno solo) | `eval.py` | prova pitch |
| 16:15–16:30 | **Stop funzioni nuove**, azzerare db, video di riserva (anche del momento MCP) | | |
| 16:30 / 17:00 | Guida la demo | Presenta | Verifica finanziaria, video |

## 11. Copione della demo (3 minuti)

1. **(20 s)** Chat: Gianpaolo chiede il reso, l'agente vero rimborsa 120 € subito.
2. **(10 s)** "Resoconto ricevuto": il cliente ha già finito.
3. **(30 s)** Allarme + scheda tipizzata: **Decisione** (rimborso 120 €) ← **Assunzione** ("il prezzo dell'articolo è il rimborso") + **Evidenza** (listino 1 nov). **Contraddizione** con l'**Osservazione** "pagato 80 €". Risolutore: SUPERATO dal dato più specifico, con la catena di prove.
4. **(20 s)** Macchina del tempo: "alle 10:42 l'agente sapeva solo il listino" (lo giudichiamo in modo equo) contro "era vero che aveva pagato 80 €" (calcoliamo il danno).
5. **(25 s)** Casi simili + replay controfattuale: 37 clienti, 1.480 € recuperabili, elenco pronto.
6. **(25 s)** Correzione con approvazione di una persona, versione nuova, la vecchia resta. Nuovo reso: 80 €.
7. **(25 s)** **Momento MCP**: in Claude, "Perché Gianpaolo ha ricevuto 120 € e chi altro è coinvolto?" → risposta con fonti da MemoLens.
8. **(10 s)** Fabbrica: stesso motore sull'agente dei riordini (lotto minimo superato).
9. **(15 s)** Chiusura: "Il modello capisce, il codice decide, e quando le prove non bastano lo dice. MemoLens è la memoria verificabile degli agenti che agiscono."

⚠️ 3 minuti sono stretti: se un pezzo non è perfetto, si taglia dal copione (prima la macchina del tempo, poi la fabbrica). Provare il copione con il cronometro almeno 3 volte.

## 12. Come risponde ai criteri della giuria

| Criterio | Cosa lo alza |
|---|---|
| Tema 25% (spareggio) | Oggetti tipizzati, supersession, contraddizioni con segno, bitemporalità, astensione, MCP: il vocabolario e i principi di OIDA, applicati a un caso nuovo |
| Tecnica 25% | Due agenti veri, risolutore deterministico, valutazione con numeri, MCP funzionante |
| Problema 25% | E-commerce + fabbrica, fonti, Air Canada, AI Act |
| Business 20% | Tesi d'investimento, difendibilità, roadmap con misure, legame con portafoglio KVA |
| Demo 5% | Momento "wow" (Claude che interroga MemoLens) |

## 13. Rischi e piano B

| Rischio | Piano B |
|---|---|
| Troppe cose, niente funziona bene | **Controllo delle 15:15**: se il medio non è completo, niente strati H. Meglio un medio perfetto che un difficile rotto |
| MCP non si collega sul computer della demo | Provato stanotte; video registrato alle 16:15 |
| Demo oltre i 3 minuti | Tagli già decisi (macchina del tempo, poi fabbrica) |
| Un giurato dice "è OIDA rifatto" | "OIDA governa le decisioni delle persone; noi la memoria degli agenti che agiscono, collegata all'impatto in euro. Stessi principi, problema diverso" |
| Valutazione con numeri deboli | Mostrare comunque il metodo e dire onestamente i limiti (dati sintetici, pochi scenari) |
| Chiave API | Riserva Gemini, cache, conversazioni registrate |

## 14. Domande probabili della giuria (in più rispetto al medio)

- **(Ferrero) "Come calcolate che un ricordo è superato, senza LLM?"** "Quattro regole in ordine: validità nel tempo, specificità, autorità della fonte, data. Ogni verdetto mostra la catena di prove."
- **(Lai) "Come lo valutate?"** "100 scenari sintetici con 5 tipi di bug iniettati: richiamo X%, precisione Y%. Il prossimo passo è misurare il tempo di scoperta sui design partner."
- **"Perché bitemporale?"** "Per separare due domande: cosa sapeva l'agente (responsabilità) e cosa era vero (danno). Senza i due orologi si confondono."
- **"Cosa succede se il risolutore non sa?"** "Crea una Domanda aperta e la manda a una persona. Non inventa."
- **"Perché MCP?"** "Perché le aziende avranno molti agenti e molte AI: la memoria verificabile deve essere interrogabile da tutte, non chiusa nella nostra dashboard."
- **"Come vi integrate con OIDA o Gergo?"** "MemoLens potrebbe pubblicare le sue Contraddizioni e Domande aperte nel registro OIDA, e spiegare le azioni del cobot di Gergo."

## 15. Checklist di consegna

- [ ] README: descrizione, avvio dashboard e server MCP, architettura, **strumenti AI usati**
- [ ] Dati sintetici e scenari di valutazione registrati in `research/data/README.md`
- [ ] Nessuna chiave committata
- [ ] Database azzerato prima della demo
- [ ] Video di riserva con il momento MCP
- [ ] Slide: valutazione (dichiarata sintetica), tesi d'investimento, fonti


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

## Prima di iniziare: come è organizzata questa guida

Il piano difficile è **il piano medio + strati in più**. Per non ripetere 30 passi uguali, questa guida dice "fai i passi X–Y di `piano/02_MEDIO.md`": apri quel file, vai in fondo alla sua **GUIDA PASSO PASSO**, fai quei passi, poi torna qui. Tutto il resto è spiegato qui sotto.

---

## PARTE 1 · Venerdì sera: preparazione (più lunga che negli altri piani)

### Passo 1.1 · Tutta la preparazione del medio (Sian, Giorgia, Filippo)
- Fai i **passi 1.1–1.7 della guida di `piano/02_MEDIO.md`**: dati negozio e fabbrica, registro dei dati, prova dell'agente vero (10 volte), prompt della spiegazione, ricalcolo del margine, copione.
- **Controllo**: `prototype/check_data.py` stampa 37 casi e 1.480 €; l'agente rimborsa 120 almeno 9 volte su 10.

### Passo 1.2 · Provare il server MCP (Giorgia, 40 min) ⚠️ il più importante
- **Obiettivo**: sapere stanotte che Claude Code, sul computer della demo, riesce a usare un nostro server MCP.
- **Cos'è MCP, in breve**: un modo standard per dare a un'AI (Claude) degli "strumenti" scritti da noi. Il nostro server MCP sarà un piccolo programma Python; Claude lo avvia e gli fa domande.
- **Terminale** (aggiunge la libreria ufficiale; Giorgia è la proprietaria delle dipendenze):
  ```bash
  cd ~/kva-ai-brain
  uv add mcp
  ```
- **Messaggio per Claude Code**:
  > Crea una prova usa e getta `prototype/mcp_test.py`: un server MCP minimo con la libreria ufficiale `mcp` per Python (FastMCP), trasporto stdio, con un solo strumento `prezzo_in_memoria(sku)` che legge `data/shop/memory_versions.json` e restituisce valore, fonte e versione. Dimmi il comando esatto per collegarlo a Claude Code con `claude mcp add`, usando `uv run --directory` sulla cartella del progetto.
- **Terminale** (il comando sarà simile a questo; usa quello che ti dà Claude):
  ```bash
  claude mcp add memolens-test -- uv run --directory ~/kva-ai-brain python prototype/mcp_test.py
  claude
  ```
- Dentro Claude Code scrivi `/mcp`.
- **Controllo**: `memolens-test` risulta **connected**. Poi chiedi a Claude: "Usa lo strumento prezzo_in_memoria per SKU-SCARPA-01" → risponde 120 € con la fonte.
- **Se non va**: copia l'errore di `/mcp` in un'altra sessione di Claude Code (passo 0.7). Dopo 40 minuti senza successo: **niente strato H1 sabato**, lo si mostra solo in video o a parole.
- Alla fine: `claude mcp remove memolens-test` (sabato si collega quello vero).

### Passo 1.3 · Gli scenari per la valutazione (Sian, 40 min)
- **Obiettivo**: poter dire "su 100 scenari sintetici MemoLens trova X% dei bug".
- **Messaggio per Claude Code**:
  > Leggi `piano/03_DIFFICILE.md` sezione 7. Crea `prototype/make_eval.py` che genera `data/eval/scenarios.json`: 100 scenari sintetici, 50 con un bug iniettato (10 per tipo: rimborso maggiore del pagato, promozione scaduta ancora applicata, sconto applicato due volte, lotto minimo superato, ricordo di un altro cliente) e 50 puliti. Ogni scenario ha gli eventi, i ricordi usati e l'etichetta giusta (bug sì/no, tipo). Crea anche `prototype/run_eval.py` che per ora usa regole semplici e stampa richiamo e precisione. Spiegami in 5 righe cosa vogliono dire richiamo e precisione.
- **Terminale**: `uv run python prototype/make_eval.py` e poi `uv run python prototype/run_eval.py`
- **Controllo**: stampa due percentuali. Non importa che siano alte stanotte: serve che il metodo funzioni.
- Registra `data/eval/` in `research/data/README.md` (sintetici, CC0).

### Passo 1.4 · Decidere i tipi di conoscenza (Sian + Giorgia, 15 min)
- Leggete insieme la sezione 5.1. Decidete i 6 tipi e il colore di ognuno nella dashboard. Scrivetelo in un file `prototype/knowledge_types.md` (tipo, esempio, colore, regola di comportamento). Sabato Claude lo userà.

### Passo 1.5 · Slide da investitore (Filippo, 40 min)
- Usare la sezione 3 (tesi in 4 righe, difendibilità, roadmap, legame con OIDA e Gergo). Ogni numero con la sua fonte; "stima del team" scritto in piccolo sotto.
- Preparare la slide "Valutazione" con lo spazio per i numeri di sabato.

### Passo 1.6 · Salvare tutto
- Giro di salvataggio (passo 0.6), compresi `pyproject.toml` e `uv.lock` (cambiati da `uv add mcp`).

---

## PARTE 2 · Sabato mattina

### Passo 2.1 · Come nel medio
- Fai i **passi 2.1–2.2 della guida di `piano/02_MEDIO.md`** (ambiente, chiave KVA, agente ancora a 120, regole delle 10:00).
- In più: ripeti il controllo MCP del passo 1.2 con `memolens-test` sul **computer della demo** (quello di Giorgia), poi rimuovilo.

### Passo 2.2 · Alle 13:00, file vuoti (Giorgia)
- **Messaggio per Claude Code**:
  > Leggi `piano/02_MEDIO.md` sezioni 5 e 8 e `piano/03_DIFFICILE.md` sezioni 5 e 8. Crea in `src/` i file vuoti con un commento iniziale (cosa farà e proprietario) per tutti i moduli dei due piani: `models.py`, `store.py`, `memolens_sdk.py`, `shop_agent.py`, `resolver.py`, `graph.py`, `sentinel.py`, `explain.py`, `texts.py`, `app.py`, `knowledge.py`, `temporal.py`, `counterfactual.py`, `mcp_server.py`, `redact.py`, `export.py`, `factory_agent.py`, `eval.py`. Scrivi subito `src/models.py` con i modelli pydantic del medio **più** il campo `knowledge_type` (i 6 tipi di `prototype/knowledge_types.md`) e i campi bitemporali `recorded_at` e `retracted_at` sulle versioni di memoria.
- Giro di salvataggio; tutti fanno `git pull --rebase`.

---

## PARTE 3 · Sabato 14:00–16:15: costruzione

### Passo 3.1 · Prima il medio, con scadenza 15:15 (tutti)
- Fai i **passi 3.1–3.9 della guida di `piano/02_MEDIO.md`** (database, spiegazioni, sentinella, app, SDK, agente, storico, risolutore, grafo, dashboard). Quando un messaggio per Claude nomina `piano/02_MEDIO.md`, aggiungi alla fine: "Tieni conto anche dei campi in più di `src/models.py` (tipo di conoscenza e tempi bitemporali)".
- Poi il **passo 3.10** del medio (correzione e nuovo reso).

### 15:15 · CONTROLLO (tutti, 2 minuti)
Il giro completo del medio funziona (Negozio → Allarme → Scheda SUPERATO → Grafo → 37 casi → Correzione → 80 €)?
- **No** → **niente strati difficili.** Continuate con la guida del medio dal passo 3.11 e consegnate il medio. È la scelta giusta, non una sconfitta.
- **Sì** → avanti, nell'ordine sotto. Ogni strato ha **un tempo massimo**: scaduto il tempo, si torna all'ultimo salvataggio e si passa oltre.

### Passo 3.2 · H1, il server MCP (Giorgia, max 35 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/mcp_server.py` seguendo `piano/03_DIFFICILE.md` sezione 6, riusando quello che abbiamo provato in `prototype/mcp_test.py`. Server MCP con la libreria `mcp` (FastMCP, stdio) che legge **lo stesso database** `memolens.db` usato dalla dashboard, usando le funzioni già esistenti di `store.py`, `resolver.py` e `graph.py` (non riscrivere la logica). Strumenti: `perche(event_id o nome cliente)` con ricordi usati, fonte, autore, verdetto e catena di prove; `casi_simili(event_id)` con elenco e totale euro; `memoria_al(chiave, istante)`; `contraddizioni_aperte()`; `proponi_correzione(...)` che salva solo una **proposta** in una tabella `proposals` senza applicarla. Ogni strumento ha una descrizione chiara in italiano. Dimmi il comando `claude mcp add` per collegarlo.
- **Terminale**:
  ```bash
  claude mcp add memolens -- uv run --directory ~/kva-ai-brain python src/mcp_server.py
  ```
- **Controllo**: apri `claude` in una nuova finestra, scrivi `/mcp` → `memolens` connected. Poi chiedi: **"Perché Gianpaolo ha ricevuto 120 € e quanti altri clienti sono nella stessa situazione?"** → risposta con ricordo v1, fonte "listino_2026-11-01.csv", 37 casi, 1.480 €.
- **In più** (Giorgia, 5 min): nella pagina Correzione dell'app, mostrare le proposte arrivate via MCP con un pulsante "Approva" che applica la correzione.

### Passo 3.3 · H2, oggetti di conoscenza tipizzati (Sian, max 30 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/knowledge.py` seguendo `piano/03_DIFFICILE.md` sezione 5.1 e `prototype/knowledge_types.md`. Funzione che, dato un evento, costruisce gli oggetti tipizzati: la scelta dell'agente = Decisione; i ricordi da documento = Evidenza; il prezzo pagato nell'ordine = Osservazione; la regola implicita nel prompt = Assunzione; due valori incompatibili per lo stesso fatto = Contraddizione (arco con segno negativo nel grafo); un'EVIDENZA_INSUFFICIENTE del risolutore = Domanda aperta. Aggiorna `graph.py` perché i nodi abbiano il tipo e il colore deciso. In `app.py` (d'accordo con Giorgia) mostra nella scheda una riga per ogni oggetto con un'etichetta colorata del suo tipo.
- **Controllo**: la scheda di Gianpaolo mostra Decisione ← Assunzione + Evidenza, e la Contraddizione con l'Osservazione "pagato 80 €".

### Passo 3.4 · H4, replay controfattuale (Sian, max 20 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/counterfactual.py`: per un allarme, prende tutti i casi simili e ricalcola in modo deterministico (senza LLM) cosa avrebbe deciso l'agente con il valore indicato dal risolutore. Restituisce una tabella cliente per cliente (rimborsato, giusto, da recuperare) e il totale. Nella pagina Allarmi aggiungi un pulsante "Se il ricordo fosse stato giusto" che mostra la tabella e il totale recuperabile.
- **Controllo**: totale **1.480 €** (37 × 40 €), più i 40 € di Gianpaolo se incluso: decidere quale numero dire e usarlo uguale ovunque.

### Passo 3.5 · H3 macchina del tempo **oppure** H9 fabbrica (Giorgia, max 20 min, uno solo)
- **Scegliete**: la fabbrica alza "industry" (consigliata se il dataset `data/factory/` è pronto); la macchina del tempo alza "tema".
- **H9 fabbrica**: fai il **passo 3.13 della guida di `piano/02_MEDIO.md`**.
- **H3 macchina del tempo**, messaggio per Claude Code:
  > Scrivi `src/temporal.py` seguendo `piano/03_DIFFICILE.md` sezione 5.2: `sapeva_al(chiave, istante)` usa il tempo di registrazione (cosa conosceva il sistema), `vero_al(chiave, istante)` usa il tempo di validità (cosa era vero). Per la demo, aggiungi ai dati una versione del ricordo "prezzo pagato da Gianpaolo = 80 €" registrata **dopo** il rimborso. In `app.py` aggiungi nella scheda un cursore temporale che mostra affiancati "Cosa sapeva l'agente" e "Cosa era vero" in quell'istante.

### Passo 3.6 · H5, valutazione (Sian, max 15 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/eval.py` partendo dall'idea di `prototype/run_eval.py` ma usando le **vere** `sentinel.py`, `resolver.py` e `graph.py` sugli scenari di `data/eval/scenarios.json`. Stampa richiamo, precisione e tempo medio per scenario, e salva i risultati in `data/eval/results.json`. Dimmi come lanciarlo.
- **Terminale**: `uv run python src/eval.py`
- **Controllo**: escono i numeri → Sian li manda a Filippo per la slide "Valutazione" (con la scritta "100 scenari sintetici").

### Passo 3.7 · H6 export e H7 mascheramento (solo se avanzano 15 minuti)
- **Export (Filippo)**, messaggio per Claude Code:
  > Scrivi `src/export.py`: crea `export/registro_ai_act.json` con tutti gli eventi, le versioni di memoria e di regola, gli autori e i verdetti, ordinati per tempo. Aggiungi nella pagina Correzione un pulsante di download (`st.download_button`). Niente PDF.
- **Mascheramento (Giorgia)**, messaggio per Claude Code:
  > Scrivi `src/redact.py` che sostituisce nomi ed email con codici (es. CLIENTE-0001) **prima** che `memolens_sdk.py` salvi l'evento; la tabella di corrispondenza resta in un file separato non esportato. Nella dashboard si vede il nome solo se un interruttore "mostra dati personali" è attivo.
- Se non c'è tempo: si dicono nel pitch come "progettati", senza mostrarli.

---

## PARTE 4 · 16:15–17:00: chiusura

### Passo 4.1 · Stop alle funzioni nuove (16:15)
Solo correzioni di errori che rompono la demo. Se uno strato H è a metà, si toglie dal menu: **niente di rotto davanti alla giuria**.

### Passo 4.2 · Video di riserva (Giorgia + Filippo)
- "Azzera demo", registra tutto il copione della sezione 11, **compreso il momento MCP** in Claude Code. Windows: `Win + G`; Ubuntu: `Ctrl + Alt + Shift + R`; oppure OBS Studio.
- Registra anche una versione senza MCP, più corta. Salva entrambe in due posti.

### Passo 4.3 · Prova a cronometro (tutti)
- Il copione difficile è pieno: provarlo e **tagliare** ciò che sfora (prima la macchina del tempo, poi la fabbrica). Deve stare in 3 minuti.

### Passo 4.4 · README e chiavi (Giorgia)
- **Messaggio per Claude Code**:
  > Aggiorna `README.md` per la consegna: cos'è MemoLens in 3 righe; avvio (`uv sync`, chiave con `bash scripts/set_key.sh`, `uv run streamlit run src/app.py`); come collegare il server MCP (`claude mcp add memolens -- uv run --directory <cartella> python src/mcp_server.py`) e una domanda di esempio; architettura in 6 righe; i tipi di conoscenza; come lanciare test e valutazione (`uv run pytest`, `uv run python src/eval.py`) dicendo che gli scenari sono sintetici; sezione obbligatoria "Strumenti AI usati".
- **Terminale** (non deve stampare niente):
  ```bash
  git log -p | grep -iE "api_key|sk-|AIza"
  ```
- Giro di salvataggio finale.

### Passo 4.5 · Prima della presentazione
- "Azzera demo"; app a schermo intero (`F11`); **finestra di Claude Code già aperta con `memolens` connected** e la domanda già scritta (basta premere Invio); notifiche spente.
- Decidere prima: agente vero o modalità registrata; MCP dal vivo o video.
- Filippo ha i video aperti. Sian ha copione e risposte (sezioni 13–14).
