from odoo import models, fields, api, exceptions
import re
from datetime import timedelta


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'hms.patient'
    _rec_name = 'first_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    email = fields.Char()
    age = fields.Integer(compute='_compute_age', store=True)
    department_id = fields.Many2one('hms.department', string='Department')
    department_capacity = fields.Integer(related='department_id.capacity')
    doctors_ids = fields.Many2many('hms.doctor', string='Doctors')
    state = fields.Selection(
        [('undetermined', 'Undetermined'), ('good', 'Good'), ('fair', 'Fair'), ('serious', 'Serious')],
        default="undetermined")
    log_history_ids = fields.One2many('hms.log_history', 'patient_id')

    _sql_constraints = [
        (
            "unique_email",
            "UNIQUE(email)",
            "Email already exist"
        )
    ]

    @api.constrains('email, vat')
    def check_email_valid(self):
        email_pattern = r"^[A-z0-9_\.]+@[A-z0-9_\.]+\.(com|net|org)"
        for record in self:
            is_email = re.search(email_pattern, record.email)
            if not is_email:
                raise exceptions.ValidationError("Invalid Email Address")

    def set_state_undetermined(self):
        self.state = 'undetermined'

    def set_state_fair(self):
        self.state = 'fair'

    def set_state_good(self):
        self.state = 'good'

    def set_state_serious(self):
        self.state = 'serious'

    def write(self, vals):
        if 'state' in vals:
            new_state = vals['state']
            self.env['hms.log_history'].create({
                'patient_id': self.id,
                'description': f"State changed to {new_state}"
            })
        super().write(vals)

    @api.onchange('age')
    def on_change_age(self):
        if self.age:
            if self.age < 30:
                self.pcr = True
                return {
                    'warning': {
                        'title': 'Age less than 30',
                        'message': 'The pcr has been checked'
                    }
                }

    @api.depends('birth_date')
    def _compute_age(self):
        current_date = fields.Date.today()
        for record in self:
            if record.birth_date:
                result = current_date.year - record.birth_date.year
                record.age = result


class Department(models.Model):
    _name = 'hms.department'
    _description = 'hms.department'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_ids = fields.One2many('hms.patient', 'department_id')


class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'hms.doctor'

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Binary()


class LogHistory(models.Model):
    _name = 'hms.log_history'
    _description = 'log history of patient'

    patient_id = fields.Many2one('hms.patient', readonly=True)
    patient_name = fields.Char(compute='_get_patient_name', store=True)
    description = fields.Text()

    @api.depends('patient_id')
    def _get_patient_name(self):
        for rec in self:
            rec.patient_name = f"{rec.patient_id.first_name} {rec.patient_id.last_name}"


class Customers(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one('hms.patient')

    @api.constrains('email')
    def confirm_email(self):
        for record in self:
            if self.env['hms.patient'].search([('email', '=', record.email)]):
                raise exceptions.UserError("Email already exist")

    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise exceptions.UserError("Cannot delete a customer linked to a patient")
        return super().unlink()
