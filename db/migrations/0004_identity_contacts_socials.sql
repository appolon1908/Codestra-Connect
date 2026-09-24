BEGIN;
CREATE TABLE IF NOT EXISTS connect_contact_methods (
 id uuid PRIMARY KEY, profile_id uuid NOT NULL REFERENCES connect_profiles(id) ON DELETE CASCADE,
 kind text NOT NULL CHECK (kind IN ('email','phone','website','address')),
 value text NOT NULL, verified boolean NOT NULL DEFAULT false, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS connect_social_accounts (
 id uuid PRIMARY KEY, profile_id uuid NOT NULL REFERENCES connect_profiles(id) ON DELETE CASCADE,
 provider text NOT NULL, handle text NOT NULL, profile_url text NOT NULL CHECK (profile_url LIKE 'https://%'),
 created_at timestamptz NOT NULL DEFAULT now(), UNIQUE(profile_id,provider,handle)
);
ALTER TABLE connect_card_field_policies ADD COLUMN IF NOT EXISTS field_owner text NOT NULL DEFAULT 'user'
 CHECK (field_owner IN ('user','organization'));
CREATE INDEX IF NOT EXISTS idx_connect_contact_methods_profile ON connect_contact_methods(profile_id);
CREATE INDEX IF NOT EXISTS idx_connect_social_accounts_profile ON connect_social_accounts(profile_id);
COMMIT;
