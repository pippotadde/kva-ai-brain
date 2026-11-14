# Ricerca grezza — NON VERIFICATA (14.11)

Risultati incollati da Filippo. Solo le risposte finali; tolto il ragionamento interno dei motori ("We need to search...").
Stato: da verificare (T3). Nessun numero va nel pitch prima della verifica.

Indice:
- DeepSeek · G1 Problema e mercato
- DeepSeek · G2 Concorrenti e prezzi
- DeepSeek · G3 Dolciario e grandi gruppi
- DeepSeek · D2 Verifica numeri
- (manca) DeepSeek · D1 Gestione interna e tempi
- Gemini · G1, G2, G3 → file separato `ricerca_gemini.md` (salvati 14.11 ~12:00; manca ancora 1 risultato)

Note rapide prima della verifica (Claude):
- DeepSeek G1 cita uno studio MDPI "Foods 2026" e un round Biorsaf "Sep 2026": da controllare che esistano davvero.
- G1 dice FSAI 2024 = 58 allergen alerts; la stessa ricerca ha visto anche "57" (probabile 2025). Da chiarire.
- G1 riga Eurostat NACE 10.71 "1.142.268 imprese UE" sembra irrealistico (troppo alto): probabile errore di tabella. Da verificare su Eurostat.
- G3 contiene il richiamo Ferrero Kinder 2022: NON usarlo nel pitch (Ferrero partner).


## VERIFICA T3 (Claude, 14.11 11:40) — URL aperti uno per uno

### OK — verificato sulla fonte (numero trovato testuale)
| Dato | Fonte verificata |
|---|---|
| RASFF 2024: 5.250 notifiche, +12% | EC newsroom https://ec.europa.eu/newsroom/sante/items/882537 (non dà il n. allergeni 2024) |
| RASFF 2023: 4.695 notifiche, +8% | https://ec.europa.eu/newsroom/sante/items/847722/en |
| RASFF 2023: allergeni = 217 notifiche (latte il più notificato, 39) → ~4,6% | ACN Annual Report 2023 PDF (testo estratto, pag. con sez. 3.5) |
| USA 2024: 101 richiami per allergeni non dichiarati = 34% (FDA+USDA) | food-safety.com art. 10126 (riporta PIRG) |
| USA 2023: 154 di 313 = 49,2% | food-safety.com art. 9437 (riporta PIRG) |
| USA 2025: 38,8% di 320 richiami, prima causa | Statista chart 36281 (cita PIRG Food for Thought 2026) |
| USA 2004-13: 27,4% allergeni, 41,0% patogeni | USDA ERS EIB-191 Summary PDF (testo estratto) |
| Costo medio diretto richiamo USD 10M | Interroll fact sheet 2018 che cita studio FMI/GMA (2011) → livello [fonte di settore], dato vecchio |
| Biorsaf: round €5,2M guidato da P101 + acquisizione Cooki, 10.09.2026 | Teleborsa / Borsa Italiana / financecommunity.it |
| Veralto compra TraceGains $350M, ott. 2024 (~$30M ricavi, >95% ricorrenti) | Veralto 10-K FY2024 (sec.gov), qualityassurancemag.com |
| Ideagen compra Safefood 360° + Authenticate, luglio 2025 | Business Wire 20.07.2025 (importi £ non verificati) |
| CAOBISCO: >14.000 produttori cioccolato/biscotti/dolciario UE, 99% PMI | caobisco.eu, comunicato gen. 2026 |
| FSAI 2024: 58 allergen alerts su 126 avvisi di richiamo | Food Safety News 07/2025 (sintesi report FSAI) → [fonte di settore] |
| FoodDocs: Standard $199, Professional $299/mese (Lite $79-99/sito) | G2/Capterra; listino ufficiale non aperto → [fonte di settore] |

### NON REGGE — scartare o riformulare
- Eurostat NACE 10.71 "1.142.268 imprese UE / 181.442 Italia": FALSO. Italia 10.71 ≈ 25.300 imprese (2021, Statista su Eurostat/Istat). Non usare.
- Cause radice "50,1% etichetta / 16,3% fornitura / 9,4% processo": studio non trovato. Alternativa verificabile: FDA FY2013-19, 914 richiami allergeni → 71,1% errori di etichettatura, 23,4% contaminazione crociata (food-safety.com art. 8496).
- UK FSA "101 allergy alerts 2024 vs 64": numeri esatti non trovati; il report FSA 2024/25 dice +55% Allergy Alerts (incidente senape/arachidi). Usare "+55%" se serve.
- MDPI Foods 2026 (27,1% FDA / 38,6% FSIS): sito risponde 403, esistenza non verificata. Non usare.
- Biorsaf "3,4M imprese italiane, digitalizzazione 3%": stima dell'azienda, non usare come dato.

### NON ANCORA VERIFICATI (fonti non date da DeepSeek)
- ATECO 10.82 Italia 821 imprese / €5,117 mld; Italia 56.780 imprese F&B (fonte rivista, include bevande); stabilimenti Ferrero/Mondelez; prezzi concorrenti di terze parti (Safefood €500-2.000, Redzone $2-6K, TraceGains $20K/anno); QAD-Redzone ~$1B; Reg. 2021/382 (testo EUR-Lex esiste, citazione da controllare).

### Numeri consigliati per pitch/abstract
1. "Gli allergeni non dichiarati sono la prima causa di richiamo alimentare negli USA: 38,8% nel 2025" (Statista/PIRG).
2. "Il 71% dei richiami per allergeni nasce da errori di etichettatura, il 23% da contaminazione crociata" (FDA 2013-19).
3. "RASFF 2024: 5.250 allerte UE, +12%" (Commissione UE).
4. "14.000 produttori dolciari UE, 99% PMI" (CAOBISCO) — il nostro cliente.
5. Mercato si muove: Biorsaf €5,2M (set. 2026), TraceGains $350M (2024).


---

## DeepSeek · G1 — Problema e mercato

### 1. Evidence Table
| # | Topic | Figure | Year | Geography | Source | URL | Verbatim quote | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1a | USA: share of FDA + USDA recalls due to undeclared allergens | 101 recalls = 34% of total (296 recalls) | 2024 | USA (FDA + USDA) | Food Safety Magazine (reporting on PIRG's Food for Thought 2025 report). Secondary source; not FDA/USDA primary. | https://www.food-safety.com/articles/print/10126-hospitalizations-deaths-caused-by-foodborne-illnesses-more-than-doubled-in-2024 | "Undeclared allergens/ingredients caused the most recalls (101), accounting for 34 percent of all recalls issued by USDA and FDA in 2024." | Medium (secondary, but specific year and count) |
| 1a | USA: share of FDA + USDA recalls due to undeclared allergens | 154 recalls = "nearly half" of total (313 recalls) | 2023 | USA (FDA + USDA) | Same Food Safety Magazine article. Secondary source. | https://www.food-safety.com/articles/print/10126-hospitalizations-deaths-caused-by-foodborne-illnesses-more-than-doubled-in-2024 | "This represents a decrease from the 154 allergen/ingredient recalls seen in 2023, comprising nearly half of the year's total." | Medium |
| 1a | USA: cumulative allergen share (peer-reviewed) | FDA 27.1%; FSIS 38.6% | FY2013–FY2025 | USA | Zhang et al., Foods (MDPI), 2026. Peer-reviewed analysis of openFDA and FSIS data. | https://www.mdpi.com/2304-8158/15/17/3115/pdf?version=1788339146 | "FSIS allergen recalls (38.6%) outnumber microbiological recalls (23.0%)—the opposite of FDA, where microbiological (46.2%) leads allergen (27.1%)." (Abstract/search snippet) | High for the study, but not annual 2022–2025 |
| 1a | USA: official annual share from FDA or USDA | NOT FOUND | 2022–2025 | USA | FDA / USDA FSIS | — | Neither FDA nor FSIS publishes a single annual table of "% of all food recalls due to undeclared allergens" in the sources reviewed. FSIS does publish annual recall summaries with reason categories, but a consolidated FDA+USDA share is not available from a primary source. | — |
| 1b | EU: RASFF allergen notifications | 217 notifications (≈4.6% of 4,695 RASFF notifications) | 2023 | EU-27 | European Commission, 2023 ACN Annual Report (primary). | https://food.ec.europa.eu/document/download/911d49f2-b3ef-4752-8ea3-5f20dbbe9945_en?filename=acn_annual-report_2023.pdf | "These were followed by allergens (217 notifications), mainly in relation to prepared dishes and snacks (41 notifications). It is worth mentioning that milk related allergens were the most notified (39)." | High |
| 1b | EU: total RASFF notifications (denominator) | 4,695 | 2023 | EU-27 | European Commission, 2023 ACN Annual Report / news release. | https://ec.europa.eu/newsroom/sante/items/847722/en | "In 2023, there was an 8% rise in RASFF notifications, with a total of 4695 notifications." | High |
| 1b | EU: RASFF allergen notifications 2024 | NOT FOUND | 2024 | EU-27 | 2024 ACN Annual Report | — | The full 2024 ACN report was not accessible in this session. The ACN Overview 2024 confirms 5,250 RASFF notifications but does not break out allergens. | — |
| 1c | UK FSA: allergy alerts | 101 allergy alerts | 2024 | UK | FSA / secondary compilation | https://www.food.gov.uk (alerts portal); compiled figure from Food Hygiene Certificate / industry summaries | Search snippet: "101 allergy alerts were issued by the Food Standards Agency, up from 64 in 2023." | Medium (official FSA annual count not directly opened) |
| 1c | Ireland FSAI: allergen alerts | 58 allergen alerts (of 126 total recall warnings) | 2024 | Ireland | FSAI Annual Report 2024 / Food Safety News summary | https://www.foodsafetynews.com (FSAI annual report coverage) | "A total of 126 warnings about food being recalled were issued in the form of 68 food alerts and 58 allergen alerts, an increase from 71 alerts in 2023." | Medium (official PDF not opened) |
| 2 | Root causes of allergen recalls | Label/packaging errors: 50.1%; Supply-chain: 16.3%; Process/cross-contact: 9.4% | Not stated | Multi-country (FDA/FSA/FSAI/FSANZ review) | Peer-reviewed / industry review; secondary compilation | https://www.food-safety.com (summary of PAL study) | "Label/packaging errors 50.1% / Supply chain related 16.3% / Process/cross-contact related 9.4%." | Medium (original study not opened) |
| 2 | Root causes: cleaning/changeover failure separately | NOT FOUND | — | — | — | — | No source broke out "cleaning/changeover failure" as a standalone percentage. | — |
| 3 | Cost of a food recall: average direct cost, large companies | USD 10 million (average direct cost) | 2010 study / widely cited | USA | FMI & GMA study (via secondary citations) | https://www.biomerieux.com / https://www.qualityassurancemag.com | "Food recalls cost American companies in the food sector on average 10 million dollars in direct costs." | Medium (dated and secondary) |
| 3 | Cost of a food recall: SME figure | NOT FOUND | — | — | — | — | No robust SME average found. A New Zealand study mentions "less than €100,000" for a 150,000 kg milk batch, but that is not an SME average. | — |
| 3 | Indirect costs | NOT FOUND as a single average figure | — | — | — | — | Sources note indirect costs "could multiply direct costs by +3" or more, but no primary average found. | — |
| 4 | NACE 10.71 — EU-27 enterprises | 1,142,268 enterprises | Not explicit | EU-27 | Eurostat SBS (via Cultura Veneto table) | https://www.culturaveneto.it | Table shows EU-27 1,142,268 enterprises; Italy 181,442. | Medium |
| 4 | NACE 10.71 — Italy enterprises | 181,442 enterprises | Not explicit | Italy | Eurostat SBS (via Cultura Veneto table) | https://www.culturaveneto.it | Same table. | Medium |
| 4 | NACE 10.72, 10.82, local units, turnover | NOT FOUND | — | EU-27 / Italy | — | — | Not retrieved within the step limit. | — |
| 5 | Reg. (EU) 2021/382 | Requires a documented allergen-management programme based on hazard assessment | In force from 24 March 2021 | EU | European Commission / EUR-Lex | https://ec.europa.eu/newsroom/sante/items/710612/en ; https://eur-lex.europa.eu/eli/reg/2021/382/oj | Regulation "amending the Annexes to Regulation (EC) No 852/2004 … as regards food allergen management, redistribution of food and food safety culture." Annex requires an allergen management programme "based on an assessment of the sources and the nature of potential allergens." | High |
| 5 | BRCGS Food Safety Issue 9 | Requires validated allergen changeover procedures | Issue 9 (audits from Feb 2023) | Global | BRCGS (paywalled), secondary descriptions | https://www.brcgs.com | Clause 5.3: allergens managed through validated procedures; changeover cleaning validated and effectiveness verified regularly. | Medium |
| 5 | IFS Food v8 | Requires allergen risk assessment and validated cleaning between runs | v8 (audits from Jan 2024) | Global | IFS Food v8 (paywalled), secondary | https://www.ifs-food.org | Requirement 4.19: documented allergen risk assessment and procedures to prevent cross-contamination; cleaning effectiveness at changeover validated. | Medium |

### 2. Summary (DeepSeek)
- EU RASFF 2023: 217 allergen notifications (≈4.6% of all RASFF notifications). Primary, official.
- USA 2024: 101 undeclared-allergen recalls = 34% of all FDA+USDA recalls (secondary).
- Root causes: ~50% label/packaging errors, ~16% supply-chain changes, ~9% process/cross-contact.
- Caveat: USD 10M recall cost is dated and secondary. No SME or Italy recall-cost figure found.

---

## DeepSeek · G2 — Concorrenti e prezzi

Analyst note (as of 14 Nov 2026). Linkage scale (analyst judgment): L3 = data graph across specs/products/suppliers/lots; L2 = workflow-linked records; L1 = repository with approval/version control.

### 1. Allergen, linkage, AI
| Vendor (HQ) | Allergens | Linkage | AI |
|---|---|---|---|
| Safefood 360° (Ideagen) — Ireland/UK | Allergen ingredient flags → auto allergen lists/matrices; supplier spec reviews; supplier doc approval; no dedicated changeover validation engine; no label artwork check | L2: documents attached to assessments/audits, versioned, two-stage approval; no revision → SKU → batch graph | Limited native; parent Ideagen embedding Mazlan AI, allergen/label compliance on roadmap |
| TraceGains — US | Allergen forms, specs, certificates, COAs; allergen dashboards; automated change control when ingredient/claim/allergen changes, cascading to products and packaging | L3: supplier/spec data graph, specs → products → packaging → suppliers; not plant batch execution | Native IDP: extracts supplier docs, COAs, specs; AI formulation |
| Trustwell (FoodLogiQ + Genesis) — US | AI spec scanning; detects allergen declaration gaps before label finalisation; allergen plans; label checks | L3: recipes → specs → labels → supplier compliance → traceability; weak on operator execution | AI spec extraction, label-risk detection, guided workflows, AskReg |
| SafetyChain — US | Cross-process allergen workflow: supplier declarations → incoming verification → scheduling → changeover → sanitation validation → testing → label review → CAPA | L2–L3: links quality/production/supplier data; not document-revision reasoning | "Decision Intelligence" analytics; little evidence of generative document reasoning |
| Icicle — Canada | Allergen database, tracking, labelling, cross-contamination, supplier approval; "dynamic model" of ingredients/allergens/hazards | L2–L3: relational model; no real-time revision-to-batch graph | Nascent "AI Assist" |
| Redzone (QAD) — US | Line checks, allergen-concern events, changeover validation with swabs, holds, CAPA | L2–L3 for events, not documents | ChampionAI "next best action" |
| Ideagen Food & Beverage — UK | Version control of specs and allergen declarations; flags dependent declarations and labels when a spec changes; supplier audits | L3 within QMS; not plant-floor events | Mazlan AI / agentic; allergen/label compliance on roadmap |
| Intact — Austria | Audit/certification; flags high allergen non-conformity rates | L1–L2: audit evidence and certificates | Intact Analytics ML/NLP on audit data |
| FoodDocs — Estonia | Digital recipe book with allergen overview; HACCP allergen tasks; corrective actions | L2: HACCP, SOPs, tasks; no supplier-spec graph | AI HACCP plan generation, AI reports |
| Nutritics — Ireland | Recipe/nutrition/allergen calculation; AI Auto Allergen Detector (Enterprise); labels | L2 for recipe/label data; not QMS | AI Auto Allergen Detector |
| Biorsaf / Cooki — Italy | Cooki: allergen risk in recipes, labels, traceability; Biorsaf: digital HACCP | L2; deep linking not publicly evidenced | AI agent for monitoring, compliance, document management |
| AYAMA Quality — Italy | Actual-allergen and cross-contamination management; EATsoft label module (Reg. 1169/2011); HACCP checklists | L2: modules share data, document archive, supplier portal | No public AI |

### 2. Workflow, target, price
| Vendor | Approval / escalation / operator dispatch | Target | Public price per site/month |
|---|---|---|---|
| Safefood 360° | Two-stage document approval; supplier approval; CAPA; no operator dispatch | SME → mid, multi-site | Not published. Third-party: ~€500–€2,000/month; entry ~$15K/year |
| TraceGains | Configurable supplier/item approvals, alerts; no plant hierarchy or dispatch | Mid → enterprise | Not published. Third-party from ~$20,000/year |
| Trustwell | Multi-stage approvals (R&D, FSQA, legal, procurement); no dispatch | Mid → enterprise | Quote only. AskReg $299/year (adjacent product) |
| SafetyChain | Configurable workflows, escalations, CAPA, mobile operator forms, tasks | Mid → enterprise, multi-facility | Not published; annual per-facility subscription; one-time setup fee |
| Icicle | Supplier approval, document management; no public hierarchical escalation | SME → mid | Not published |
| Redzone | Strongest operator execution: escalations, CAPA, hold/release, line tasks | Mid → enterprise | Not published; third-party estimate $2,000–$6,000/site/month |
| Ideagen F&B | Document approval, supplier certificates, CAPA; no operator dispatch | Mid → enterprise | Not published; Capterra $238/user/month, $25,000 starting |
| Intact | Audit tasks, review workflows, corrective actions | Certification bodies | From €199/month (Capterra) |
| FoodDocs | Tasks, corrective actions, notifications; no multi-level approval | Micro → SME | Published: $99/$199/$299 per site/month (monthly); $79/$167/$250 (annual) |
| Nutritics | None (recipe/label data only) | SME foodservice, small manufacturers | From ~€90/quarter (entry); enterprise quote |
| Biorsaf / Cooki | Automated checks and tasks; hierarchy not public | Italian SME → mid, HORECA, retail | Not published |
| AYAMA Quality | Supplier qualification, audits, non-conformities, checklists | Italian SME → mid | Not published |

### 3. Typical SME price range (DeepSeek)
| Tier | Per site/month | Evidence |
|---|---|---|
| Light HACCP tools | $79–$300 | FoodDocs public pricing |
| SME / mid food QMS | ~€500–€2,000 | Safefood 360 third-party range; entry ~$15K/year |
| Plant QMS with operator execution | ~$2,000–$6,000 | Redzone third-party estimate |
| Supplier network / enterprise | ~$1,700–$8,000+ ($20K–$120K+/year) | TraceGains ~$20K/year; Ideagen $25K starting |
Practical SME: €750–€2,000/site/month + €5K–€25K implementation; with operator dispatch €2,000–€5,000.

### 4. Funding and acquisitions 2022–2026 (DeepSeek)
| Date | Event | Amount |
|---|---|---|
| Feb 2022 | FoodDocs round led by Bonnier Capital | $2.4M |
| Oct 2022 | ESHA Research + FoodLogiQ merge (→ Trustwell); FoodLogiQ total raised $33.1M | Undisclosed |
| Jan 2023 | Ideagen acquires Qadex | Undisclosed |
| Feb 2023 | QAD acquires Redzone | ~$1B |
| Jan 2024 | TraceGains acquires NutriCalc | Undisclosed |
| Apr 2024 | Nutritics acquires Ten Kites | Undisclosed |
| Oct 2024 | Veralto acquires TraceGains | $350M |
| Jul 2025 | Ideagen acquires Safefood 360° (£9.92M) and Authenticate (£7.91M) | £17.83M total |
| Jan 2026 | TPG Rise majority investment in Trustwell | Undisclosed |
| Jan 2026 | Kester Capital minority investment in Nutritics | Undisclosed |
| Sep 2026 | Biorsaf raises €5.2M (lead P101) and acquires Cooki | €5.2M |
| (2021, context) | SafetyChain $50M growth equity (JMI Equity) | $50M |

### 5. Strategic read (DeepSeek, summary)
- Three groups: supplier/spec data networks (TraceGains, Trustwell), plant execution (SafetyChain, Redzone, Ideagen), audit (Intact). SME tools (FoodDocs, Biorsaf/Cooki, AYAMA) are cheaper but none publicly shows the full chain: document revision → allergen impact → batch hold → hierarchy approval → operator dispatch.
- Our difference: "temporal document memory" — knows which procedure revision was valid when a batch was produced.
- Document-centric vendors are weak on operator dispatch; Redzone/SafetyChain are strong on dispatch but weak on document reasoning. That gap is the wedge.
- Price gap between €300 and €2,000/site/month; suggested entry €750–€1,500/site/month.
- "Human signs risky actions" is a credible trust position (BRCGS/IFS/FSSC 22000, Reg. 1169/2011).

---

## DeepSeek · G3 — Dolciario e grandi gruppi

Caveat (DeepSeek): no public census of plants owned by large groups vs SMEs/co-packers; split is qualitative. "daD" = not found.

| Topic | Evidence | Source (URL as given / missing) |
|---|---|---|
| EU structure | CAOBISCO: >14,000 chocolate, biscuit and confectionery manufacturers; 99% SMEs; mostly family-run | CAOBISCO (URL not given) |
| Italy companies | ATECO 10.82: 821 companies, 292 joint-stock; turnover €5.117 billion | (URL not given) |
| Ferrero Italy | 4 plants in Italy (Alba, Pozzuolo Martesana, Sant'Angelo dei Lombardi, Balvano), 7,754 employees at 31 Aug 2025; 37 plants worldwide | (URL not given) |
| Mondelez Italy | 2 plants (Caramagna Piemonte, Capriata d'Orba), ~900 employees | (URL not given) |
| Mars Italy | No manufacturing plants in Italy | (URL not given) |
| Nestlé / Perugina | Perugina plant, Perugia (San Sisto) | (URL not given) |
| Co-packing EU | Ludwig Schokolade: 4 sites, divisions brands / private label / co-manufacturing. Natra: "one of Europe's largest vertically integrated private-label and co-manufacturing platforms for chocolate products", 5 factories after Gudrun | (URL not given) |
| Co-packing Italy | Pernigotti: private label for COOP, Carrefour, Conad, Pam Panorama, Despar, Bennet. Indaco: contract manufacturing for gum, candies, nutraceuticals | (URL not given) |
| Shared lines | Tree nuts, peanuts, milk, egg, soy, gluten, sesame on shared lines; "more allergen touchpoints than a single-SKU plant" | Cookie Label article (URL not given) |
| Changeover validation | Visual inspection insufficient; validated cleaning, disassembly, swab tests (ATP; lateral-flow for gluten/milk/egg); records requested by brands and retailers | (URL not given) |
| Ferrero suppliers | Supplier Code; suppliers >80% of spend acknowledged it; ~100 on-site supplier audits/year; 100% food-safety audit coverage of co-packers and storage points | (URL not given) |
| Mondelez suppliers | Written QMS per MDLZ Supplier Quality Expectations Manual; GFSI certification (BRCGS, IFS, FSSC 22000), ISO 9001, cGMP, HACCP; aim: all material suppliers GFSI-certified | (URL not given) |
| Nestlé suppliers | Supplier Code; third-party audits (BVQI, SGS, ITS); Responsible Sourcing Standard | (URL not given) |
| Mars suppliers | Supplier Code of Conduct, applies to co-manufacturers and subcontractors | (URL not given) |
| Barilla suppliers | Third-party certified suppliers; Code of Ethics; SMETA | (URL not given) |
| Ferrero Kinder 2022 (DO NOT USE IN PITCH) | Arlon, Salmonella; >3,000 t withdrawn; plant closed; "tens of millions of euros"; >150,000 claims | VRT NWS (URL not given) |
| Ferrero Arlon 2023 (DO NOT USE) | Salmonella detected again, precautionary stop, no recall | (URL not given) |
| Mondelez 2022 | Grany (Belgium) plastic; LU Granola (France) metal particles | (URL not given) |
| Nestlé/Froneri 2021 | ≥46 ice-cream varieties withdrawn, ethylene oxide | (URL not given) |
| Mars 2021–2022 | Snickers, Twix, Bounty, M&M's ice cream, ethylene oxide from a French supplier ingredient | (URL not given) |
| Haribo 2023 | Nordic markets, metal particles | (URL not given) |
| Lindt 2023 | Italy: pralines with pistachio filling, pistachio not declared → allergen recall | (URL not given) |

Summary (DeepSeek): co-packing is structural; 99% SMEs face the hardest compliance burden; big brands require GFSI/HACCP/audits from suppliers and co-packers ("licence to operate"); allergen cross-contact on shared lines is the hardest control; recall consequences are severe but rarely documented.

---

## DeepSeek · D2 — Verifica numeri

| Claim | Verdict | Correct value | Year | Source | URL | Quote |
|---|---|---|---|---|---|---|
| 1. 38.8% of FDA+USDA recalls in 2025 = undeclared allergens (Statista 36281) | TRUE (snippet; chart paywalled) | 38.8% of 320 recalls; most common reason | 2025 | Statista | https://www.statista.com/chart/36281/fda-and-usda-food-recalls-in-the-united-states/ (DeepSeek gave a search URL) | "The most common reason for food recalls in 2025 was undeclared allergens. This accounted for nearly four in ten cases (38.8 percent) of all food recalls." |
| 2. 2023: about half of US recalls, driven by sesame (PIRG) | TRUE | 49.2% (154 of 313) | 2023 | Food Safety Magazine / PIRG | https://www.food-safety.com/articles/print/9437-thanks-sesame-us-food-recalls-due-to-undeclared-allergens-skyrocketed-in-2023-causing-half-of-all-food-recalls | "According to PIRG's analysis, half of the total 313 food product recalls (49.2 percent) were issued due to undeclared allergens" |
| 3. USDA ERS 27.4% in 2004–2013 | TRUE | 27.4% (41.0% pathogens) | 2018 report | USDA ERS, Trends in Food Recalls 2004-13 | https://ers.usda.gov/sites/default/files/_laserfiche/publications/88497/eib191-Summary.pdf?v=10932 | "… 41.0 percent were the result of pathogen contamination … and 27.4 percent were the result of undeclared allergens." |
| 4. USD 10M average direct cost (FMI/GMA) | TRUE (2010 study) | USD 10M | 2010 | Interroll fact sheet citing FMI/GMA | https://www.interroll.com/fileadmin/user_upload/Downloads__PDF_/Industry_Fact_Sheets/Industry_Fact_Sheet__1_Food.pdf | "Food recalls … cost companies an average of $10 million in direct costs alone, according to a study by the Food Marketing Institute and the Grocery Manufacturers Association (GMA) in the US." |
| 5. RASFF 2024: 5,250, +12% | TRUE | 5,250, +12% | 2024 | European Commission, ACN 2024 | https://ec.europa.eu/newsroom/sante/items/882537 | "RASFF notifications (non-compliances with risks for public health) rose by 12%, totalling 5,250." |
| 6. Italy ~56,000 food manufacturing enterprises | PARTIALLY TRUE | 56,780 food & beverage enterprises (not only manufacturing); other registries 54,557 / 56,595 | 2024 | Ristorazione Italiana Magazine (RS Group / We Live Context) | https://www.ristorazioneitalianamagazine.it/italia-francia-food-beverage-emea/ | "L'Italia si conferma leader assoluto per numero di aziende operative nel settore food & beverage, con ben 56.780 unità." |
| 7. Reg. 2021/382: allergen management incl. cleaning and segregation | TRUE | Amends 852/2004 | 2021 | BAV-Institut summary | https://www.bav-institut.de/ | "Equipment, means of transport, and containers intended for the harvesting, transport, or storage of allergenic products must not be used for foodstuffs that do not contain the corresponding allergen. Exceptions apply with appropriate cleaning and visual inspection." |

Strongest (DeepSeek): RASFF 2024 (official); USDA ERS 27.4% (official, old); PIRG 49.2% 2023 (recent, advocacy group). Weaker: USD 10M (2010), 56,780 (food & beverage, not manufacturing), Statista 38.8% (paywalled, small base of 320 recalls).

---

## Gemini — vedi `ricerca_gemini.md`
