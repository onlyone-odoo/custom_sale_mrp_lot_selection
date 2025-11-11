# License AGPL-3.0 or later[](https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MrpProduction(models.Model):
    """Inherit mrp.production to hold component lot and restrict raw move."""

    _inherit = "mrp.production"

    component_lot_id = fields.Many2one(
        comodel_name="stock.lot",
        string="Component Lot",
        help="Lot of the main component propagated from sale order line.",
    )

    def _get_move_raw_values(self, bom_line, line_data):
        """Override to restrict raw move to the selected component lot."""
        vals = super()._get_move_raw_values(bom_line, line_data)
        if (
            self.component_lot_id
            and bom_line.product_id == self.component_lot_id.product_id
        ):
            vals["restrict_lot_id"] = self.component_lot_id.id
        return vals
