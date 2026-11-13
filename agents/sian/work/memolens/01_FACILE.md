# MemoLens · Versione FACILE ("sicura")

> Obiettivo: una demo che **non può rompersi**, costruibile in 3 ore da 3 persone, che mostra tutto il racconto di Gianpaolo dall'inizio alla fine.
> Principio: l'agente è **simulato** (un programma che si comporta come un agente AI con un bug). L'AI vera serve solo per scrivere le spiegazioni in italiano semplice, e anche quella ha una riserva già pronta.

---

## 1. L'idea in una frase

Le AI ormai spendono soldi per conto delle aziende. MemoLens è il "registratore di volo" che mostra a chiunque **cosa ha ricordato l'agente, perché ha deciso così e quanti altri casi sono stati colpiti dallo stesso errore**.

## 2. Cosa costruiamo (e cosa NO)

| Sì | No (per ora) |
|---|---|
| Un negozio finto con un "agente resi" simulato che ha il bug del prezzo di listino | Un agente LLM vero |
| Il resoconto inviato **dopo** aver servito il cliente | Server separato, rete, API proprie |
| Timeline di schede leggibili (azione, ricordo usato, fonte, data) | Grafo visuale complesso |
| Allarme con regole semplici ("mai rimborsare più del pagato") | Rilevatore statistico di anomalie |
| "Casi simili": elenco + totale in euro | Ricerca semantica |
| Correzione della regola con un clic + nuovo reso di Gianpaolo a 80 € | Versionamento completo della memoria |
| Spiegazione in italiano scritta da un LLM, con testo di riserva | Più lingue, più settori |

## 3. Business plan (sintesi da usare nel pitch)

Tutti i numeri vengono dal documento `MemoLens_Hackathon_Track4.docx`; il numero tra parentesi quadre è la fonte nel documento. **"Stima del team" va detto ad alta voce.**

**Problema.** Gli agenti AI agiscono (rimborsi, sconti, ordini) usando una memoria che nessuno vede. Quando sbagliano, l'azienda vede solo i soldi che mancano.
- 51% delle aziende ha già avuto un danno dall'AI, il più comune è l'imprecisione (McKinsey) [9].
- 362 incidenti AI documentati nel 2025, 233 nel 2024 (Stanford AI Index) [7][8].
- Caso Air Canada: il tribunale ha condannato l'azienda per il chatbot. Ciò che fa l'agente lo fa l'azienda [10].

**Cliente che paga.** Chi gestisce soldi e rischi: responsabile e-commerce o customer care, controllo di gestione, compliance. Prima nicchia: PMI europee con un agente AI che parla con i clienti.

**Prezzo.** Free (0 €) · Starter 49 €/mese · Business 299 €/mese · Enterprise da 1.500 €/mese (stima del team, coerente con LangSmith e Langfuse [21][22]).

**Perché lo comprano.** Un solo incidente tipo Gianpaolo costa circa 29.400 € senza visibilità e circa 1.450 € con MemoLens. L'abbonamento Business costa 3.588 €/anno, quindi **un incidente evitato lo ripaga circa 8 volte** (stima del team, ipotesi dichiarate).

**Mercato.** Agenti AI: da 7,84 a 52,62 mld $ tra 2025 e 2030 (MarketsandMarkets) [1]. Osservabilità degli agenti: 0,4 mld $ nel 2025, 7,1 mld $ nel 2035 [3]. SOM al 3° anno: circa 1 mln €/anno (stima del team).

**Perché ora.** AI Act art. 12: log automatici obbligatori per i sistemi ad alto rischio dal 2 dic 2027 [16][17].

**Concorrenti.** LangSmith, Langfuse, Datadog parlano ai tecnici. Mem0 e Zep danno memoria agli agenti ma non la rendono verificabile. MemoLens parla al business.

**Margine.** Circa 88% sul piano Business (stima del team). ⚠️ Il documento calcola il costo con GPT-4o mini: se usiamo un modello Claude, ricalcolare con il prezzo ufficiale del modello scelto prima di dirlo in pitch.

## 4. Architettura

Tutto gira in **un solo programma Streamlit**, sul computer di Giorgia. Nessun server, nessuna rete tranne la chiamata facoltativa all'LLM.

```
┌──────────────── app Streamlit (un solo processo) ─────────────────┐
│                                                                    │
│  LATO CLIENTE                         LATO AZIENDA                 │
│  ┌─────────────┐   resoconto (dopo)   ┌─────────────────────────┐  │
│  │ Agente resi │ ───────────────────▶ │ Registro (events.jsonl) │  │
│  │ (simulato)  │                      └───────────┬─────────────┘  │
│  └──────┬──────┘                                  │                │
│         │ legge                                   ▼                │
│  ┌──────▼──────┐   ┌──────────┐   ┌────────────┐  ┌─────────────┐  │
│  │ Memoria     │   │ Ordini   │   │ Sentinella │  │ Spiegazione │  │
│  │ memory.json │   │orders.csv│   │ (regole)   │  │ LLM + cache │  │
│  └─────────────┘   └──────────┘   └─────┬──────┘  └──────┬──────┘  │
│                                         ▼                ▼         │
│                        ┌────────────────────────────────────────┐  │
│                        │ Pagine: Negozio · Timeline · Allarmi   │  │
│                        │ · Casi simili · Correzione             │  │
│                        └────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
```

**L'idea chiave da far vedere:** il cliente riceve la risposta subito; il resoconto arriva al registro "dopo" (nella demo: un messaggio "Resoconto ricevuto" che compare 1 secondo dopo la risposta al cliente).

## 5. I dati (preparare stanotte)

Tutti finti, creati dal team. Vanno in `data/` e registrati in `research/data/README.md` come "sintetici, creati dal team, licenza CC0".

| File | Contenuto | Esempio |
|---|---|---|
| `catalog.csv` | articoli con prezzo di listino attuale | `SKU-SCARPA-01, Scarpe running, 120` |
| `orders.csv` | 200 ordini con prezzo pagato e se c'era promozione | `ORD-1001, Gianpaolo, SKU-SCARPA-01, pagato 80, promo sì, 01/11` |
| `returns.csv` | 40 richieste di reso (38 su articoli in promo) | `RET-01, ORD-1001` |
| `memory.json` | i "ricordi" dell'agente, ognuno con **fonte, autore, data** | `{"id":"M-07","chiave":"prezzo SKU-SCARPA-01","valore":120,"fonte":"listino 1 nov (prima dello sconto)","autore":"import catalogo","salvato":"2026-11-01"}` |
| `rules.json` | le regole dell'agente, con versione | `{"v":1,"rimborso_usa":"prezzo_in_memoria","autore":"setup","data":"2026-10-15"}` |
| `explanations_cache.json` | spiegazioni già generate per i casi della demo | — |

**I numeri della demo devono tornare:** 37 casi simili × 40 € = **1.480 €** a rischio (come nelle slide).

## 6. Moduli del programma (cosa fa ognuno, senza codice)

| File in `src/` | Cosa fa | Chi |
|---|---|---|
| `data_load.py` | Legge CSV e JSON, li tiene in memoria | Giorgia |
| `agent_sim.py` | "Agente resi": per un reso legge la regola attiva; con la v1 prende il prezzo dalla **memoria** (listino), con la v2 dal **prezzo pagato** nell'ordine. Restituisce la risposta al cliente e prepara il resoconto | Giorgia |
| `recorder.py` | Riceve il resoconto e lo aggiunge a `events.jsonl`: orario, cliente, azione, importo, **ID dei ricordi usati**, fonte, versione della regola | Giorgia |
| `sentinel.py` | Regole di buon senso: rimborso > pagato; sconto applicato due volte; importo oltre una soglia. Restituisce allarmi con gravità | Sian |
| `similar.py` | Dato un allarme, trova tutti gli eventi che hanno usato **lo stesso tipo di ricordo** e violano la stessa regola; somma gli euro | Sian |
| `explain.py` | Trasforma un evento in una frase semplice. Prima guarda la cache; se manca, chiama l'LLM; se l'LLM non risponde, usa un modello di frase fisso ("Ho rimborsato X € perché il prezzo in memoria era X €, salvato il ... da ...") | Sian |
| `app.py` | Interfaccia Streamlit con 4 pagine (sotto) | Giorgia + Filippo (testi e numeri) |

**Le 4 pagine dell'app**
1. **Negozio**: pulsante "Gianpaolo chiede il reso" → risposta dell'agente ("Rimborso di 120 € avviato"). Poi appare "Resoconto ricevuto dall'azienda".
2. **Timeline**: schede in ordine di tempo. Ogni scheda ha 4 righe fisse: *Cosa ha fatto · Quale ricordo ha usato · Da dove arriva · Cosa non torna*. Il dato originale è sempre accanto alla spiegazione.
3. **Allarmi e casi simili**: elenco allarmi rossi; pulsante "Trova casi simili" → tabella dei 37 clienti e totale "1.480 € a rischio".
4. **Correzione**: mostra la regola attiva (v1, autore, data) → pulsante "Rimborso = prezzo pagato" → crea la v2 con autore e data (la v1 resta nello storico) → ripete il reso di Gianpaolo → 80 €.

## 7. Collegamenti e strumenti

| Cosa | Scelta | Note |
|---|---|---|
| Linguaggio | Python 3.12 + `uv` | già nel `pyproject.toml` |
| Interfaccia | `streamlit` | già installato |
| Dati | `pandas` + file CSV/JSON | niente database |
| Modelli dei dati | `pydantic` | per evento, ricordo, regola |
| LLM per le spiegazioni | `anthropic` (es. `claude-haiku-5-5`, veloce ed economico) oppure `google-genai` | chiave solo in `.env`; **sempre con cache e testo di riserva** |
| Avvio | `uv run streamlit run src/app.py` | da scrivere nel README |

Nessuna dipendenza nuova da aggiungere.

## 8. Piano della giornata

| Ora | Cosa | Chi |
|---|---|---|
| prima delle 9:30 | Chiave API provata, dati in `data/`, repo pubblica | tutti |
| 10:30–12:30 | Confermare l'idea; storia e slide; Sian prova il pitch | Sian, Filippo |
| 13:00–14:00 | Giorgia fissa i nomi dei file e i campi dei dati (sezione 5–6). Ognuno sa cosa tocca | Giorgia |
| 14:00–14:45 | `data_load`, `agent_sim`, `recorder` · `sentinel`, `explain` · testi dell'app | G · S · F |
| 14:45–15:30 | `app.py` pagine 1–2 · `similar` · numeri nella pagina 3 | G · S · F |
| 15:30–16:15 | Pagine 3–4, correzione e replay. **Primo giro completo della demo** | tutti |
| 16:15–16:30 | Solo correzioni di errori. **Stop alle funzioni nuove.** Video di riserva | Giorgia, Filippo |
| 16:30 | Verifica finanziaria | Filippo, Sian |
| 17:00 | Pitch e demo | Sian parla, Giorgia guida, Filippo ha il video |

Commit piccoli ogni 20–30 minuti, `git pull --rebase` prima del push.

## 9. Copione della demo (3 minuti)

1. **(30 s) Il problema.** Pagina Negozio. "Gianpaolo ha pagato le scarpe 80 € in promozione. Chiede il reso." Clic. "L'agente rimborsa subito 120 €. Il cliente è contento, nessuno se ne accorge."
2. **(15 s) Il resoconto.** "Un istante dopo, in background, il resoconto arriva all'azienda. Il cliente ha già finito."
3. **(30 s) L'allarme.** Pagina Allarmi: "Rimborso superiore al prezzo pagato."
4. **(30 s) Il perché.** Si apre la scheda: ricordo usato "prezzo 120 €", fonte "listino del 1° novembre, prima dello sconto". Accanto, il dato originale.
5. **(30 s) L'impatto.** "Trova casi simili": 37 clienti, 1.480 € a rischio.
6. **(30 s) La correzione.** Regola v2 "rimborso = prezzo pagato", con autore e data; la v1 resta nello storico. Nuovo reso di Gianpaolo: 80 €.
7. **(15 s) Chiusura.** "Senza MemoLens: settimane e migliaia di euro. Con MemoLens: due minuti, e il cliente non ha aspettato un secondo."

## 10. Come risponde ai criteri della giuria

| Criterio | Cosa lo alza in questa versione | Punto debole |
|---|---|---|
| Tema (25%) | Ogni decisione è legata al ricordo usato, con fonte, autore, data; regole con versioni | L'agente è simulato: un giurato può dire "non è vera memoria di un agente". Risposta pronta sotto |
| Tecnica (25%) | Tutto funziona dal vivo, zero rischi di rete | Poca complessità tecnica |
| Problema reale (25%) | Caso concreto, numeri con fonte, Air Canada | Settore e-commerce, non industria (vedi variante) |
| Business (20%) | Prezzi, ROI 8x, mercato, AI Act | — |
| Demo (5%) | Copione chiaro, 3 minuti precisi | — |

## 11. Variante industriale (20 secondi in più nella demo)

Stesso motore, secondo file di dati: **agente che riordina materiale in fabbrica**.
- Ricordo vecchio: "lotto minimo del fornitore = 500 pezzi" (contratto 2024).
- Ricordo nuovo non letto dall'agente: "lotto minimo = 200 pezzi" (contratto 2026).
- L'agente ordina 500 pezzi: magazzino pieno, soldi immobilizzati.
- MemoLens: allarme "ordine superiore al fabbisogno", scheda con la fonte "contratto 2024", casi simili su altri articoli dello stesso fornitore.

Frase da dire: "Lo stesso vale in fabbrica: ogni agente che ordina, rimborsa o pianifica usa una memoria che deve essere visibile."

## 12. Rischi e piano B

| Rischio | Piano B |
|---|---|
| L'LLM non risponde o la chiave finisce | Cache delle spiegazioni + frase fissa di riserva (la demo non cambia) |
| L'app si blocca | Video di riserva registrato alle 16:15 |
| I numeri non tornano (37, 1.480 €) | Controllarli stanotte nel dataset, non sabato |
| Finiamo prima | Passare al piano MEDIO, uno strato alla volta (`02_MEDIO.md`) |

## 13. Domande probabili della giuria (risposte da 20 secondi)

- **"L'agente è finto?"** "Sì, per la demo abbiamo simulato l'agente per avere un caso controllato. MemoLens non dipende dall'agente: riceve un resoconto standard (azione, ricordi usati, fonte). Qualsiasi agente può mandarlo con poche righe."
- **"Perché non basta ChatGPT sui log?"** "Perché il problema non è leggere un log, è collegare ogni decisione al ricordo che l'ha causata e trovare tutti i casi colpiti. Le regole decidono, l'AI spiega soltanto, e accanto c'è sempre il dato originale."
- **"Chi paga e quanto?"** "Il responsabile e-commerce o customer care. Da 49 a 299 € al mese. Un incidente evitato ripaga l'anno circa 8 volte (stima nostra, ipotesi nel documento)."
- **"Cosa succede se l'AI sbaglia la spiegazione?"** "La spiegazione è solo una traduzione; il dato originale è sempre accanto e l'allarme è fatto da regole, non dall'AI."
- **"Primi 10 clienti?"** "PMI e-commerce italiane che hanno appena messo un agente AI nel customer care: piano gratuito, installazione in 10 minuti, poi Business."

## 14. Checklist di consegna

- [ ] README: cosa fa, come si avvia (`uv run streamlit run src/app.py`), **strumenti AI usati**
- [ ] `research/data/README.md` aggiornato (dati sintetici)
- [ ] Nessuna chiave nel codice (`git log -p | grep -iE "api_key|sk-|AIza"` vuoto)
- [ ] Video di riserva salvato
- [ ] Slide con le fonti dei numeri


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

## PARTE 1 · Venerdì sera: preparare dati, prompt e copione

Prima di sabato **non si scrive il prodotto** (regola della gara): si preparano dati, prompt e prove usa e getta in `prototype/`.

### Passo 1.1 · Creare i dati finti della demo
- **Obiettivo**: i file `data/catalog.csv`, `data/orders.csv`, `data/returns.csv`, `data/memory.json`, `data/rules.json`, con numeri che tornano.
- **Chi**: Sian.
- **Messaggio per Claude Code**:
  > Leggi `piano/01_FACILE.md` sezione 5. Crea i dati sintetici della demo nella cartella `data/` (dati inventati, nessuna persona reale tranne il nome di fantasia "Gianpaolo"):
  > - `catalog.csv`: 15 articoli con colonne sku, nome, prezzo_listino_attuale. Uno è `SKU-SCARPA-01`, "Scarpe running", 120.
  > - `orders.csv`: 200 ordini con colonne order_id, cliente, sku, prezzo_pagato, in_promo (si/no), data (tra 20/10/2026 e 10/11/2026). L'ordine `ORD-1001` è di Gianpaolo: SKU-SCARPA-01, pagato 80, in promo, 01/11/2026.
  > - `returns.csv`: 40 richieste di reso (return_id, order_id, data_richiesta). Esattamente 38 riguardano ordini in promozione (compreso ORD-1001) e in tutte queste 38 la differenza tra prezzo di listino e prezzo pagato è **esattamente 40 €**. Le altre 2 non sono in promo.
  > - `memory.json`: i ricordi dell'agente, uno per articolo, con campi id, chiave ("prezzo <sku>"), valore (prezzo di listino), fonte ("listino 1 nov 2026, prima dello sconto"), autore ("import catalogo"), salvato ("2026-11-01").
  > - `rules.json`: lista di versioni di regole; la prima è `{"versione":1,"rimborso_usa":"prezzo_in_memoria","autore":"setup iniziale","data":"2026-10-15"}`.
  >
  > Alla fine scrivi un piccolo controllo in `prototype/check_data.py` che verifica: 38 resi in promo, tutti con differenza 40 €, quindi 37 casi oltre Gianpaolo = 1.480 €. Dimmi il comando per lanciarlo.
- **Terminale** (il comando che ti dà Claude, di solito):
  ```bash
  uv run python prototype/check_data.py
  ```
- **Controllo**: stampa 38, 40 €, 37 casi, **1.480 €**.
- **Se non va**: chiedi a Claude di correggere i dati (non il controllo!) finché i numeri tornano.

### Passo 1.2 · Registrare i dati
- **Chi**: Sian.
- **Messaggio per Claude Code**:
  > Aggiungi a `research/data/README.md` una riga per ogni file creato in `data/`: cosa contiene, fonte "sintetici, creati dal team", licenza CC0, aggiunto da Sian, nota "persone inventate".

### Passo 1.3 · Provare il prompt della spiegazione
- **Obiettivo**: sapere già venerdì che l'AI scrive frasi chiare e corrette.
- **Chi**: Sian.
- **Messaggio per Claude Code**:
  > Crea `prototype/explain_test.py` (prova usa e getta). Prende un evento di esempio (rimborso di 120 € a Gianpaolo; ricordo usato: "prezzo SKU-SCARPA-01 = 120", fonte "listino 1 nov 2026, prima dello sconto"; prezzo pagato 80) e chiede all'LLM, con la chiave in `.env`, di rispondere in JSON con 4 campi in italiano semplice, massimo 20 parole ciascuno: cosa_ha_fatto, ricordo_usato, da_dove_arriva, cosa_non_torna. Il prompt deve vietare di inventare dati non presenti nell'evento. Stampa il risultato.
- **Terminale**: `uv run python prototype/explain_test.py` (lancialo 5 volte).
- **Controllo**: 5 risposte su 5 sono corrette, brevi, senza numeri inventati.
- **Se non va**: "Le risposte sono troppo lunghe / inventano X. Migliora il prompt." Quando funziona, **copia il prompt in un file `prototype/explain_prompt.txt`**: sabato lo riusiamo.

### Passo 1.4 · Copione e slide
- **Chi**: Sian (copione), Filippo (numeri).
- Stampa o tieni aperta la sezione 9 di questo piano. Leggila ad alta voce **con il cronometro**: deve stare in 3 minuti.

### Passo 1.5 · Salvare tutto
- Fai il giro di salvataggio (passo 0.6). Controlla che `data/`, `prototype/` e `research/data/README.md` siano su GitHub.

---

## PARTE 2 · Sabato mattina (prima delle 14:00)

### Passo 2.1 · Prima delle 9:30 (tutti)
- Ripeti i passi 0.1–0.4 (pull, `uv sync`, `check_env`, chiave di KVA, `smoke_llm`).
- Filippo rende pubblica la repo (vedi `docs/PLAN.md` §4), **dopo** aver controllato che non ci siano chiavi.

### Passo 2.2 · Alle 10:00, regole
- Leggere bene le istruzioni sulle consegne. **Domanda da chiarire**: si può iniziare a scrivere in `src/` già durante la Fase I (10:30–12:30)? Se sì, Giorgia anticipa i passi 3.1–3.3.

### Passo 2.3 · Alle 13:00, preparare i file vuoti (Giorgia)
- **Messaggio per Claude Code**:
  > Leggi `piano/01_FACILE.md` sezioni 4, 5 e 6. Crea in `src/` i file vuoti con solo un commento iniziale che dice cosa farà ciascuno e chi ne è il proprietario: `data_load.py`, `agent_sim.py`, `recorder.py`, `sentinel.py`, `similar.py`, `explain.py`, `texts.py`, `app.py`. Crea anche `src/models.py` con i modelli pydantic Ricordo, Evento, Allarme, Regola usando i campi della sezione 5. Non scrivere ancora la logica.
- Poi giro di salvataggio. **Tutti fanno `git pull --rebase`** per avere i file.

---

## PARTE 3 · Sabato 14:00–16:15: costruzione

Lavorate **in parallelo**, ognuno nei suoi file. Dopo ogni passo: provarlo, poi giro di salvataggio.

### Passo 3.1 · Leggere i dati (Giorgia, 10 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/data_load.py`: funzioni che leggono i file in `data/` e restituiscono catalogo, ordini, resi, ricordi e regole (usando i modelli di `src/models.py`). Aggiungi una funzione per salvare una nuova versione di regola in `data/rules.json` senza cancellare le vecchie. Alla fine dammi un comando di una riga per provarlo.
- **Controllo**: il comando stampa 15 articoli, 200 ordini, 40 resi.

### Passo 3.2 · L'agente simulato (Giorgia, 20 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/agent_sim.py` seguendo `piano/01_FACILE.md` sezione 6. Funzione `gestisci_reso(return_id)`: trova l'ordine, legge la regola attiva più recente. Se la regola dice "prezzo_in_memoria" prende il prezzo dal ricordo in memoria (bug: è il listino); se dice "prezzo_pagato" prende il prezzo pagato nell'ordine. Restituisce due cose separate: (1) la risposta per il cliente ("Rimborso di X € avviato") e (2) il resoconto per l'azienda (Evento con orario, cliente, azione, importo, ID del ricordo usato, fonte del ricordo, versione della regola). L'agente non deve aspettare niente prima di rispondere.
- **Controllo**: provato su `RET` di Gianpaolo dà 120 €; su un reso non in promo dà il prezzo giusto.

### Passo 3.3 · Il registro (Giorgia, 10 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/recorder.py`: aggiunge un Evento in fondo al file `data/events.jsonl` (una riga per evento) e rilegge tutti gli eventi. Aggiungi una funzione `azzera()` che svuota il registro e una `carica_storico()` che fa passare all'agente tutti i resi tranne quello di Gianpaolo con date nelle due settimane passate, segnandoli come "storico" (sono i resi avvenuti prima della demo).
- **Controllo**: dopo `carica_storico()` il file ha 39 righe.

### Passo 3.4 · La sentinella (Sian, 15 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/sentinel.py` seguendo `piano/01_FACILE.md` sezione 6. Funzione `controlla(evento, ordini)` che restituisce una lista di allarmi. Regole: (1) rimborso maggiore del prezzo pagato → gravità alta, euro a rischio = differenza; (2) importo sopra 500 € → gravità media. Le regole sono scritte nel codice, niente AI. Dammi un comando per provarla sull'evento di Gianpaolo.
- **Controllo**: sull'evento di Gianpaolo esce "rimborso superiore al prezzo pagato", 40 € a rischio.

### Passo 3.5 · I casi simili (Sian, 15 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/similar.py`: dato un allarme, trova tutti gli altri eventi nel registro che hanno usato lo stesso tipo di ricordo (prezzo dalla memoria) e violano la stessa regola della sentinella. Restituisce l'elenco (cliente, ordine, rimborsato, pagato, differenza) e il totale in euro.
- **Controllo**: dopo lo storico e il reso di Gianpaolo: **37 casi, 1.480 €**.

### Passo 3.6 · Le spiegazioni (Sian, 20 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/explain.py` usando il prompt in `prototype/explain_prompt.txt`. Funzione `spiega(evento)`: prima cerca in `data/explanations_cache.json`; se non c'è, chiama l'LLM e salva in cache; se l'LLM dà errore o ci mette più di 8 secondi, usa una frase fissa costruita dai campi dell'evento ("Ho rimborsato X € perché il prezzo in memoria era X €, salvato il ... da ..."). Non deve mai far bloccare l'app.
- **Controllo**: funziona con la chiave; poi **prova a rinominare `.env` in `.env.off`**: deve uscire comunque la frase fissa. Rimetti il nome `.env`.

### Passo 3.7 · L'app, pagine Negozio e Timeline (Giorgia, 30 min)
- **Messaggio per Claude Code**:
  > Scrivi `src/app.py` con Streamlit seguendo `piano/01_FACILE.md` sezione 6, "Le 4 pagine dell'app". Per ora solo le pagine 1 e 2, con menu laterale. All'avvio: se il registro è vuoto, chiama `carica_storico()`. Pagina Negozio: pulsante "Gianpaolo chiede il reso" → mostra subito la risposta dell'agente; poi, dopo 1 secondo, "Resoconto ricevuto dall'azienda" e salva l'evento. Pagina Timeline: schede in ordine di tempo, più recenti in alto, ognuna con 4 righe fisse (Cosa ha fatto, Quale ricordo ha usato, Da dove arriva, Cosa non torna) e sotto il dato originale. Prendi tutti i testi visibili da `src/texts.py`. Aggiungi nel menu un pulsante "Azzera demo".
- **Terminale** (seconda finestra):
  ```bash
  cd ~/kva-ai-brain
  uv run streamlit run src/app.py
  ```
- **Controllo**: si apre il browser su `http://localhost:8501` (se non si apre, copia l'indirizzo nel browser). Clic sul pulsante → 120 €, poi "Resoconto ricevuto", e la scheda in Timeline.
- **Se non va**: errore rosso nella pagina → copialo in Claude Code (passo 0.7). Per riavviare l'app: `Ctrl+C` nel terminale e rilancia il comando. Streamlit di solito si aggiorna da solo quando salvi un file: premi "Rerun" in alto a destra.

### Passo 3.8 · Testi e numeri (Filippo, in parallelo dalle 14:00)
- **Messaggio per Claude Code**:
  > Scrivi `src/texts.py`: un dizionario con tutti i testi in italiano dell'app (titoli delle pagine, nomi dei pulsanti, frase di chiusura "Senza MemoLens: settimane e migliaia di euro. Con MemoLens: due minuti") e i numeri dello scenario (prezzo Business 299 €/mese, ROI circa 8x, con la nota "stima del team"). Niente logica, solo testi.

### Passo 3.9 · Pagine Allarmi e Correzione (Giorgia + Sian, 30 min)
- **Messaggio per Claude Code** (Giorgia):
  > In `src/app.py` aggiungi la pagina 3 "Allarmi e casi simili": usa `sentinel.controlla` sugli eventi nuovi (non sullo storico) e mostra gli allarmi in rosso; pulsante "Trova casi simili" che usa `similar.py` e mostra tabella e totale grande in euro. Aggiungi la pagina 4 "Correzione": mostra la regola attiva (versione, autore, data) e lo storico delle versioni; pulsante "Rimborso = prezzo pagato" che salva una nuova versione (autore "Responsabile customer care", data di oggi) e poi ripete il reso di Gianpaolo mostrando il nuovo importo.
- **Controllo**: allarme rosso → 37 casi, 1.480 € → correzione → reso di Gianpaolo a **80 €**, la versione 1 resta nello storico.

### Passo 3.10 · Primo giro completo (tutti, entro le 16:00)
1. Clic su "Azzera demo".
2. Sian legge il copione (sezione 9), Giorgia clicca, Filippo cronometra.
3. Ogni cosa che non va → una riga su un foglio. Si correggono **solo errori**, niente idee nuove.

### Passo 3.11 · Se avanza tempo: variante fabbrica (Sian, 20 min)
- **Messaggio per Claude Code**:
  > Leggi `piano/01_FACILE.md` sezione 11. Crea un secondo set di dati in `data/factory/` (ordini a fornitori, ricordo "lotto minimo fornitore = 500 pezzi, contratto 2024" con il contratto 2026 che dice 200) e aggiungi all'app un selettore "Negozio / Fabbrica" che usa lo stesso motore. Registra i nuovi dati in `research/data/README.md`.

---

## PARTE 4 · 16:15–17:00: chiusura

### Passo 4.1 · Stop alle funzioni nuove (16:15)
Da qui in poi si toccano solo errori che rompono la demo.

### Passo 4.2 · Video di riserva (Giorgia + Filippo, 10 min)
- "Azzera demo", poi registra lo schermo mentre fai tutto il copione.
- **Come registrare**: su Windows `Win + G` (barra Xbox) → registra; su Ubuntu `Ctrl + Alt + Shift + R` (si ferma con la stessa combinazione); in alternativa OBS Studio.
- Salva il video sul computer di Filippo **e** su una chiavetta o un Drive.

### Passo 4.3 · README e controllo chiavi (Giorgia)
- **Messaggio per Claude Code**:
  > Aggiorna `README.md` per la consegna: cos'è MemoLens in 3 righe, come si avvia (`uv sync` e `uv run streamlit run src/app.py`), struttura dei file di `src/`, dati sintetici, e una sezione obbligatoria "Strumenti AI usati" (Claude Code per scrivere il codice, il modello LLM usato nell'app per le spiegazioni, eventuali altri). Poi controlla che nessuna chiave sia mai stata salvata nella storia di git.
- **Terminale** (controllo finale delle chiavi; non deve stampare niente):
  ```bash
  git log -p | grep -iE "api_key|sk-|AIza"
  ```
- Giro di salvataggio finale (passo 0.6).

### Passo 4.4 · Prima della presentazione (tutti)
- App aperta, "Azzera demo" premuto, browser a schermo intero (`F11`), altre finestre chiuse, notifiche spente.
- Video di riserva aperto in un'altra finestra (Filippo).
- Sian ha davanti il copione e le risposte della sezione 13.
