from dataclasses import dataclass
@dataclass(frozen=True)
class Entitlements:
 plan:str; max_personas:int; enterprise_sso:bool=False; custom_domain:bool=False
 def allows(self,feature:str)->bool:
  return bool(getattr(self,feature,False))
