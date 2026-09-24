from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4
class ConsentScope(StrEnum):
    CONTACT="contact"; SOCIALS="socials"; CONNECT_BACK="connect_back"
@dataclass(frozen=True)
class ConsentGrant:
    share_token_id: UUID; scopes: frozenset[ConsentScope]; policy_version: str
    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    def __post_init__(self):
        if not self.scopes: raise ValueError("at least one consent scope is required")
        if not self.policy_version.strip(): raise ValueError("policy_version is required")
