from dataclasses import dataclass
@dataclass(frozen=True)
class CustomDomain:
 hostname:str; verified:bool=False
 def __post_init__(self):
  if "." not in self.hostname or "://" in self.hostname: raise ValueError("hostname only")
