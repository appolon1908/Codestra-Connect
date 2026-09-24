from dataclasses import dataclass
from datetime import datetime,timezone
from uuid import UUID
@dataclass(frozen=True)
class EventShare:
 event_id:UUID; persona_id:UUID; expires_at:datetime
 def active(self,now:datetime|None=None)->bool:
  return self.expires_at>(now or datetime.now(timezone.utc))
