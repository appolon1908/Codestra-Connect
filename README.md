# Codestra Connect
Standalone Codestra application for identity, personas, QR/NFC sharing, consent, connections, social adapters and enterprise identity.

## Standalone application rule
Codestra Connect owns its own runtime, database migrations, API contract, tests, CI, deployment manifests, observability contract and release lifecycle. Other Codestra applications integrate only through versioned APIs/events. No application may require another repository's source tree to build or boot.

## Environment branches
- development — active integration
- testing — automated/integration acceptance
- staging — staging promotion
- production — production promotion
- main — protected canonical release history

API target: https://connect.codestra.co/v1
Staging: https://staging-connect.codestra.co
Local: http://localhost:8095
