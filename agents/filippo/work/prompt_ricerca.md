# Prompt di ricerca — da copiare (14.11)

Ordine: G1 e G2 su Gemini Deep Research, D1 e D2 su DeepSeek (ricerca web attiva), G3 su Gemini se resta tempo.
Ogni risposta → incollarla in `ricerca_raw.md`.

## G1 — Gemini Deep Research · Problema e mercato
```
ROLE
You are a senior food-safety and market analyst preparing evidence for an investor pitch. Accuracy matters more than completeness.

CONTEXT
We are building an AI system for food manufacturing plants that handle several allergens on shared lines (confectionery, chocolate, biscuits, bakery, co-packers). It reads supplier documents, cleaning logs, procedures and shift reports as they arrive, links them (supplier → ingredient → machine → batch → label), detects undeclared-allergen risk before products ship, and routes the decision through the plant's approval chain. Target market: Italy first, then EU-27.

TASKS
1. Undeclared allergens as a cause of recalls:
   a. USA: share of FDA + USDA recalls due to undeclared allergens, latest available years (2022-2025).
   b. EU: number and share of RASFF notifications related to allergens, 2023 and 2024 (official RASFF / ACN annual reports).
   c. UK (FSA) or Ireland (FSAI): number of allergy alerts per year, if available.
2. Root causes of allergen recalls: shares due to cross-contact on shared lines, supplier ingredient changes, cleaning/changeover failures, labelling or packaging errors. Use FDA, FSA, FSAI, FSANZ or peer-reviewed studies.
3. Cost of a food recall: average direct cost for large companies AND any figure for SMEs (EUR or USD), including indirect costs (brand, lost sales, retailer penalties).
4. Market size: number of enterprises and of local units (plants) in Italy and in the EU-27 for NACE codes 10.71 (bread and fresh pastry), 10.72 (rusks, biscuits, preserved pastry), 10.82 (cocoa, chocolate and sugar confectionery). Use Eurostat Structural Business Statistics or ISTAT, latest year. Include turnover if available.
5. Regulatory pressure: what Regulation (EU) 2021/382 (amending 852/2004) requires on allergen management, and what BRCGS Food Safety Issue 9 and IFS Food v8 require on allergen control and changeover validation.

RULES
- Do not invent or estimate numbers. If you cannot find a figure, write "NOT FOUND".
- Prefer primary sources (official agencies, regulators, statistical offices) over blogs or vendor marketing.
- For every figure give: value, year, geography, source name, exact URL, a verbatim quote from the source, and confidence (high / medium / low).
- Flag any figure that comes from a paywalled report or a secondary citation.

OUTPUT
1. One markdown table with columns: # | Topic | Figure | Year | Geography | Source | URL | Verbatim quote | Confidence.
2. A summary of max 5 lines: the 3 strongest numbers for a pitch.
```

## G2 — Gemini Deep Research · Concorrenti e prezzi
```
ROLE
You are a B2B SaaS analyst specialised in food-manufacturing software.

CONTEXT
Same product as above: an AI "memory" for a food plant that links scattered documents in real time, knows which procedure revision is current, detects undeclared-allergen risk, proposes a targeted batch hold, and routes approvals through the internal hierarchy (line supervisor → QA manager → plant director), then sends instructions to workers. A human always signs risky actions.

TASKS
1. Map 8-12 competitors in food-safety / quality-management / allergen-management software (EU and US). Include at least: Safefood 360, TraceGains, Trustwell (FoodLogiQ), SafetyChain, Icicle, Redzone, Ideagen, Intact, plus any Italian or EU vendors serving food SMEs.
2. For each competitor report:
   - What it does for allergens (supplier specification changes, cleaning/changeover validation, label checks).
   - Does it LINK documents and events together, or only store them?
   - Does it use AI, and for what?
   - Does it have approval workflows / escalation / task dispatch to operators?
   - Target customer size (SME / mid / enterprise).
   - Public price per site per month, if published.
3. Typical price range of food-safety QMS software for an SME plant (per site per month).
4. Any recent funding rounds or acquisitions in this space (2022-2026), with amounts.

RULES
- No invented data. Write "NOT PUBLIC" when a price is not published, "NOT FOUND" when a feature cannot be confirmed.
- Every row must have a source URL and the date of the page or article.

OUTPUT
1. Markdown table: Vendor | Country | Allergen features | Links documents? | AI | Approval workflow | Target size | Public price | Source URL.
2. Max 5 lines: the gap that none of them covers well.
```

## D1 — DeepSeek · Gestione interna e tempi
```
Search the web and answer only with sourced facts.

Context: we are pitching an AI system that speeds up internal quality decisions in food plants. Today, when a risk is detected, the case goes up the hierarchy by hand (line supervisor → QA manager → plant director) with emails and forms; meanwhile production continues.

Find data (studies, surveys, regulator guidance, industry reports) on:
1. How long food companies take from detecting a non-conformity to deciding a hold or recall (hours or days).
2. How much time QA / food-safety managers spend on documentation, record keeping and audit preparation (hours per week or % of working time).
3. Measured benefits of moving HACCP, CAPA or quality workflows from paper/spreadsheets to digital systems (time saved, errors reduced, audit findings reduced).
4. Typical number of QA / food-safety staff in an SME food plant (20-250 employees).
5. Most common audit non-conformities related to allergen management (BRCGS, IFS, FDA inspections).

Rules: do not estimate. For each finding give value, year, source name, URL and a verbatim quote. If nothing reliable exists, write NOT FOUND.
Output: one markdown table, then 3 lines on which numbers are strongest.
```

## D2 — DeepSeek · Verifica dei numeri che usiamo
```
Search the web and fact-check each claim. For each one answer TRUE, FALSE or PARTIALLY TRUE, give the correct value and year, the exact source URL and a verbatim quote.

1. "Undeclared allergens were the leading cause of US food recalls in 2025: 38.8% of FDA and USDA recalls." (Statista chart 36281)
2. "In 2023 undeclared allergens caused about half of all US food recalls, driven by sesame." (PIRG report, food-safety.com)
3. "According to USDA ERS, 27.4% of US food recalls in 2004-2013 were due to undeclared allergens."
4. "The average direct cost of a food recall to a company is about USD 10 million." (FMI/GMA study)
5. "In 2024 the EU RASFF network recorded 5,250 notifications, 12% more than in 2023."
6. "Italy has about 56,000 food manufacturing enterprises."
7. "Regulation (EU) 2021/382 introduced an explicit obligation for food business operators to manage allergens, including cleaning and segregation."

Output: markdown table with columns Claim | Verdict | Correct value | Year | Source | URL | Quote.
```

## G3 (opzionale) — Gemini Deep Research · Settore dolciario e grandi gruppi
```
ROLE
You are an industry analyst for the European confectionery sector.

TASKS
1. Structure of the confectionery supply chain in Italy and the EU: how many plants are owned by large groups versus SMEs and co-packers; how common co-packing and third-party suppliers are for large confectionery brands.
2. Why allergen management is especially hard in confectionery: tree nuts (hazelnuts, almonds), peanuts, milk, egg, soy, gluten on shared lines; typical changeover and cleaning validation practices.
3. Public commitments of large confectionery groups (e.g. Ferrero, Mondelez, Nestlé, Mars, Barilla) on food safety, supplier quality requirements and digitalisation of quality processes: what they require from their suppliers and co-packers (codes of conduct, supplier quality manuals, certifications).
4. Large recalls in the confectionery sector in the EU in 2020-2025 (any cause), with the documented consequences (plant closures, volumes withdrawn, costs) — factual, sourced only.

RULES
No invented data. Every item: source URL, date, verbatim quote; "NOT FOUND" if missing.
OUTPUT
Markdown table + 5-line summary on the opportunity for a tool sold to suppliers and co-packers of large confectionery brands.
```
