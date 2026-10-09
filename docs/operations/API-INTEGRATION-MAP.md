# Integration Map
Public: https://connect.codestra.co
Staging: https://staging-connect.codestra.co
Local API: http://localhost:8095
API base: /v1
Public share: /c/{opaque-token}

External systems integrate through adapters:
- Keycloak/OIDC: authentication/SSO
- OpenBao: secret references
- Odoo/CRM: explicit-consent lead handoff
- Social providers: capability-declared adapters
- Caddy/Kong: public edge/API gateway
- Prometheus/Alertmanager/Grafana/Loki/Tempo/Alloy: operations

Connect remains deployable if any optional adapter is disabled.
