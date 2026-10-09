import sys,unittest
from pathlib import Path
from uuid import uuid4
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"services/api/src"))
from connect.domain.middleware import MiddlewareCommand
class M(unittest.TestCase):
 def cmd(self,t): return MiddlewareCommand(uuid4(),t,uuid4(),"user",uuid4(),"idem-key-123",{})
 def test_owned(self): self.assertEqual(self.cmd("connect.crm.create").command_type,"connect.crm.create")
 def test_direct_rejected(self):
  with self.assertRaises(ValueError): self.cmd("instagram.follow")
 def test_idempotency(self):
  with self.assertRaises(ValueError): MiddlewareCommand(uuid4(),"connect.crm.create",uuid4(),"u",uuid4(),"x",{})
