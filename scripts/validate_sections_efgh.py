from pathlib import Path
import subprocess,sys
r=Path(__file__).resolve().parents[1]
for p in ["docs/missions/SECTION-E-SOCIAL-PLATFORM.md","docs/missions/SECTION-F-ENTERPRISE.md","docs/missions/SECTION-G-PRODUCT-UX.md","docs/missions/SECTION-H-TRUST-RELEASE.md"]:
 if not (r/p).exists(): raise SystemExit("missing "+p)
raise SystemExit(subprocess.run([sys.executable,"-m","unittest","discover","-s","tests/unit","-p","test_*.py","-v"],cwd=r).returncode)
