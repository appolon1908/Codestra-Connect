from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID, uuid4
class ConnectionState(StrEnum):
    PENDING="pending"; ACCEPTED="accepted"; DECLINED="declined"; REVOKED="revoked"; BLOCKED="blocked"
@dataclass
class Connection:
    initiator_profile_id: UUID; recipient_profile_id: UUID
    id: UUID = field(default_factory=uuid4); state: ConnectionState = ConnectionState.PENDING
    def accept(self): self.state=ConnectionState.ACCEPTED
    def decline(self): self.state=ConnectionState.DECLINED
    def revoke(self): self.state=ConnectionState.REVOKED
    def block(self): self.state=ConnectionState.BLOCKED
