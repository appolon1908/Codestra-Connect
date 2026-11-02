# Integration Map — Middleware V3 authority
Public: https://connect.codestra.co
Staging: https://staging-connect.codestra.co
Local Connect API: http://localhost:8095
API base: /v1
Public share: /c/{opaque-token}

Connect owns its product API and database. Every cross-service or provider effect goes through Middleware V3 `/platform/v1/commands`, through the configured Caddy/Kong gateway. Operation readback uses `/platform/v1/operations/{operation_id}`; service governance uses `/platform/v1/services`.

Keycloak/OIDC, OpenBao, Odoo/CRM, social providers, notifications, provisioning and webhooks are reached through Middleware adapters. There is no direct-provider bypass. CRM handoff requires explicit consent. Every mutation carries tenant, actor, correlation ID and an Idempotency-Key.

Prometheus, Alertmanager, Grafana, Loki, Tempo and Alloy provide operations telemetry. Connect remains deployable with optional integrations disabled; disabling an integration never permits bypassing Middleware for its effects.
