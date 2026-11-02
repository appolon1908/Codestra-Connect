#!/usr/bin/env bash
set -euo pipefail
if [[ -n "$(git status --porcelain)" ]]; then
  git status --short
  echo "Refusing to proceed with a dirty worktree." >&2
  exit 1
fi
git branch --show-current
git rev-parse HEAD
python3 scripts/validate_foundation.py
python3 scripts/validate_sections_ab.py
python3 scripts/validate_sections_cd.py
python3 scripts/validate_sections_efgh.py
python3 scripts/validate_next_six.py
python3 scripts/validate_next_eight.py
