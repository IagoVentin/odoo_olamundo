# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odoo_olamundo(models.Model):
    _name = 'odoo_olamundo.odoo_olamundo'
    _description = 'odoo_olamundo.odoo_olamundo'

    name = fields.Char(string="Ola Mundos:")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
