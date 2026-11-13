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
