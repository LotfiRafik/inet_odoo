# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PartnerCategory(models.Model):
    _inherit = 'res.partner.category'

    #Changing original String of the field "name" from 'Tag Name' To 'Category Name'
    name = fields.Char(string='Category Name', required=True, translate=True)