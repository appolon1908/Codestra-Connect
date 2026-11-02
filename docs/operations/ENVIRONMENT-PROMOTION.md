# Environment Promotion
development -> testing -> staging -> production

development: integration branch and developer environment.
testing: automated integration/acceptance candidate.
staging: production-like release candidate and runtime smoke gate.
production: live release branch; promotion requires staging evidence.
main: canonical repository history, not a shortcut around environment gates.

Every promotion records source SHA, artifact identity, health/readiness, API smoke, migration state, observability readback and rollback procedure.
