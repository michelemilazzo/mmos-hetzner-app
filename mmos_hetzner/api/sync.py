import frappe


@frappe.whitelist()
def list_nodes() -> list[dict[str, str]]:
    return frappe.get_all(
        "MMOS Hetzner Node",
        fields=["name", "node_id", "public_ip", "state"],
    )


@frappe.whitelist()
def set_node_state(node: str, state: str) -> dict[str, str]:
    frappe.db.set_value("MMOS Hetzner Node", node, "state", state)
    frappe.db.set_value("MMOS Hetzner Node", node, "last_seen", frappe.utils.data.now_datetime())
    return {"node": node, "state": state}
