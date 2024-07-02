from odoo import models, fields, api


class MedicineOrder(models.Model):
    _inherit = "sale.order"

    commercial_name = fields.Char(string='Commercial name')
    side_effects = fields.Text(string="Side effects")
    directions_for_use = fields.Text(string="Directions for use")
    department_id = fields.Many2one(
        comodel_name='hms.department',
        string='Department',
        ondelete='restrict',
    )
    invoice_id = fields.Many2one('account.move', string="Invoice")


class MedicineInvoice(models.Model):
    _inherit = "account.move"

    code = fields.Char(string='Code', required=True, index=True)
    medicine_orders_id = fields.One2many(
        'sale.order',
        'invoice_id',
        string='Medicine',
        ondelete='restrict',
    )
    doctor_id = fields.Many2one(
        comodel_name='hms.doctor',
        string='The doctor in charge',
        ondelete='restrict',
        )

    patient_id = fields.Many2one(
        comodel_name='hms.patient',
        string='Patient',
        ondelete='restrict',
    )
