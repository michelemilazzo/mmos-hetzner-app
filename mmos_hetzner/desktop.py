from frappe import _


def get_data():
    return [
        {
            "module_name": "MMOS Hetzner",
            "label": _("Setup Panel"),
            "type": "page",
            "link": "mmos-hetzner-setup",
            "icon": "octicon octicon-settings",
            "description": "Vista rapida per token, project ID e regione di default.",
        }
    ]
