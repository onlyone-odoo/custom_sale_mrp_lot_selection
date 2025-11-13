===========
custom_sale_mrp_lot_selection
===========

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2| |badge3|

This module extends the functionality of Sale and MRP to allow selecting the lot of the main BOM component directly from the sale order line, and propagates it to the manufacturing order to restrict the raw material move to that specific lot.

**Table of contents**

.. contents::
   :local:

Install
=======

To install this module, you need to:

1. Clone the module into your addons path.
2. Update the apps list in Odoo (Apps > Update Apps List).
3. Search for "Custom Sale MRP Lot Selection" and install it.
4. Ensure products are configured as "Manufacturable" with traceability "By Lots" and appropriate BOMs (e.g., variant for "Recorte" consuming "Rollo Completo").

No additional non-Python dependencies are required.

Configure
=========

To configure this module, you need to:

1. Go to **Inventory > Configuration > Settings** and enable "Lots & Serial Numbers".
2. For the sold product (e.g., "Recorte"), ensure it has a route "Manufacture" and a BOM where the main component (e.g., "Rollo Completo") is the first line.
3. Optionally, use Studio to add custom fields to stock.lot for dimensions (e.g., remaining width/length).

No further configuration is needed for basic usage.

Usage
=====

1. Go to **Sales > Orders > Sales Orders** and create a new quotation.
2. Add a line for the manufacturable product (e.g., "Recorte" with qty in m²).
3. In the "Component Lot" field (appears after product selection if BOM exists), select the desired lot from available ones with stock > 0.
4. Confirm the sales order to trigger the manufacturing order (MO).
5. In the generated MO (**Manufacturing > Operations > Manufacturing Orders**), the component line will have the selected lot pre-restricted (visible in "Serial Numbers/Lots" column; no manual selection needed).
6. Proceed with production: the operario consumes from the specified lot, ensuring traceability.

For multi-location setups (e.g., lots split across factories), the restriction applies globally to the lot, reserving from the location with available stock.

Known issues / Roadmap
======================

* None currently known.
* Roadmap: Add wizard for lot selection with dimension checks (e.g., sufficient remaining width/length); support multi-components via configurable BOM line index.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/YourOrg/custom_sale_mrp_lot_selection/issues>`__
Although in the past bugs were reported on `Answer <https://github.com/OCA/maintainer-tools/issues>`__.

In case of trouble, please check there if your issue has already been reported. If you spotted it first, help us to smash it! If you want to contribute to the module, please create a `Pull Request on GitHub <https://github.com/YourOrg/custom_sale_mrp_lot_selection/pulls>`__.

* Help Contact: support@yourcompany.com
* Website: https://yourcompany.com

Credits
=======

Authors
~~~~~~~

* Your Company

Contributors
~~~~~~~~~~~~

* `Your Company <https://yourcompany.com/>`_

  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Your Company.
