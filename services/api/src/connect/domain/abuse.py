from dataclasses import dataclass
@dataclass
class AttemptWindow:
 attempts:int=0; limit:int=20
 def allow(self)->bool: return self.attempts<self.limit
 def record(self): self.attempts+=1
