from pathlib import Path
import subprocess, sys
root=Path(__file__).resolve().parents[1]
for p in ["services/api/src/connect/domain/share.py","db/migrations/0002_share_tokens.sql","docs/missions/MISSION-03-SHARE-TRANSPORT.md"]:
    if not (root/p).exists(): raise SystemExit(f"missing {p}")
r=subprocess.run([sys.executable,"-m","unittest","discover","-s","tests/unit","-v"],cwd=root)
raise SystemExit(r.returncode)
