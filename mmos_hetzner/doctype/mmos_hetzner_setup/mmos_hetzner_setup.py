import frappe
from frappe.model.document import Document


class MMOSHetznerSetup(Document):
    def validate(self) -> None:
        if self.token and len(self.token) < 8:
            frappe.throw("Inserisci un token API valido, almeno 8 caratteri.")
