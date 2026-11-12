# Piano operativo — da giovedì 12 a sabato 14 novembre

**Obiettivo: vincere.** Ogni attività qui sotto esiste perché alza un criterio della giuria. Se un'attività non lo fa, si taglia.

## 1. Strategia: dove si vince

| Criterio (peso) | Cosa ci fa vincere | Quando si prepara |
|---|---|---|
| Tema (25%, decide i pareggi) | Memoria con regole che si sostituiscono + ontologia con inferenza visibili **nella demo**, non solo a parole | Ven: test di fattibilità |
| Tecnica (25%) | Pochissime funzioni, ma che funzionano dal vivo senza errori; dati veri | Ven: test; Sab: freeze alle 16:00 |
| Problema reale (25%) | Un settore preciso, una persona vera sentita, un numero con fonte | Gio–Ven: ricerca |
| Business (20%) | Cliente che paga, prezzo, mercato con fonti, "perché ora" (Filippo) | Ven: bozza; Sab: definitivo |
| Demo (5%) | Nome che si ricorda, copione provato 3 volte, video di riserva | Ven sera + Sab 16:00 |

**Chi giudica** (vedi `docs/jury.md`): KVA è un venture studio AI che investe in startup e fa consulenza per aziende tramite il Gruppo Excellence (banche, assicurazioni, grandi aziende). Ragionano da investitori: vogliono vedere **un'azienda possibile**, non solo un bel progetto tecnico.

**Come ci distinguiamo:** la maggior parte delle squadre farà "chatbot sui documenti" (RAG). Noi facciamo vedere che il sistema **sa quando una regola non vale più, ragiona sulle relazioni e spiega perché**, in un settore preciso con numeri veri.

## 2. Fino a sabato: passi in ordine, senza orari

Siamo studenti e prima di sabato non abbiamo orari fissi: ognuno avanza quando può, nell'ordine giusto. La lista è in `docs/site/generale.html` (sezione "Cosa fare entro sabato, in ordine") e, per le AI, in `docs/AI_ONBOARDING.md` sezione 7.

### Pronti per sabato se:

- [ ] Problema principale e riserva scelti, con fonti
- [ ] Almeno una persona del settore sentita (o una citazione vera)
- [ ] Business plan v1 con cliente, prezzo, mercato, concorrenti
- [ ] Dati della demo nella repo, con fonte e licenza
- [ ] Il test ha dimostrato che la parte difficile funziona (o abbiamo cambiato approccio)
- [ ] Architettura decisa, ogni persona sa quali file tocca
- [ ] Nome del prodotto, copione demo, 3 slide checkpoint, slide pitch v1, pitch provato 2 volte
- [ ] Tutti con `check_env.sh` verde e canale AI collegato

**Regola sul codice:** il prototipo resta in `prototype/` ed è usa e getta. Sabato il prodotto si scrive da zero in `src/`; ci portiamo dietro conoscenze, prompt e dati.

## 4. Sabato 14

La scaletta minuto per minuto è in `docs/site/generale.html`. In più:

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
