app_name = "mmos_hetzner"
app_title = "MMOS Hetzner"
app_publisher = "MMOS"
app_description = "Gestisce server Hetzner per Press"
app_email = "dev@onekeyco.com"
app_license = "MIT"

app_version = "0.1.0"

after_install = "mmos_hetzner.install.after_install"

whitelisted_methods = [
    "mmos_hetzner.api.sync.list_nodes",
    "mmos_hetzner.api.sync.set_node_state",
]
