<!-- CODESTRA-GOVERNANCE-V3:BEGIN -->
# Codestra Governed Development Contract v3

Standalone family: Codestra Connect
Component: Codestra-Connect

Mandatory hierarchy:
Product -> Section -> Subsection -> Atomic Task

Only authorized promotion:
subsection -> section -> development -> testing -> staging -> production

Agent rules:
- one active lease per subsection;
- work only in the assigned subsection branch/worktree;
- implementation + tests + evidence + commit + push are required;
- review-only output is not completion;
- no force push and no direct protected-environment writes;
- every promotion requires codestra-control-plane plus repository CI;
- dirty, stale, divergent, dependency-incomplete, or uncertified work fails closed.

Production safety:
- PRODUCTION_GO=NO
- LIVE_CAPABILITIES_ENABLED=NO
- EXTERNAL_EFFECTS=false
<!-- CODESTRA-GOVERNANCE-V3:END -->


# Existing repository-specific instructions

# Agent Rules
Execution: Recon → Scope → Contract → Implement → Test → Security/Privacy → Evidence → PR → Review → Merge Readback → Promotion.
Never weaken consent-before-effect, mix corporate/private authorization, embed private data in QR/NFC, overclaim provider capability, overwrite unrelated work, or merge red CI.
Mission 1 owns foundation only. Mission 2 starts after the canonical Git remote is supplied.
