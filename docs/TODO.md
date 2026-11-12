# Tutto quello che va fatto prima della gara

Passi in ordine, senza orari: ognuno avanza quando può. **F** = Filippo (organizzazione), **G** = Giorgia (architettura e prodotto), **S** = Sian (idea, business, pitch, dati).
La versione per le persone è in `docs/site/generale.html`; quella per le AI in `docs/AI_ONBOARDING.md`.

## Subito (Filippo)
- [ ] **F** Condividere il link delle pagine (menu Share) e mandare nel gruppo: link, invito GitHub, frase per il proprio Claude
- [ ] **F** Creare la chiave Gemini e il file `.env`
- [ ] **F** Lanciare 2 Deep Research su Gemini (`docs/research-prompts.md`), problemi A e D

## 1. Preparare il computer
- [ ] **G S** Accettare l'invito GitHub: https://github.com/pippotadde/kva-ai-brain/invitations
- [ ] **G S** Far leggere `docs/AI_ONBOARDING.md` al proprio Claude: setup + canale AI
- [ ] **F G S** `bash scripts/check_env.sh` → **0 to fix**
- [ ] **F G S** Accedere alla dashboard KVA (obbligatorio entro 7 giorni dalla conferma)

## 2. Opinione sui problemi
- [ ] **F G S** Leggere `docs/site/problemi.html`, scrivere i 2 preferiti e perché (`.coord/agents/<nome>/work/opinione-problemi.md`)

## 3. Lettura serale
- [ ] **F G S** `docs/site/lettura.html`, con l'esercizio sul codice d'esempio

## 4. Approfondire i 2–3 candidati più votati
- [ ] **G** Test veloci di fattibilità → `prototype/<lettera>/NOTES.md`
- [ ] **S** Cliente, mercato, concorrenti → `.coord/agents/sian/work/<lettera>-business.md`
- [ ] **F** Deep Research verificate, dati disponibili, tabella di sintesi in `.coord/SITUAZIONE.md`
- [ ] **G** (facoltativo) Deep Research su ChatGPT per confronto

## 5. Sentire una persona del settore
- [ ] **chi riesce** 10 minuti al telefono con chi lavora nel settore (conoscenti, professori, LinkedIn)

## 6. Scegliere
- [ ] **F G S** Problema principale + riserva, votando sui criteri della giuria (call breve o chat)
- [ ] **F** Registrarla: `coord.sh decide`

## 7. Preparare il problema scelto
- [ ] **S** `business/business-plan.md` v1 con fonti; storia del problema; 3 nomi per il prodotto
- [ ] **G** Test di fattibilità serio
- [ ] **F** Dati della demo raccolti e registrati in `research/data/README.md`
- [ ] **S** Glossario del settore: 20 termini in `.coord/shared/glossario.md`

## 8. Architettura
- [ ] **G** `docs/architecture.md`: com'è fatto il prodotto e chi tocca quali file sabato

## 9. Pitch
- [ ] **S** 3 slide per le 12:30, slide e copione del pitch (`pitch/pitch-script.md`)
- [ ] **F G S** 2 prove cronometrate, anche in call
- [ ] **F G S** Una risposta da 20 secondi per ogni domanda probabile (`docs/jury.md`)
- [ ] **F G S** Opzione del premio se vinciamo: A (€1.500, si cede il progetto) o B (società, KVA investe per il 15%)

## 10. Logistica
- [ ] **F** Controllare email e dashboard KVA: istruzioni consegne, crediti AI, link della call
- [ ] **F G S** Confermare il ritrovo da Giorgia alle 09:00
- [ ] **F G S** Portatile carico, caricatore, cuffie con microfono, ciabatta. Dormire.

## Sabato
Scaletta minuto per minuto in `docs/site/generale.html`. Le cose da non dimenticare:
- [ ] **F** Prima delle 09:30: controllo chiavi, repo pubblica, file `LICENSE` (proposta: MIT)
- [ ] **F G S** Un solo computer con l'audio nella call KVA
- [ ] 12:30 consegna del checkpoint
- [ ] 16:00 stop funzioni nuove, video di riserva registrato
- [ ] Consegna finale: repo pubblica, README con descrizione, come avviarlo e **strumenti AI usati**
