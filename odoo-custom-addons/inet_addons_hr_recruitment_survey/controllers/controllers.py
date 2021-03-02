# -*- coding: utf-8 -*-
# from odoo import http


# class InetAddonsHrRecruitmentSurvey(http.Controller):
#     @http.route('/inet_addons_hr_recruitment_survey/inet_addons_hr_recruitment_survey/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inet_addons_hr_recruitment_survey/inet_addons_hr_recruitment_survey/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inet_addons_hr_recruitment_survey.listing', {
#             'root': '/inet_addons_hr_recruitment_survey/inet_addons_hr_recruitment_survey',
#             'objects': http.request.env['inet_addons_hr_recruitment_survey.inet_addons_hr_recruitment_survey'].search([]),
#         })

#     @http.route('/inet_addons_hr_recruitment_survey/inet_addons_hr_recruitment_survey/objects/<model("inet_addons_hr_recruitment_survey.inet_addons_hr_recruitment_survey"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inet_addons_hr_recruitment_survey.object', {
#             'object': obj
#         })
