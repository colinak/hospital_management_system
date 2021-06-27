#!usr/bin/env python3
# -*-coding: UTF-8 -*-

{
    'name': "Hospital Management System",
    'author': "Kewitz Colina",
    'summary': 'Management Hospital',
    'description': 'Management Hospital',
    'category': 'Hospital',
    'depends': [
        'base',
        'hr',
        'product',
    ],
    'data': [
        'security/appointment/ir.model.access.csv',
        'security/diseases/ir.model.access.csv',
        'security/symptoms/ir.model.access.csv',
        'views/menu_config_view.xml',
        'views/medical_appointment_view.xml',
        'views/diseases_view.xml',
        'views/symptoms_view.xml',
        'views/res_partner_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
