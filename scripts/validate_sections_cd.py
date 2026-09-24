from pathlib import Path
import subprocess,sys
r=Path(__file__).resolve().parents[1]
for p in ["docs/missions/SECTION-C-SHARE-TRANSPORT.md","docs/missions/SECTION-D-CONSENT-CONNECTIONS.md","packages/contracts/openapi/sections-cd-v1.yaml","services/api/src/connect/domain/vcard.py"]:
 if not (r/p).exists(): raise SystemExit("missing "+p)
raise SystemExit(subprocess.run([sys.executable,"-m","unittest","discover","-s","tests/unit","-p","test_*.py","-v"],cwd=r).returncode)
