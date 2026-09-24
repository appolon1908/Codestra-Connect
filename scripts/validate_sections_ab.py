from pathlib import Path
import subprocess,sys
r=Path(__file__).resolve().parents[1]
required=[".github/workflows/ci.yml","pyproject.toml","db/migrations/0004_identity_contacts_socials.sql","tests/contract/test_openapi_contract.py"]
for p in required:
 if not (r/p).exists(): raise SystemExit("missing "+p)
for suite in ["tests/unit","tests/contract"]:
 rc=subprocess.run([sys.executable,"-m","unittest","discover","-s",suite,"-p","test_*.py","-v"],cwd=r).returncode
 if rc: raise SystemExit(rc)
print("SECTIONS A+B PASS")
