from dataclasses import dataclass,field
from enum import StrEnum
from uuid import UUID,uuid4
class OrgRole(StrEnum):
 OWNER="owner"; ADMIN="admin"; MANAGER="manager"; MEMBER="member"
@dataclass(frozen=True)
class Organization:
 name:str; id:UUID=field(default_factory=uuid4)
 def __post_init__(self):
  if not self.name.strip(): raise ValueError("organization name required")
@dataclass(frozen=True)
class Membership:
 organization_id:UUID; user_id:UUID; role:OrgRole; id:UUID=field(default_factory=uuid4)
