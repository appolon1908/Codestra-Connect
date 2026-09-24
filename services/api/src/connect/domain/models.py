from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID, uuid4

class PersonaKind(StrEnum):
    BUSINESS="business"; PERSONAL="personal"; FRIENDS_FAMILY="friends_family"; SOCIAL_LEISURE="social_leisure"; DATING_PRIVATE="dating_private"; EVENT="event"; TRAVEL="travel"; CUSTOM="custom"

class DisclosureLevel(StrEnum):
    PUBLIC="public"; ASK_FIRST="ask_first"; PRIVATE="private"; NEVER_AUTO_SHARE="never_auto_share"

@dataclass(frozen=True)
class Profile:
    user_id: UUID
    display_name: str
    id: UUID = field(default_factory=uuid4)
    def __post_init__(self):
        if not self.display_name.strip(): raise ValueError("display_name is required")

@dataclass(frozen=True)
class Persona:
    profile_id: UUID
    kind: PersonaKind
    name: str
    organization_id: UUID | None = None
    id: UUID = field(default_factory=uuid4)
    def __post_init__(self):
        if not self.name.strip(): raise ValueError("persona name is required")

@dataclass(frozen=True)
class CardFieldPolicy:
    field_name: str
    disclosure: DisclosureLevel
    def can_disclose_without_owner_approval(self) -> bool:
        return self.disclosure is DisclosureLevel.PUBLIC
