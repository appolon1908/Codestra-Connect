import sys,unittest
from pathlib import Path
from uuid import uuid4
from datetime import datetime,timedelta,timezone
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"services/api/src"))
from connect.domain.provider_registry import provider
from connect.domain.enterprise import OrgRole
from connect.domain.enterprise_policy import admin_can_access_persona
from connect.domain.event_badge import EventShare
from connect.domain.webhooks import WebhookEndpoint
from connect.domain.analytics import Funnel
from connect.domain.abuse import AttemptWindow
class NextSix(unittest.TestCase):
 def test_provider_registry(self): self.assertTrue(provider("instagram").capabilities.profile_link)
 def test_private_persona_denied_to_org_admin(self): self.assertFalse(admin_can_access_persona(OrgRole.ADMIN,"personal")); self.assertTrue(admin_can_access_persona(OrgRole.ADMIN,"business"))
 def test_event_expiry(self): self.assertTrue(EventShare(uuid4(),uuid4(),datetime.now(timezone.utc)+timedelta(minutes=1)).active())
 def test_webhook_https(self):
  with self.assertRaises(ValueError): WebhookEndpoint("http://bad.example")
 def test_funnel(self): self.assertEqual(Funnel(10,5,2).conversion(),.2)
 def test_abuse_limit(self):
  w=AttemptWindow(limit=1); self.assertTrue(w.allow()); w.record(); self.assertFalse(w.allow())
