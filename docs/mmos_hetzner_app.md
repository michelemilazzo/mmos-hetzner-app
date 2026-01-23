# MMOS Hetzner app

L'app `mmos_hetzner` fornisce doc type e API per gestire i server Hetzner dentro Press/Dev. È pensata per essere usata insieme a job Frappe che sincronizzano lo stato tramite Hetzner Cloud API.

## DocType principali
- **MMOS Hetzner Account**: memorizza token, project id e regione. Puoi usare Fields `token` come Password e `status` per tracciare i progetti attivi.
- **MMOS Hetzner Node**: rappresenta un server con IP, tipo (Cloud/Dedicated/Storage) e stato operativo; `last_seen` viene aggiornato quando un job ne ripesca lo stato.

## API
- `mmos_hetzner.api.sync.list_nodes`: restituisce `name`, `node_id`, `public_ip`, `state`.
- `mmos_hetzner.api.sync.set_node_state`: aggiorna manualmente lo `state` e `last_seen` (utilizzata quando un job di monitoring scopre un servizio offline).

## Installazione
```bash
cd /tmp/zfsv3/nvme11/_michelemilazzo/data/mmos-dev
bench get-app ./apps/mmos_hetzner
bench --site dev.onekeyco.com install-app mmos_hetzner
bench --site dev.onekeyco.com migrate
```

## Workflow operativo
1. Aggiungi gli account Hetzner con token e project ID.
2. Registra i server e associa un `role` (es. `gateway`, `monitor`).
3. Schedula un job per chiamare `Hetzner Cloud API` (es. `hcloud server list`) e popolare `MMOS Hetzner Node` aggiornando `last_seen`.
4. Usa `frappe.call` verso le API whitelisted dal resto della piattaforma (Press Desk, Notion, network status).
