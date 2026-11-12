# Prompt per Deep Research (Gemini Pro / ChatGPT)

Come si usa:
1. Apri https://gemini.google.com → seleziona **Deep Research** (su ChatGPT: "Deep research").
2. Incolla un prompt intero, avvia, approva il piano di ricerca che ti propone.
3. Ci mette 5–15 minuti; puoi lanciarne due in parallelo in due chat diverse.
4. Esporta il report (Gemini: "Esporta in Documenti Google"), scaricalo come Markdown o PDF e mettilo in `research/market/` con nome `A-gemini.md`, `D-gemini.md`, ecc. Oppure incolla il testo a Claude e lo sistemo io.

Perché non uno script automatico: Deep Research nell'app è incluso nell'abbonamento Pro, cerca e legge decine di fonti da solo ed è più accurato di uno script fatto in fretta. Lo script avrebbe bisogno di chiavi API a pagamento e di tempo che non abbiamo.

---

## Prompt A — Direttive di aeronavigabilità (manutenzione aeronautica)

```
I am preparing a business and product case for an AI startup idea. Do a thorough, source-backed research report. Write the final report in Italian, but keep technical terms in English.

Idea: an "AI brain" for aircraft maintenance organisations (Part-145 MROs and CAMOs) that keeps a structured, versioned memory of Airworthiness Directives (EASA and FAA), service bulletins and maintenance tasks. It knows when a directive supersedes another, infers which directives apply to which aircraft/engine/part (by model and serial number), and explains every answer with its source and the reason a decision was taken.

Answer with numbers and sources (links) for each point:
1. How AD compliance is managed today in MROs/CAMOs: process, roles, typical tools, main pain points and errors. Cite real incidents or audit findings caused by missed or misapplied ADs.
2. Volume: how many ADs EASA and FAA issue per year; how often ADs are superseded or revised; how much time a CAMO/MRO spends on AD research and applicability assessment (hours per aircraft per year if available).
3. Cost of getting it wrong: fines, groundings, AOG costs per hour/day, audit findings.
4. Market: number of Part-145 organisations and CAMOs in Italy and in the EU; size of the MRO software market and of the aviation maintenance tracking software market (global and Europe), with growth rates.
5. Competitors: existing software (e.g. AMOS, TRAX, CAMP, Rusada, Ramco, Veryon/Traxxall and others) — what they do for AD management, pricing if public, and whether they use AI. Also AI startups in this space.
6. Who buys: job titles of decision makers, typical budget, sales cycle length.
7. Regulation and "why now": EASA rules relevant to continuing airworthiness (Part-M, Part-CAMO, Part-145), any upcoming changes, and the EU AI Act implications for AI in safety-related aviation tasks.
8. Public data we could use for a demo: where to download EASA and FAA ADs in bulk (APIs, formats, licences).
9. Turin/Piedmont aerospace ecosystem: main companies and MROs that could be early customers.
End with: the 5 strongest numbers for a 3-minute pitch, and the 3 biggest risks of this business.
```

---

## Prompt D — Sicurezza sul lavoro (D.Lgs. 81/08)

```
Sto preparando il caso di business e prodotto per un'idea di startup AI. Fai un report di ricerca approfondito, con fonti (link) per ogni dato. Scrivi in italiano.

Idea: un "AI brain" per la sicurezza sul lavoro nelle PMI manifatturiere italiane. Tiene una memoria strutturata e versionata di Documento di Valutazione dei Rischi (DVR), procedure operative, macchine, mansioni e formazione obbligatoria dei lavoratori (Accordo Stato-Regioni). Quando cambia una procedura o una macchina, capisce da solo quali documenti sono superati, quali lavoratori vanno riformati e se un operatore oggi è abilitato a usare una macchina, spiegando ogni risposta con la fonte e il motivo.

Rispondi con numeri e fonti su:
1. Come le aziende gestiscono oggi DVR, procedure e scadenze della formazione: strumenti usati (Excel, software, consulenti), ruoli (datore di lavoro, RSPP, RLS, preposto), problemi tipici ed errori più frequenti.
2. Dati INAIL più recenti: infortuni e morti sul lavoro nel manifatturiero, cause principali, quanti infortuni sono legati a formazione mancante o procedure non aggiornate.
3. Costo del problema: sanzioni del D.Lgs. 81/08 per formazione mancante o DVR non aggiornato (importi), costo medio di un infortunio per l'azienda, premi INAIL e riduzioni (es. modello OT23) per chi investe in prevenzione.
4. Novità normative recenti e in arrivo (2024–2027): nuovo Accordo Stato-Regioni sulla formazione, patente a crediti in edilizia, Regolamento Macchine UE 2023/1230, altri obblighi che rendono il tema urgente ("perché ora").
5. Mercato: numero di imprese manifatturiere in Italia per dimensione (10–49, 50–249 addetti), numero di RSPP esterni e studi di consulenza sicurezza, dimensione del mercato del software per la sicurezza sul lavoro (EHS) in Italia ed Europa.
6. Concorrenti: software italiani ed europei per la gestione della sicurezza e della formazione, cosa fanno, prezzi se pubblici, se usano AI.
7. Chi compra: chi decide l'acquisto in una PMI, budget tipico per la sicurezza, ciclo di vendita; ruolo dei consulenti esterni come canale di vendita.
8. Dati pubblici utilizzabili per una demo (testi normativi, open data INAIL, esempi di procedure) e loro licenze.
Chiudi con: i 5 numeri più forti per un pitch di 3 minuti e i 3 rischi principali di questo business.
```

---

## Prompt generico (per il problema scelto venerdì, o per C / B)

```
I am preparing a business and product case for an AI startup idea. Do a thorough, source-backed research report. Write the final report in Italian.

Idea: [DESCRIVI IN 3 RIGHE: chi è il cliente, cosa fa il prodotto, perché memoria/ontologia].

Answer with numbers and sources for: (1) how the problem is handled today and its pain points; (2) the cost of the problem, with real cases; (3) market size in Italy, EU and globally with growth rates, plus number of target companies; (4) competitors, their features, prices and use of AI; (5) who decides the purchase and with what budget; (6) regulations and deadlines that make it urgent now; (7) public data usable for a demo and its licence. End with the 5 strongest numbers for a 3-minute pitch and the 3 biggest risks.
```
