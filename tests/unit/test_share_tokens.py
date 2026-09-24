import sys, unittest
from pathlib import Path
from uuid import uuid4
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "services/api/src"))
from connect.domain.share import issue_share_token, verify_share_token

class ShareTokenTests(unittest.TestCase):
    def test_token_is_opaque_and_only_hash_is_persistable(self):
        card=uuid4(); issued=issue_share_token(card)
        self.assertNotIn(str(card), issued.plaintext)
        self.assertNotEqual(issued.plaintext, issued.token_hash)
        self.assertTrue(verify_share_token(issued.plaintext, issued.token_hash))
        self.assertFalse(verify_share_token("forged", issued.token_hash))
if __name__ == "__main__": unittest.main()
