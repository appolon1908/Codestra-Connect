import sys, unittest
from pathlib import Path
from uuid import uuid4
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "services/api/src"))
from connect.domain import CardFieldPolicy, DisclosureLevel, Persona, PersonaKind, Profile

class PersonaTests(unittest.TestCase):
    def test_profile_requires_name(self):
        with self.assertRaises(ValueError): Profile(user_id=uuid4(), display_name=" ")
    def test_persona_kinds_include_life_contexts(self):
        self.assertEqual(PersonaKind.BUSINESS.value, "business")
        self.assertEqual(PersonaKind.SOCIAL_LEISURE.value, "social_leisure")
        self.assertEqual(PersonaKind.EVENT.value, "event")
    def test_only_public_auto_discloses(self):
        self.assertTrue(CardFieldPolicy("website", DisclosureLevel.PUBLIC).can_disclose_without_owner_approval())
        for level in [DisclosureLevel.ASK_FIRST, DisclosureLevel.PRIVATE, DisclosureLevel.NEVER_AUTO_SHARE]:
            self.assertFalse(CardFieldPolicy("phone", level).can_disclose_without_owner_approval())
    def test_corporate_persona_does_not_change_private_persona(self):
        profile=Profile(user_id=uuid4(), display_name="Example")
        org=uuid4()
        work=Persona(profile.id, PersonaKind.BUSINESS, "Work", organization_id=org)
        personal=Persona(profile.id, PersonaKind.PERSONAL, "Personal")
        self.assertEqual(work.organization_id, org)
        self.assertIsNone(personal.organization_id)
if __name__ == "__main__": unittest.main()
