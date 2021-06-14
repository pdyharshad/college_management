# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Invoicing',
    'version': '0.1',
    'summary': 'Customer Invoicing',
    'description': """This module is for training purpose on Invoicing
    """,
    'depends': ['base','hotel_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/invoice.xml',
        'views/order.xml',
    ],
    'installable': True,
    'auto_install': False
}
