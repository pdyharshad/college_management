from odoo import models, fields

class CustomerInvoice(models.Model):
    _name='customer.invoice'

    customer_name=fields.Char('Customer')
    total_amount=fields.Float('Total')


