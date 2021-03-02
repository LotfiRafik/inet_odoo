# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsSurvey(http.Controller):
#     @http.route('/inet_addons_survey/inet_addons_survey/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_survey/inet_addons_survey/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_survey.listing', {
#             'root': '/inet_addons_survey/inet_addons_survey',
#             'objects': http.request.env['inet_addons_survey.inet_addons_survey'].search([]),
#         })

#     @http.route('/inet_addons_survey/inet_addons_survey/objects/<model("inet_addons_survey.inet_addons_survey"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_survey.object', {
#             'object': obj
#         })
