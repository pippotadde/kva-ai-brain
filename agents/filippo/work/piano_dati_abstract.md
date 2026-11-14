# Piano dati + business plan + abstract — Filippo (14.11, 11:20 → 12:05)

**Obiettivo:** entro le 12:05 avere (1) numeri verificati con fonte per pitch e modello economico, (2) abstract finale ≤1200 caratteri, pronto da caricare entro le 12:20.
**Metodo:** due motori in parallelo (Gemini Deep Research per i dati lunghi, DeepSeek per le verifiche rapide), poi Claude verifica ogni link e scrive. Nessun numero senza fonte; se manca la fonte lo diciamo.

## Regole globali
- Ogni numero ha un livello: **[verificato]** (link aperto, numero trovato nella pagina) · **[fonte di settore]** (report a pagamento/citazione indiretta) · **[ipotesi nostra]**.
- Non usare: "30% dei richiami sono allergeni" (non verificato).
- Già verificati: RASFF 2024 = 5.250 notifiche, +12% · Reg. 1169/2011 · Reg. 2021/382.
- Output dei motori sempre in tabella: dato | valore | anno | fonte (URL) | citazione testuale | affidabilità.

## ⚠ Da allineare con Giorgia SUBITO (prima delle 11:30)
| Tema | Giorgia (`pitch/04_FABBRICA.md`) | Filippo (`piano_progetto.md`) | Proposta |
|---|---|---|---|
| Nome | MemoLens | Cervello allergeni | decide Sian/Giorgia |
| Prezzo | 390 €/mese | 800 €/mese | decidere uno solo, i dati di T2 aiutano |
| Abstract | suo, 1.197 caratteri, già pronto | `abstract.txt` | uno solo; chi carica? (lei, entro 12:20) |
| Focus | memoria dell'agente sui cambi formato | rischio allergeni + gestione interna/approvazioni | unire: memoria + flusso approvazioni |

---

## T1 — Lancia la ricerca (11:20-11:25)
- [ ] Apri Gemini → Deep Research → incolla **Prompt G1**. In un'altra scheda **Prompt G2**.
- [ ] Apri DeepSeek (con ricerca web attiva) → incolla **Prompt D1**, poi in nuova chat **Prompt D2**.
- [ ] Mentre girano: messaggio a Giorgia sulla tabella "Da allineare" (testo in fondo).
**Fatto quando:** 4 ricerche in corso + messaggio inviato.

## T2 — Raccogli e incolla (11:35-11:45)
- [ ] Incolla le 4 risposte in `.coord/agents/filippo/work/ricerca_raw.md` (anche se incomplete).
- [ ] Di' a Claude: "verifica ricerca_raw.md".
**Fatto quando:** il file esiste con le 4 tabelle.

## T3 — Verifica (Claude, 11:45-11:50)
- [ ] Claude apre ogni URL e controlla che il numero ci sia davvero; assegna il livello.
- [ ] Scarta tutto quello che non regge.
**Fatto quando:** `numeri_pitch.md` contiene solo dati con livello e link.

## T4 — Business plan in numeri (11:50-11:58)
In `numeri_pitch.md`, sezione per il modello economico (serve alle 16:45 con /hack-economic-model):
- [ ] Problema: % richiami per allergeni (USA, UE/RASFF), costo medio richiamo (grandi vs PMI).
- [ ] Mercato: n. stabilimenti target Italia/UE (codici NACE 10.71 pane e pasticceria fresca, 10.72 biscotti, 10.82 cacao/cioccolato/confetteria) → TAM/SAM/SOM.
- [ ] Prezzo unico (deciso con Giorgia), costo per cliente (server + modello), margine.
- [ ] Canale: consulenti HACCP, enti di certificazione (BRCGS/IFS), associazioni (es. Unione Italiana Food); CAC stimato.
- [ ] Concorrenti: 4-6 nomi con cosa fanno e cosa non fanno.
- [ ] Gestione interna: tempi di approvazione/escalation oggi (se trovati) — altrimenti [ipotesi nostra].
**Fatto quando:** ogni riga ha valore + livello.

## T5 — Abstract finale (11:58-12:05)
- [ ] Claude scrive l'abstract unendo: problema (1 numero verificato), soluzione (memoria + mappa + provenienza), gestione interna (caso già pronto, inoltro automatico lungo la gerarchia, istruzioni ai lavoratori), regola "l'AI propone, la persona decide", test di oggi, cliente.
- [ ] Conta caratteri: `wc -m abstract.txt` ≤ 1200.
- [ ] Passalo a Giorgia/chi carica entro le 12:10; caricamento ≤ 12:20.
**Fatto quando:** abstract ≤1200 caratteri approvato da Giorgia.

## T6 — Chiusura (12:05)
- [ ] Fonti registrate in `research/data/README.md` (solo quelle usate).
- [ ] `status.md` aggiornato + `bash scripts/coord.sh sync`.

---

## Prompt pronti da copiare

### G1 — Gemini Deep Research: problema e mercato
```
You are a food-safety market analyst. I need VERIFIABLE numbers only, for a pitch about an AI system that prevents undeclared-allergen incidents in food plants (focus: confectionery, bakery, co-packers, Italy and EU).

Find:
1. Share of food recalls caused by undeclared allergens: USA (FDA+USDA, latest year available, 2023-2025) and EU (RASFF: number/share of allergen-related notifications 2023-2024).
2. Average cost of a food recall: for large companies AND for SMEs (any figure for small/medium plants, in EUR or USD).
3. Number of food manufacturing enterprises/plants in Italy and in the EU-27 for NACE codes 10.71, 10.72, 10.82 (Eurostat SBS or ISTAT), latest year.
4. Root causes of allergen recalls: share due to cross-contact, supplier ingredient changes, labelling/packaging errors, cleaning failures (any study or FDA/FSA/FSAI analysis).
5. EU regulatory pressure: Reg. (EU) 2021/382 allergen management obligations; BRCGS / IFS allergen requirements.

Rules: do NOT invent numbers. For every figure give: value, year, geography, exact source URL, a verbatim quote from the source, and confidence (high/medium/low). If you cannot find something write "NOT FOUND". Output as one markdown table, then a 5-line summary.
```

### G2 — Gemini Deep Research: concorrenti e prezzi
```
You are a B2B SaaS analyst. Map the software competitors for allergen management and food-safety/quality management in food manufacturing (EU and US), e.g. Safefood 360, TraceGains, Trustwell/FoodLogiQ, SafetyChain, Icicle, Redzone, Intact, Ideagen, and any Italian vendors.

For each: what it does for allergens (supplier spec changes, cleaning/changeover validation, label checks), whether it links documents together or only stores them, whether it uses AI, whether it has approval workflows/escalation, target customer size, and PUBLIC price (per site/month) if available.

Also find: typical price range for food-safety QMS software per plant per month for SMEs.

Rules: no invented data. Every row: source URL and date. Write "NOT PUBLIC" when the price is not public. Output: one markdown table + 5-line summary of the gap none of them covers (cross-checking scattered documents in real time + fast internal approval chain).
```

### D1 — DeepSeek: gestione interna e tempi
```
Search the web. I am building a pitch about speeding up internal quality decisions in food plants (allergen incident → line supervisor → QA manager → plant director → instructions to workers).

Find any data (studies, surveys, industry articles, FDA/FSA guidance) about:
1. How long food companies take to decide on a hold/recall after a non-conformity is detected (hours/days).
2. Time QA managers spend on documentation/audit preparation (hours per week or % of time).
3. Cost of paper/manual HACCP and CAPA workflows vs digital ones (time saved, errors reduced).
4. Number of QA/food-safety staff in a typical SME food plant.

For each: value, year, source URL, verbatim quote. If not found write NOT FOUND. Do not estimate. Markdown table.
```

### D2 — DeepSeek: verifica dei numeri che abbiamo già
```
Fact-check each claim. For each say TRUE / FALSE / PARTIALLY, give the correct value and the exact source URL with a verbatim quote:
1. "Undeclared allergens were the leading cause of US food recalls in 2025, 38.8% of FDA+USDA recalls" (Statista chart 36281).
2. "In 2023 undeclared allergens caused about half of all US food recalls, driven by sesame" (PIRG / food-safety.com).
3. "USDA ERS: 27.4% of food recalls 2004-2013 were due to allergens."
4. "The average direct cost of a food recall is USD 10 million" (FMI/GMA study).
5. "RASFF 2024: 5,250 notifications, +12% vs 2023."
6. "Italy has about 56,000 food enterprises."
Markdown table.
```

### Messaggio per Giorgia (copia)
```
Giorgia, sto facendo dati + business plan + abstract fino alle 12:05. Per non avere due versioni: 1) prezzo: tu 390 €/mese, io 800 €/mese → teniamo il tuo 390 se non trovo dati contro? 2) abstract: uso il tuo da 04_FABBRICA.md come base e aggiungo la parte di gestione interna (inoltro automatico lungo la gerarchia, istruzioni ai lavoratori), te lo mando alle 12:05 per l'ok. 3) carichi tu entro 12:20? 4) nome: MemoLens o altro, decidete tu e Sian.
```
