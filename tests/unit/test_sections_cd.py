import sys,unittest
from pathlib import Path
from uuid import uuid4
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"services/api/src"))
from connect.domain.share import *
from connect.domain.vcard import *
from connect.domain.consent import ConsentGrant,ConsentScope
from connect.domain.connections import Connection,ConnectionState
class CD(unittest.TestCase):
 def test_qr_nfc_same_canonical_url(self):
  x=issue_share_token(uuid4()); self.assertEqual(qr_payload("https://connect.codestra.co",x.plaintext),ndef_uri_payload("https://connect.codestra.co",x.plaintext))
 def test_revocation_fails_active(self):
  x=issue_share_token(uuid4()); self.assertTrue(x.active()); x.revoke(); self.assertFalse(x.active())
 def test_vcard_is_scoped(self):
  v=render_vcard(VCardProjection("Ralph",email="r@example.com")); self.assertIn("EMAIL:r@example.com",v); self.assertNotIn("TEL:",v)
 def test_consent_scope(self):
  g=ConsentGrant(uuid4(),frozenset({ConsentScope.CONTACT}),"v1"); self.assertEqual(g.scopes,frozenset({ConsentScope.CONTACT}))
 def test_connection_block_state(self):
  c=Connection(uuid4(),uuid4()); c.block(); self.assertEqual(c.state,ConnectionState.BLOCKED)
