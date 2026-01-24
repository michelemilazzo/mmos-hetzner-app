frappe.pages['mmos-hetzner-setup'] = {
    on_page_load(wrapper) {
        const page = frappe.ui.make_app_page({
            parent: wrapper,
            title: 'MMOS Hetzner Setup Panel',
            single_column: true,
        });
        this.body = page.body.find('.layout-main-section').addClass('mmos-setup-panel');
        this.render_loading();
        this.refresh();
    },

    render_loading() {
        this.body.empty().append('<div class="text-muted">Caricamento setup Hetzner...</div>');
    },

    refresh() {
        frappe.call({
            method: 'frappe.client.get_single',
            args: { doctype: 'MMOS Hetzner Setup' },
        }).then(({ message }) => {
            if (!message) {
                this.body.html('<div class="alert alert-warning">Imposta prima il pannello di setup.</div>');
                return;
            }
            this.render_panel(message);
        });
    },

    render_panel(doc) {
        const rows = [
            ['Account di default', doc.account_name || '-'],
            ['Project ID', doc.project_id || '-'],
            ['Regione di default', doc.default_region || '-'],
            ['Monitoring role', doc.monitoring_role || '-'],
            ['Ultimo trigger', doc.last_sync || '-'],
            ['Note', doc.notes || '-'],
        ];

        const cards = rows
            .map(([label, value]) => `
                <div class="frappe-card">
                    <div class="frappe-card-body">
                        <strong>${label}</strong>
                        <p>${value}</p>
                    </div>
                </div>
            `)
            .join('');

        this.body.empty().append(`
            <div class="setup-panel-grid">
                ${cards}
            </div>
            <div class="setup-panel-actions">
                <button class="btn btn-primary btn-sm" id="trigger-sync">Trigger sync now</button>
            </div>
        `);

        this.body.find('#trigger-sync').on('click', () => {
            const button = $(this.body).find('#trigger-sync');
            button.prop('disabled', true).text('Avvio in corso...');
            frappe.call({
                method: 'mmos_hetzner.api.sync.trigger_sync',
            }).then(() => {
                button.prop('disabled', false).text('Trigger sync now');
                frappe.show_alert('Trigger registrato');
                this.refresh();
            }).catch(() => {
                button.prop('disabled', false).text('Trigger sync now');
            });
        });
    },
};
