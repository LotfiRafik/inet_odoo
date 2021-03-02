# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import random
import uuid
import werkzeug

from odoo import api, exceptions, fields, models, _
from odoo.exceptions import AccessError
from odoo.osv import expression
from odoo.tools import is_html_empty


class Survey(models.Model):

    _inherit = 'survey.survey'


    def action_start_survey(self, answer=None):
        """ Open the website page with the survey form """
        self.ensure_one()
        url = '%s?%s' % (self.get_start_url(), werkzeug.urls.url_encode({'answer_token': answer and answer.access_token or None}))
        return {
            'type': 'ir.actions.act_url',
            'name': "Start Survey",
            'target': '_blank',
            'url': url,
        }

    def action_print_survey(self, answer=None):
        """ Open the website page with the survey printable view """
        self.ensure_one()
        url = '%s?%s' % (self.get_print_url(), werkzeug.urls.url_encode({'answer_token': answer and answer.access_token or None}))
        return {
            'type': 'ir.actions.act_url',
            'name': "Print Survey",
            'target': '_blank',
            'url': url
        }

    def action_result_survey(self):
        """ Open the website page with the survey results view """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'name': "Results of the Survey",
            'target': '_blank',
            'url': '/survey/results/%s' % self.id
        }

    def action_test_survey(self):
        ''' Open the website page with the survey form into test mode'''
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'name': "Test Survey",
            'target': '_blank',
            'url': '/survey/test/%s' % self.access_token,
        }

