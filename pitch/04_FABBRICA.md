# MemoLens in fabbrica

14.11.2026 · Giorgia (con Claude) · Documento vivo: https://claude.ai/artifact/UrpYoBtKr4PpBQWvtY9BEp

## Consegna delle 12:30

Alle 12:30 servono l'abstract qui sotto (1.197 caratteri su 1.200) e un video di 50 secondi. Il video si gira con lo schermo e una voce: niente codice, bastano tre slide o un mock-up del grafo disegnato a mano.

Traccia consigliata: **Blackbox agents** (seconda scelta: Making memory visible to people). Si cambia fino alle 12:15.

### Abstract

PROBLEMA. In uno stabilimento dolciario un agente AI decide l'ordine dei lotti e le pulizie tra i prodotti, usando schede fornitori e procedure. Quando un documento cambia, nessuno sa quali decisioni si basavano sulla versione vecchia.

DATI. Nel 2023 il 49% dei richiami alimentari USA era dovuto ad allergeni non dichiarati, e un richiamo costa in media 10 milioni di dollari. Gartner prevede che oltre il 40% dei progetti con agenti AI verrà cancellato entro il 2027, anche per controlli sul rischio inadeguati.

PROPOSTA. MemoLens registra la memoria degli agenti di fabbrica: per ogni decisione, quale informazione è stata usata, da quale documento e revisione, e se era ancora valida.

PROTOTIPO. Un agente pianifica 14 lotti con la scheda cacao rev 2. Carichiamo la rev 3 ("può contenere arachidi"): MemoLens segna superata la rev 2, trova i lotti decisi con quella e li blocca. Se una nota di turno smentisce la procedura di pulizia, applica la procedura e spiega perché. Se manca una validazione, risponde "evidenza insufficiente".

EFFICACIA. Le regole sugli allergeni le applica il codice, non il modello AI. Ogni decisione si ricostruisce fino al documento, pronta per audit e AI Act.

Fonti dei dati: PIRG via Food Safety Magazine (richiami USA 2023), New Food Magazine (costo medio di un richiamo), Gartner (progetti agentici cancellati). I 14 lotti e le schede sono dati sintetici del team.

### Copione del video (50 secondi)

| Secondi | Cosa si vede | Voce (Sian) |
| --- | --- | --- |
| 0-8 | Foto o disegno di una linea di cioccolatini, scritta "L'agente AI ha deciso: giovedì linea 2, nocciola poi fondente" | "In questa fabbrica un agente AI decide l'ordine dei lotti e le pulizie tra un prodotto e l'altro." |
| 8-18 | Scheda del cacao rev 2 accanto alla rev 3, evidenziata la riga "può contenere arachidi" | "Lunedì il fornitore cambia la scheda del cacao. L'agente non se ne accorge e continua a usare quella vecchia." |
| 18-24 | Numero grande: "49% dei richiami USA 2023 = allergeni · 10 M$ a richiamo" | "Metà dei richiami alimentari nasce così, e ognuno costa milioni." |
| 24-40 | Mock-up di MemoLens: grafo decisione → ricordo → documento, il ricordo rev 2 diventa rosso, compaiono "14 lotti a rischio" in rosso | "MemoLens è il registratore di volo della sua memoria. Mostra quale ricordo ha usato ogni decisione, lo segna in rosso quando viene superato e trova tutti i lotti colpiti prima che escano dalla fabbrica." |
| 40-46 | Riquadro: "Per la linea 3 non ho una validazione della pulizia per il sesamo: non posso dire se è ammesso" | "E quando mancano le prove, lo dice." |
| 46-50 | Logo MemoLens, nomi del team | "MemoLens: l'AI in fabbrica, con la memoria in vista. Team Giorgia, Sian, Filippo." |

Il numero di lotti (14) è inventato per la demo: i dati restano sintetici e lo diciamo nel pitch. Video: registrazione schermo di Google Slides con voce, MP4 sotto i 25 MB.

- [ ] Sian registra la voce entro le 12:00
- [ ] Filippo prepara le 4 schermate del video entro le 11:50
- [ ] Giorgia carica video e abstract su /hackathon/live entro le 12:20

## Il progetto in breve

MemoLens registra la memoria degli agenti AI che decidono in fabbrica e blocca le decisioni prese con un ricordo superato. Il primo caso è l'agente che pianifica i cambi formato in uno stabilimento dolciario, dove un ricordo vecchio sugli allergeni porta a un richiamo.

| Voce | Contenuto |
| --- | --- |
| Problema | L'agente decide con ricordi presi da schede fornitori, procedure di pulizia e note di turno. Quando un documento cambia, nessuno sa quali decisioni usavano la versione vecchia |
| Prodotto | Un SDK che avvolge gli strumenti dell'agente e registra ogni ricordo usato, con fonte e validità. Sopra: grafo decisione → ricordo → documento, allarme, lotti colpiti, correzione con traccia |
| Utente | Responsabile qualità e capoturno: capiscono in un minuto perché l'agente ha deciso così |
| Compratore | Direttore di stabilimento o responsabile qualità, soprattutto nei co-packer che lavorano per i marchi della GDO |
| Installazione | Lo sviluppatore o l'integratore che ha costruito l'agente: poche righe di codice, nessuna attesa per l'agente |
| Il numero che migliora | Lotti bloccati o richiamati per allergeni, ore per preparare un audit, tempo per capire un errore dell'agente |

**I tre momenti della demo.** Il ricordo superato (scheda cacao rev 2 sostituita dalla rev 3). La contraddizione (la nota di turno dice "dopo la nocciola basta la pulizia a secco", la procedura PUL-07 rev 5 chiede quella umida: vince la procedura, e MemoLens dice perché). Il "non lo so" (nessuna validazione della pulizia per il sesamo sulla linea 3).

**Perché non è OIDA.** OIDA di KVA è un registro governato delle decisioni prese dalle persone. MemoLens lavora un livello sotto: la memoria che un agente usa mentre agisce, ricordo per ricordo. Applichiamo gli stessi principi (sostituzione, provenienza, astensione) agli agenti, e MemoLens potrebbe leggere da OIDA come fonte.

**Perché ora.** L'AI Act chiede log automatici per i sistemi ad alto rischio (art. 12). Il Reg. UE 1169/2011 obbliga a dichiarare 14 allergeni, e la tracciabilità dei lotti è già obbligatoria. Gli agenti stanno entrando in pianificazione e qualità, ma nessuno controlla la loro memoria.

## Analisi di mercato

Lo spazio libero sta tra due mercati affollati: gli strumenti di osservabilità per gli agenti parlano solo agli sviluppatori, e i software per gli allergeni sono checklist che non sanno nulla degli agenti. Nessuno dei concorrenti trovati collega la revisione di una scheda fornitore alle decisioni già prese da un agente. I numeri "stima del team" vanno detti così ad alta voce.

### Il problema in numeri

- Nel 2023 il 49,2% dei 313 richiami alimentari USA era dovuto ad allergeni non dichiarati ([PIRG via Food Safety Magazine](https://www.food-safety.com/articles/9437-thanks-sesame-us-food-recalls-due-to-undeclared-allergens-skyrocketed-in-2023-causing-half-of-all-food-recalls)).
- Un richiamo costa in media 10 M$ di soli costi diretti ([New Food Magazine](https://newfoodmagazine.com/?p=247701)).
- Gartner prevede che oltre il 40% dei progetti con agenti AI sarà cancellato entro il 2027, anche per controlli sul rischio inadeguati ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)).
- L'AI Act chiede log automatici per i sistemi ad alto rischio, obbligo dal 2 dicembre 2027 secondo il calendario aggiornato ([AI Act, art. 12](https://artificialintelligenceact.eu/article/12/)).

### Dimensione

| Livello | Chi | Valore |
| --- | --- | --- |
| Mercato di contesto | Agenti AI nel mondo | da 7,84 a 52,62 mld $ tra 2025 e 2030 ([MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/ai-agents-market-15761548.html)) |
| Mercato di contesto | Osservabilità degli agenti | 0,4 mld $ nel 2025, 7,1 mld $ nel 2035 ([Astute Analytica](https://www.astuteanalytica.com/industry-report/ai-agent-observability-market)) |
| Bacino in Italia | Imprese alimentari | 60.000 ([Federalimentare-Censis via Italpress](https://www.italpress.com/per-lindustria-del-food-italiano-179-mld-di-fatturato-annuo/)) |
| Primo segmento | Stabilimenti con linee condivise tra prodotti con e senza allergeni, soprattutto co-packer per la GDO | Da verificare: circa 2.000-3.000 in Italia (stima del team) |
| Obiettivo al 3° anno | 150 stabilimenti a 390 €/mese | circa 700 k€/anno (stima del team) |

### Concorrenti

| Concorrente | Cosa fa | Cosa non fa |
| --- | --- | --- |
| [Langfuse](https://langfuse.com/faq/all/langsmith-alternative), LangSmith, Arize, Datadog | Tracciano chiamate e passaggi degli agenti, per sviluppatori | Non sanno cos'è un allergene, un lotto o una revisione di documento; nessuna vista per la qualità |
| [Mem0](https://guide.mem0.ai/faq/we-built-our-ai-memory-layer-in-house-and-it-has-no-audit-trail-we-are-losing-deals-because-of-it-wh-5bf5c6), Zep | Danno memoria agli agenti, Mem0 aggiunge una traccia per audit | Memoria generica, non collegata alle decisioni di fabbrica né ai lotti colpiti |
| [iFactory](https://ifactoryapp.com/industries/food-manufacturing/best-allergen-changeover-cip-verification-software-2026), [Oxmaint](https://oxmaint.com/industries/food-manufacturing/allergen-changeover-validation-maintenance-cmms-guide) | Checklist digitali, convalida della pulizia, manutenzione | Non controllano agenti AI; non propagano la revisione di una scheda fornitore |
| [Redzone](https://www.rzsoftware.com/product/compliance), [Tulip](https://tulip.co/traceability-and-compliance/line-clearance-software/), SafetyCulture | Line clearance, conformità, app di reparto | Registrano cosa fa l'operatore, non cosa ricordava l'agente |
| OIDA (KVA) | Registro governato delle decisioni, via MCP | Decisioni delle persone, non la memoria degli agenti mentre agiscono; possibile fonte per MemoLens, non un concorrente |

Saturazione: media (3 su 5). L'osservabilità generica è piena, ma la combinazione "agente di fabbrica + documenti di qualità + lotti colpiti" è libera per quanto visto. Rischio: Langfuse o un MES aggiungono la funzione. Difesa: modello dei dati di qualità alimentare e canale dei consulenti HACCP.

### Prezzi e conti (stima del team)

| Piano | Prezzo | Cosa include |
| --- | --- | --- |
| Pilota | 0 € per 60 giorni | 1 linea, 1 agente |
| Stabilimento | 390 €/mese | Tutte le linee, lotti colpiti, registro per audit, 12 mesi di storico |
| Gruppo | da 1.500 €/mese | Più stabilimenti, installazione presso il cliente, collegamento a MES ed ERP |

- Il piano Stabilimento costa 4.680 €/anno, meno dello 0,05% del costo medio di un richiamo.
- Costo per cliente: circa 40 €/mese tra server e modello, margine lordo intorno all'89%. Da ricalcolare con il prezzo del modello Claude usato oggi (il piano di Sian usava GPT-4o mini).
- Canale: consulenti HACCP e certificatori (BRCGS, IFS), e gli integratori che costruiscono gli agenti.

## Bozza di pitch (3:00 di demo + 1:30 di domande)

Demo dal vivo raccontata: problema in 30 secondi, poi lo schermo fa il lavoro. Parla Sian, Giorgia guida l'app, Filippo chiude con i numeri. Pitch artifact con link alla repo e modelli usati entro le 16:45.

| Tempo | Chi | Cosa si vede | Cosa si dice |
| --- | --- | --- | --- |
| 0:00-0:25 | Sian | Piano di giovedì della linea 2, tutto verde | "Questo piano l'ha fatto un agente AI. Decide l'ordine dei lotti e la pulizia tra uno e l'altro. Ma su cosa si basa? Nessuno lo vede." |
| 0:25-0:55 | Giorgia | Clic su un cambio formato: grafo decisione → ricordo → documento, con fonte e data | "MemoLens mostra ogni ricordo usato: questa decisione si basa sulla scheda cacao rev 2, pagina 2, valida dal 3 marzo." |
| 0:55-1:35 | Giorgia | Si carica la scheda cacao rev 3. La rev 2 diventa rossa, due cambi formato diventano rossi, compare "14 lotti colpiti" | "Il fornitore aggiunge le tracce di arachidi. MemoLens trova da solo tutte le decisioni prese con il ricordo vecchio e le blocca. Il modello legge la scheda, ma è il codice a decidere." |
| 1:35-2:00 | Giorgia | Allarme contraddizione: nota di turno contro PUL-07 rev 5 | "Due fonti si contraddicono. Vince la procedura validata, e MemoLens dice perché." |
| 2:00-2:15 | Giorgia | Domanda sul sesamo alla linea 3: "evidenza insufficiente" | "Quando mancano le prove, non indovina." |
| 2:15-2:25 | Giorgia | (Se pronto) Claude chiede a MemoLens via MCP "perché il lotto 2611 è bloccato?" | "E ogni altra AI può chiedergli perché." |
| 2:25-3:00 | Filippo | Slide con prezzo, ROI e canale | "390 euro al mese per stabilimento, meno dello 0,05% di un richiamo. Vendiamo tramite consulenti HACCP. Si collega all'agente con poche righe." |

### Domande probabili e risposte

| Domanda | Risposta |
| --- | --- |
| Che differenza c'è con OIDA? | OIDA registra le decisioni delle persone. MemoLens registra la memoria degli agenti mentre agiscono, e può usare OIDA come fonte |
| Ci sono davvero agenti AI che pianificano in fabbrica? | Stanno arrivando, e Gartner dice che il 40% dei progetti fallisce anche per mancanza di controlli. MemoLens serve a farli passare in produzione |
| E se l'AI sbaglia a leggere la scheda? | L'AI estrae con citazione della pagina, il codice applica le regole. Ogni estrazione si vede e si corregge, con traccia |
| Perché voi? | Punto debole: va detto il contatto nella qualità alimentare, se lo troviamo stamattina |
| Come entrate in un'azienda? | Pilota gratuito di 60 giorni su una linea, tramite il consulente HACCP che già la segue |
| Dati veri? | Oggi sintetici, creati dal team e dichiarati. Gli allergeni sono i 14 del Reg. UE 1169/2011 |
| Quanto costa a voi un cliente? | Circa 40 € al mese tra server e modello, ricalcolato con il prezzo di Claude |

## Piano operativo della giornata

Si costruisce il MEDIO di Sian "a scala", cambiando solo dati e testi: dalle 14:00 alle 16:15 uno strato alla volta, alle 16:15 stop alle funzioni nuove. Prima delle 14:00 solo dati, prompt e copione in `prototype/`; il codice del prodotto si scrive oggi in `src/`, nella repo pubblica.

### Cosa cambia rispetto ai piani di Sian

| Nel piano MEDIO | Diventa |
| --- | --- |
| Agente resi del negozio | Agente pianificatore della linea 2 (strumenti: leggere il piano, leggere le schede, ricordare, proporre sequenza e pulizia) |
| Ricordo "rimborsa il prezzo di listino" | Ricordo "cacao fornitore X: senza arachidi" da scheda rev 2 |
| 38 resi con articoli in promozione | 10-14 lotti pianificati con il cacao del fornitore X |
| Allarme "rimborso maggiore del pagato" | Regola in codice: "prodotto etichettato senza arachidi dopo un ingrediente che può contenerle, senza pulizia umida validata = non ammesso" |
| Euro di rimborsi persi | Lotti bloccati prima della spedizione ed euro di richiamo evitati |
| Evidenza insufficiente: due ricordi in conflitto | Nota di turno contro PUL-07 rev 5, e la validazione del sesamo che manca |

### Ora per ora

| Ora | Giorgia (architettura) | Sian (dati, AI, pitch) | Filippo (schermata, business) |
| --- | --- | --- | --- |
| 10:40-11:00 | Conferma l'idea sul canale del team, legge questo documento | Legge il copione del video | Legge il copione del video |
| 11:00-12:00 | Schema dei dati: Documento (rev, valido dal/fino al), Ricordo, Decisione, Lotto, Regola | Scrive le schede inventate: cacao rev 2 e rev 3, 5 ricette, PUL-07 rev 5, 10 note di turno, piano di 14 lotti | Prepara le 4 schermate del video e la slide dei numeri |
| 12:00-12:30 | Carica video e abstract entro le 12:20 | Registra la voce del video | Monta il video in MP4 sotto i 25 MB |
| 13:00-14:00 | Architettura su un foglio: SDK, registro, motore regole, Streamlit | Prompt di estrazione con citazione di pagina, provato 5 volte in `prototype/` | Business plan: prezzi, costo per cliente con Claude, conti a 3 anni |
| 14:00-15:00 | Strato FACILE: registro eventi, memoria con versioni, motore regole, "lotti colpiti" | Agente pianificatore con strumenti (LLM vero), con riserva simulata | Streamlit: piano a semafori e scheda della decisione |
| 15:00 | Controllo: la demo di base gira dall'inizio alla fine? Se no, si resta sul FACILE | | |
| 15:00-15:45 | Strati MEDIO: sostituzione rev 2 → rev 3, contraddizione, "evidenza insufficiente" | Estrazione AI dalla scheda nuova con citazione; spiegazioni in italiano con testo di riserva | Grafo decisione → ricordo → documento con ricordo rosso |
| 15:45-16:15 | Un solo pezzo del DIFFICILE: server MCP che risponde "perché è bloccato?" | Prova del copione con l'app vera | Ricalcola i numeri del pitch, README della repo |
| 16:15 | Stop alle funzioni nuove | Registra il video di riserva della demo | |
| 16:15-16:45 | Correzioni, push finale, link alla repo | Prova del pitch due volte, a tempo | Pitch artifact con repo e modelli usati, consegna alle 16:45 |
| 17:05 | Show-off: guida l'app | Racconta | Chiude con i numeri e risponde sul business |

### Prima delle 12:30

- [ ] Messaggio sul canale del team: idea scelta "MemoLens in fabbrica"
- [ ] Traccia cambiata in Blackbox agents (entro le 12:15)
- [ ] Abstract incollato su /hackathon/live
- [ ] Video MP4 da 50 secondi caricato
- [ ] Una telefonata o un messaggio a qualcuno della qualità alimentare, per il diritto di vincere

## Rischi e piano B

| Rischio | Piano B |
| --- | --- |
| L'agente LLM vero non funziona entro le 15:00 | Agente simulato del FACILE: la demo resta identica |
| La chiave KVA finisce o il gateway non risponde | Cache delle spiegazioni e testi di riserva già scritti |
| L'app si blocca durante lo show-off | Video di riserva registrato alle 16:15 |
| La giuria lo vede come una copia di OIDA | Frase pronta: "OIDA per le decisioni delle persone, MemoLens per la memoria degli agenti" |
| "Agenti in fabbrica non esistono ancora" | Si parte dal problema reale (richiami per allergeni) e da Gartner sul 40% di progetti cancellati |
| Diritto di vincere basso | Un contatto vero nella qualità alimentare, anche solo citato |

## Fonti

- [Food Safety Magazine su PIRG](https://www.food-safety.com/articles/9437-thanks-sesame-us-food-recalls-due-to-undeclared-allergens-skyrocketed-in-2023-causing-half-of-all-food-recalls): richiami USA 2023 per allergeni
- [New Food Magazine](https://newfoodmagazine.com/?p=247701): costo medio di un richiamo
- [Italpress, Federalimentare-Censis](https://www.italpress.com/per-lindustria-del-food-italiano-179-mld-di-fatturato-annuo/): imprese alimentari in Italia
- [MarketsandMarkets, AI Agents Market](https://www.marketsandmarkets.com/Market-Reports/ai-agents-market-15761548.html) e [Astute Analytica, AI Agent Observability](https://www.astuteanalytica.com/industry-report/ai-agent-observability-market), dal documento di Sian
- [Gartner, progetti agentici cancellati](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- [AI Act, articolo 12](https://artificialintelligenceact.eu/article/12/)
- Concorrenti: [Langfuse](https://langfuse.com/faq/all/langsmith-alternative), [Mem0](https://guide.mem0.ai/faq/we-built-our-ai-memory-layer-in-house-and-it-has-no-audit-trail-we-are-losing-deals-because-of-it-wh-5bf5c6), [iFactory](https://ifactoryapp.com/industries/food-manufacturing/best-allergen-changeover-cip-verification-software-2026), [Oxmaint](https://oxmaint.com/industries/food-manufacturing/allergen-changeover-validation-maintenance-cmms-guide), [Redzone](https://www.rzsoftware.com/product/compliance), [Tulip](https://tulip.co/traceability-and-compliance/line-clearance-software/)
- Piani di Sian: 00_LEGGIMI, 01_FACILE, 02_MEDIO, 03_DIFFICILE e MemoLens_Hackathon_Track4.docx
