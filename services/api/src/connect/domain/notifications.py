from dataclasses import dataclass
@dataclass(frozen=True)
class Notification:
 kind:str; recipient_id:str; data:dict
ALLOWED={"connect_back","connection_accepted","follow_up"}
def validate(n:Notification)->bool: return n.kind in ALLOWED and bool(n.recipient_id)
