# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsContacts(http.Controller):
#     @http.route('/inet_addons_contacts/inet_addons_contacts/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_contacts/inet_addons_contacts/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_contacts.listing', {
#             'root': '/inet_addons_contacts/inet_addons_contacts',
#             'objects': http.request.env['inet_addons_contacts.inet_addons_contacts'].search([]),
#         })

#     @http.route('/inet_addons_contacts/inet_addons_contacts/objects/<model("inet_addons_contacts.inet_addons_contacts"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_contacts.object', {
#             'object': obj
#         })
