BEGIN;
CREATE TABLE IF NOT EXISTS connect_consent_grants (
 id uuid PRIMARY KEY, share_token_id uuid NOT NULL REFERENCES connect_share_tokens(id),
 policy_version text NOT NULL, scopes text[] NOT NULL CHECK (cardinality(scopes)>0),
 created_at timestamptz NOT NULL DEFAULT now(), revoked_at timestamptz NULL
);
CREATE TABLE IF NOT EXISTS connect_connections (
 id uuid PRIMARY KEY, initiator_profile_id uuid NOT NULL REFERENCES connect_profiles(id),
 recipient_profile_id uuid NOT NULL REFERENCES connect_profiles(id),
 state text NOT NULL CHECK (state IN ('pending','accepted','declined','revoked','blocked')),
 created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now(),
 UNIQUE (initiator_profile_id, recipient_profile_id)
);
COMMIT;
