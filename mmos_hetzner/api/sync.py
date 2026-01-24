import frappe
from frappe.utils import data


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


@frappe.whitelist()
def trigger_sync() -> dict[str, str]:
    doc = frappe.get_single("MMOS Hetzner Setup")
    doc.last_sync = data.now_datetime()
    doc.save(ignore_permissions=True)
    frappe.msgprint("Trigger Hetzner registrato.")
    return {"last_sync": doc.last_sync}
