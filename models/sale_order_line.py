# Copyright 2025 Your Company <https://yourcompany.com>
# License AGPL-3.0 or later[](https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    """Inherit sale.order.line to add component lot selection."""

    _inherit = "sale.order.line"

    component_lot_id = fields.Many2one(
        comodel_name="stock.lot",
        string="Component Lot",
        domain="[('product_id', '=', component_product_id), ('product_qty', '>', 0)]",
        help="Select the lot of the main component to use in manufacturing.",
    )
    component_product_id = fields.Many2one(
        comodel_name="product.product",
        compute="_compute_component_product_id",
        store=False,
    )

    @api.depends("product_id")
    def _compute_component_product_id(self):
        """Compute the main component product from the BOM."""
        for line in self:
            line.component_product_id = False
        products = self.mapped("product_id")
        if products:
            boms = self.env["mrp.bom"]._bom_find(products)
            for line in self:
                bom = boms.get(line.product_id)
                if bom and bom.bom_line_ids:
                    # Assume first component is the main one (e.g., 'Rollo Completo'); tweak if needed.
                    line.component_product_id = bom.bom_line_ids[0].product_id
