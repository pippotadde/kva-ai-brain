# Idea search — 14.11.2026 (night session, Filippo's Claude)

## Where we are
- Business plan for "allergen-safe changeovers" (Idea 1, food): Claude Doc https://claude.ai/artifact/82b3FHhYHTJVVvXcvUmiyJ
  (problem numbers, TAM/SAM/SOM, competitors 2x2, pricing, 3-yr revenue, GTM, risks).
- Filippo: Idea 1 is hard to understand/build; Sian's MemoLens is clearer and liked more.
  Direction now: keep MemoLens pattern ("agent/person uses stale memory -> silent € loss -> show which memory,
  source, which version supersedes it, similar cases, fix") and move it to a precise INDUSTRIAL sector.
- Filippo is running the DeepSeek prompt below to find one idea that passes all gates; results to be checked here.

## Candidates discussed (short)
| Idea | Verdict |
| --- | --- |
| Spare parts / machine revision (OEM service): wrong part because manual rev B used, machine is rev C | Best so far if kept narrow on revisions. Competitors: Sparetech ($20M, 10.11.2026), Partium, Neuron7 ($63M), Aquant, Sapienta; none seen doing serial->revision checks. No contacts. |
| Quotes in metalworking (stale steel price) | Very clear, but strong competitors (Paperless Parts $30M+, Offeri, Xometry, CloudNC $20M) and less "memory" |
| Food purchasing (supplier spec rev 3 adds peanut traces / EUDR proof missing) | Good fit, harder to explain |
| "Veteran in pocket" (operator/maintenance memory) | Strong problem (ETQ: 70% labour shortage, 88% hurts quality; PMMI: 65% SSOP compliance issue; Unioncamere: 31.7% food machine operators hard to find) |
| Recall "who did I hit?" | Serious problem, harder to build |
| MemoLens original (retail refund) | Clear but not industry, crowded (LangSmith, Langfuse, Datadog) |
| Maintenance agent | Saturated (Augury, Tractian, CMMS) |

## Key facts gathered (sources in the Claude Doc and chat)
- US recalls 2024: 101/296 (34%) undeclared allergens (PIRG). RASFF 2024: 5,250 notifications.
- EUDR applies 30.12.2026 (large/medium), 30.06.2027 (micro/small); fines >= 4% EU turnover; origin data 8-12 weeks.
- PMMI 2025 food end users: labour shortage/turnover 61%, cross-contamination 59%, changing regulations 52%.

## DeepSeek prompt (Italian, as given to Filippo)

```
Sei un analista di venture capital e un ricercatore di mercato. Oggi è il 14 novembre 2026.
Devi trovare UNA idea di startup precisa per un hackathon e dimostrare con fonti che è valida.
Non fermarti finché un'idea non supera TUTTE le soglie qui sotto.
Rispondi in italiano semplice, frasi brevi, niente gergo.

## CONTESTO
- Hackathon "AI brain for industry" di Kakashi Ventures (Torino/online), oggi.
  Tema: memoria, ontologie e "cervelli AI" su misura per l'industria.
- Voto della giuria:
  - aderenza al tema (memoria/ontologie/cervelli AI) 25%, anche spareggio;
  - qualità tecnica di ciò che funziona alla demo 25%;
  - problema industriale reale e impatto 25%;
  - business case 20%;
  - chiarezza della demo 5%.
- La giuria ha costruito "Project OIDA": un registro delle decisioni dove ogni fatto ha
  fonte, autore e data; una nuova versione sostituisce la vecchia; le contraddizioni sono
  segnalate; il sistema dice "non lo so" se mancano prove; le regole sono codice, non AI.
  Nelle loro call cercano manifattura e "AI fisica" e KPI di reparto (tempo ciclo, scarti, fermi).
  Il loro portafoglio è finanza, assicurazioni e media: l'industria è il loro buco.
- Squadra: 3 studenti del Politecnico di Torino, bravi a programmare, nessun contatto nelle aziende.
  Tempo di costruzione: 2,5 ore. Servono una demo funzionante e un business plan.
- La forma che ci piace (da un'idea del team, "MemoLens"):
  "un agente AI o una persona agisce → usa un'informazione vecchia o sbagliata → danno
  silenzioso in euro → il sistema mostra quale informazione è stata usata, da dove viene,
  quale versione la sostituisce, quanti altri casi sono colpiti, e la corregge".
  Esempio originale: un agente rimborsa 120 € invece di 80 € perché usa il prezzo di listino
  vecchio. È chiarissimo, ma è retail: noi vogliamo l'industria.

## IDEE GIÀ ESAMINATE (non riproporle uguali; puoi migliorarle solo se superi le soglie)
MemoLens retail; allergeni nei cambi formato alimentari; richiamo alimentare "chi ho colpito";
ricambi sbagliati per revisione macchina; preventivi metalmeccanici con prezzo vecchio;
manutenzione predittiva; parametri dei cambi formato; EUDR (deforestazione) per cacao e caffè;
documenti per audit qualità; assistente "veterano" per operatori; piano di controllo IATF
automotive; taratura strumenti; deroghe qualità; Regolamento Macchine UE; sicurezza sul lavoro;
direttive di aeronavigabilità.
Motivi degli scarti: troppa concorrenza finanziata, non è industria, difficile da spiegare,
oppure è solo un chatbot sui documenti (RAG), che non basta.

## SOGLIE (un'idea è valida solo se le passa tutte)
S1 Problema provato: almeno 2 fonti indipendenti (non solo vendor che vendono la soluzione)
   lo misurano in euro, ore, % di errori o fermi.
S2 Mercato grande: almeno 5.000 aziende bersaglio in UE oppure almeno 100 M€/anno di valore
   indirizzabile. Chi paga è una figura precisa con un budget (es. direttore di stabilimento).
S3 Concorrenza: elenca i 5-10 concorrenti principali con sito e soldi raccolti.
   L'idea passa solo se:
   (a) ci sono meno di 3 concorrenti diretti che fanno la stessa cosa, OPPURE
   (b) abbiamo una cosa in più che nessuno dei primi 5 ha. Va verificata sui loro siti,
       citando la pagina.
S4 Precedenti reali: almeno 1 caso pubblico (incidente, richiamo, multa, causa, fermo,
   articolo) causato da questo problema, con danno di almeno 100.000 € o finito sui giornali.
S5 Perché adesso: una legge con una data, un cambio tecnologico, o un'ondata di
   investimenti negli ultimi 12 mesi.
S6 Serve davvero una memoria: la soluzione deve gestire fatti che cambiano nel tempo
   (versioni che si sostituiscono), con fonte per ogni fatto, contraddizioni e "non lo so".
   Un semplice chatbot sui documenti NON passa.
S7 Industria: manifattura, energia, logistica, aerospazio, produzione alimentare, chimica,
   farmaceutica. NON retail, finanza, assicurazioni, media.
S8 Demo fattibile: 3 programmatori in 2,5 ore, con dati pubblici o inventati in modo
   realistico. Indica da dove si prendono i dati (link).
S9 Chiarezza: si spiega in una frase a chi non è del settore, con una storia tipo
   "una persona, un'azione sbagliata, X € persi" raccontabile in 30 secondi.
S10 Qualcuno paga: almeno 3.000 €/anno per cliente, e un solo errore evitato ripaga l'abbonamento.

## COME LAVORARE (ripeti finché un'idea passa tutto)
1. Genera 20 idee candidate in settori industriali diversi, ognuna con la sua storia
   in stile MemoLens.
2. Primo filtro veloce su S6, S7, S9: tieni le 5 migliori.
3. Per le 5 rimaste fai ricerca vera sul web per S1-S5, S8, S10. Apri le pagine,
   non fidarti dei soli snippet.
4. Se nessuna passa tutte le soglie, scrivi perché e torna al punto 1 con 20 idee NUOVE
   in altri settori o con un'altra angolazione. Fai almeno 3 giri prima di arrenderti.
5. Quando una passa, cerca attivamente di smontarla: un giudice severo cosa direbbe?
   Se regge, è la vincitrice.

## REGOLE SUI DATI
- Ogni numero ha un link alla fonte. Distingui: dato verificato / stima di un vendor /
  stima nostra.
- Non inventare numeri, aziende o casi. Se un dato manca, scrivi "non trovato".
- Preferisci fonti europee e italiane (Eurostat, ISTAT, associazioni di settore,
  autorità pubbliche).

## FORMATO DELLA RISPOSTA
A) L'IDEA VINCITRICE, in una pagina:
   1. In una frase: per chi, quale problema, cosa fa.
   2. La storia (30 secondi): persona, azione sbagliata, informazione vecchia usata, euro persi.
   3. Il problema in numeri (con fonti).
   4. Chi paga e quanto.
   5. Mercato: numero di aziende in UE e in Italia, valore annuo (TAM/SAM/SOM, ipotesi scritte).
   6. Concorrenti: tabella (nome, paese, cosa fa, soldi raccolti, cosa gli manca rispetto a noi).
   7. Precedenti reali (con fonti).
   8. Perché adesso.
   9. Tabella delle soglie S1-S10: passa/non passa + prova in una riga.
   10. Demo di 3 minuti, passo per passo.
   11. Dati per la demo (link) e cosa costruire in 2,5 ore, diviso tra 3 persone.
   12. I 3 rischi principali e come rispondere.
B) LE 2 RISERVE: per ciascuna, le stesse voci 1, 2, 6 e 9.
C) LE IDEE SCARTATE: una riga ciascuna, con la soglia che non hanno passato.
```
