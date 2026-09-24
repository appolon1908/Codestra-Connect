BEGIN;
CREATE TABLE IF NOT EXISTS connect_profiles (
  id uuid PRIMARY KEY,
  user_id uuid NOT NULL UNIQUE,
  display_name text NOT NULL CHECK (length(trim(display_name)) > 0),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS connect_personas (
  id uuid PRIMARY KEY,
  profile_id uuid NOT NULL REFERENCES connect_profiles(id) ON DELETE CASCADE,
  organization_id uuid NULL,
  kind text NOT NULL CHECK (kind IN ('business','personal','friends_family','social_leisure','dating_private','event','travel','custom')),
  name text NOT NULL CHECK (length(trim(name)) > 0),
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS connect_cards (
  id uuid PRIMARY KEY,
  persona_id uuid NOT NULL REFERENCES connect_personas(id) ON DELETE CASCADE,
  name text NOT NULL,
  active boolean NOT NULL DEFAULT true,
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS connect_card_field_policies (
  card_id uuid NOT NULL REFERENCES connect_cards(id) ON DELETE CASCADE,
  field_name text NOT NULL,
  disclosure text NOT NULL CHECK (disclosure IN ('public','ask_first','private','never_auto_share')),
  PRIMARY KEY (card_id, field_name)
);
CREATE INDEX IF NOT EXISTS idx_connect_personas_profile ON connect_personas(profile_id);
COMMIT;
