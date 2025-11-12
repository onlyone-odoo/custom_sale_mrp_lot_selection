{
    "name": "Custom Sale MRP Lot Selection",
    "summary": "Allow selecting component lot from sale order line for manufacturing.",
    "description": """
        This module extends sale.order.line to add a field for selecting the lot of the main component 
        in the BOM, and propagates it to the manufacturing order for restriction on raw moves.
    """,
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "category": "Manufacturing",
    "version": "18.0.3.1.1",
    "depends": ["sale", "mrp", "stock"],
    "data": ["views/sale_order_line_views.xml"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
