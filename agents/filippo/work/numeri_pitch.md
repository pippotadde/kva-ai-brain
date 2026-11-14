# Numeri per pitch, abstract e modello economico (fase 3, 14.11)

Fonte: confronto VERIFICA T3 (DeepSeek, `ricerca_raw.md`) + VERIFICA GEMINI (`ricerca_gemini.md`).
Livelli: **[verificato]** = numero letto sulla fonte primaria · **[fonte di settore]** = fonte secondaria/terzi · **[ipotesi nostra]** = calcolo o stima del team.
Regola: in pitch/abstract solo [verificato]; [fonte di settore] solo con "secondo..."; [ipotesi nostra] dichiarata a voce.

## 1. Problema

| # | Dato | Valore | Livello | Fonte | DeepSeek vs Gemini |
|---|---|---|---|---|---|
| P1 | Allergeni non dichiarati = prima causa richiami USA 2025 | 38,8% (124 su 320), prima causa per il 3° anno | [verificato] su Statista; SafetyChain [fonte di settore] | Statista chart 36281 (PIRG Food for Thought 2026); SafetyChain blog | Concordano (38,8% ≈ 39%) |
| P2 | USA 2024 | 101 richiami = 34% | [fonte di settore] | food-safety.com art. 10126 (PIRG) | Solo DeepSeek |
| P3 | Cause radice richiami allergeni, Australia 2017-22 | 48% imballaggio/etichetta sbagliata · 22% verifica fornitori · 15% contaminazione crociata | [verificato] | FSANZ allergen-stats, tab. 3 (agg. 25.02.2025) | Sostituisce il "50,1/16,3/9,4" di DeepSeek (non trovato) |
| P4 | Cause radice USA FDA 2013-19 (914 richiami) | 71% errori di etichettatura · 23% contaminazione crociata | [fonte di settore] | food-safety.com art. 8496 | Solo DeepSeek; alternativa a P3 |
| P5 | Chi scopre il problema (Australia) | primo canale = reclamo del cliente (102 su 231) | [verificato] | FSANZ tab. 2 | Solo Gemini |
| P6 | Allerte UE RASFF 2024 | 5.250 notifiche, +12% | [verificato] | EC newsroom items/882537 | Concordano |
| P7 | Allergeni in RASFF | 2022: 210 · 2023: 217 (latte il più notificato) | [verificato] | ACN Annual Report 2022 e 2023 (PDF) | Combinati: serie in crescita |
| P8 | UK FSA Allergy Alerts | 2023/24: 62 → 2024/25: 96 (+55%) | 62 e +55% [verificato]; 96 [fonte di settore] | FSA Annual Report 2024; Sessions UK | Il "101 vs 64" di DeepSeek NON regge |
| P9 | Irlanda FSAI 2024 | 58 allerte allergeni su 126 | [fonte di settore] | Food Safety News 07/2025 | Solo DeepSeek |
| P10 | Costo richiamo | "fino a 10 M$ di costi diretti per i grandi gruppi", dato 2010, esclude marchio e vendite perse | [fonte di settore] | FMI/GMA/Deloitte 2010 | NON usarlo come costo per PMI. Costo PMI: non trovato |
| P11 | Norma UE | Reg. 2021/382: pulizia e verifica di assenza residui su attrezzature condivise + cultura della sicurezza alimentare (NON impone segregazione) | [verificato] (testo EUR-Lex) | eur-lex.europa.eu/eli/reg/2021/382/oj | Riformulato da Gemini-verifica |

**Da NON usare:** "30% richiami = allergeni" UE; Eurostat 10.71 "1,1 M imprese"; MDPI 27,1/38,6; "101 vs 64" UK; Biorsaf "3,4 M imprese / 3% digitali"; benchmark operativi dei fornitori (-50% CAPA, ore risparmiate).

## 2. Mercato (TAM / SAM / SOM)

| # | Dato | Valore | Livello | Fonte |
|---|---|---|---|---|
| M1 | Produttori dolciari (cioccolato, biscotti, confetteria) UE27+CH | 14.300 imprese, 99% PMI, 280.470 addetti | [verificato] | caobisco.eu/facts (2020) |
| M2 | Industrie alimentari Italia (ATECO 10) | 50.177 imprese, 422.567 addetti | [verificato] (anno da ricontrollare) | ISTAT Settori produttivi 2025, PDF settore 10 |
| M3 | Italia ATECO 10.71 pane/pasticceria | ≈ 25.300 imprese (2021) | [fonte di settore] | Statista su Eurostat/Istat |
| M4 | Italia ATECO 10.82 cacao/cioccolato/confetteria | 821 imprese | non verificato — non usare | — |

Calcolo con prezzo piano Stabilimento 390 €/mese = 4.680 €/anno (prezzo ancora da confermare, vedi §3):
- **SAM** = 14.300 produttori dolciari UE × 4.680 € ≈ **67 M€/anno** [ipotesi nostra; 1 stabilimento per impresa].
- **TAM** = 50.177 imprese alimentari Italia × 4.680 € ≈ **235 M€/anno** solo Italia [ipotesi nostra; molte sono micro e non comprano].
- **SOM 3° anno** = 150 stabilimenti × 4.680 € ≈ **0,7 M€/anno** [ipotesi nostra, da `pitch/04_FABBRICA.md`] = ~1% del SAM.

## 3. Prezzo, costo, margine

| # | Voce | Valore | Livello |
|---|---|---|---|
| R1 | Prezzo piano Stabilimento | **390 €/mese** (Giorgia) — APERTO: Filippo aveva 800 €/mese. Decidere prima del modello economico | [ipotesi nostra] |
| R2 | Pilota | 0 € per 60 giorni, 1 linea | [ipotesi nostra] |
| R3 | Gruppo | da 1.500 €/mese | [ipotesi nostra] |
| R4 | Costo per cliente (server + modello) | ~40 €/mese → margine lordo ~89% (da ricalcolare con prezzo Claude) | [ipotesi nostra] |

Posizionamento prezzo rispetto al mercato (perché 390 regge):

| Fascia | Esempi | Prezzo per sito/mese | Livello |
|---|---|---|---|
| HACCP digitale base | FoodDocs | $99 / $199 / $299 (listino) | [fonte di settore] (G2/Capterra; listino ufficiale non aperto) |
| QMS modulare | AlisQI | $249-369 per modulo, 3-4 moduli = $926-1.235 | [verificato] alisqi.com/en/pricing |
| Fornitori/specifiche enterprise | TraceGains | da ~$20.000/anno (~$1.667/mese) | [fonte di settore] |
| Esecuzione in linea | Redzone, SafetyChain | $2.000-6.000 (Redzone, stima terzi); SafetyChain $150 → $8-25K | [fonte di settore] |

→ 390 €/mese sta sopra l'HACCP base e sotto un QMS modulare: prezzo da PMI. Se si sceglie 800 €/mese resta sotto AlisQI con 3 moduli.

**Non dire** "meno dello 0,05% del costo medio di un richiamo": si basa sui 10 M$ dei grandi gruppi (P10). Alternativa: "costa meno di un modulo di un QMS industriale" (AlisQI, [verificato]).

## 4. Canale e CAC

| # | Voce | Valore | Livello |
|---|---|---|---|
| C1 | Canale | consulenti HACCP e certificatori (BRCGS, IFS); grandi marchi come leva (chiedono qualità a fornitori e co-packer) | [ipotesi nostra] |
| C2 | CAC | nessun dato trovato. Stima: commissione consulente 20% del 1° anno ≈ 940 € + pilota 60 gg ≈ 80 € costo → CAC ≈ 1.000 €, payback ≈ 3 mesi a 390 €/mese con margine 89% | [ipotesi nostra] |

## 5. Concorrenti (cosa fanno / cosa manca)

| Nome | Cosa fa | Cosa non fa (il nostro spazio) | Livello |
|---|---|---|---|
| TraceGains (Veralto, comprata 350 M$ 2024) | Grafo fornitori-specifiche-formule-etichette, AI su COA | Si ferma prima della linea: niente lotti in produzione, niente istruzioni agli operatori | acquisizione [verificato] (10-K Veralto) |
| Trustwell (FoodLogiQ + Genesis) | Ricette → etichette, AI allergeni nascosti | Niente controlli in linea né invio istruzioni | [fonte di settore] |
| SafetyChain | Controlli in linea, blocchi lotto, CAPA | Niente ragionamento AI sui documenti | [fonte di settore] |
| QAD Redzone | Compiti agli operatori, escalation, SOP attiva | Allergeni e specifiche fornitori fuori dal sistema | [fonte di settore] |
| Safefood 360° / Ideagen | Documenti, approvazioni, fornitori | Niente AI propria, niente operatori | acquisizione 2025 [verificato] (Business Wire); prezzi non verificati |
| Biorsaf / Cooki (Italia) | HACCP digitale + allergeni nelle ricette, AI | Collegamento profondo e gerarchia non dimostrati pubblicamente | round 5,2 M€ set. 2026 [verificato] |

Sintesi per il pitch: chi collega i documenti non arriva in linea; chi è in linea non legge i documenti. Nessuno unisce fornitore → ingrediente → macchina → lotto → etichetta con firma lungo la gerarchia [ipotesi nostra, su materiale pubblico].
Valori: Ideagen £1,05 mld e Redzone ~1 mld$ NON verificati → non citare cifre.

## 6. Gestione interna (tempi di approvazione/escalation)

| # | Voce | Valore | Livello |
|---|---|---|---|
| G1 | Tempi di approvazione/escalation oggi | non trovati in fonti indipendenti | — |
| G2 | UK FSA: prima causa nelle analisi delle cause = mancati controlli, 30% | [fonte di settore] (Sessions UK, cita FSA giu. 2026) |
| G3 | Tempo da avviso a istruzione in linea con il nostro sistema | da misurare nella demo [ipotesi nostra] |

## 7. I 5 numeri consigliati (abstract e slide)

1. **38,8%**: allergeni non dichiarati = prima causa di richiamo alimentare negli USA nel 2025 (Statista/PIRG) [verificato].
2. **48% + 22%**: in Australia quasi metà dei richiami per allergeni nasce da imballaggio o etichetta sbagliata, uno su cinque da un fornitore (FSANZ 2017-22) [verificato] — i due punti dove interviene il sistema.
3. **5.250 allerte UE nel 2024, +12%** (Commissione UE, RASFF) [verificato].
4. **14.300 produttori dolciari UE, 99% PMI** (CAOBISCO) [verificato] — il nostro cliente.
5. **Il mercato si muove**: TraceGains comprata 350 M$ (2024), Biorsaf 5,2 M€ (set. 2026) [verificato].
