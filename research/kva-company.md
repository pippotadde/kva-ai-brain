# KVA — chi sono, cosa fanno, cosa ne deduciamo per vincere

Ricerca del 12.11.2026 su sito kakashi.ventures, projectoida.com, arXiv, GitHub di KVA e stampa. Le affermazioni di KVA su prestazioni e clienti sono loro (non verificate).

## 1. Chi sono

- **Kakashi Venture Accelerator (KVA)**, Torino (Via Sant'Antonino 17B), fondata nel 2022 da **Federico Bottino** (CEO) e **Alberto Trivero**. "Primo AI Native Venture Studio in Italia". Circa 11 persone, team di ricerca internazionale (cercano neuroscienziati, fisici, matematici).
- A novembre 2025 il **Gruppo Excellence** (consulenza per banche, assicurazioni, asset management; fondato nel 2007 da Maurizio Primanni e Renato Ferri Pacini) ne ha preso la maggioranza. Obiettivo dichiarato: un unico operatore italiano dalla consulenza alle soluzioni AI proprietarie e agli investimenti.
- Dicono di essere **Anthropic Ambassadors** e nel programma Claude for Organizations; "tutti i nostri venture builder sono certificati Claude".
- Fonti: [FinanceCommunity](https://financecommunity.it/il-gruppo-excellence-acquisisce-ai-native-venture-studio-kva/), [AziendaBanca](https://www.aziendabanca.it/notizie/tecno/excellence-acquisisce-kva), [Gruppo Excellence](https://gruppoexcellence.com/en/excellence-group-acquires-kva-kakashi-venture-accelerator-the-first-ai-native-venture-studio-in-italy), [kakashi.ventures](https://www.kakashi.ventures/en).

## 2. Cosa fanno

| Linea | In breve |
|---|---|
| Venture building | Costruiscono startup da zero con un loro stack e team ("MVP in 4–8 settimane") |
| Corporate acceleration | "Department as a Service" per aziende: strategia, tech, AI |
| Venture capital | Seed / pre-Series A, 50–100 k€ (Call4Ventures) |
| Technology | RAG con provenienza e rilevazione delle contraddizioni, piccoli modelli locali, agenti, server MCP, **Knowledge Architecture**, Privacy Gateway |
| Research | Paper su arXiv e conferenze NLP, dataset aperti |
| Knowledge transfer | Workshop e academy aziendali |

**Metodo dichiarato:** AI native, guidato dai dati, veloce, europeo (GDPR e AI Act by design). "Ogni prodotto è validato due volte: su benchmark accademici e con clienti paganti."

## 3. I loro prodotti — il punto chiave

| Prodotto | Cosa fa | Settore |
|---|---|---|
| **Project OIDA** | "Ontologie e memoria per infrastruttura agentica". Registro governato delle decisioni aziendali: per ogni decisione evidenze, date di efficacia, storia, **sostituzioni** e **conflitti**. Un **risolutore deterministico** stabilisce quale decisione vale; se le evidenze non bastano **lo dice invece di indovinare**. Esposto via **MCP** a Claude, ChatGPT, Cursor, Copilot. Round di finanziamento da luglio 2026. | Banche, assicurazioni, consulenza |
| **Control8** | "Il cervello operativo di un'organizzazione": progetti, compiti, documenti e decisioni in un registro, usato dagli agenti via MCP. | Interno / aziende |
| Catalyst | Multi-agente per migrare codice legacy (COBOL, mainframe) | Banche, assicurazioni |
| Vaglio | Pubblici sintetici per testare prodotti | Banche, assicurazioni |
| Valico (Privacy Gateway) | Pseudonimizzazione di documenti regolamentati prima dell'AI | Finanza italiana |
| AskMadarAI | Suite AI per wealth management | Finanza |
| NewJee, Kansei | Analisi delle notizie, redazione agentica | Media |
| Magellan | Ricerca scientifica multi-agente | Scienza |
| Elevia, JyraIA | Competenze e formazione; corsi di compliance da testi normativi | HR, compliance |
| gergoAI (GitHub, nov 2026) | Controllo vocale per addestrare robot collaborativi | Robotica |

## 4. La loro teoria (il paper dei giurati)

**"Retrieval Is Not Enough: Why Organizational AI Needs Epistemic Infrastructure"** — Bottino, **Ferrero**, Dosio, Beneventano, arXiv 2604.11759, aprile 2026. Dataset: [oida-evaluation-corpora](https://github.com/kakashi-ventures/oida-evaluation-corpora).

- Tesi: il limite dell'AI aziendale non è trovare i documenti giusti ma la **"fedeltà epistemica"**: rappresentare quanto è forte un impegno, se c'è una contraddizione e **cosa l'organizzazione non sa**, come proprietà calcolabili.
- **Knowledge Objects** tipizzati in 9 classi: Decision, Evidence, Hypothesis, Observation, Open Question, Contradiction, Assumption, Claim, Signal. Il tipo decide peso, velocità di "decadimento" e sensibilità alle contraddizioni.
- Archi di contraddizione con segno; importanza e decadimento calcolati **con formule deterministiche, "non dall'umore di un LLM"**.
- **Open Question** con decadimento inverso: ciò che non si sa diventa sempre più urgente.
- Pipeline in 7 passi: ingestione → segmentazione per affermazione → chi l'ha detto e con quale autorità → classificazione epistemica → provenienza ancorata al pezzo di testo → confidenza e decadimento → ciclo di vita (versioni, **supersession**, archiviazione, contraddizioni).
- Governance: "gli LLM leggono gli schemi; il sistema li definisce". Violazioni dello schema = errore bloccante, nessuna scorciatoia.
- Differenza dichiarata dalle "piattaforme ontologiche tipo Palantir": loro lavorano sul livello epistemico (cosa si crede, con quale fiducia, come cambia).

## 5. La giuria

| Giurato | Chi è |
|---|---|
| Federico Bottino | CEO KVA, primo autore del paper; parla di AI come "filosofia applicata fondata su matematica e logica" |
| Carlo Ferrero | KVA, coautore del paper OIDA |
| Davide Lai | Lead Researcher KVA; nel comitato scientifico con affiliazione DESY (centro di ricerca di fisica) |
| Dario Martinelli | Non trovato |
| Quinto | Non annunciato |

## 6. Come scelgono le idee (Call4Ideas)

"Innovation Potential Score" su 5 assi: **massa di lavoro** (quante persone fanno quel lavoro), **vuoto di innovazione**, **leva di automazione**, **barriere superabili**, **diritto di vincere**. "Due assi sono decisivi: leva di automazione e diritto di vincere. Se manca uno dei due, la proposta non passa."

Aree della Call4Ideas: servizi professionali, deep tech agentica, **memoria e ontologie**, business intelligence, **industria e robotica**, scienza e ingegneria. Call4Ventures tematiche: fintech, insurtech, cybersecurity, servizi professionali, **manufacturing**, **physical AI**, ricerca autonoma.

## 7. Cosa ne deduciamo

1. **La giuria ha scritto la teoria del tema.** Il tema della gara coincide con OIDA. Ci giudicheranno con il loro modo di pensare: supersession, provenienza, contraddizioni, determinismo, astensione quando mancano prove.
2. **Non copiare OIDA in generale.** Un "OIDA più debole" perde. Vince **applicare quei principi a un'industria che KVA non copre** con un'ontologia di dominio vera.
3. **Il vuoto di KVA è l'industria.** Il loro portafoglio è finanza, assicurazioni, media. Mancano manifattura, aerospazio, energia, sanità, logistica, costruzioni. Hanno però call aperte su manufacturing e physical AI, e il tema è "AI brain per industrie deep-tech". Le nostre proposte A (aviazione) e D (sicurezza in fabbrica) cadono esattamente nel vuoto.
4. **Il nostro principio "l'AI estrae, le regole decidono" è il loro.** Va detto con le loro parole: risoluzione deterministica, provenienza, supersession, "evidenza insufficiente" invece di inventare.
5. **Elementi che li colpiranno:** classificare le informazioni per tipo (decisione, evidenza, ipotesi, domanda aperta…); mostrare una contraddizione rilevata; rispondere "non ho abbastanza evidenze" quando serve; esporre la memoria via **MCP** così Claude la può interrogare.
6. **Pitch con i loro criteri:** dire esplicitamente massa di lavoro, leva di automazione e **diritto di vincere** (perché noi). Pensare all'opzione B: presentarci come possibile verticale industriale compatibile con il loro ecosistema.
7. **Linguaggio corretto sulla privacy:** loro distinguono "pseudonimizzazione" da "anonimizzazione". Se usiamo dati di persone, usare il termine giusto.
8. **Usare Claude** nel prodotto e dirlo: sono Anthropic Ambassadors.
