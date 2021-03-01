# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsHrContract(http.Controller):
#     @http.route('/inet_addons_hr_contract/inet_addons_hr_contract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_hr_contract/inet_addons_hr_contract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_hr_contract.listing', {
#             'root': '/inet_addons_hr_contract/inet_addons_hr_contract',
#             'objects': http.request.env['inet_addons_hr_contract.inet_addons_hr_contract'].search([]),
#         })

#     @http.route('/inet_addons_hr_contract/inet_addons_hr_contract/objects/<model("inet_addons_hr_contract.inet_addons_hr_contract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_hr_contract.object', {
#             'object': obj
#         })
