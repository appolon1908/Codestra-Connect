from dataclasses import dataclass, field
from datetime import datetime, timezone
from hashlib import sha256
from secrets import token_urlsafe
from uuid import UUID, uuid4
@dataclass(frozen=True)
class IssuedShareToken:
    id: UUID; card_id: UUID; plaintext: str; token_hash: str; expires_at: datetime | None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
def issue_share_token(card_id: UUID, expires_at: datetime | None = None) -> IssuedShareToken:
    if expires_at is not None and expires_at <= datetime.now(timezone.utc): raise ValueError("expires_at must be in the future")
    plaintext=token_urlsafe(32)
    return IssuedShareToken(uuid4(),card_id,plaintext,sha256(plaintext.encode()).hexdigest(),expires_at)
def verify_share_token(plaintext: str, expected_hash: str) -> bool:
    return sha256(plaintext.encode()).hexdigest()==expected_hash
def public_share_url(base_url: str, plaintext: str) -> str:
    return base_url.rstrip("/")+"/c/"+plaintext
