from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = ["README.md",".env.example","packages/contracts/openapi/connect-v1.yaml","docs/architecture/FOUNDATION.md","docs/adr/0001-modular-foundation.md","docs/adr/0002-consent-before-effect.md","services/api/src/connect/app.py","infra/docker/compose.yaml"]
missing = [p for p in required if not (root / p).exists()]
contract = (root / "packages/contracts/openapi/connect-v1.yaml").read_text()
checks = {"OpenAPI 3.1":"openapi: 3.1.0" in contract,"Idempotency":"Idempotency-Key" in contract,"Consent endpoint":"/share-sessions/{token}/consents:" in contract,"Persona kinds":"friends_family" in contract and "social_leisure" in contract}
failed = [n for n,ok in checks.items() if not ok]
if missing or failed:
    print("FOUNDATION FAIL"); print("Missing:", missing); print("Checks:", failed); sys.exit(1)
print("FOUNDATION PASS")
for n in checks: print("  PASS", n)
