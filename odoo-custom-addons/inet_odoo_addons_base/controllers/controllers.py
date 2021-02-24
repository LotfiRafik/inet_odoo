# -*- coding: utf-8 -*-
# from odoo import http


# class InetOdooAddonsBase(http.Controller):
#     @http.route('/inet_odoo_addons_base/inet_odoo_addons_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_odoo_addons_base/inet_odoo_addons_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_odoo_addons_base.listing', {
#             'root': '/inet_odoo_addons_base/inet_odoo_addons_base',
#             'objects': http.request.env['inet_odoo_addons_base.inet_odoo_addons_base'].search([]),
#         })

#     @http.route('/inet_odoo_addons_base/inet_odoo_addons_base/objects/<model("inet_odoo_addons_base.inet_odoo_addons_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_odoo_addons_base.object', {
#             'object': obj
#         })
