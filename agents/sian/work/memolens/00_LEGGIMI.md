# MemoLens: tre piani per l'hackathon (facile, medio, difficile)

Autore: Sian (con Claude) · 13.11.2026 · Base: `MemoLens_Hackathon_Track4.docx` e `.pptx`

Questi file sono **mappe**: come costruirei MemoLens, non il codice. Ognuno è autonomo: idea, business, architettura, collegamenti, piano ora per ora, demo, rischi e domande della giuria.

| File | Per chi | Cosa si vede nella demo | Rischio | Punteggio atteso |
|---|---|---|---|---|
| `01_FACILE.md` | Se sabato abbiamo poco tempo o poca esperienza | Agente simulato (script), timeline, allarme, casi simili, correzione con replay | Molto basso | Buono in tecnica e demo, medio in "tema" |
| `02_MEDIO.md` | **Consigliato.** Equilibrio tra effetto "wow" e sicurezza | Agente vero (LLM con strumenti), memoria con versioni e fonte, grafo decisione→ricordo, supersession, "evidenza insufficiente" | Medio | Alto su tutti i criteri |
| `03_DIFFICILE.md` | Solo se il medio è pronto alle 15:30 o se prepariamo molto stanotte | Tutto il medio + oggetti di conoscenza tipizzati stile OIDA, memoria bitemporale, server MCP interrogabile da Claude, replay controfattuale, export AI Act | Alto | Massimo sul "tema" (25%, decide i pareggi), se funziona |

## Il vincolo che decide tutto

L'agenda ufficiale di sabato lascia **3 ore di costruzione (14:00–17:00)**. In più ci sono 10:30–12:30 (ideazione) e 13:00–14:00 (pranzo e architettura). Le regole dicono che il prodotto si scrive in `src/` il giorno stesso: prima si possono preparare solo dati, prompt, scaletta e test usa e getta in `prototype/`.

Quindi: **il piano medio si fa solo se stanotte prepariamo dati e prompt**. Il difficile si costruisce a strati, sopra un medio che funziona già.

## Strategia consigliata: "a scala"

1. Si parte dal **FACILE** (è il primo strato del medio, non un lavoro buttato).
2. Alle 15:00 il facile funziona? Si aggiungono gli strati del **MEDIO**.
3. Alle 15:45 il medio funziona? Si aggiunge **un solo** pezzo del DIFFICILE: il server MCP (è il più forte per la giuria, che ha costruito OIDA esposto via MCP).
4. **16:30 stop alle funzioni nuove**, video di riserva, prova del pitch.

## Attenzione: il tema della gara è "AI brain for **industry**"

Il caso Gianpaolo è e-commerce. La giuria (KVA) guarda adesso all'industria (Gergo, bando manifattura, vedi `research/kva-interests.md`). Ogni piano ha una sezione **"Variante industriale"**: stesso motore, secondo scenario in fabbrica (agente che riordina materiale a un fornitore usando un lotto minimo superato). Basta un secondo file di dati: mostrarlo per 20 secondi alza il punteggio su "tema" e "problema reale".

## Da fare stanotte (venerdì 13), qualunque piano si scelga

- [ ] Sian: decidere con Filippo e Giorgia quale livello puntare (messaggio sul canale `coord`).
- [ ] Preparare il **dataset finto**: 1 catalogo, 200 ordini, 40 resi di cui 38 con articoli in promozione (servono i 37 "casi simili" della demo + Gianpaolo). Va registrato in `research/data/README.md` come "dati sintetici, creati dal team".
- [ ] Scrivere il prompt della "spiegazione in italiano semplice" e provarlo 5 volte in `prototype/`.
- [ ] Tenere almeno una chiave API funzionante in `.env` (`bash scripts/set_key.sh`).
- [ ] Copione della demo stampato (sezione "Demo" del file scelto).
