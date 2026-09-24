from dataclasses import dataclass
from urllib.parse import urlparse
@dataclass(frozen=True)
class WebhookEndpoint:
 url:str
 def __post_init__(self):
  u=urlparse(self.url)
  if u.scheme!="https" or not u.netloc: raise ValueError("webhook must use https")
