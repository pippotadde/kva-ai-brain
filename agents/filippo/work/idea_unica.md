# Idea unica — proposta (Filippo + Claude, 14.11 ~11:00) — DA CONFERMARE IN CALL

Traccia proposta: **Blackbox agents**. Settore: **stabilimento dolciario, allergeni**.
Nome provvisorio: *Scatola nera degli allergeni* (il nome finale lo decide Sian).

## Da dove viene: le tre idee
| Idea | Di chi | Cosa porta nell'idea unica |
|---|---|---|
| Blackbox agents (traccia KVA) | KVA | Il meccanismo: controllo PRIMA di ogni azione (consentita / serve persona / bloccata), traccia a prova di manomissione, replay, report per l'auditor |
| Cambi produzione sicuri per allergeni (Allergen-safe changeovers) | Giorgia | Il problema reale: il cambio da un prodotto CON nocciole a uno SENZA è il momento in cui nasce la contaminazione |
| MemoLens + linea di produzione | Sian (+ team) | La memoria visibile: quale procedura/ricordo l'agente ha usato, se era ancora valido (revisione superata), vista della linea con passaggi ed errori |

## L'idea in una frase
In uno stabilimento dolciario un agente AI gestisce il cambio linea da un prodotto con nocciole a uno senza nocciole; ogni sua azione passa prima da un controllo sulle regole allergeni, quelle rischiose aspettano la firma del responsabile qualità, quelle vietate vengono bloccate, e tutto finisce in una scatola nera che un ispettore può rileggere mesi dopo.

## Scenario della demo (linea a 4 stazioni, dati sintetici dichiarati)
Linea 2: impasto → farcitura → confezionamento → etichettatura/rilascio. Lotto A = biscotto alla crema di nocciole. Lotto B = biscotto "senza frutta a guscio".
1. ✅ **Consentita** — l'agente legge piano di produzione e procedura di pulizia e ordina la pulizia allergeni + il tampone di verifica.
2. 🟡 **Serve una persona** — tampone negativo: l'agente chiede di avviare il lotto B. Si ferma finché la responsabile qualità firma (nome + ora nella traccia).
3. ⛔ **Bloccata** — in un secondo giro il tampone è positivo (o la pulizia non è registrata) e l'agente prova a rilasciare il lotto B per la spedizione, oppure a togliere "nocciole" dall'etichetta: bloccato, con la regola citata.
4. **Memoria/supersession (Sian)** — l'agente cita la procedura di pulizia rev. A, ma esiste la rev. B: la traccia lo mostra e il controllo blocca.
5. **Replay** — una persona esterna clicca sul passo 3 e risponde da sola "perché?" leggendo input, regola, versione delle regole, firma.
6. **Report per l'ispettore** — generato dalla traccia, non scritto a mano.
7. **Manomissione** — modifichiamo una riga nel database: la verifica degli hash la segnala.

## Fonti pubbliche degli obblighi (richieste dalla traccia)
- Reg. (UE) 1169/2011, art. 9 e 21 + Allegato II: 14 allergeni da dichiarare in etichetta. https://eur-lex.europa.eu/eli/reg/2011/1169/oj
- Reg. (UE) 2021/382 che modifica il Reg. 852/2004: gestione degli allergeni nell'igiene alimentare, riprende Codex CXC 80-2020. https://eur-lex.europa.eu/eli/reg/2021/382/oj/eng
- Codex Alimentarius CXC 80-2020: codice di pratica per la gestione degli allergeni negli operatori alimentari (pulizia, cambi linea, verifica) — da aprire e citare per clausola.
- Reg. (CE) 178/2002, art. 19: ritiro/richiamo e avviso all'autorità — da citare se il lotto è già uscito.
⚠ Il testo esatto degli articoli va letto e citato prima del pitch (ora sono riferimenti da ricerca, non ancora verificati riga per riga).

## Numeri per il pitch (con livello di verifica)
- RASFF 2024: 5.250 notifiche (+12%) [verificato: Commissione UE, via foodsafetynews]. Quota allergeni: non trovata in fonte ufficiale → non usarla.
- "~30% dei richiami alimentari per allergeni non dichiarati" [non verificato: wikifarmer] → NON usare finché non c'è fonte ufficiale.

## Le trappole della traccia e come le evitiamo
| Trappola | Risposta |
|---|---|
| Log non strutturati | Ogni riga: input, contesto recuperato, modello+versione prompt, tool+argomenti, regola+versione, esito, firma |
| Chiedere all'LLM "perché" dopo | Il motivo è la regola che ha deciso, registrata PRIMA dell'azione; il testo dell'LLM è solo commento |
| Controllo dopo l'azione | Il controllo avvolge la funzione: senza esito "consentita" la funzione non parte |
| Settore che nessuno conosce | Fonti pubbliche + call con un mentor (food/qualità) entro 12:30 + 1 persona del settore se la troviamo |

## Architettura minima (Giorgia decide)
Python. Agente LLM con 5 strumenti (leggi piano, leggi procedura, ordina pulizia, avvia lotto, rilascia lotto/modifica etichetta) → ogni chiamata passa dal **controllo regole** (tabella in YAML/Python, versionata) → esito consentita / attesa firma / bloccata → **traccia** in SQLite append-only con hash concatenati → pagina web: linea + passaggi + replay + pulsante firma + report.

## Chi compra (da verificare)
Responsabile qualità di PMI dolciarie e co-packer che producono per grandi marchi e subiscono audit (BRCGS/IFS) [non verificato]. Il prezzo va nel modello economico (Filippo).

## Rischi aperti
1. Nessuno del team conosce l'industria alimentare → mentor + fonti pubbliche.
2. 1 team già iscritto su Blackbox → differenziarci col settore (allergeni) e con la memoria visibile di Sian.
3. Testo delle norme non ancora letto riga per riga.
