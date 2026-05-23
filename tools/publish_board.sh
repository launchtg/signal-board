#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ "$(git branch --show-current)" != "main" ]]; then
  echo "ERROR: current branch is not main"
  exit 1
fi

python3 tools/validate_projects.py

if [[ -z "${1:-}" ]]; then
  echo "Usage: tools/publish_board.sh "'"'commit message'"'"
  exit 1
fi

if [[ -z "$(git status --porcelain)" ]]; then
  echo "No changes to commit"
  exit 0
fi

git add .
git commit -m "$1"
git push signal-board main

echo "Published to main. Next: verify GitHub Pages if needed."
