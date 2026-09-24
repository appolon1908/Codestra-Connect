from dataclasses import dataclass
from uuid import UUID
from .enterprise import OrgRole
@dataclass(frozen=True)
class CorporatePersonaPolicy:
 organization_id:UUID
 managed_fields:frozenset[str]
 def organization_can_manage(self,field:str)->bool: return field in self.managed_fields
PRIVATE_PERSONA_KINDS={"personal","friends_family","social_leisure","dating_private","travel"}
def admin_can_access_persona(role:OrgRole,kind:str)->bool:
 return role in {OrgRole.OWNER,OrgRole.ADMIN} and kind=="business"
