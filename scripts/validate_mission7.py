from pathlib import Path
import subprocess,sys
r=Path(__file__).resolve().parents[1]
required=["docs/missions/MISSION-04-CONSENT.md","docs/missions/MISSION-05-VCARD.md","docs/missions/MISSION-06-CONNECT-BACK.md","docs/missions/MISSION-07-SOCIAL-ADAPTERS.md","docs/architecture/API-URL-MAP.md","services/api/src/connect/domain/social.py","db/migrations/0003_consent_connections.sql"]
for p in required:
 if not (r/p).exists(): raise SystemExit("missing "+p)
raise SystemExit(subprocess.run([sys.executable,"-m","unittest","discover","-s","tests/unit","-v"],cwd=r).returncode)
