# Secure Share Transport
QR, NFC, wallet, badge and plain links carry the same canonical HTTPS path: /c/{opaque-token}.
Persist token hashes only. Unknown, expired and revoked tokens resolve uniformly. Raw profile/contact fields never enter QR or NDEF payloads. Public resolution is rate limited. Revocation is immediate at application authority.
NFC uses one HTTPS URI NDEF record. QR contains exactly the same canonical URL.
