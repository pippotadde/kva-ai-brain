# Piano operativo — da giovedì 12 a sabato 14 novembre

**Obiettivo: vincere.** Ogni attività qui sotto esiste perché alza un criterio della giuria. Se un'attività non lo fa, si taglia.

## 1. Strategia: dove si vince

| Criterio (peso) | Cosa ci fa vincere | Quando si prepara |
|---|---|---|
| Tema (25%, decide i pareggi) | Memoria con regole che si sostituiscono + ontologia con inferenza visibili **nella demo**, non solo a parole | Ven: test di fattibilità |
| Tecnica (25%) | Pochissime funzioni, ma che funzionano dal vivo senza errori; dati veri | Ven: test; Sab: freeze alle 16:00 |
| Problema reale (25%) | Un settore preciso, una persona precisa, un numero con fonte | Gio–Ven: ricerca |
| Business (20%) | Cliente che paga, prezzo, mercato con fonti, "perché ora" | Ven: bozza; Sab: definitivo |
| Demo (5%) | Copione provato 3 volte, video di riserva | Ven sera + Sab 16:00 |

**Chi giudica** (vedi `docs/jury.md`): KVA è un venture studio AI che investe in startup e fa consulenza per aziende tramite il Gruppo Excellence (banche, assicurazioni, grandi aziende). Ragionano da investitori: vogliono vedere **un'azienda possibile**, non solo un bel progetto tecnico.

**Come ci distinguiamo:** la maggior parte delle squadre farà "chatbot sui documenti" (RAG). Noi facciamo vedere che il sistema **sa quando una regola non vale più, ragiona sulle relazioni e spiega perché**, in un settore preciso con numeri veri.

## 2. Giovedì 12 — sera

| Chi | Cosa | Fatto quando |
|---|---|---|
| Filippo | Condivide la pagina del team e questo piano nel gruppo | Giorgia e Sian li aprono |
| Tutti | Accettano l'invito GitHub e completano `docs/SETUP.md` | `check_env.sh` → 0 to fix, screenshot nel gruppo |
| Tutti | Leggono `research/problems/candidates.md` e scelgono i loro 2 preferiti, con il perché | Voto pronto per domani |
| Tutti | Corso AI, parte 1 (concetti 1–3 della pagina, ~1h30) | Ognuno ha fatto girare una chiamata LLM con risposta in JSON |
| Claude | Modelli di business plan, pitch, registro dati; note sulla giuria | File nella repo |

## 3. Venerdì 13

| Ora | Filippo | Giorgia | Sian |
|---|---|---|---|
| 09:00–09:30 | **Call: scelta del problema** principale + riserva (Sian conduce, voto sui criteri) | ← | ← |
| 09:30–11:30 | Mercato e bozza business plan (`business/`) | Raccolta e analisi dati (`research/data/`) | Storia del problema, persona, copione demo v0 (`pitch/`) |
| 11:30–12:00 | **Sync**: ognuno mostra cosa ha, si decide cosa mostrare nella demo | ← | ← |
| 12:00–14:00 | Pausa + corso AI parte 2 (concetti 4–7) | ← | ← |
| 14:00–16:30 | **Test di fattibilità nelle condizioni di sabato** (2h30, stessi ruoli). Filippo: tempi, integrazione, prova il flusso | Cuore tecnico: estrazione ontologia, memoria con versioni | Interfaccia demo e grafo |
| 16:30–17:00 | Simulazione verifica finanziaria (Filippo presenta i numeri, gli altri attaccano) | ← | ← |
| 17:00–17:30 | Simulazione pitch 3 minuti (Sian), cronometrato | ← | ← |
| 17:30–18:00 | **Bilancio**: cosa ha funzionato, cosa cambiare. Architettura definitiva e divisione dei file | ← | ← |
| Sera | Business plan v1, 3 slide del checkpoint | Elenco dei prompt e degli schemi che funzionano | Slide del pitch v1 |
| | **A letto presto.** Domani si vince con la testa lucida. | | |

### Pronti per sabato se venerdì sera:

- [ ] Problema principale e riserva scelti, con fonti
- [ ] Business plan v1 con cliente, prezzo, mercato, concorrenti
- [ ] Dati della demo nella repo, con fonte e licenza
- [ ] Il test di fattibilità ha dimostrato che la parte difficile funziona (o abbiamo cambiato approccio)
- [ ] Architettura decisa, ogni persona sa quali file tocca
- [ ] Copione demo + 3 slide checkpoint + slide pitch v1
- [ ] Tutti con `check_env.sh` verde

**Regola sul codice:** il prototipo di venerdì resta in `prototype/` ed è usa e getta. Sabato il prodotto si scrive da zero in `src/`; quello che ci portiamo dietro sono le conoscenze, i prompt e i dati. È quello che il regolamento chiede.

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
