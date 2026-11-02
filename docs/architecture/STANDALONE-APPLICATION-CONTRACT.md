# Standalone Application Contract
Codestra Connect must build, boot, test, deploy, observe and roll back without another application's source checkout.

It owns: API/OpenAPI; schema/migrations; runtime/container; environment config; health/readiness; tests/CI; secrets references; telemetry/SLOs; deployment/rollback docs.

Cross-app communication: versioned HTTPS APIs, authenticated webhooks, or versioned events only. No cross-repo source imports and no direct ownership of another app's tables.
