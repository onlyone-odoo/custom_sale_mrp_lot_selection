# Copyright 2025 Your Company <https://yourcompany.com>
# License AGPL-3.0 or later[](https://www.gnu.org/licenses/agpl).

from odoo import models


class StockRule(models.Model):
    """Inherit stock.rule to propagate component lot to MO vals."""

    _inherit = "stock.rule"

    def _prepare_mo_vals(
        self,
        product_id,
        product_qty,
        product_uom,
        location_dest_id,
        name,
        origin,
        company_id,
        values,
        bom,
    ):
        """Override to add component_lot_id from sale.order.line."""
        vals = super()._prepare_mo_vals(
            product_id,
            product_qty,
            product_uom,
            location_dest_id,
            name,
            origin,
            company_id,
            values,
            bom,
        )
        so = self.env["sale.order"].search([("name", "=", origin)], limit=1)
        if so:
            # Find matching SOL by product and qty (assume unique per SO; handle multiples if needed).
            sol = so.order_line.filtered(
                lambda l: l.product_id == product_id
                and l.product_uom_qty == product_qty
            )
            if sol:
                vals["component_lot_id"] = sol.component_lot_id.id
        return vals
