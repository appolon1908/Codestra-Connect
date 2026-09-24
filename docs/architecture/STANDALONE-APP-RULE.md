# Standalone Application Architecture
Each Codestra application must stand alone:
1. Own API/OpenAPI contract.
2. Own schema/migrations; no cross-repo table ownership.
3. Own runtime/container build.
4. Own health/readiness.
5. Own tests and CI.
6. Own environment configuration and secret references.
7. Own telemetry/SLO contract.
8. Integrate through APIs/events, never direct source imports.
9. Version external contracts.
10. Deploy and roll back independently.
