import sys,unittest
from pathlib import Path
from uuid import uuid4
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"services/api/src"))
from connect.domain.models import *
class IdentitySection(unittest.TestCase):
 def test_contact_validation(self):
  p=uuid4(); self.assertEqual(ContactMethod(p,"email","a@example.com").kind,"email")
  with self.assertRaises(ValueError): ContactMethod(p,"secret","x")
 def test_social_requires_https(self):
  with self.assertRaises(ValueError): SocialAccount(uuid4(),"x","me","http://bad")
 def test_org_only_business(self):
  with self.assertRaises(ValueError): Persona(uuid4(),PersonaKind.PERSONAL,"Private",uuid4())
 def test_org_owned_policy_still_respects_disclosure(self):
  x=CardFieldPolicy("title",DisclosureLevel.ASK_FIRST,FieldOwner.ORGANIZATION)
  self.assertFalse(x.can_disclose_without_owner_approval())
