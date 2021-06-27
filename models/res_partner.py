#!usr/bin/env python3
# -*-coding: UTF-8 -*-

from odoo import models, fields, api, _

class ResPartner(models.Model):
    _inherit = 'res.partner'


    def _compute_affiliate_number(self):
        count

    affiliate_number = fields.Integer(
        string=u"Número de afiliado",
        help="affiliate number"
    )
    genero = fields.Selection(
        [
            ('f', 'Femenino'),
            ('m', 'Masculino'),
            ('u', 'Indefinido')    
        ],
        string="Genero"
    )
    birth_date = fields.Date(
        string="Fecha de Nacimiento"
    )
    edad = fields.Integer(string="Edad")
    n_assisted_consultations = fields.Integer(
        string="N° Consultations"
    )
    status_marital = fields.Selection(
        [('soltero_a', 'Soltero (@)'),
         ('casado_a', 'Casado (@)'),
         ('viudo_a', 'Viudo (@)'),
         ('divorciado_a', 'Divorciado (@)'),
        ],
        string="Estado Marital"
    )
    treatments_performed = fields.One2many(
        'treatments.performed',
        'partner_id',
        string="Tratamientos Realizados"
    )
    appointment = fields.One2many(
        'medical.appointment',
        'patient_id',
        string="Citas Medicas"
    )
