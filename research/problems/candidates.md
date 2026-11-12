# Problemi candidati — rosa per la scelta di venerdì mattina

Versione 1, 12.11.2026. Preparata per la call di venerdì: si scelgono **1 problema principale + 1 di riserva**.

## Come leggere i punteggi

Ogni problema ha un voto da 1 a 5 su ciascun criterio della giuria, con lo stesso peso del regolamento:

| Criterio | Peso |
|---|---|
| Aderenza al tema (memoria / ontologie / AI brain) | 25% |
| Fattibilità tecnica in 2h30 (= "qualità di ciò che funziona") | 25% |
| Problema reale e impatto | 25% |
| Business case | 20% |
| Demo chiara e d'impatto | 5% |

I voti sono una mia prima stima: vanno discussi. Dove un numero viene da fonti deboli (blog di fornitori, report di mercato a pagamento) lo segnalo.

## Classifica

| # | Problema | Tema | Fattib. | Reale | Business | Demo | **Totale /5** |
|---|---|---|---|---|---|---|---|
| A | Direttive di aeronavigabilità che si sostituiscono (manutenzione aerei) | 5 | 4 | 5 | 4 | 5 | **4,55** |
| D | Sicurezza sul lavoro: procedure, macchine, formazione (D.Lgs. 81/08) | 5 | 4 | 5 | 4 | 5 | **4,55** |
| C | Procedure GMP nel farmaceutico: versioni, deviazioni, motivazioni | 5 | 4 | 4 | 4 | 4 | **4,25** |
| B | Nuovo Regolamento Macchine UE 2023/1230 (scadenza gennaio 2027) | 4 | 3 | 5 | 5 | 3 | **4,15** |
| E | Conoscenza dei manutentori che vanno in pensione | 4 | 4 | 4 | 3 | 4 | **3,80** |
| F | Scatola nera per agenti AI che fanno azioni critiche | 5 | 3 | 3 | 3 | 3 | **3,50** |
| G | Modello decisionale per qualifica fornitori | 3 | 4 | 3 | 3 | 3 | **3,25** |
| H | Anonimizzazione dei dati aziendali | 2 | 3 | 4 | 3 | 2 | **2,95** |

Totale = 0,25·Tema + 0,25·Fattib. + 0,25·Reale + 0,20·Business + 0,05·Demo.

---

## A. Direttive di aeronavigabilità che si sostituiscono — manutenzione aeronautica

**Il problema.** Le autorità (EASA in Europa, FAA negli USA) emettono *Airworthiness Directives* (AD): ordini obbligatori di ispezione o modifica per un certo modello di aereo, motore o componente. Le AD **si sostituiscono a vicenda** ("questa AD sostituisce la AD 2019-xx"), si applicano solo a certi numeri di serie e componenti, e interagiscono con i bollettini dei costruttori. Un'officina di manutenzione (MRO) deve sapere in ogni momento quali AD valgono per ogni aereo della flotta e dimostrare perché una certa ispezione è stata fatta o saltata.

**Perché è perfetto per il tema.** È letteralmente l'animazione del repo KVA: una regola viene superata, quella vecchia esce dalla memoria, l'agente risponde citando la regola nuova e chi l'ha emessa. Ontologia naturale: Aeromobile → Motore → Componente → AD → Task di manutenzione. Inferenza: "AD X si applica al motore tipo Y, l'aereo Z monta Y, quindi X si applica a Z".

**Chi soffre / chi paga.** Responsabili tecnici (CAMO) e officine MRO, compagnie aeree, flotte di elicotteri, aviazione generale. Torino è un polo aerospaziale (Leonardo, Avio Aero, Thales Alenia Space; l'aerospazio piemontese segnava +14% e +18% di produzione negli ultimi trimestri 2025).

**Dati.** Le AD della FAA sono pubbliche (Federal Register, dominio pubblico USA) e scaricabili via API; EASA pubblica le sue AD online. Si possono prendere 20–50 AD vere su un modello di motore e costruire una flotta finta.

**Rischi.** Dominio tecnico nuovo per noi; serve studiare un po' il lessico. Molti giurati non conoscono l'aviazione: il pitch deve essere semplice.

**Vantaggio con Giorgia.** Se ASTRA è aerospazio, Giorgia conosce già parte del mondo e del lessico.

---

## D. Sicurezza sul lavoro — procedure, macchine e formazione (D.Lgs. 81/08)

**Il problema.** Ogni azienda italiana con dipendenti deve tenere un Documento di Valutazione dei Rischi (DVR), procedure di sicurezza per macchine e reparti, e la formazione obbligatoria di ogni lavoratore. Quando cambia una procedura o una macchina, nessuno sa con certezza **chi deve essere riformato, quali documenti sono superati e se un operatore oggi può usare quella macchina**. Le informazioni stanno in PDF, Excel e nella testa dell'RSPP (il responsabile della sicurezza).

**Impatto.** In Italia nel 2025: circa 598.000 denunce di infortunio e circa 1.100–1.200 morti sul lavoro (dati INAIL, provvisori e consolidati non coincidono); il manifatturiero conta 129 morti in occasione di lavoro. Argomento forte e sentito in Italia.

**Perché è perfetto per il tema.** Ontologia: Lavoratore → Mansione → Rischio → Macchina → Procedura → Corso di formazione. Inferenza: "Mario fa la mansione X, X usa la pressa P, la procedura di P è cambiata il 3/11, la formazione di Mario è precedente → Mario non è abilitato". Memoria: procedura nuova sostituisce la vecchia, con chi l'ha cambiata e perché.

**Chi paga.** PMI manifatturiere, studi di consulenza sicurezza (che seguono decine di aziende ciascuno). Mercato software EHS (sicurezza e ambiente) stimato circa 2,3–2,8 miliardi $ nel 2025 a livello mondiale, crescita circa 9–10% l'anno (stime di report a pagamento, da prendere come indicative).

**Dati.** Il testo del D.Lgs. 81/08 è pubblico; open data INAIL; procedure e anagrafica dei lavoratori si inventano (dati finti, niente privacy).

**Rischi.** Esistono già software per la sicurezza: il nostro punto di forza deve essere il ragionamento sulle relazioni, non la gestione documenti.

---

## C. Procedure GMP nel farmaceutico — versioni, deviazioni e motivazioni

**Il problema.** Nelle aziende farmaceutiche ogni attività segue una procedura scritta (SOP) sotto le regole GMP. Le SOP cambiano spesso; le deviazioni e le azioni correttive (CAPA) vanno collegate alla versione giusta; agli ispettori va dimostrato perché si è deciso qualcosa. Tra le carenze più citate nelle lettere di richiamo FDA ci sono proprio le procedure scritte non seguite e i problemi di integrità dei dati (circa 15% delle lettere 2025 secondo un'analisi di settore).

**Perché si adatta al tema.** Memoria con versioni, provenienza, motivazione delle decisioni. Ontologia: Prodotto → Processo → SOP → Deviazione → CAPA.

**Chi paga.** Aziende farmaceutiche e biotech, produttori conto terzi. Mercato software di gestione qualità circa 8–12 miliardi $ (stime discordanti); il controllo documenti è il segmento più grande.

**Dati.** Linee guida GMP europee (EudraLex Vol. 4) pubbliche; lettere di richiamo FDA pubbliche; SOP e deviazioni finte.

**Rischi.** Settore molto regolamentato e lontano da noi; è un mercato già pieno di fornitori.

---

## B. Nuovo Regolamento Macchine UE 2023/1230

**Il problema.** Dal **20 gennaio 2027** (alcune fonti dicono 14 gennaio: da verificare sulla Gazzetta Ufficiale) il nuovo Regolamento Macchine sostituisce la Direttiva 2006/42/CE, senza periodo di transizione. Ogni costruttore di macchine deve aggiornare il fascicolo tecnico, la valutazione dei rischi, le istruzioni e la dichiarazione di conformità, con nuovi requisiti su software di sicurezza e cybersecurity.

**Perché è forte.** Scadenza tra 2 mesi = "perché proprio ora" perfetto per il business case. L'Italia è uno dei primi produttori di macchine in Europa.

**Perché meno forte sul tema.** È più un problema di confronto tra documenti (requisiti vecchi contro nuovi) che di memoria; la demo è meno visiva; i testi normativi sono lunghi e la fattibilità in 2h30 è più a rischio.

**Dati.** Testo del regolamento su EUR-Lex (pubblico).

---

## E. Conoscenza dei manutentori che vanno in pensione

**Il problema.** I tecnici esperti sanno come si ripara una macchina; quando vanno in pensione la conoscenza se ne va. Il 25% dei lavoratori del manifatturiero USA ha 55 anni o più (BLS 2025). Il fermo macchina non pianificato costa da 100.000 a oltre 1 milione $ l'ora secondo diversi report (quasi tutti di fornitori: numeri indicativi).

**Perché più debole.** È l'idea a cui penseranno molte squadre ("chatbot sui manuali di manutenzione"): difficile distinguersi. Non esiste una stima credibile del costo della conoscenza persa.

---

## F. Scatola nera per agenti AI

**Il problema.** Gli agenti AI cominciano ad approvare pagamenti o rilasciare lotti. Serve un registro a prova di manomissione di cosa hanno visto e fatto. L'AI Act (art. 12) chiede la registrazione automatica degli eventi per i sistemi ad alto rischio, ma la data di applicazione è incerta (agosto 2026 oppure rinviata a dicembre 2027 dal "Digital Omnibus": da verificare).

**Perché più debole.** Molto in tema ma astratto: il "problema reale" oggi è più regolatorio che quotidiano, e la demo è meno immediata. **Ottimo però come componente** dentro A, C o D: ogni risposta dell'agente viene registrata con le fonti.

---

## G. Qualifica fornitori con modelli decisionali — H. Anonimizzazione

Meno legati a memoria e ontologie, o con demo poco visiva. Li tengo come riserva lontana. L'anonimizzazione può diventare una funzione dentro D (dati dei lavoratori).

---

## Proposta per venerdì

1. Scegliere tra **A (aviazione)** e **D (sicurezza sul lavoro)**; l'altro diventa la riserva.
   - A ha dati veri pubblici e il legame con il polo aerospaziale torinese.
   - D è più vicino a tutti, parla a ogni azienda italiana e ha un impatto emotivo forte.
2. In entrambi i casi mettiamo dentro la "scatola nera" (F) come funzione: ogni risposta è tracciata con le fonti.
3. Dopo la scelta: Filippo studia il mercato e il business, Giorgia raccoglie i dati, Sian scrive la storia del problema e il copione della demo.

## Domande aperte per il team

- Qualcuno conosce persone che lavorano in un'officina aeronautica, in un ufficio sicurezza (RSPP) o nel farmaceutico? Una frase vera di un esperto vale moltissimo nel pitch.
- Che settore ha l'azienda della famiglia di Filippo? Se è manifatturiera, D diventa ancora più forte.

## Fonti

- Regolamento Macchine: [TÜV SÜD](https://www.tuvsud.com/en-us/knowledge-hub/articles/new-eu-machinery-regulation-what-you-need-to-know), [EU-OSHA](https://osha.europa.eu/it/legislation/directive/regulation-20231230eu-machinery), [Nemko](https://digital.nemko.com/regulations/eu-machinery-regulation)
- Infortuni INAIL 2025: [Geopop](https://www.geopop.it/in-italia-salgono-le-denunce-di-infortuni-e-malattie-sul-lavoro-in-calo-i-decessi-1-198-dati-inail-2025/), [Orizzonte Scuola](https://www.orizzontescuola.it/infortuni-sul-lavoro-in-crescita-dell14-nel-2025-quasi-81mila-le-denunce-degli-studenti-i-dati-inail/), [Il Fatto Quotidiano](https://www.ilfattoquotidiano.it/2026/02/03/morti-sul-lavoro-incidenti-dati-inail-2025-studenti-alternanza-news/8278860/)
- Lettere FDA: [Pharmaceutical Online, dic. 2025](https://www.pharmaceuticalonline.com/doc/what-fda-warning-letters-tell-us-about-gmp-compliance-0001), [ECA/GMP-compliance FY2022](https://gmp-compliance.org/gmp-news/fda-warning-letters-of-the-fiscal-year-2022-the-top-ten-gmp-deficiencies)
- Fermo macchina: [Fluke 2025](https://www.fluke.com/en/learn/blog/condition-monitoring-and-alignment-software/unplanned-downtime-costs-manufacturers-up-to-852m-weekly), [L2L 2025](https://www.l2l.com/blog/2025-report-manufacturing-downtime)
- Conoscenza persa: [Reliability Magazine](https://reliamag.com/articles/cost-of-lost-plant-knowledge/), [statistiche skills gap](https://reliamag.com/guides/manufacturing-maintenance-skills-gap-statistics/)
- Mercato EHS: [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/environmental-health-and-safety-software-market)
- Mercato QMS: [Fortune Business Insights (pharma QMS)](https://www.fortunebusinessinsights.com/pharma-quality-management-software-market-118887), [OMR](https://www.omrglobal.com/industry-reports/quality-management-software-market)
- AI Act art. 12: [Help Net Security](https://www.helpnetsecurity.com/2026/04/16/eu-ai-act-logging-requirements/), [Kovrr](https://www.kovrr.com/blog-post/eu-ai-act-compliance-roadmap-what-to-document-and-when)
- Tempo perso a cercare informazioni (19–30% del tempo di lavoro): [analisi delle fonti](https://ainora.lt/blog/hours-wasted-searching-for-information-studies)
- Piemonte manifatturiero: [Unioncamere Piemonte, congiuntura IV trim. 2025](https://www.unioncamere.gov.it/sites/default/files/articoli/2026-02/CONGIUNTURA%20IN%20PIEMONTE%20IV%20TRIMESTRE%202025%20V.2%20%281%29.pdf)
