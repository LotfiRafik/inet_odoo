#-*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging

_logger = logging.getLogger(__name__)


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patients Records'
    _order = 'id desc'

    name = fields.Char(string="Name", required=True)
    patient_age = fields.Integer(string="Age", track_visibility="always")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male','Male'),('female','Female')], String='Gender', default='male')
    image = fields.Binary(string="Image")

    age_group = fields.Selection([('major','Major'),('minor','Minor')], String='Age Group',
    compute="set_age_group")

    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('done','Done'),
        ('cancel','Cancel')
        ], String='Status', readonly=True, default="draft")


    @api.depends('patient_age')
    def set_age_group(self):
        for record in self:
            if record.patient_age < 18:
                record.age_group = 'minor'
            else:
                record.age_group = 'major'

    @api.constrains('patient_age')
    def check_age(self):
        _logger.info("2FA enable: REJECT CODE for")
        for record in self:
            if record.patient_age <= 5:
                raise exceptions.ValidationError("Age must be greater than 5")
    
    def action_confirm(self):
        for rec in self:
            rec.state = "confirm"

    def action_done(self):
        for rec in self:
            rec.state = "done"


    def test_cron_job(self):
        _logger.info("TEST_CRON_JOB")
        for rec in self:
            _logger.info("TEST_CRON_JOB")
            