from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID, uuid4

class PersonaKind(StrEnum):
    BUSINESS="business"; PERSONAL="personal"; FRIENDS_FAMILY="friends_family"; SOCIAL_LEISURE="social_leisure"; DATING_PRIVATE="dating_private"; EVENT="event"; TRAVEL="travel"; CUSTOM="custom"
class DisclosureLevel(StrEnum):
    PUBLIC="public"; ASK_FIRST="ask_first"; PRIVATE="private"; NEVER_AUTO_SHARE="never_auto_share"
class FieldOwner(StrEnum):
    USER="user"; ORGANIZATION="organization"

@dataclass(frozen=True)
class Profile:
    user_id: UUID; display_name: str; id: UUID=field(default_factory=uuid4)
    def __post_init__(self):
        if not self.display_name.strip(): raise ValueError("display_name is required")

@dataclass(frozen=True)
class ContactMethod:
    profile_id: UUID; kind: str; value: str; verified: bool=False; id: UUID=field(default_factory=uuid4)
    def __post_init__(self):
        if self.kind not in {"email","phone","website","address"}: raise ValueError("unsupported contact kind")
        if not self.value.strip(): raise ValueError("contact value is required")

@dataclass(frozen=True)
class SocialAccount:
    profile_id: UUID; provider: str; handle: str; profile_url: str; id: UUID=field(default_factory=uuid4)
    def __post_init__(self):
        if not self.provider.strip() or not self.handle.strip(): raise ValueError("provider and handle required")
        if not self.profile_url.startswith("https://"): raise ValueError("profile_url must be https")

@dataclass(frozen=True)
class Persona:
    profile_id: UUID; kind: PersonaKind; name: str; organization_id: UUID|None=None; id: UUID=field(default_factory=uuid4)
    def __post_init__(self):
        if not self.name.strip(): raise ValueError("persona name is required")
        if self.organization_id and self.kind is not PersonaKind.BUSINESS:
            raise ValueError("organization association is restricted to business persona")

@dataclass(frozen=True)
class CardFieldPolicy:
    field_name: str; disclosure: DisclosureLevel; owner: FieldOwner=FieldOwner.USER
    def can_disclose_without_owner_approval(self)->bool: return self.disclosure is DisclosureLevel.PUBLIC
