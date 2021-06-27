#!usr/bin/env python3
# -*-coding: UTF-8 -*-

from odoo import models, fields, api, _

class MedicalAppointment(models.Model):
    _name = 'medical.diseases'
    _description = 'Diseases'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string="Enfermedad", required=True)
