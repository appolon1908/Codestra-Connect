from dataclasses import dataclass
from uuid import UUID
ALLOWED_PREFIXES=("connect.crm.","connect.social.","connect.notification.","connect.provisioning.","connect.webhook.","connect.audit.")
@dataclass(frozen=True)
class MiddlewareCommand:
 command_id:UUID; command_type:str; tenant_id:UUID; requested_by:str; correlation_id:UUID; idempotency_key:str; payload:dict
 def __post_init__(self):
  if not any(self.command_type.startswith(p) for p in ALLOWED_PREFIXES): raise ValueError("command namespace not owned by Connect")
  if len(self.idempotency_key)<8: raise ValueError("durable idempotency key required")
