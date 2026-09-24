from dataclasses import dataclass
from enum import StrEnum
class SocialActionState(StrEnum):
    REQUIRES_USER_ACTION="requires_user_action"; AUTHORIZED="authorized"; COMPLETED="completed"; FAILED="failed"; REVOKED="revoked"; UNSUPPORTED="unsupported"
@dataclass(frozen=True)
class ProviderCapabilities:
    provider: str
    profile_link: bool = True
    oauth: bool = False
    api_action: bool = False
    readback: bool = False
    revoke: bool = False
@dataclass(frozen=True)
class SocialActionResult:
    state: SocialActionState
    action_url: str | None = None
    detail: str | None = None
class SocialAdapter:
    def capabilities(self) -> ProviderCapabilities: raise NotImplementedError
    def profile_url(self, handle: str) -> str: raise NotImplementedError
    def begin_action(self, action: str, handle: str) -> SocialActionResult: raise NotImplementedError
class DeepLinkAdapter(SocialAdapter):
    def __init__(self, provider: str, base_url: str):
        self.provider=provider; self.base_url=base_url.rstrip("/")
    def capabilities(self): return ProviderCapabilities(provider=self.provider, profile_link=True)
    def profile_url(self, handle: str): return self.base_url+"/"+handle.lstrip("@/")
    def begin_action(self, action: str, handle: str):
        if action not in {"view_profile","follow"}:
            return SocialActionResult(SocialActionState.UNSUPPORTED, detail="provider action unsupported")
        return SocialActionResult(SocialActionState.REQUIRES_USER_ACTION, self.profile_url(handle), "provider confirmation required")
