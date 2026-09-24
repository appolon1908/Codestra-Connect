# API and URL Map
These are **prepared target URLs**, not DNS/deployment claims.

Public product target: https://connect.codestra.co
Staging target: https://staging-connect.codestra.co
Local API: http://localhost:8095
Public scan/tap route: https://connect.codestra.co/c/{opaque-token}
API base: https://connect.codestra.co/v1
OpenAPI source: packages/contracts/openapi/connect-v1.yaml

Core endpoints:
POST /v1/profiles
POST /v1/personas
POST /v1/cards
POST /v1/cards/{card_id}/share-tokens
GET /c/{token}
POST /v1/share-sessions/{token}/consents
GET|POST /v1/connections
POST /v1/connections/{connection_id}/connect-back
POST /v1/connections/{connection_id}/revoke
GET /v1/social-adapters
GET /v1/social-adapters/{provider}/capabilities
POST /v1/social-actions
GET /v1/social-actions/{action_id}
GET /v1/oauth/{provider}/authorize
GET /v1/oauth/{provider}/callback

Mission 7 rule: adapters declare capabilities first. A provider requiring a human confirmation returns requires_user_action; the platform never labels that action completed prematurely.
