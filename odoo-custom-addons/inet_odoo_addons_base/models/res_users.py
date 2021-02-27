# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Users(models.Model):

    _inherit = 'res.users'

    @api.model
    def default_get(self, default_fields):
        """Set Algeria as default country of a partner"""
        values = super().default_get(default_fields)
        values['parent_id'] = 1
        return values

