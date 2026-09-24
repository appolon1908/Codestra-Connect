from dataclasses import dataclass
@dataclass(frozen=True)
class RetentionPolicy:
 audit_days:int=365; analytics_days:int=90
 def __post_init__(self):
  if self.audit_days<1 or self.analytics_days<1: raise ValueError("retention must be positive")
