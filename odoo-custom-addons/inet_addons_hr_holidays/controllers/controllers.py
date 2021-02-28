# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsHrHolidays(http.Controller):
#     @http.route('/inet_addons_hr_holidays/inet_addons_hr_holidays/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_hr_holidays/inet_addons_hr_holidays/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_hr_holidays.listing', {
#             'root': '/inet_addons_hr_holidays/inet_addons_hr_holidays',
#             'objects': http.request.env['inet_addons_hr_holidays.inet_addons_hr_holidays'].search([]),
#         })

#     @http.route('/inet_addons_hr_holidays/inet_addons_hr_holidays/objects/<model("inet_addons_hr_holidays.inet_addons_hr_holidays"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_hr_holidays.object', {
#             'object': obj
#         })
