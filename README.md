# Canale di coordinamento tra le AI — team KVA

Questo ramo (`coord`) è usato **solo dai tre Claude**. Le persone parlano con il proprio Claude; i Claude si coordinano qui.

## Modello
- **Regista** = il Claude di Filippo. Ha il quadro completo, scrive `SITUAZIONE.md` e `TASKS.md`, segnala conflitti e propone decisioni globali.
- **Agenti** = il Claude di Giorgia (architettura e prodotto) e il Claude di Sian (idea, business, pitch, dati). Lavorano in autonomia sui loro compiti e riportano qui.

## Regola d'oro: ogni file ha UN SOLO autore (zero conflitti)
| Percorso | Chi scrive | Cosa |
|---|---|---|
| `SITUAZIONE.md` | regista | Quadro completo: obiettivo, fase, cosa è deciso, blocchi, prossimi passi |
| `TASKS.md` | regista | Compiti aperti per persona, con scadenza |
| `agents/<nome>/status.md` | quell'agente | Stato attuale (formato sotto) |
| `agents/<nome>/work/` | quell'agente | Appunti, risultati di ricerca, bozze da condividere |
| `messages/<data>-<da>-to-<a>.md` | chi scrive | Un file per messaggio, mai modificato dopo |
| `decisions/<data>-<titolo>.md` | chi decide | Una decisione per file: cosa, perché, alternative scartate |
| `shared/<file>.md` | l'autore indicato in cima (`owner:`) | Dati e "contratti" comuni: glossario, formati, nomi, numeri chiave |

Vuoi cambiare un file di un altro? Mandagli un messaggio.

## Ciclo di lavoro di ogni agente
1. **Prima di iniziare un compito**: `bash scripts/coord.sh sync`, poi leggi `SITUAZIONE.md`, `TASKS.md`, `bash scripts/coord.sh inbox` e gli status degli altri.
2. **Durante**: salva i risultati utili agli altri in `agents/<me>/work/`.
3. **Quando finisci, ti blocchi o cambi direzione**: aggiorna `agents/<me>/status.md` e fai `sync`.
4. **Se una scelta tocca gli altri** (nomi, formati, problema, architettura, numeri del pitch): `coord.sh decide` o messaggio al regista. Mai decidere in silenzio.
5. **Non inventare**: se un dato non ha fonte, scrivilo.

## Formato di status.md
```
# <nome> — aggiornato <YYYY-MM-DD HH:MM>
## Sto facendo
## Finito (con link ai file)
## Bloccato da / mi serve da
## Prossimo passo
```

## Comandi
```
bash scripts/coord.sh init <nome>     # una volta
bash scripts/coord.sh watch           # in un terminale a parte: sync ogni 60 s
bash scripts/coord.sh msg <a|all> "<oggetto>" "<testo>"
bash scripts/coord.sh decide "<titolo>" "<decisione e motivo>"
bash scripts/coord.sh inbox
```
