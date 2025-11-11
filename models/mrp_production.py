# Copyright 2025 Your Company <https://yourcompany.com>
# License AGPL-3.0 or later[](https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class MrpProduction(models.Model):
    """Inherit mrp.production to hold component lot and pre-create move line."""

    _inherit = "mrp.production"

    component_lot_id = fields.Many2one(
        comodel_name="stock.lot",
        string="Component Lot",
        help="Lot of the main component propagated from sale order line.",
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Override to pre-create a draft move line with the selected lot."""
        mos = super().create(vals_list)
        for mo in mos:
            if mo.component_lot_id:
                # Find the raw move for the component product
                component_moves = mo.move_raw_ids.filtered(
                    lambda m: m.product_id == mo.component_lot_id.product_id
                )
                if component_moves:
                    # Assume first move is the main one; tweak if multi-moves per component
                    move = component_moves[0]
                    self.env["stock.move.line"].create(
                        {
                            "move_id": move.id,
                            "product_id": move.product_id.id,
                            "lot_id": mo.component_lot_id.id,
                            "product_uom_id": move.product_uom.id,
                            "product_uom_qty": 0,  # Reserved qty set on _action_assign
                            "qty_done": 0,
                            "location_id": move.location_id.id,
                            "location_dest_id": move.location_dest_id.id,
                            "state": "draft",
                            "company_id": mo.company_id.id,
                        }
                    )
        return mos
