# Tutto quello che va fatto prima della gara

Passi in ordine, senza orari: ognuno avanza quando può. **F** = Filippo (organizzazione e business), **G** = Giorgia (architettura e prodotto), **S** = Sian (idea, pitch, dati).
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

## 2. Due idee a testa (entro venerdì sera)
- [ ] **F G S** Iscrizione all'hackathon confermata (chiude **ven 13.11 ore 12:00**)
- [ ] **F G S** Leggere `docs/site/metodo.html` ("Scegliere l'idea") e portare **2 idee** con la scheda compilata (`.coord/agents/<nome>/idee.md`)

## 3. Lettura serale
- [ ] **F G S** `docs/site/lettura.html`, con l'esercizio sul codice d'esempio

## 4. Scegliere (call venerdì sera)
- [ ] **F G S** Voto delle 6 idee e scelta di principale + riserva (`coord.sh decide`)

## 5. Dopo la scelta (venerdì sera e notte)
- [ ] **F G S** Dati realistici con i tre casi della demo, mappa del settore, prova in `prototype/`
- [ ] **F** Business: cliente, mercato, concorrenti, numeri con fonte
- [ ] **S** Storia da 30 secondi e scheletro del pitch
- [ ] **F** (facoltativo) Lavoro notturno di Claude su un ramo separato, rapporto letto sabato prima delle 9:30
- [ ] **F** Registrarla: `coord.sh decide`

Facoltativo: sentire una persona del settore scelto.

## Dopo la scelta
Da definire insieme (dati, business plan, architettura, pitch, logistica): verranno scritti in `.coord/TASKS.md`.

## Sabato
Scaletta di sabato in `docs/site/generale.html`. Le cose da non dimenticare:
- [ ] **F** Prima delle 09:30: controllo chiavi, repo pubblica, file `LICENSE` (proposta: MIT)
- [ ] **F G S** Un solo computer con l'audio nella call KVA
- [ ] 12:30 consegna del checkpoint
- [ ] 16:00 stop funzioni nuove, video di riserva registrato
- [ ] Consegna finale: repo pubblica, README con descrizione, come avviarlo e **strumenti AI usati**
