##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def get_product_uoms(self, use=False):
        if use == 'purchase' and self.uom_ids.filtered('purchase_ok'):
            return self.uom_ids.filtered('purchase_ok').mapped('uom_id')
        return super().get_product_uoms(use=use)
