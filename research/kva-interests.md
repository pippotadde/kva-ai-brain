# KVA — cosa gli interessa davvero (segnali per scegliere l'idea)

Ricerca del 12.11.2026 sera. Completa `research/kva-company.md` (chi sono, OIDA, paper). Qui: **tutti i segnali di interesse** trovati — prodotti, bandi, clienti, ricerca, persone, ultimo progetto — e cosa ne deduciamo per l'idea. Le affermazioni di KVA sono loro, non verificate.

## 0. In sintesi (le 6 cose da ricordare)

1. **L'ultimo progetto dei fondatori è industriale.** Il 5.11.2026 (9 giorni prima della gara) Bottino e Trivero hanno presentato **Gergo** a un hackathon a Pavia: controllo vocale in italiano per cobot in fabbrica, con memoria della postazione, versioni approvate e registro. Principio: **"Il modello capisce. Il codice decide."** È la prova più fresca di dove guardano adesso.
2. **Hanno un bando aperto "AI per industria e manifattura" (fino a 75 k€)** che chiede un caso d'uso **misurabile in reparto: tempo ciclo, scarti, fermi, costi**, integrato con MES, ERP, PLC, sensori. Ambito: pianificazione, qualità, manutenzione predittiva, energia, supply chain, **know-how di stabilimento**.
3. **Bando "Physical AI e robotica" (fino a 50 k€)**: robotica, sistemi autonomi, visione, sensori, **sicurezza**; magazzini, cantieri, campi, infrastrutture.
4. **Call4Ideas**: tra le 6 aree ci sono **"memoria e ontologie"** e **"AI per le fabbriche e il mondo fisico"** (qualità, manutenzione, supply chain, robot accanto alle persone). Voto su 5 assi; **leva di automazione** e **diritto di vincere** sono decisivi: se ne manca uno, l'idea non passa.
5. **Regole della gara = venture building.** Il premio è 1.500 € per i diritti del progetto *oppure* 1.500 € per il 15% di una società da costituire entro 90 giorni; KVA ha **12 mesi di prelazione** su ogni progetto. Stanno cercando **un'azienda che vorrebbero costruire**, non un esercizio.
6. **Clienti e vendite reali sono finanza/assicurazioni** (via Gruppo Excellence). Industria = dove vogliono andare ma **non hanno ancora prodotti**, a parte Gergo. Il nostro spazio.

## 1. Gergo — il loro progetto più recente (5.11.2026)

Fonti: [repo GitHub](https://github.com/kakashi-ventures/gergoAI), [sito](https://gergoai.kakashi.ventures/), [approfondimento di mercato](https://gergoai.vercel.app/approfondimento).

- **Cosa:** l'operatore di linea "allena" il cobot a voce, in italiano, senza codice e senza aspettare il tecnico. Gergo ricorda la postazione, propone miglioramenti, ogni modifica passa da 6 controlli (persona, codice, agente AI, revisione, CI, bridge) prima di arrivare al braccio.
- **Idee che ricorrono (le stesse di OIDA, in fabbrica):**
  - l'LLM passa solo **intenzioni**; numeri, limiti e sicurezza li calcola il **codice deterministico**;
  - ogni modifica è una **versione** (bozza → confermata → deprecata), approvata da una persona, reversibile;
  - **registro** di ogni operazione (detto → capito → sì → parte → fine), esportabile come dataset;
  - "ontologia confermata" della postazione: il gergo dei reparti ("il carrello" = uscita) diventa vocabolario;
  - marcatori di verità nei documenti: `[verificato: fonte]`, `[dichiarato]`, `[non verificato]`, `[ipotesi]`;
  - **criterio di abbandono** dichiarato prima ("se meno del 25% delle richieste si risolve a voce, lo scenario base cade");
  - onestà sui limiti: "esegue routine insegnate", non "impara", perché il test di memoria non ha superato la soglia.
- **Mercato che hanno studiato:** cobot e PMI manifatturiere con cambi formato frequenti (food, packaging, cosmetica). Acquirente: prima l'**integratore**, poi la fabbrica, poi i costruttori in white label. Prezzo ipotizzato 60 €/mese per cobot. Italia 7.824 robot installati (2° in Europa).
- **Cosa ne deduciamo:** hanno appena fatto "voce → azione" sulla singola postazione. **Non hanno** la memoria del **reparto/stabilimento**: perché una ricetta, un parametro o una procedura è cambiata, chi l'ha deciso, cosa ha sostituito, cosa contraddice. È il pezzo OIDA che manca a Gergo. Un'idea lì si collega a entrambi i loro prodotti senza copiarli. Attenzione a non rifare Gergo (cobot a voce).

## 2. I bandi aperti (Call4Ventures, fino al 31.12.2026)

Fonte: [kakashi.ventures/en/call4ventures](https://www.kakashi.ventures/en/call4ventures) e sottopagine.

| Bando | Fino a | Cosa chiedono (frasi chiave) |
|---|---|---|
| **AI per industria e manifattura** | 75 k€ | caso d'uso misurabile in reparto (tempo ciclo, scarti, fermi, costi); integrazione MES/ERP/PLC/sensori; pianificazione, qualità, manutenzione predittiva, energia, supply chain, know-how di stabilimento |
| **Physical AI e robotica** | 50 k€ | prototipo già uscito dal laboratorio; primo partner industriale pronto al pilota; robotica, visione, edge, **safety** |
| AI per la ricerca autonoma | 75 k€ | biotech, pharma, chimica, materiali; dati o laboratori per validare |
| Servizi professionali agentici | 75 k€ | agent-first, ore risparmiate misurabili |
| Banche, antifrode/cyber, insurtech | 75–100 k€ | prodotto pilotabile subito, compliance già in ordine |
| Generale | 60 k€ | qualunque settore |

**Tesi d'investimento (valgono anche per giudicare il nostro business case):** il fondatore conosce il settore; il CEO capisce la tecnologia; **"un problema per cui i clienti già pagano"**; trazione verificabile (anche piloti); modello scalabile; AI dentro il prodotto.

## 3. Call4Ideas — come valutano un'idea

Fonte: [kakashi.ventures/en/call4ideas](https://www.kakashi.ventures/en/call4ideas).

- Per chi: ricercatori, dottorandi, esperti di settore, manager, "chiunque abbia un problema profondo".
- 6 aree: servizi professionali · deep tech agentica · **memoria e ontologie** · business intelligence · **AI per le fabbriche e il mondo fisico** · scienza e ingegneria.
- **Innovation Potential Score**, 5 assi:
  - **Massa di lavoro:** quante persone fanno oggi quel lavoro.
  - **Vuoto di innovazione:** quanto poco è stato toccato dalla tecnologia.
  - **Leva di automazione** *(decisivo)*: quanto di quel lavoro l'AI può fare davvero.
  - **Barriere superabili:** regole, dati, integrazioni: ostacoli che si possono superare.
  - **Diritto di vincere** *(decisivo)*: perché proprio questa squadra.

## 4. Prodotti e ricerca: cosa hanno già (da non copiare)

| Prodotto | Settore | Nota per noi |
|---|---|---|
| Project OIDA | banche, assicurazioni, consulenza | registro decisioni governato, MCP. Esempio demo: tasso minimo mutuo 2,1% in un'email vs 2,4% nel verbale del CdA |
| Control8 | interno | "cervello operativo" su MCP |
| Gergo | cobot, PMI manifatturiere | vedi §1 |
| Catalyst | migrazione COBOL, in produzione | |
| Vaglio, Elevia, AskMadarAI | banche/HR/wealth, con Excellence | |
| NewJee, Kansei | media, fact-checking | "Reality Cards", quadro epistemico |
| Magellan | ricerca scientifica multi-agente | |

**Paper** ([kakashi.ventures/en/research](https://www.kakashi.ventures/en/research)): "Retrieval Is Not Enough" (OIDA, 2026) · "Summary Is Not Enough: i giudici LLM che non vedono la fonte scambiano una citazione fedele per un'allucinazione" (giugno 2026) · MAGELLAN (2026) · framework multi-livello per analisi dell'informazione (LREC 2026) · analisi notizie politiche (LREC 2026) · eventi di minaccia (NLPAICS 2026) · conformità all'AI Act con LLM (nov. 2025).
→ Il tema "**citare fedelmente la fonte**" e "**valutare se l'AI è fedele alla fonte**" torna in più paper: ogni risposta del nostro prodotto deve citare il pezzo di testo esatto.

**Comitato scientifico:** Pierfrancesco Beneventano (MIT, coautore OIDA), Giancarlo Ruffo (UniTo/UPO), **Giuseppe Futia (GraphAware, knowledge graph / Neo4j)**, Emiliano Traini, Davide Lai (DESY), Antonello Di Mascio (Poste Vita). → Un grafo di conoscenza fatto bene viene riconosciuto.

## 5. Clienti, casi e partner nominati

- Accelerazione aziendale ("Department as a Service"): **EM Solutions** (manifattura, sistemi anti-alluvione: R&D e software), Cremeria Italiana (food), Homingo (proptech, anche partecipata), Accessiway. La pagina dice che il servizio R&D è "ideale per aziende manifatturiere".
- Portafoglio VC: Pelomatto, Homingo.
- Partner tecnologici: Nebius, AWS, Google Cloud; Anthropic (Ambassador, Claude for Organizations).
- Gruppo Excellence (proprietario di maggioranza): consulenza a banche, assicurazioni, pagamenti, rischio, ESG. Nessun cliente industriale nominato.

## 6. Le persone: cosa pensano

- **Federico Bottino** ([about](https://federicobottino.com/about), [talks](https://federicobottino.com/talks), [Gli Stati Generali, 22.12.2025](https://www.glistatigenerali.com/tecnologia-e-media/a-i/federico-bottino-sfida-etica-intelligenza-artificiale)): ora anche CEO di Project OIDA (società a New York, da aprile 2026), "infrastruttura per la conoscenza verificabile". Storia su disinformazione, etica digitale, propaganda; insegna all'ITS ICT Piemonte. Idee forti: **valori europei**, proteggere gli asset strategici, **"critica delle fonti"** come cosa che separa una democrazia viva da una morta, studiare filosofia per uscire da una visione solo ingegneristica della conoscenza, "dominare la tecnologia e non esserne dominati".
- **Alberto Trivero:** cofondatore, CTO del Gruppo Excellence, autore di MAGELLAN, coautore di Gergo.
- **Carlo Ferrero:** coautore OIDA, contatto commerciale di OIDA (demo).
- **Davide Lai:** Lead Researcher (DESY, fisica).

## 7. La gara (repo ufficiale)

- Tre blocchi di domande nel README: **AI brain per l'industria**; **memoria** (quando una regola è superata, più agenti che scrivono nella stessa memoria senza contraddirsi, registrare *perché* è stata presa una decisione); **ontologie** (come si costruisce, come si aggiorna quando l'azienda cambia, come un agente la usa per **ragionare e non solo cercare**).
- Chi cercano: "Hai competenza verticale. Conosci a fondo un settore. Sai quali dei suoi problemi aspettano ancora una soluzione."
- **Scadenza iscrizioni: venerdì 13.11 ore 12:00.** Tutti i membri devono essere iscritti e confermati.
- Premio con opzione A (cedi il progetto) o B (società + 15% a KVA) e prelazione di 12 mesi: il business case conta come in una vera Call4Ventures.

## 8. Cosa ne deduciamo per l'idea

| Segnale | Implicazione |
|---|---|
| Gergo (industria, italiano, operatori di linea, registro, versioni) | Idee **dentro lo stabilimento** sono in linea con dove stanno andando. Parlare di operatori, tecnici, integratori, responsabili qualità. |
| Bando manifattura chiede KPI di reparto | Il nostro problema deve muovere **un numero di reparto**: fermi, scarti, tempo ciclo, tempo di cambio formato, ore di un tecnico. |
| "Know-how di stabilimento" nel bando | Memoria del perché delle scelte tecniche è esplicitamente nel loro perimetro. |
| Physical AI con "safety" | Sicurezza di macchine e persone è un tema che riconoscono. |
| OIDA + paper "Summary Is Not Enough" | Citazione esatta della fonte, supersession, contraddizioni, astensione: obbligatori nella demo. |
| GraphAware nel comitato | Un grafo di conoscenza vero (non solo vettori) è un plus. |
| Prelazione e opzione B | Presentarci come **una venture che KVA vorrebbe costruire**, compatibile con OIDA (es. esposta via MCP). |
| Clienti reali solo in finanza | Nessuna concorrenza interna se restiamo in industria. |

Proposte di idee nuove nate da questi segnali: vedi `research/problems/candidates.md` §Nuove proposte.
