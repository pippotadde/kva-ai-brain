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
