import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"services/api/src"))
from connect.domain.api_keys import issue_api_key
from connect.domain.custom_domain import CustomDomain
from connect.domain.scim import ScimUser
from connect.domain.crm import CrmLeadHandoff
from connect.domain.notifications import Notification,validate
from connect.domain.retention import RetentionPolicy
from connect.domain.export_delete import export_sections,deletion_plan
from connect.domain.slo import SLO
class Eight(unittest.TestCase):
 def test_api_key_hash(self): 
  k=issue_api_key({"connections.read"}); self.assertNotEqual(k.plaintext,k.key_hash)
 def test_custom_domain(self):
  with self.assertRaises(ValueError): CustomDomain("https://bad.example")
 def test_scim(self): self.assertTrue(ScimUser("1","a@b.com").active)
 def test_crm_consent(self):
  with self.assertRaises(ValueError): CrmLeadHandoff("1","odoo","none")
 def test_notification(self): self.assertTrue(validate(Notification("connect_back","u",{})))
 def test_retention(self):
  with self.assertRaises(ValueError): RetentionPolicy(0,90)
 def test_export_delete(self): self.assertIn("consents",export_sections()); self.assertEqual(deletion_plan()[0],"revoke_tokens")
 def test_slo(self): self.assertEqual(SLO().p95_ms,500)
