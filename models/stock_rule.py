# Copyright 2025 Your Company <https://yourcompany.com>
# License AGPL-3.0 or later[](https://www.gnu.org/licenses/agpl).

from odoo import models
import logging  # Para el log temporal

_logger = logging.getLogger(__name__)  # Logger para debug


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
        _logger.info(
            f"Preparing MO vals for origin {origin}, product {product_id.id}, qty {product_qty}"
        )
        so = self.env["sale.order"].search([("name", "=", origin)], limit=1)
        if so:
            _logger.info(f"Found SO {so.name} (id {so.id})")
            sol = so.order_line.filtered(
                lambda l: l.product_id == product_id
                and l.product_uom_qty == product_qty
            )
            if sol:
                sol = sol[0]  # Explicit first if multiple (rare)
                vals["component_lot_id"] = sol.component_lot_id.id
                _logger.info(
                    f"Found SOL id {sol.id}, setting component_lot_id to {sol.component_lot_id.id}"
                )
            else:
                _logger.info("No matching SOL found for product/qty")
        else:
            _logger.info("No SO found for origin")
        _logger.info(f"Final MO vals component_lot_id: {vals.get('component_lot_id')}")
        return vals
