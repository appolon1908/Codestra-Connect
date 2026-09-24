from dataclasses import dataclass,field
from hashlib import sha256
from secrets import token_urlsafe
@dataclass(frozen=True)
class IssuedApiKey:
 plaintext:str; key_hash:str; scopes:frozenset[str]
def issue_api_key(scopes:set[str])->IssuedApiKey:
 if not scopes: raise ValueError("scopes required")
 p="cc_"+token_urlsafe(24); return IssuedApiKey(p,sha256(p.encode()).hexdigest(),frozenset(scopes))
