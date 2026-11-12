# Piano operativo — da giovedì 12 a sabato 14 novembre

**Obiettivo: vincere.** Ogni attività qui sotto esiste perché alza un criterio della giuria. Se un'attività non lo fa, si taglia.

## 1. Strategia: dove si vince

| Criterio (peso) | Cosa ci fa vincere | Quando si prepara |
|---|---|---|
| Tema (25%, decide i pareggi) | Memoria con regole che si sostituiscono + ontologia con inferenza visibili **nella demo**, non solo a parole | Ven: test di fattibilità |
| Tecnica (25%) | Pochissime funzioni, ma che funzionano dal vivo senza errori; dati veri | Ven: test; Sab: freeze alle 16:00 |
| Problema reale (25%) | Un settore preciso, una persona vera sentita, un numero con fonte | Gio–Ven: ricerca |
| Business (20%) | Cliente che paga, prezzo, mercato con fonti, "perché ora" (Sian) | Ven: bozza; Sab: definitivo |
| Demo (5%) | Nome che si ricorda, copione provato 3 volte, video di riserva | Ven sera + Sab 16:00 |

**Chi giudica** (vedi `docs/jury.md`): KVA è un venture studio AI che investe in startup e fa consulenza per aziende tramite il Gruppo Excellence (banche, assicurazioni, grandi aziende). Ragionano da investitori: vogliono vedere **un'azienda possibile**, non solo un bel progetto tecnico.

**Come ci distinguiamo:** la maggior parte delle squadre farà "chatbot sui documenti" (RAG). Noi facciamo vedere che il sistema **sa quando una regola non vale più, ragiona sulle relazioni e spiega perché**, in un settore preciso con numeri veri.

## 2. Giovedì 12 — sera: preparazione

| Chi | Cosa | Fatto quando |
|---|---|---|
| Filippo | Condivide pagina, piano, `docs/AI_ONBOARDING.md` nel gruppo | Giorgia e Sian li aprono |
| Giorgia, Sian | Aprono Claude Code nella repo e gli fanno leggere `docs/AI_ONBOARDING.md`: setup + canale AI | `check_env.sh` → 0 to fix, status nel canale |
| Tutti | Leggono la rosa dei problemi, scrivono la propria opinione | File in `.coord/agents/<nome>/work/opinione-problemi.md` |
| Tutti | Studio serale con il PDF di teoria | — |
| Filippo | Lancia le Deep Research su A e D | Report in `research/market/` |

## 3. Venerdì 13 — capire, provare, decidere

| Ora | Filippo (regia) | Giorgia (architettura e prodotto) | Sian (idea, business, pitch, dati) |
|---|---|---|---|
| 09:00–09:20 | **Call di avvio:** opinioni a confronto, si tengono 2–3 candidati | ← | ← |
| 09:20–12:30 | Dati disponibili per ogni candidato; sintesi per la decisione | Test di fattibilità di 30 min per candidato (`prototype/`) | Mercato, cliente, concorrenti per candidato; **trovare una persona del settore da sentire** |
| 12:30–13:30 | Pausa | ← | ← |
| 13:30–14:00 | **DECISIONE con limite fisso:** principale + riserva, voto sui 5 criteri. Senza accordo decide Filippo | ← | ← |
| 14:00–17:00 | Integrazione, dati, regia; prova del flusso completo | Test di fattibilità serio sul problema scelto | Business plan v1, storia, copione demo, 3 nomi per il prodotto |
| 17:00–17:30 | Simulazione verifica finanziaria (gli altri attaccano i numeri) | ← | ← |
| 17:30–18:30 | **Architettura definitiva e divisione dei file**; bilancio | Guida | ← |
| Sera | Organizzazione di sabato, controllo istruzioni KVA | Note sui prompt e schemi che funzionano | Slide checkpoint + pitch v1; **2 prove del pitch** cronometrate |
| | **A letto entro mezzanotte.** | | |

### Pronti per sabato se venerdì sera:

- [ ] Problema principale e riserva scelti, con fonti
- [ ] Almeno una persona del settore sentita (o una citazione vera)
- [ ] Business plan v1 con cliente, prezzo, mercato, concorrenti
- [ ] Dati della demo nella repo, con fonte e licenza
- [ ] Il test ha dimostrato che la parte difficile funziona (o abbiamo cambiato approccio)
- [ ] Architettura decisa, ogni persona sa quali file tocca
- [ ] Nome del prodotto, copione demo, 3 slide checkpoint, slide pitch v1, pitch provato 2 volte
- [ ] Tutti con `check_env.sh` verde e canale AI collegato

**Regola sul codice:** il prototipo di venerdì resta in `prototype/` ed è usa e getta. Sabato il prodotto si scrive da zero in `src/`; ci portiamo dietro conoscenze, prompt e dati. È quello che il regolamento chiede.

## 4. Sabato 14

La scaletta minuto per minuto è nella pagina del team (sezione "Scaletta di sabato"). In più:

- **09:00** Filippo rende pubblica la repo: `gh repo edit pippotadde/kva-ai-brain --visibility public --accept-visibility-change-consequences`. Prima controlla che non ci siano chiavi: `git log -p | grep -iE "api_key|sk-|AIza"` deve essere vuoto.
- **10:15** durante i talk: annotare parole e esempi usati dai giurati e riusarli nel pitch.
- **16:00** stop alle funzioni nuove, si registra il video di riserva della demo.
- **Consegna:** README aggiornato con descrizione, come si avvia e **strumenti AI usati** (obbligatorio, §7).

## 5. Rischi e piano B

| Rischio | Piano B |
|---|---|
| Internet cade | Hotspot del telefono già provato; demo che gira in locale |
| Chiave API finita o bloccata | Seconda chiave (Gemini di un altro membro, o crediti KVA) già in `.env` di riserva |
| Limiti di Claude Code Pro | Usarlo con parsimonia venerdì; sabato riserva su Gemini Pro e ChatGPT Pro |
| La demo dal vivo si rompe | Video di riserva registrato alle 16:00 |
| Al talk emerge che il nostro problema non interessa | Problema di riserva già studiato |
| Conflitti Git all'ultimo | Ognuno sui suoi file; push ogni 20–30 minuti; `main` sempre funzionante |
| Discussione che si blocca | Dopo 5 minuti decide il responsabile dell'area |

## 6. Cosa resta da scoprire

- Quali crediti AI darà KVA e su quali modelli.
- Cosa va consegnato ai checkpoint (istruzioni KVA in arrivo, controllare email e dashboard).
- Nomi e profili esatti dei giurati: Filippo controlla su LinkedIn.
