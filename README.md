# MMOS Hetzner

`mmos_hetzner` è l'app Frappe per governare i server Hetzner (Cloud, Dedicated, Storage Boxes) utilizzati da Press/MMOS. Tiene traccia di account API, risorse attive e fornisce API per sincronizzare il parco server col backend.

## Highlights
- `MMOS Hetzner Account`: conserva token, tipo di progetto, stato del progetto.
- `MMOS Hetzner Node`: memorizza server, IP, ruolo e stato operativo (`Active`, `Maintenance`, `Offline`).
- `MMOS Hetzner Setup`: single DocType che raccoglie token, project ID, default region e monitoring role in un unico pannello.
- API whitelisted per estrarre riepiloghi e aggiornare regolarmente lo stato.
- `after_install` crea un account demo per evitare installazioni a zero record.

## Installazione
```bash
cd /tmp/zfsv3/nvme11/_michelemilazzo/data/mmos-dev
bench get-app ./apps/mmos_hetzner
bench --site dev.onekeyco.com install-app mmos_hetzner
bench --site dev.onekeyco.com migrate
```

## Pannello di setup
1. Apri `MMOS Hetzner Setup` e definisci il `Default Account`, `Project ID`, `API Token`, `Default Region` e `Monitoring Role`.
2. Usa questi valori nei job che interrogano le Hetzner Cloud API (es. `hcloud server list`).

## Operazioni tipiche
1. Registra le API key/Project ID su `MMOS Hetzner Account`.
2. Inserisci server e assegnali a `role` (`gateway`, `storage`, `monitor`).
3. Usa job schedulati (es. `bench execute mmos_hetzner.api.sync.refresh_nodes`) per aggiornare `last_seen` e segnalare anomalie.
