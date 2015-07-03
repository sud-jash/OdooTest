# -*- coding: utf-8 -*-

from openerp import models, fields, api

class banker(models.Model):
	_name = 'banker.banker'
	name = fields.Char()
	phone_num = fields.Many2one('res.partner', string="Phone number")
#	name = fields.Char(string="Title", required=True)
#   	description = fields.Text()
