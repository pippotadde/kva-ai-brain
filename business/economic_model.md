# Modello economico — Cervello allergeni (bozza)

14.11.2026 · Giorgia (con Claude) · Bozza da rivedere con Filippo.

Ogni numero porta un'etichetta: **[verificato: fonte]**, **[stima del team]** (lo decidiamo noi) o **[da verificare]**. Lo stesso modello è salvato su Control8 con `update_economic_model`: la giuria legge quello, non questo file. Se cambiate un numero qui, va cambiato anche lì (e nel pitch).

## Cosa vendiamo

Un abbonamento mensile per stabilimento. Compra il direttore di stabilimento o il responsabile qualità, soprattutto nei co-packer che producono per i marchi della GDO.

| Piano | Prezzo | Cosa include | Etichetta |
| --- | --- | --- | --- |
| Pilota | 0 € per 60 giorni | 1 linea, 1 agente | [stima del team] |
| Stabilimento | 390 €/mese | Tutte le linee, lotti colpiti, registro per audit, 12 mesi di storico | [stima del team] |
| Gruppo | da 1.500 €/mese | Più stabilimenti, installazione presso il cliente, collegamento a MES ed ERP | [stima del team] |

## Costo per servire un cliente (piano Stabilimento)

| Voce | €/mese | Ipotesi |
| --- | --- | --- |
| Modello AI (Claude Haiku 5.5 via gateway KVA, il modello di `scripts/smoke_llm.py`) | ~25 | 20 documenti al giorno per stabilimento (schede fornitori, note di turno, registri di pulizia), circa 5.000 token in ingresso e 1.000 in uscita ciascuno: circa 3,6 M token al mese. **[da verificare]**: va moltiplicato per il listino del modello usato oggi |
| Server, database, storage | ~10 | Un'istanza condivisa ogni 10-20 clienti [stima del team] |
| Supporto | ~5 | Assistenza via mail [stima del team] |
| **Totale** | **~40** | [stima del team] |

Margine lordo: (390 − 40) / 390 ≈ **90%** [stima del team].

## Come arrivano i clienti

| Canale | Costo per contatto | Contatti che diventano clienti | Contatti nel 1° anno | Clienti | Etichetta |
| --- | --- | --- | --- | --- | --- |
| Consulenti HACCP e certificatori (BRCGS, IFS) | 234 € | 25% | 32 | 8 | [stima del team]. Il costo è la commissione del 20% sul primo anno (936 €) divisa per 4 contatti per cliente |
| Contatto diretto dei fondatori (LinkedIn, fiere, telefono) | 50 € | 5% | 40 | 2 | [stima del team] |

- CAC medio: (32 × 234 + 40 × 50) / 10 ≈ **949 €** [stima del team].
- Rientro del CAC: 949 € / 350 € di margine al mese ≈ **2,7 mesi** [stima del team].
- Budget pubblicitario: 0 €. Niente pubblicità a pagamento il primo anno.
- Squadra commerciale: i 3 fondatori, part-time e non pagati nel 1° anno.

## Scenario a 3 anni (ricavi annui a fine anno, stima del team)

| | Anno 1 | Anno 2 | Anno 3 |
| --- | --- | --- | --- |
| Stabilimenti (piano Stabilimento) | 10 | 50 | 150 |
| Clienti Gruppo | 1 | 3 | 8 |
| Ricavi annui | 64.800 € | 288.000 € | 846.000 € |
| Costo per servire (40 €/mese per stabilimento) | 4.800 € | 24.000 € | 72.000 € |
| Commissioni consulenti (936 € per nuovo stabilimento) | 9.400 € | 37.400 € | 93.600 € |
| Fondatori (3 a tempo pieno dal 2° anno, 4.000 €/mese ciascuno) | 0 € | 144.000 € | 144.000 € |
| Strumenti, viaggi, fiere | 6.000 € | 12.000 € | 24.000 € |
| **Risultato** | **+44.600 €** | **+70.600 €** | **+512.400 €** |

Il risultato è positivo dal 1° anno solo perché i fondatori non si pagano. Con gli stipendi, l'equilibrio arriva nel 2° anno con circa 35-40 stabilimenti. I ricavi sono il ritmo a fine anno, non la media dell'anno: il primo anno reale sarà più basso.

Verifica del mercato: 150 stabilimenti al 3° anno sono il 5-7% dei 2.000-3.000 stabilimenti italiani con linee condivise tra prodotti con e senza allergeni. Questo bacino è **[da verificare]**: è una stima del team su 60.000 imprese alimentari italiane ([Federalimentare-Censis via Italpress](https://www.italpress.com/per-lindustria-del-food-italiano-179-mld-di-fatturato-annuo/)).

## Ritorno per il cliente

- Il piano Stabilimento costa 4.680 €/anno.
- Un richiamo costa in media 10 milioni di dollari di soli costi diretti [verificato: [New Food Magazine](https://newfoodmagazine.com/?p=247701)].
- Nel 2023 il 49,2% dei richiami alimentari USA era dovuto ad allergeni non dichiarati [verificato: [PIRG via Food Safety Magazine](https://www.food-safety.com/articles/9437-thanks-sesame-us-food-recalls-due-to-undeclared-allergens-skyrocketed-in-2023-causing-half-of-all-food-recalls)]. Per il 2025 circola il 38,8% sui richiami FDA e USDA (Statista) **[da verificare]**: manca ancora il link.
- L'abbonamento annuo vale lo 0,05% di un richiamo. Basta evitarne uno ogni circa 2.000 anni-stabilimento per ripagarlo.

## Cosa resta da fare prima delle 16:45

1. Il costo del modello AI: prezzo di Claude Haiku 5.5 per milione di token sul gateway, moltiplicato per 3,6 M token.
2. Il link Statista del 38,8%, oppure lo togliamo.
3. Prezzo e volumi qui sopra devono coincidere con quelli del pitch.
4. Una conferma da un consulente HACCP sulla commissione del 20%: è il numero su cui regge il CAC.
