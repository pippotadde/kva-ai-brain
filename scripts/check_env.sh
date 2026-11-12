#!/usr/bin/env bash
# Verify that this machine is ready for the hackathon. Run from the repo root:
#   bash scripts/check_env.sh
set -u
ok=0; fail=0
pass() { printf "  \033[32mOK\033[0m   %s\n" "$1"; ok=$((ok+1)); }
bad()  { printf "  \033[31mFAIL\033[0m %s\n       -> %s\n" "$1" "$2"; fail=$((fail+1)); }

echo "== System"
if grep -qi microsoft /proc/version 2>/dev/null; then pass "running inside WSL"; else pass "running on native Linux"; fi
case "$PWD" in /mnt/*) bad "repo is on the Windows disk ($PWD)" "clone it inside WSL, e.g. ~/kva-ai-brain (much faster, fewer bugs)";; *) pass "repo is on the Linux filesystem";; esac

echo "== Tools"
for t in git gh uv node claude; do
  if command -v "$t" >/dev/null 2>&1; then pass "$t: $($t --version 2>/dev/null | head -1)"; else bad "$t missing" "see docs/SETUP.md"; fi
done

echo "== Git / GitHub"
[ -n "$(git config user.name)" ] && [ -n "$(git config user.email)" ] && pass "git identity: $(git config user.name)" || bad "git identity not set" "git config --global user.name 'Name'; git config --global user.email 'you@mail'"
gh auth status >/dev/null 2>&1 && pass "gh logged in" || bad "gh not logged in" "gh auth login"
git ls-remote origin >/dev/null 2>&1 && pass "can reach the team repo" || bad "cannot reach origin" "accept the GitHub invite, then gh auth login"

echo "== Python"
if uv sync --quiet >/dev/null 2>&1; then pass "uv sync: dependencies installed ($(uv run python --version))"; else bad "uv sync failed" "run 'uv sync' to see the error"; fi

echo "== Secrets"
[ -f .env ] && pass ".env exists" || bad ".env missing" "cp .env.example .env and paste your GEMINI_API_KEY"
git check-ignore -q .env && pass ".env is ignored by git" || bad ".env NOT ignored" "tell Filippo immediately"

echo "== LLM"
if [ -f .env ]; then uv run python scripts/smoke_llm.py && pass "LLM call works" || bad "LLM call failed" "check the key in .env"; fi

echo; echo "Result: $ok ok, $fail to fix"; [ "$fail" -eq 0 ]
