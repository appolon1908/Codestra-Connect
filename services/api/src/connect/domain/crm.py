from dataclasses import dataclass
@dataclass(frozen=True)
class CrmLeadHandoff:
 connection_id:str; destination:str; consent_scope:str
 def __post_init__(self):
  if self.consent_scope!="crm_handoff": raise ValueError("explicit crm_handoff consent required")
