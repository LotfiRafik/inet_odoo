# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsHrRecruitment(http.Controller):
#     @http.route('/inet_addons_hr_recruitment/inet_addons_hr_recruitment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_hr_recruitment/inet_addons_hr_recruitment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_hr_recruitment.listing', {
#             'root': '/inet_addons_hr_recruitment/inet_addons_hr_recruitment',
#             'objects': http.request.env['inet_addons_hr_recruitment.inet_addons_hr_recruitment'].search([]),
#         })

#     @http.route('/inet_addons_hr_recruitment/inet_addons_hr_recruitment/objects/<model("inet_addons_hr_recruitment.inet_addons_hr_recruitment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_hr_recruitment.object', {
#             'object': obj
#         })
