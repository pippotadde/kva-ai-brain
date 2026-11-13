#!/usr/bin/env bash
# "What are we working on" window: the chosen idea, the current phase,
# my task and (on Saturday) the next step of the schedule.
# Read-only, refreshes every N seconds (default 30). Ctrl+C to stop.
#
#   bash scripts/focus.sh [seconds]
set -uo pipefail
ROOT="$(git rev-parse --show-toplevel)"
CO="$ROOT/.coord"
ME="$(cat "$ROOT/.coord-me" 2>/dev/null || echo '?')"
EVERY="${1:-30}"

B=$'\e[1m'; D=$'\e[2m'; I=$'\e[7m'; N=$'\e[0m'
section() { awk -v h="## $2" '$0 ~ "^"h {f=1; next} /^## /{f=0} f && NF' "$1" 2>/dev/null | sed 's/\*\*//g; s/`//g'; }
bar() { printf '%s %-68s%s\n' "$I$B" "$1" "$N"; }

render() {
  clear
  printf '%sKVA · SU COSA LAVORIAMO · io: %s · %s%s\n\n' "$B" "$ME" "$(date '+%H:%M')" "$N"

  # --- The idea: latest decision whose title mentions problem/idea ---------
  bar "L'IDEA"
  local dec
  dec="$(grep -liE '^title:.*(problema|idea|prodotto|nome)' "$CO"/decisions/*.md 2>/dev/null | sort | tail -1)"
  if [ -n "$dec" ]; then
    printf '  %s%s%s  %s(%s)%s\n' "$B" "$(sed -n 's/^title: //p' "$dec")" "$N" "$D" "$(sed -n 's/^date: //p' "$dec")" "$N"
    awk 'BEGIN{n=0} /^---/{n++; next} n>=2 && NF' "$dec" | head -6 | fold -s -w 68 | sed 's/^/  /'
  else
    printf '  %sNon ancora scelta.%s Candidati:\n' "$B" "$N"
    section "$CO/SITUAZIONE.md" "Candidati" | grep '^- ' | sed 's/^/  /'
  fi
  echo

  bar "FASE"
  section "$CO/SITUAZIONE.md" "Fase attuale" | head -2 | fold -s -w 68 | sed 's/^/  /'
  echo

  bar "IO ($ME)"
  local st="$CO/agents/$ME/status.md"
  printf '  %sSto facendo:%s\n' "$B" "$N"
  section "$st" "Sto facendo" | head -3 | fold -s -w 66 | sed 's/^/    /'
  printf '  %sProssimo passo:%s\n' "$B" "$N"
  section "$st" "Prossimo passo" | head -3 | fold -s -w 66 | sed 's/^/    /'
  local blk; blk="$(section "$st" "Bloccato da" | grep -viE '^- *(niente|nessuno|-)$' | head -3)"
  [ -n "$blk" ] && { printf '  %sBloccato da:%s\n' "$B" "$N"; echo "$blk" | fold -s -w 66 | sed 's/^/    /'; }
  echo

  # --- Saturday: where we are in the official schedule ---------------------
  if [ "$(date +%F)" = "2026-11-14" ]; then
    bar "SCALETTA DI OGGI"
    local now; now="$(date +%H:%M)"
    grep -o '<td class="time">[0-9:]*</td><td>[^<]*' "$ROOT/docs/site/generale.html" \
      | sed 's/<td class="time">//; s#</td><td>#|#' \
      | awk -F'|' -v now="$now" '
          $1 <= now { cur = $0; next }
          !nx { nx = $0 }
          END {
            if (cur) { split(cur, c, "|"); printf "  ORA:     %s  %s\n", c[1], c[2] }
            if (nx)  { split(nx,  x, "|"); printf "  DOPO:    %s  %s\n", x[1], x[2] }
          }'
    echo
  fi

  printf '%sAggiornamento ogni %ss · fonte: .coord/ (SITUAZIONE, decisions, status) · Ctrl+C esce%s\n' "$D" "$EVERY" "$N"
}

while true; do render; sleep "$EVERY"; done
