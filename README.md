# Codestra Connect
One identity. Many personas. One consent layer.

Consent-first identity and relationship platform for personal, business, leisure, events, and enterprise use.

## Mission 1 — Foundation
Modular monorepo boundaries: apps/web (PWA), services/api (API), packages/contracts (OpenAPI), packages/domain (invariants), packages/ui (shared UX), infra, docs, tests.

## Invariants
1. Consent before effect.
2. One account may own many isolated personas.
3. Corporate Work personas never expose private personas to corporate admins.
4. QR/NFC transports never contain raw private contact data.
5. Social actions report actual provider capability.
6. Tenant authorization is server-side and default-deny.
7. Effectful operations are idempotent and auditable.

First slice: Profile → Persona → Card → Share Token → Public Connect → Consent → scoped vCard.
Git remote is intentionally not configured yet. Mission 2 begins after the canonical GitHub repository is provided.
