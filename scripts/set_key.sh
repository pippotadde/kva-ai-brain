#!/usr/bin/env bash
# Store an API key in .env without echoing it or leaving it in shell history.
#
#   bash scripts/set_key.sh                      # ANTHROPIC_API_KEY (default)
#   bash scripts/set_key.sh GEMINI_API_KEY
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
ENV="$ROOT/.env"
NAME="${1:-ANTHROPIC_API_KEY}"

[ -f "$ENV" ] || cp "$ROOT/.env.example" "$ENV"
git -C "$ROOT" check-ignore -q .env || { echo "ERRORE: .env non è in .gitignore, mi fermo."; exit 1; }

read -rsp "Incolla $NAME (non verrà mostrata) e premi Invio: " KEY; echo
KEY="$(printf '%s' "$KEY" | tr -d '[:space:]')"
[ -n "$KEY" ] || { echo "Chiave vuota, niente salvato."; exit 1; }

# Value passed via environment, not argv, so it never shows up in `ps`.
KEY="$KEY" NAME="$NAME" awk '
  BEGIN { done = 0 }
  $0 ~ "^" ENVIRON["NAME"] "=" { print ENVIRON["NAME"] "=" ENVIRON["KEY"]; done = 1; next }
  { print }
  END { if (!done) print ENVIRON["NAME"] "=" ENVIRON["KEY"] }
' "$ENV" > "$ENV.tmp" && mv "$ENV.tmp" "$ENV"
chmod 600 "$ENV"
echo "OK: $NAME salvata in .env (${#KEY} caratteri)."
