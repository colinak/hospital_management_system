#!usr/bin/env python3
# -*-coding: UTF-8 -*-

from odoo import models, fields, api, _

class MedicalAppointment(models.Model):
    _name = 'medical.appointment'
    _description = 'Citas Medicas'
    _rec_name = 'name'
    _order = 'id'

    name = fields.Char(string="N° Cita")

    patient_id = fields.Many2one(
        'res.partner',
        string="Paciente"
    )
    doctor_id = fields.Many2one(
        'hr.employee',
        string="Doctor"
    )
    fecha_cita = fields.Date(
        string="Fecha Cita"
    )
    patient_status = fields.Char(
        string="Estado de Paciente"
    )
    type_appointment = fields.Selection(
        [('preventiva', 'Preventiva'),
            ('rutina', 'Rutinaria'),
            ('cirujia', 'Cirujias')]
    )

