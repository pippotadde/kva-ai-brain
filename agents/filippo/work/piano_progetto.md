# Piano del progetto — Cervello allergeni (nome provvisorio, decide Sian)

Versione 14.11 — riscrittura semplice dell'idea del team. Livello di verifica di ogni numero tra [quadre].

## 1. L'idea in una frase
Un'AI che legge tutto quello che arriva in uno stabilimento alimentare (schede dei fornitori, registri di pulizia, procedure, report dei dipendenti, avvisi esterni), lo tiene collegato in un'unica "mappa" dello stabilimento e avvisa il responsabile qualità **prima** che un allergene finisca dove non è dichiarato. Se il rischio c'è già, propone di bloccare subito i lotti coinvolti e fa partire le istruzioni ai lavoratori appena il responsabile approva.

## 2. Il problema
- Gli allergeni non dichiarati sono la **prima causa di richiami alimentari** negli USA: 38,8% dei richiami FDA+USDA nel 2025 [fonte di settore, Statista/FDA-USDA]; nel 2023 sono esplosi per il sesamo, metà di tutti i richiami [food-safety.com, analisi PIRG].
- In UE le notifiche RASFF nel 2024 sono state 5.250, +12% [verificato, Commissione UE].
- Un richiamo costa in media **10 milioni di dollari** di costi diretti, più danno al marchio [studio FMI/GMA, campione di grandi aziende: per le PMI il costo è più basso ma pesa di più sul fatturato].
- **Perché succede:** le informazioni che servono esistono già, ma sono sparse. Il fornitore cambia ricetta e lo scrive in una mail. La procedura di pulizia passa da rev. A a rev. B ma in linea si usa ancora la vecchia. Un macchinario viene spostato vicino a quello delle nocciole. Ognuna di queste cose da sola sembra innocua; nessuno le mette insieme in tempo.
- **E le approvazioni sono lente:** ogni cambiamento sale la catena (capo reparto → qualità → direzione) a mano, con mail e moduli. Nel frattempo si produce.

## 3. La soluzione: cosa fa, passo per passo
1. **Legge tutto, in continuo:** schede tecniche e mail dei fornitori, registri di pulizia (quale macchina, quando, chi), procedure con la loro revisione, report di turno dei dipendenti, avvisi esterni (RASFF, fornitori, clienti).
2. **Tiene una mappa dello stabilimento:** macchine, distanze tra linee, ingredienti, fornitori, lotti, persone, regole. Ogni fatto ha la sua fonte (documento, autore, data). Quando arriva un'informazione nuova, quella vecchia viene marcata come superata, non cancellata.
3. **Incrocia e trova il rischio:** "il nuovo lotto di farina del fornitore X può contenere soia + la linea 2 non è stata pulita dopo il lotto con nocciole + l'etichetta del prodotto B dice senza frutta a guscio → rischio".
4. **Avvisa il manager con il perché:** cosa è successo, quali rischi, quali documenti lo dimostrano, quale regola (Reg. UE 1169/2011, Reg. 2021/382) è in gioco.
5. **Se l'allergene non dichiarato c'è già:** propone il blocco di tutti i lotti prodotti nelle stesse condizioni (stessa linea, stessa materia prima, stessa finestra di tempo), prima che escano.
6. **Approvazione veloce lungo la gerarchia:** il manager approva con un clic; l'AI inoltra al livello successivo solo se serve, e appena approvato manda le istruzioni ai lavoratori ("pulite di nuovo la linea 2", "spostate la stazione di farcitura a distanza X", "più persone sulla pulizia di Y").
7. **Tutto resta registrato:** ogni avviso, decisione, firma e istruzione, rileggibile da un ispettore mesi dopo.

Regola di sicurezza: l'AI **non decide da sola** le azioni rischiose (bloccare o rilasciare un lotto, cambiare un'etichetta). Le propone; una persona firma.

## 4. Perché è efficace
- **Prende il rischio prima, non dopo il richiamo:** il problema nasce dall'unione di informazioni sparse; noi le uniamo nel momento in cui arrivano.
- **Blocca solo ciò che serve:** sapendo quale linea, quale materia prima e quale finestra di tempo, il blocco è mirato. Meno prodotto buttato rispetto a un richiamo largo.
- **Approvazioni in minuti invece che giorni:** il manager riceve il caso già spiegato con le prove; non deve ricostruirlo.
- **Pronto per l'audit:** la traccia di chi ha deciso cosa e su quale documento è già scritta (utile per audit BRCGS/IFS [da verificare con mentor]).

## 5. Cosa ci distingue
| Oggi si usa | Limite | Noi |
|---|---|---|
| Fogli Excel + piano HACCP su carta | Statici, nessuno li incrocia con le mail dei fornitori | Si aggiorna da solo a ogni documento nuovo |
| Software qualità/ERP (gestione documenti, non conformità) | Archiviano i documenti, non li collegano tra loro | Mappa dello stabilimento: collega fornitore → ingrediente → macchina → lotto → etichetta |
| Chatbot generici sui documenti | Rispondono se chiedi, non avvisano; non sanno quale versione è valida | Avvisa da solo, sa cosa è superato, ogni risposta cita la fonte |
| Consulenti esterni / audit annuale | Una foto all'anno | Controllo continuo |

In una frase: gli altri conservano documenti, noi **ricordiamo e colleghiamo** i fatti dello stabilimento — è esattamente il tema "memoria/AI brain per l'industria" della challenge.
⚠ Concorrenti specifici (nomi di software qualità alimentare) da verificare con /8hack prima del pitch.

## 6. Mercato e soldi (ipotesi dichiarate, da mettere nel modello economico)
**Chi compra:** responsabile qualità di stabilimenti alimentari che lavorano più allergeni sulle stesse linee — dolciario, prodotti da forno, co-packer per grandi marchi.

**Quanto costa al cliente:** abbonamento **€800/mese per stabilimento** (€9.600/anno) [ipotesi nostra].
Confronto: un solo richiamo evitato vale molte volte il costo (media $10M per grandi aziende; per una PMI anche solo €100k di prodotto ritirato + danno al cliente [ipotesi]).

**Dimensione (calcolo semplice):**
- Italia: ~56.000 imprese alimentari [Luiss, dato 2019, vecchio]. Ipotizziamo **5.000 stabilimenti** con una funzione qualità e più allergeni in linea [ipotesi da verificare].
  → mercato servibile Italia: 5.000 × €9.600 = **~€48M/anno**.
- Europa: ordine di grandezza 5-6 volte l'Italia [ipotesi] → **€250M+/anno**.
- Obiettivo 3 anni: **150 stabilimenti in Italia → ~€1,4M di ricavi ricorrenti/anno**.

**Come arriviamo ai clienti:** partire dal dolciario (allergeni tipici: frutta a guscio, latte, uova, glutine, soia), attraverso associazioni di settore, consulenti HACCP ed enti di certificazione che già entrano negli stabilimenti.

## 7. Cosa mostriamo oggi nella demo (14:00-16:30)
Stabilimento dolciario finto, dati sintetici dichiarati, una linea a 4 stazioni.
1. Arriva la mail del fornitore: "la nostra farina ora può contenere soia". L'AI aggiorna la mappa e mostra i prodotti toccati.
2. Arriva il registro di pulizia: la linea 2 è stata pulita con la procedura rev. A, ma vale la rev. B → avviso.
3. Un dipendente manda il report di turno → l'AI incrocia tutto e manda al manager: "rischio, ecco perché, ecco le prove".
4. L'AI propone il blocco dei lotti coinvolti; il manager approva; partono le istruzioni ai lavoratori.
5. Un ispettore apre la traccia e vede chi ha deciso cosa, quando e su quale documento.

## 8. Rischi e come li gestiamo
1. Nessuno di noi lavora nell'alimentare → call con mentor food/qualità prima delle 12:30.
2. Idea ampia → in demo solo 1 linea, 3 tipi di documento, 1 catena di approvazione.
3. Numeri di mercato ancora ipotesi → li dichiariamo come tali nel pitch.

## Fonti
- Statista, richiami FDA/USDA: https://www.statista.com/chart/36281/fda-and-usda-food-recalls-in-the-united-states/
- Richiami 2023 per sesamo (PIRG): https://www.food-safety.com/articles/9437-thanks-sesame-us-food-recalls-due-to-undeclared-allergens-skyrocketed-in-2023-causing-half-of-all-food-recalls
- USDA ERS 2004-2013, 27,4% richiami per allergeni: https://www.foodsafetymagazine.com/news/new-usda-report-breaks-down-us-food-recalls-2004-2013/
- Costo richiamo $10M (FMI/GMA): https://www.fooddive.com/news/more-than-money-what-a-recall-truly-costs/426855/
- 56.000 imprese alimentari Italia (Luiss 2019): https://www.ruralhack.org/wp-content/uploads/2019/05/Alimentare-140-miliardi-di-ricavi-«La-politica-non-ci-lasci-soli»-1.pdf
- Reg. UE 1169/2011: https://eur-lex.europa.eu/eli/reg/2011/1169/oj
- Reg. UE 2021/382: https://eur-lex.europa.eu/eli/reg/2021/382/oj/eng
