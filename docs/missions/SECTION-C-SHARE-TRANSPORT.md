# Section C — Share Transport
Status: COMPLETE FOUNDATION LOCALLY / REMOTE CI PENDING

C1 Share Tokens: opaque token generation, hash-only persistence contract, expiry and revocation state.
C2 QR Engine: canonical HTTPS QR payload.
C3 NFC/Wallet/Badge: NFC NDEF URI uses identical canonical URL; wallet/badge remain transport abstractions.
C4 Public Share: /c/{token} contract with uniform unknown/expired/revoked behavior.

Exit evidence: QR and NFC resolve to the same URL and contain no raw card/contact data; token revocation is tested.
