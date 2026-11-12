# Tutto quello che va fatto prima della gara

Lista completa, in ordine di scadenza. **F** = Filippo (regia, tutto), **G** = Giorgia (architettura e prodotto), **S** = Sian (idea, business, pitch, dati), **C** = il Claude di Filippo (regista).
Il dettaglio ora per ora è in `docs/PLAN.md`; il contesto completo per le AI in `docs/AI_ONBOARDING.md`.

## Giovedì 12 — stasera: preparazione

### Organizzazione
- [ ] **F** Condividere la pagina del team (menu Share) e mandare nel gruppo: link pagina, invito GitHub, istruzione "fate leggere `docs/AI_ONBOARDING.md` al vostro Claude"
- [ ] **F** Fissare la call di venerdì alle 09:00 (link nel gruppo)
- [ ] **F** Decidere dove ci troviamo sabato (casa di chi, indirizzo, ore 09:00)
- [ ] **G S** Accettare l'invito GitHub: https://github.com/pippotadde/kva-ai-brain/invitations
- [ ] **F G S** Accedere alla dashboard KVA (obbligatorio entro 7 giorni dalla conferma)

### Ambiente e canale AI
- [ ] **G S** Clonare la repo e far leggere `docs/AI_ONBOARDING.md` al proprio Claude: setup completo + `coord.sh init <nome>`
- [ ] **F G S** `bash scripts/check_env.sh` → **0 to fix**, screenshot nel gruppo
- [ ] **F G S** Ognuno crea la propria chiave Gemini (3 chiavi = riserva)

### Problemi
- [ ] **F G S** Leggere `research/problems/candidates.md`, scrivere la propria opinione (2 preferiti e perché) in `.coord/agents/<nome>/work/opinione-problemi.md`
- [ ] **F** Lanciare 2 Deep Research su Gemini (prompt in `docs/research-prompts.md`), problemi A e D
- [ ] **G** (facoltativo) Stessi prompt su ChatGPT Deep Research, per confrontare

### Studio
- [ ] **F G S** PDF di teoria serale (AI, industria, business: parole chiave e concetti) — in arrivo in `docs/`

## Venerdì 13 — capire, provare, decidere

### Mattina (09:00–12:30)
- [ ] **F G S** 09:00 call di avvio: opinioni a confronto, si tengono 2–3 candidati
- [ ] **G** Test di fattibilità di 30 minuti per candidato → `prototype/<lettera>/NOTES.md`
- [ ] **S** Mercato, cliente, concorrenti per candidato → `.coord/agents/sian/work/<lettera>-business.md`
- [ ] **S** Trovare **una persona del settore** da sentire 10 minuti (contatti, professori PoliTo, LinkedIn)
- [ ] **F** Dati disponibili per candidato + tabella di sintesi per la decisione
- [ ] **C** Dossier completo sui candidati con le Deep Research verificate

### Decisione (13:30–14:00, limite fisso)
- [ ] **F G S** Problema principale + riserva, votando sui 5 criteri della giuria. Senza accordo decide Filippo
- [ ] **F** Registrare la decisione: `coord.sh decide`

### Pomeriggio
- [ ] **G** Test di fattibilità serio sul problema scelto
- [ ] **S** `business/business-plan.md` v1 con fonti; storia del problema; copione demo v0; 3 nomi per il prodotto
- [ ] **F** Dati della demo raccolti e registrati in `research/data/README.md`; prova del flusso completo
- [ ] **F G S** Glossario del settore: 20 termini in `.coord/shared/glossario.md` (owner Sian)
- [ ] **F G S** 17:00 simulazione verifica finanziaria (gli altri attaccano i numeri)
- [ ] **F G S** 17:30 architettura definitiva e divisione dei file → `docs/architecture.md` (owner Giorgia)

### Sera
- [ ] **S** 3 slide checkpoint 12:30 + slide pitch v1 (Google Slides condiviso)
- [ ] **F G S** **2 prove del pitch** cronometrate
- [ ] **F G S** Una risposta da 20 secondi per ogni domanda probabile (`docs/jury.md`)
- [ ] **F G S** Opzione del premio in caso di vittoria: A (€1.500, si cede il progetto) o B (società, KVA investe per il 15%)
- [ ] **F** Controllare email e dashboard KVA: istruzioni checkpoint, crediti AI, link della call
- [ ] **F G S** Caricare portatili, preparare caricatore, cuffie con microfono, ciabatta
- [ ] **F G S** A letto entro mezzanotte

## Sabato 14 — prima delle 09:30

- [ ] **F G S** 09:00 ritrovo, Wi-Fi + hotspot del telefono provati
- [ ] **F G S** `git pull`, `check_env.sh` verde, `coord.sh watch` acceso su tutti i computer
- [ ] **F** Controllare che non ci siano chiavi nella repo, poi renderla pubblica (comando in `docs/PLAN.md`)
- [ ] **F** Aggiungere il file `LICENSE` (proposta: MIT)
- [ ] **F G S** Prova di condivisione schermo e audio nella call KVA
- [ ] **G** Registratore dello schermo pronto per il video di riserva (Windows: Win+G; Ubuntu: Ctrl+Alt+Shift+R)
- [ ] **S** Blocco note pronto per i talk delle 10:15

## Durante la gara
- [ ] 12:30 materiale del checkpoint (secondo le istruzioni KVA)
- [ ] 16:00 stop funzioni nuove, video di riserva registrato
- [ ] 1 prova del pitch prima delle 17:00
- [ ] Consegna finale: repo pubblica, README con descrizione, come avviarlo e **strumenti AI usati**
