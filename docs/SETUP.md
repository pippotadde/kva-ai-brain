# Setup — da fare entro giovedì sera

Obiettivo: alla fine `bash scripts/check_env.sh` deve dire **0 to fix** sul computer di ognuno.
Tempo: 30–45 minuti. Se ti blocchi più di 10 minuti su un passo, scrivi nel gruppo.

## 0. Windows (Sian; Filippo è già a posto)

In PowerShell **come amministratore**:

```powershell
wsl --install -d Ubuntu-24.04
```

Riavvia, apri "Ubuntu" dal menu Start, scegli utente e password. **Da qui in poi si lavora sempre nel terminale Ubuntu**, mai in PowerShell, e i file stanno in `~/` (non in `/mnt/c/...`, che è lentissimo).

Installa VS Code su Windows con l'estensione **WSL**; dal terminale Ubuntu, `code .` apre la cartella.

## 1. Strumenti (Ubuntu / WSL)

```bash
sudo apt update && sudo apt install -y git curl build-essential
# GitHub CLI (versione recente dal repo ufficiale)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install -y gh
# uv (gestisce Python e dipendenze; installa da solo Python 3.12)
curl -LsSf https://astral.sh/uv/install.sh | sh
# Node 22 (serve a Claude Code e a eventuali interfacce web)
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash - && sudo apt install -y nodejs
# Claude Code
npm install -g @anthropic-ai/claude-code
```

Chiudi e riapri il terminale.

## 2. Git e GitHub

```bash
git config --global user.name "Nome Cognome"
git config --global user.email "la-tua-email-di-github"
gh auth login          # GitHub.com -> HTTPS -> login con browser
```

Accetta l'invito alla repo: https://github.com/pippotadde/kva-ai-brain/invitations

```bash
cd ~ && gh repo clone pippotadde/kva-ai-brain && cd kva-ai-brain
```

## 3. Python e dipendenze

```bash
uv sync      # crea .venv con Python 3.12 e installa tutto
```

Per eseguire codice: `uv run python file.py` oppure `uv run streamlit run app.py`.
Per aggiungere una libreria: `uv add nome` (poi commit di `pyproject.toml` e `uv.lock`).

## 4. Chiave API (per il prodotto)

1. Vai su https://aistudio.google.com/apikey e crea una chiave (gratis).
2. `cp .env.example .env` e incolla la chiave dopo `GEMINI_API_KEY=`.
3. **Mai** copiare la chiave in un file diverso da `.env`, mai in chat pubbliche, mai in un commit.

## 5. Claude Code

```bash
claude        # al primo avvio fai login con il tuo account Pro
```

Dentro la repo Claude legge da solo `CLAUDE.md` con le regole del team.

## 6. Verifica finale

```bash
bash scripts/check_env.sh
```

Manda nel gruppo lo screenshot con **0 to fix**.
