# Foundation Architecture
Account → Personas → Cards → Share Transports → Consent → Connection → Relationship.
Corporate hierarchy: Tenant → Organization → Business Unit → Team → User → Corporate Persona.
Bounded domains: Identity/Auth; Tenancy/RBAC; Personas/Profiles; Cards/Disclosure; Share Transport; Consent; Connections; Social Adapters; CRM/Integrations; Events; Billing/Entitlements; Developer Platform; Audit/Compliance; Analytics; Admin.
Begin modular. Extract services only when throughput, isolation, ownership, or deployment needs justify it. OpenAPI 3.1 is the HTTP contract. PostgreSQL is transactional authority.
