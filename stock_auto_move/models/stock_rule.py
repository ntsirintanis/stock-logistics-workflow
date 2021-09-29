# Copyright 2014-2015 NDP Systèmes (<https://www.ndp-systemes.fr>)
# Copyright 2020 ACSONE SA/NV (<https://acsone.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class StockRule(models.Model):
    _inherit = "stock.rule"

    auto_move = fields.Boolean(
        "Automatic move",
        help="If this option is selected, the generated move will be "
        "automatically processed as soon as the products are available. "
        "This can be useful for situations with chained moves where we "
        "do not want an operator action.",
    )

    def _get_stock_move_values(self, *procurement):
        res = super()._get_stock_move_values(*procurement)
        res.update({"auto_move": self.auto_move})
        return res

    @api.model
    def _apply(self, move):
        """Set auto move to the new move created by push rule."""
        move.auto_move = self.auto == "transparent"
        return super()._apply(move)
