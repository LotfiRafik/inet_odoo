# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Users(models.Model):

    _inherit = 'res.users'

    @api.model
    def default_get(self, default_fields):
        """Set parent_id of the partner related to the user to the default partner of the main company"""
        values = super().default_get(default_fields)
        values['parent_id'] = 1
        return values

