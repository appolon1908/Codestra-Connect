#!/usr/bin/env bash
set -euo pipefail
git status --short
git branch --show-current
git rev-parse HEAD
python3 scripts/validate_foundation.py
python3 scripts/validate_sections_ab.py
python3 scripts/validate_sections_cd.py
python3 scripts/validate_sections_efgh.py
python3 scripts/validate_next_six.py
python3 scripts/validate_next_eight.py
