# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsCrm(http.Controller):
#     @http.route('/inet_addons_crm/inet_addons_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_crm/inet_addons_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_crm.listing', {
#             'root': '/inet_addons_crm/inet_addons_crm',
#             'objects': http.request.env['inet_addons_crm.inet_addons_crm'].search([]),
#         })

#     @http.route('/inet_addons_crm/inet_addons_crm/objects/<model("inet_addons_crm.inet_addons_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_crm.object', {
#             'object': obj
#         })
