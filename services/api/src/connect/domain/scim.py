from dataclasses import dataclass
@dataclass(frozen=True)
class ScimUser:
 external_id:str; email:str; active:bool=True
 def __post_init__(self):
  if not self.external_id.strip() or "@" not in self.email: raise ValueError("invalid SCIM user")
