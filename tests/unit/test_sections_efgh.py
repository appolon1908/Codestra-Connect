import sys,unittest
from pathlib import Path
from uuid import uuid4
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"services/api/src"))
from connect.domain.social import DeepLinkAdapter,SocialActionState
from connect.domain.enterprise import Organization,Membership,OrgRole
from connect.domain.entitlements import Entitlements
from connect.domain.trust import redact,ReleaseGate
from connect.domain.ux import PERSONA_LABELS,CONNECT_ACTIONS
class EFGH(unittest.TestCase):
 def test_social_never_silent(self):
  self.assertEqual(DeepLinkAdapter("x","https://x.example").begin_action("follow","a").state,SocialActionState.REQUIRES_USER_ACTION)
 def test_org_membership_is_scoped(self):
  o=Organization("Acme"); m=Membership(o.id,uuid4(),OrgRole.MEMBER); self.assertEqual(m.organization_id,o.id)
 def test_entitlement(self):
  e=Entitlements("business",20,enterprise_sso=True); self.assertTrue(e.allows("enterprise_sso")); self.assertFalse(e.allows("custom_domain"))
 def test_user_language(self):
  self.assertEqual(PERSONA_LABELS["social_leisure"],"Social & Leisure"); self.assertIn("Connect & Share Mine",CONNECT_ACTIONS)
 def test_redaction_and_release_gate(self):
  self.assertEqual(redact({"email":"a@b","status":"ok"})["email"],"[REDACTED]")
  self.assertFalse(ReleaseGate(True,True,False,True).production_ready())
  self.assertTrue(ReleaseGate(True,True,True,True).production_ready())
