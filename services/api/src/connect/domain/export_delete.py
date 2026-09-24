PRIVATE_EXPORT_FIELDS={"profile","personas","contacts","social_accounts","connections","consents"}
def export_sections()->set[str]: return set(PRIVATE_EXPORT_FIELDS)
def deletion_plan()->tuple[str,...]: return ("revoke_tokens","disconnect_adapters","delete_private_data","retain_required_audit")
