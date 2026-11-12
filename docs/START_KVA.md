# START KVA — file da dare al proprio Claude

> **Per la persona (Giorgia o Sian).** Il resto lo fa Claude; tu scegli solo dove farlo lavorare.
>
> **Se usi Windows: consigliamo WSL (Linux dentro Windows), ma non è obbligatorio.** Con WSL gli script del team funzionano senza sorprese e il progetto resta separato dalle tue cose. Se preferisci restare sull'app di Claude Code che usi già, va bene: salta questa parte, apri l'app su una cartella nuova e vuota (non in OneDrive), mettici questo file e scrivi la frase in fondo. Il tuo Claude si adatterà.
>
> **Per usare WSL:** prima controlla se ce l'hai già: apri PowerShell e scrivi `wsl -l -v`.
> - Se compare una riga con **Ubuntu**: ce l'hai già, apri "Ubuntu" dal menu Start e salta al passo successivo.
> - Se dà errore o la lista è vuota: apri PowerShell **come amministratore** (tasto destro → "Esegui come amministratore"), scrivi `wsl --install -d Ubuntu-24.04`, **riavvia il computer**, poi apri "Ubuntu" dal menu Start e scegli un nome utente e una password (servirà come password `sudo`). Ci vogliono circa 10–15 minuti.
> - Se l'installazione si lamenta della "virtualizzazione": va attivata nel BIOS; scrivi nel gruppo e ci guardiamo insieme.
>
> Con WSL, da qui in poi usa il terminale Ubuntu per il progetto.
>
> **Poi (Ubuntu e WSL), nel terminale:**
> ```bash
> sudo apt update && sudo apt install -y curl git
> curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt install -y nodejs
> sudo npm install -g @anthropic-ai/claude-code
> ```
> Se `claude --version` funziona già, salta questi comandi.
>
> **Infine:** salva questo file nella home di Linux (su WSL: copialo da Windows con `cp /mnt/c/Users/<tuo-utente>/Downloads/START_KVA.md ~/`), poi nel terminale scrivi `cd ~ && claude`, fai il login con il tuo account e scrivi:
> *"Leggi START_KVA.md, sono <Giorgia|Sian>. Fai tutto tu."*
>
> Claude ti chiederà solo: la password del computer (`sudo`), il login GitHub nel browser, una chiave API gratuita di Google, e di approvare i comandi che lancia.

---

> **Per Claude:** sei il Claude di una persona del team KVA (Filippo, Giorgia, Sian: 3 studenti PoliTo) che sabato 14.11.2026 partecipa all'hackathon "AI brain for industry" di Kakashi Venture Accelerator, con l'obiettivo di vincere. Parla con la persona in italiano; codice, commenti e commit in inglese. La repo del team è privata e la persona non l'ha ancora sul computer: il tuo compito è portarla dentro e farla partire. Fai tu tutto il lavoro meccanico; chiedi solo quello che solo la persona può fare.

## 0. Rispetta il computer della persona

Lavora solo nella cartella del progetto; non toccare altri file né impostazioni del sistema. Prima di ogni installazione di' in una riga cosa installi e perché. **Non installare WSL** se la persona non l'ha scelto: se lavori su Windows senza WSL (shell Git Bash dell'app), adatta i comandi (per esempio `winget install --id GitHub.cli -e`, `winget install --id astral-sh.uv -e`) e segnala a Filippo nel messaggio finale cosa non funziona. Se serve qualcosa da amministratore, chiedi prima.

## 1. Strumenti di base

Lavora in Linux (WSL su Windows, oppure Ubuntu), nella home, mai in `/mnt/c/...`.

```bash
git --version; gh --version; uv --version; node --version; claude --version
```

Installa quello che manca:
- `git`: `sudo apt-get update && sudo apt-get install -y git`
- `gh` (GitHub CLI): segui https://github.com/cli/cli/blob/trunk/docs/install_linux.md (repository apt ufficiale)
- `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`, poi riapri la shell o `source ~/.local/bin/env`
- `node` 22: `curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt install -y nodejs`
- Comandi completi e alternativi: dopo il clone, `docs/SETUP.md` nella repo.

Quando serve la password `sudo`, chiedila alla persona (o falle lanciare il comando con `! <comando>`).

## 2. Login GitHub

Controlla con `gh auth status`. Se non è loggata, il login è interattivo: chiedi alla persona di scrivere nel prompt

```
! gh auth login --web --git-protocol https
```

e di seguire le istruzioni nel browser. Poi configura git: `gh auth setup-git`, e se mancano `git config --global user.name` / `user.email`, chiedili alla persona.

## 3. Accettare l'invito alla repo

L'invito a `pippotadde/kva-ai-brain` lo accetti tu:

```bash
gh api user/repository_invitations --jq '.[] | select(.repository.full_name=="pippotadde/kva-ai-brain") | .id'
gh api -X PATCH user/repository_invitations/<id>
```

Se non c'è nessun invito: forse è già accettato (prova il passo 4) oppure va chiesto a Filippo; in alternativa la persona apre https://github.com/pippotadde/kva-ai-brain/invitations.

## 4. Scaricare la repo

```bash
gh repo clone pippotadde/kva-ai-brain ~/kva-ai-brain
```

## 5. Da qui in poi segui l'onboarding della repo

Leggi **`~/kva-ai-brain/docs/AI_ONBOARDING.md`** e seguilo in ordine: contesto della gara, preparazione dell'ambiente (`docs/SETUP.md`, `bash scripts/check_env.sh` fino a **0 to fix**), collegamento al canale di coordinamento `.coord/` (`bash scripts/coord.sh init <nome>`), lettura dei messaggi (`bash scripts/coord.sh inbox`). Da quel momento valgono le regole del `CLAUDE.md` della repo.

Nota: le prossime sessioni conviene aprirle direttamente da `~/kva-ai-brain` (lì Claude legge `CLAUDE.md` da solo). Dillo alla persona.

## 6. Il compito di adesso

Entro **venerdì 13.11 sera** la persona porta alla call **2 idee**:
1. Prima controlla con lei che sia **iscritta e confermata** all'hackathon (le iscrizioni chiudono **venerdì 13.11 alle 12:00**) e che sia entrata nella dashboard KVA https://hackathon.kakashi.ventures (obbligatorio entro 7 giorni dalla conferma).
2. Leggete insieme `docs/site/metodo.html` ("Scegliere l'idea"). I segnali di KVA completi sono in `research/kva-interests.md`; proposte già pronte in `docs/site/problemi.html`.
3. Aiutala a trovare 2 idee con le 5 strade della pagina, a passarle nel filtro sì/no e a compilare la scheda (chi soffre, chi paga, numero che migliora, cosa cambia nel tempo, momento "wow", dati, perché noi).
4. Salva le 2 schede in `.coord/agents/<nome>/idee.md`, aggiorna `status.md` e fai `bash scripts/coord.sh sync`.
5. **Non scegliere l'idea finale:** si decide insieme in call.

## 7. Alla fine

Manda a Filippo: `bash scripts/coord.sh msg filippo "Setup completato" "check_env: <risultato>. Canale collegato. Iscrizione: <sì/no>. Prossimo: 2 idee."`
Poi riassumi alla persona in 5 righe: cosa è installato, se `check_env.sh` è verde, se il canale funziona, cosa resta da fare (2 idee entro venerdì sera).
