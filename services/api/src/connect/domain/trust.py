from dataclasses import dataclass
SENSITIVE={"phone","email","address","token","authorization","oauth_token"}
def redact(event:dict)->dict:
 return {k:("[REDACTED]" if k.lower() in SENSITIVE else v) for k,v in event.items()}
@dataclass(frozen=True)
class ReleaseGate:
 tests_green:bool; security_clear:bool; rollback_verified:bool; observability_green:bool
 def production_ready(self)->bool:
  return self.tests_green and self.security_clear and self.rollback_verified and self.observability_green
