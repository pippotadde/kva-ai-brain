# START KVA — file da dare al proprio Claude

> **Per la persona (Giorgia o Sian):**
> 1. Serve Claude Code già installato. Su Windows usalo **dentro WSL (Ubuntu)**, non da Windows: apri il terminale Ubuntu.
> 2. Metti questo file nella tua cartella home di Linux (`~`), poi da lì lancia `claude` e scrivi:
>    *"Leggi START_KVA.md, sono <Giorgia|Sian>. Fai tutto tu."*
> 3. Claude ti chiederà solo poche cose: la password del computer (`sudo`), il login GitHub nel browser, eventualmente una chiave API.

---

> **Per Claude:** sei il Claude di una persona del team KVA (Filippo, Giorgia, Sian: 3 studenti PoliTo) che sabato 14.11.2026 partecipa all'hackathon "AI brain for industry" di Kakashi Venture Accelerator, con l'obiettivo di vincere. Parla con la persona in italiano; codice, commenti e commit in inglese. La repo del team è privata e la persona non l'ha ancora sul computer: il tuo compito è portarla dentro e farla partire. Fai tu tutto il lavoro meccanico; chiedi solo quello che solo la persona può fare.

## 1. Strumenti di base

Lavora in Linux (WSL su Windows, oppure Ubuntu), nella home, mai in `/mnt/c/...`.

```bash
git --version; gh --version; uv --version
```

Installa quello che manca:
- `git`: `sudo apt-get update && sudo apt-get install -y git`
- `gh` (GitHub CLI): segui https://github.com/cli/cli/blob/trunk/docs/install_linux.md (repository apt ufficiale)
- `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`, poi riapri la shell o `source ~/.local/bin/env`

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
1. Prima controlla con lei che sia **iscritta e confermata** all'hackathon: le iscrizioni chiudono **venerdì 13.11 alle 12:00**.
2. Leggete insieme `docs/site/metodo.html` ("Scegliere l'idea"). I segnali di KVA completi sono in `research/kva-interests.md`; proposte già pronte in `docs/site/problemi.html`.
3. Aiutala a trovare 2 idee con le 5 strade della pagina, a passarle nel filtro sì/no e a compilare la scheda (chi soffre, chi paga, numero che migliora, cosa cambia nel tempo, momento "wow", dati, perché noi).
4. Salva le 2 schede in `.coord/agents/<nome>/idee.md`, aggiorna `status.md` e fai `bash scripts/coord.sh sync`.
5. **Non scegliere l'idea finale:** si decide insieme in call.

## 7. Alla fine

Riassumi alla persona in 5 righe: cosa è installato, se `check_env.sh` è verde, il canale funziona, cosa resta da fare (2 idee entro venerdì sera).
