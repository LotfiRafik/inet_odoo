# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsMail(http.Controller):
#     @http.route('/inet_addons_mail/inet_addons_mail/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_mail/inet_addons_mail/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_mail.listing', {
#             'root': '/inet_addons_mail/inet_addons_mail',
#             'objects': http.request.env['inet_addons_mail.inet_addons_mail'].search([]),
#         })

#     @http.route('/inet_addons_mail/inet_addons_mail/objects/<model("inet_addons_mail.inet_addons_mail"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_mail.object', {
#             'object': obj
#         })
