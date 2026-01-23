import frappe


def after_install() -> None:
    if frappe.db.exists("MMOS Hetzner Account", "demo-project"):
        return

    frappe.get_doc(
        {
            "doctype": "MMOS Hetzner Account",
            "account_name": "demo-project",
            "project_id": "demo",
            "status": "Draft",
        }
    ).insert(ignore_permissions=True)
