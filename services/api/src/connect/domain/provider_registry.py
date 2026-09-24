from dataclasses import dataclass
from .social import ProviderCapabilities
@dataclass(frozen=True)
class ProviderSpec:
 name:str; profile_base:str; capabilities:ProviderCapabilities
REGISTRY={
 "instagram":ProviderSpec("instagram","https://www.instagram.com",ProviderCapabilities("instagram",True)),
 "linkedin":ProviderSpec("linkedin","https://www.linkedin.com/in",ProviderCapabilities("linkedin",True)),
 "tiktok":ProviderSpec("tiktok","https://www.tiktok.com/@",ProviderCapabilities("tiktok",True)),
 "youtube":ProviderSpec("youtube","https://www.youtube.com/@",ProviderCapabilities("youtube",True)),
 "x":ProviderSpec("x","https://x.com",ProviderCapabilities("x",True)),
 "whatsapp":ProviderSpec("whatsapp","https://wa.me",ProviderCapabilities("whatsapp",True)),
}
def provider(name:str)->ProviderSpec:
 if name not in REGISTRY: raise KeyError("unsupported provider")
 return REGISTRY[name]
