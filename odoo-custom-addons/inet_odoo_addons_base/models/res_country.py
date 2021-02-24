# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CountryState(models.Model):
    _inherit = "res.country.state"
    _order = 'name'

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, "{} ({})".format(record.name, record.code)))
        return result
