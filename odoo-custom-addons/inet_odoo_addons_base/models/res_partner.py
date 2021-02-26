# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class Partner(models.Model):
    _inherit = 'res.partner'
    
    employee_id = fields.Many2one('hr.employee', string='Related employee', index=True)

    @api.model
    def default_get(self, default_fields):
        """Set Algeria as default country of a partner"""
        values = super().default_get(default_fields)
        values['country_id'] = 62
        return values


class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    #Changing original String of the field "name" from 'Tag Name' To 'Category Name'
    name = fields.Char(string='Category Name', required=True, translate=True)


    