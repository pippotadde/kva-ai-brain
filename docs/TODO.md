# Tutto quello che va fatto prima della gara

Lista completa, in ordine di scadenza. Spuntate qui (commit) o nel gruppo.
**F** = Filippo, **G** = Giorgia, **S** = Sian, **C** = Claude (lo faccio io su richiesta di Filippo).

## Giovedì 12 — stasera

### Organizzazione
- [ ] **F** Condividere la pagina del team (menu Share) e mandare il link nel gruppo
- [ ] **F** Fissare la call di venerdì alle 09:00 (link Meet/Discord nel gruppo)
- [ ] **F** Decidere dove ci troviamo sabato (casa di chi, indirizzo, orario 09:00)
- [ ] **G S** Accettare l'invito GitHub: https://github.com/pippotadde/kva-ai-brain/invitations
- [ ] **F G S** Accedere alla dashboard KVA (il regolamento chiede di farlo entro 7 giorni dalla conferma)

### Ambiente
- [ ] **F G S** Seguire `docs/SETUP.md` → `bash scripts/check_env.sh` con **0 to fix** → screenshot nel gruppo
- [ ] **F G S** Ognuno crea la propria chiave Gemini (così ne abbiamo 3 di riserva)

### Problema
- [ ] **F G S** Leggere `research/problems/candidates.md`, scegliere i propri 2 preferiti con il perché
- [ ] **F** Lanciare 2 Deep Research su Gemini (prompt pronti in `docs/research-prompts.md`), problemi A e D
- [ ] **G** (facoltativo) Stessi prompt su ChatGPT Deep Research, per confrontare le fonti

### Studio
- [ ] **F G S** Corso AI parte 1 (concetti 1–3 della pagina), ~1h30, con un esempio fatto girare

## Venerdì 13

### Mattina
- [ ] **F G S** 09:00 call: scelta problema principale + riserva (si decide sui criteri della giuria)
- [ ] **C** Subito dopo: dossier completo sul problema scelto (mercato, concorrenti, numeri, fonti)
- [ ] **F** Ricerca di mercato + `business/business-plan.md` v0
- [ ] **G** Raccolta dati per la demo + `research/data/README.md` compilato
- [ ] **S** Persona, storia del problema, copione demo v0 in `pitch/pitch-script.md`
- [ ] **S** Proporre 3 nomi per il prodotto (corto, pronunciabile, dice cosa fa)
- [ ] **F G S** Glossario del settore scelto: 20 termini che dobbiamo saper usare
- [ ] **F G S** 11:30 sync di 30 minuti

### Pomeriggio
- [ ] **F G S** Corso AI parte 2 (concetti 4–7)
- [ ] **F G S** 14:00–16:30 test di fattibilità nelle condizioni di sabato (in `prototype/`)
- [ ] **F** 16:30 simulazione verifica finanziaria (gli altri attaccano i numeri)
- [ ] **S** 17:00 simulazione pitch cronometrata
- [ ] **F G S** 17:30 bilancio + architettura definitiva + chi tocca quali file
- [ ] **G** Scrivere l'architettura in `docs/architecture.md` (1 pagina, uno schema)

### Sera
- [ ] **F** Business plan v1 completo, numeri con fonti
- [ ] **S** 3 slide per il checkpoint delle 12:30 + slide del pitch v1 (Google Slides condiviso)
- [ ] **G** Elenco dei prompt e degli schemi che hanno funzionato nel test (`prototype/NOTES.md`)
- [ ] **F G S** Una risposta da 20 secondi a ciascuna domanda probabile della giuria (`docs/jury.md`)
- [ ] **F G S** Decidere cosa scegliere se vinciamo: opzione A (€1.500, si cede il progetto) o B (società, KVA investe per il 15%). La giuria può chiederlo.
- [ ] **F** Controllare email e dashboard KVA: istruzioni per i checkpoint, crediti AI, link della videochiamata
- [ ] **F G S** Caricare il portatile, preparare caricatore, cuffie con microfono, ciabatta
- [ ] **F G S** A letto entro mezzanotte

## Sabato 14 — prima delle 09:30

- [ ] **F G S** 09:00 ritrovo, Wi-Fi + hotspot del telefono provati
- [ ] **F G S** `git pull` e `check_env.sh` verde su tutti i computer
- [ ] **F** Controllare che nella repo non ci siano chiavi, poi renderla pubblica (comando in `docs/PLAN.md`)
- [ ] **F** Aggiungere il file `LICENSE` (proposta: MIT) — il regolamento chiede di scegliere una licenza
- [ ] **F G S** Prova di condivisione schermo e audio nella piattaforma della call KVA
- [ ] **G** Programma per registrare lo schermo pronto (Windows: Win+G; Ubuntu: Ctrl+Alt+Shift+R) per il video di riserva
- [ ] **S** Blocco note pronto per i talk delle 10:15

## Durante la gara

Segue la scaletta della pagina del team. Le consegne obbligatorie:
- [ ] 12:30 materiale del checkpoint (secondo le istruzioni KVA)
- [ ] 16:00 video di riserva della demo registrato
- [ ] Consegna finale: repo pubblica, README con descrizione, come avviarlo e **strumenti AI usati**
