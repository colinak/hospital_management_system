#!usr/bin/env python3
# -*-coding: UTF-8 -*-

from odoo import models, fields, api, _

class MedicalSymptoms(models.Model):
    _name = 'medical.symptoms'
    _description = 'Sintomas'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string="Sintoma", required=True)

