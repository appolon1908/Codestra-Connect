from dataclasses import dataclass
@dataclass
class Funnel:
 scans:int=0; consents:int=0; connections:int=0
 def conversion(self)->float:
  return 0.0 if self.scans==0 else self.connections/self.scans
