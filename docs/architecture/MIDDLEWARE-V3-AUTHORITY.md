# Middleware V3 is the only integration authority
Connect stays standalone but all cross-service/provider effects go through Middleware V3.
Effect path: Connect -> Caddy/Kong -> Middleware V3 port 8095 -> /platform/v1/commands -> registry -> policy/safety -> durable ledger/outbox -> one adapter -> target.
Command families: connect.crm.*, connect.social.*, connect.notification.*, connect.provisioning.*, connect.webhook.*, connect.audit.*.
Every mutation carries tenant, actor, correlation id and Idempotency-Key. Readback uses /platform/v1/operations/{operation_id}. Service governance uses /platform/v1/services. No direct-provider bypass.
