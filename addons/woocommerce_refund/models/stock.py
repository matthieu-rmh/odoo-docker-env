from odoo import models, fields
from odoo.exceptions import UserError
# from woocommerce import API

class Stock(models.Model):
    _inherit = 'stock.picking'


    def trigger_woo_refund_call(self):
        raise UserError("Woo API refund call")

        wcapi = API(
            url=self.env['ir.config_parameter'].sudo().get_param('woocommerce_url'),
            consumer_key=self.env['ir.config_parameter'].sudo().get_param('woocommerce_consumer_key'),
            consumer_secret=self.env['ir.config_parameter'].sudo().get_param('woocommerce_consumer_secret'),
            version="wc/v3"
        )

        refund_data = {
            "order_id": self.woo_order_id,
            "amount": str(sum(line.quantity * line.product_id.lst_price for line in self.product_return_moves)),
            "reason": "Retour client",
            "refunded_by": self.env.user.id,
            "line_items": [
                {
                    "product_id": line.product_id.woo_product_id,
                    "quantity": line.quantity,
                } for line in self.product_return_moves
            ]
        }

        response = wcapi.post("orders/{}/refunds".format(self.woo_order_id), refund_data)

        if response.status_code == 201:
            self.woo_refund_id = response.json().get('id')
            self.message_post(body="Remboursement créé sur WooCommerce avec l'ID: {}".format(self.woo_refund_id))
        else:
            raise UserError("Erreur lors de la création du remboursement sur WooCommerce: {}".format(response.text))