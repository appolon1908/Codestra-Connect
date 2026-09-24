import sys, unittest
from pathlib import Path
from uuid import uuid4
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"services/api/src"))
from connect.domain.consent import ConsentGrant,ConsentScope
from connect.domain.connections import Connection,ConnectionState
from connect.domain.social import DeepLinkAdapter,SocialActionState
class M(unittest.TestCase):
 def test_consent_requires_scope(self):
  with self.assertRaises(ValueError): ConsentGrant(uuid4(),frozenset(),"v1")
 def test_connection_lifecycle(self):
  c=Connection(uuid4(),uuid4()); c.accept(); self.assertEqual(c.state,ConnectionState.ACCEPTED); c.revoke(); self.assertEqual(c.state,ConnectionState.REVOKED)
 def test_deep_link_follow_requires_user_action(self):
  a=DeepLinkAdapter("example","https://social.example"); r=a.begin_action("follow","person"); self.assertEqual(r.state,SocialActionState.REQUIRES_USER_ACTION)
 def test_unsupported_is_explicit(self):
  a=DeepLinkAdapter("example","https://social.example"); self.assertEqual(a.begin_action("silent_follow","person").state,SocialActionState.UNSUPPORTED)
