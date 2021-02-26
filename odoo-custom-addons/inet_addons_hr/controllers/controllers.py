# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsHr(http.Controller):
#     @http.route('/inet_addons_hr/inet_addons_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_hr/inet_addons_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_hr.listing', {
#             'root': '/inet_addons_hr/inet_addons_hr',
#             'objects': http.request.env['inet_addons_hr.inet_addons_hr'].search([]),
#         })

#     @http.route('/inet_addons_hr/inet_addons_hr/objects/<model("inet_addons_hr.inet_addons_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_hr.object', {
#             'object': obj
#         })
