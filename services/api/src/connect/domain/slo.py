from dataclasses import dataclass
@dataclass(frozen=True)
class SLO:
 availability:float=99.9; p95_ms:int=500
 def __post_init__(self):
  if not 0<self.availability<=100 or self.p95_ms<=0: raise ValueError("invalid SLO")
