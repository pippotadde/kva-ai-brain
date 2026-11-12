#!/usr/bin/env bash
# AI coordination channel for team KVA.
# The channel lives on the git branch `coord`, checked out in the folder .coord/
# (separate from the code, so syncing never touches your work in progress).
#
#   bash scripts/coord.sh init <filippo|giorgia|sian>   once per computer
#   bash scripts/coord.sh sync                           pull others' updates + push yours
#   bash scripts/coord.sh watch                          sync every 60s (leave running in a terminal)
#   bash scripts/coord.sh msg <to|all> "<subject>" "<text>"
#   bash scripts/coord.sh decide "<title>" "<decision and why>"
#   bash scripts/coord.sh inbox                          messages for me, newest first
set -euo pipefail
ROOT="$(git rev-parse --show-toplevel)"
CO="$ROOT/.coord"
ME_FILE="$ROOT/.coord-me"
me() { [ -f "$ME_FILE" ] && cat "$ME_FILE" || { echo "run: bash scripts/coord.sh init <name>" >&2; exit 1; }; }
ts() { date +%Y%m%d-%H%M%S; }
now() { date '+%Y-%m-%d %H:%M'; }

sync() {
  cd "$CO"
  git add -A
  git diff --cached --quiet || git commit -qm "coord: $(me) $(now)"
  git pull -q --rebase origin coord || { echo "coord: pull failed (conflict?). Tell Filippo." >&2; exit 1; }
  git push -q origin coord
}

case "${1:-}" in
  init)
    name="${2:?usage: init <filippo|giorgia|sian>}"
    echo "$name" > "$ME_FILE"
    if [ ! -d "$CO" ]; then
      git -C "$ROOT" fetch -q origin coord
      git -C "$ROOT" worktree add -q "$CO" -B coord origin/coord
      git -C "$CO" branch -q --set-upstream-to=origin/coord coord
    fi
    mkdir -p "$CO/agents/$name/work"
    echo "coord ready: you are '$name', channel in .coord/"
    ;;
  sync) sync; echo "coord synced $(now)";;
  watch)
    echo "coord: syncing every 60s (Ctrl+C to stop)"
    while true; do sync || true; sleep 60; done
    ;;
  msg)
    to="${2:?to}"; subj="${3:?subject}"; text="${4:?text}"
    f="$CO/messages/$(ts)-$(me)-to-$to.md"
    printf -- "---\nfrom: %s\nto: %s\ndate: %s\nsubject: %s\n---\n\n%s\n" "$(me)" "$to" "$(now)" "$subj" "$text" > "$f"
    sync; echo "sent: $f"
    ;;
  decide)
    title="${2:?title}"; text="${3:?text}"
    slug="$(echo "$title" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | cut -c1-40)"
    f="$CO/decisions/$(ts)-$slug.md"
    printf -- "---\nby: %s\ndate: %s\ntitle: %s\n---\n\n%s\n" "$(me)" "$(now)" "$title" "$text" > "$f"
    sync; echo "recorded: $f"
    ;;
  inbox)
    sync >/dev/null 2>&1 || true
    ls -1r "$CO/messages" 2>/dev/null | grep -E -- "-to-($(me)|all)\.md$" | head -15 | while read -r m; do
      echo "== $m"; sed -n '6,$p' "$CO/messages/$m"; echo
    done
    ;;
  *) sed -n '2,13p' "$0";;
esac
