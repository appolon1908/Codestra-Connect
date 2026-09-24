BEGIN;
CREATE TABLE IF NOT EXISTS connect_share_tokens (
  id uuid PRIMARY KEY,
  card_id uuid NOT NULL REFERENCES connect_cards(id) ON DELETE CASCADE,
  token_hash char(64) NOT NULL UNIQUE,
  expires_at timestamptz NULL,
  revoked_at timestamptz NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS idx_connect_share_tokens_card ON connect_share_tokens(card_id);
COMMIT;
