# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class inet_addons_mail(models.Model):
#     _name = 'inet_addons_mail.inet_addons_mail'
#     _description = 'inet_addons_mail.inet_addons_mail'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
