from dataclasses import dataclass
def esc(v:str)->str:
    return v.replace("\\","\\\\").replace("\n","\\n").replace(";","\\;").replace(",","\\,")
@dataclass(frozen=True)
class VCardProjection:
    full_name:str; phone:str|None=None; email:str|None=None; website:str|None=None
def render_vcard(p:VCardProjection)->str:
    if not p.full_name.strip(): raise ValueError("full_name required")
    lines=["BEGIN:VCARD","VERSION:4.0","FN:"+esc(p.full_name)]
    if p.phone: lines.append("TEL:"+esc(p.phone))
    if p.email: lines.append("EMAIL:"+esc(p.email))
    if p.website: lines.append("URL:"+esc(p.website))
    return "\r\n".join(lines+["END:VCARD",""])
