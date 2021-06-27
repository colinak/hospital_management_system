#!usr/bin/env python3
# -*-coding: UTF-8 -*-

from odoo import models, fields, api, _

class TreatmentsPerformed(models.Model):
    _name = 'treatments.performed'
    _description = 'Tratamientos'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string="Description")
    partner_id = fields.Many2one(
        'res.partner',
        string="Pasiente"
    )
