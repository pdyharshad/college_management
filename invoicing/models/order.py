from odoo import models, api, fields

class RestaurantOrder(models.Model):
    _inherit='restaurant.order'
    
    invoice_id=fields.Many2one('customer.invoice', 'Invoice')

    def create_invoice(self):
        vals={}
        invoice_obj=self.env['customer.invoice']
        vals={'customer_name':self.customer,
                'total_amount':self.order_total}
        invoice=invoice_obj.create(vals)
        self.write({'invoice_id':invoice.id})
