from odoo import models, fields

class Product(models.Model):
    _inherit = 'product.template'

    # New field preferred_seller
    preferred_seller = fields.Many2one("res.partner",string='Fournisseur préféré')