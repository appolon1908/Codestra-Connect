import unittest
from pathlib import Path
class Contract(unittest.TestCase):
 def test_required_paths_and_servers(self):
  s=(Path(__file__).resolve().parents[2]/"packages/contracts/openapi/connect-v1.yaml").read_text()
  for x in ["openapi: 3.1.0","https://connect.codestra.co","/v1/profiles:","/v1/personas:","/v1/cards:","Idempotency-Key"]:
   self.assertIn(x,s)
