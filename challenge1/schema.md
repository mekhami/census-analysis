
## `widget` Table

This table keeps records of widgets. A record is a unique combination of (widget, supplier_id), and includes the unit cost that the widget was purchased for in bulk, as well as the locations where it is stored.

Field | Type | Default | Indexed | Unique | Description
------|------|---------|---------|--------|-------------
`id` | BIGINT | None | True | True | A unique identifier for this widget from this supplier
`widget` | String | None | True | False | The name of widget
`unit_cost` | DECIMAL(7, 2) | 0.00 | False | False | The acquisition cost per unit of this widget from a particular supplier
`supplier_id` | BIGINT | None | True | False | A foreign key for `supplier.id`. This is the supplier providing this widget at this `unit_cost`
`warehouses` | SET('AUS', 'ATL', 'MSP') | None | True | False | One or more warehouses that this widget is stored in. These are foreign keys for `warehouse.id`
`qty` | BIGINT | 0 | False | False | The total number of this widget that we have in inventory accross all warehouses

## `price` Table

Field | Type | Default | Indexed | Unique | Description
------|------|---------|---------|--------|-------------
`id` | BIGINT | None | True | True | A unique identifier for this price agreement
`widget_id` | BIGINT | None | True | False | This is a foreign key for `widget.id`. This is the widget being packaged and sold at this price.
`package_type` | String | None | False | False | The type of packagine the widget comes in. e.g. "box" or "bag"
`package_qty` | SMALLINT | 1 | False | False | The number of widgets that come in each package
`price` | DECIMAL(7, 2) | 0.00 | False | False | The sale price of this package of widgets
`customer_id` | BIGINT | None | True | False | A foreign key for `customer.id`. This is the customer who we have promised this price-point for this package of widgets
`min_qty` | BIGINT | 0 | False | False | The minimum order quantity to receive this price

## `supplier` Table

Field | Type | Default | Indexed | Unique | Description
------|------|---------|---------|--------|-------------
`id` | BIGINT | None | True | True | A unique identifier for this supplier
`name` | VARCHAR(255) | None | False | The legal name of this supplier
`phone` | VARCHAR(255) | None | False | True | The phone number of this supplier
`address` | VARCHAR(255) | None | False | False | The street address for this supplier. e.g. 123 Main St.
`city` | VARCHAR(255) | None | False | False | The city, township, or municipality for this supplier. e.g. Austin
`province` | VARCHAR(255) | None | False | False | The state or provine for this supplier. e.g. Texas
`country` | CHAR(3) | None | False | False | The ISO 3166-1 alpha-3 country code for this supplier. e.g. USA
`postal_code` | VARCHAR(10) | None | False | False | The postal code for the supplier.
`gps` | POINT | None | True | False | The lat/long coordinates for the supplier

## `customer` Table

Field | Type | Default | Indexed | Unique | Description
------|------|---------|---------|--------|-------------
`id` | BIGINT | None | True | True | A unique identifier for this customer
`name` | VARCHAR(255) | None | False | The legal name of this customer
`phone` | VARCHAR(255) | None | False | True | The phone number of this customer
`address` | VARCHAR(255) | None | False | False | The street address for this customer. e.g. 123 Main St.
`city` | VARCHAR(255) | None | False | False | The city, township, or municipality for this customer. e.g. Austin
`province` | VARCHAR(255) | None | False | False | The state or provine for this customer. e.g. Texas
`country` | CHAR(3) | None | False | False | The ISO 3166-1 alpha-3 country code for this customer. e.g. USA
`postal_code` | VARCHAR(10) | None | False | False | The postal code for the customer.
`gps` | POINT | None | True | False | The lat/long coordinates for the customer

## `warehouse` Table

Field | Type | Default | Indexed | Unique | Description
------|------|---------|---------|--------|-------------
`id` | CHAR(3) | None | True | True | A unique identifier for this warehouse. e.g. AUS
`name` | VARCHAR(255) | None | False | The legal name of this warehouse
`phone` | VARCHAR(255) | None | False | True | The phone number of this warehouse
`address` | VARCHAR(255) | None | False | False | The street address for this warehouse. e.g. 123 Main St.
`city` | VARCHAR(255) | None | False | False | The city, township, or municipality for this warehouse. e.g. Austin
`province` | VARCHAR(255) | None | False | False | The state or provine for this warehouse. e.g. Texas
`country` | CHAR(3) | None | False | False | The ISO 3166-1 alpha-3 country code for this warehouse. e.g. USA
`postal_code` | VARCHAR(10) | None | False | False | The postal code for the warehouse.
`gps` | POINT | None | True | False | The lat/long coordinates for the warehouse

## `invoice` Table

Field | Type | Default | Indexed | Unique | Description
------|------|---------|---------|--------|-------------
`id` | BIGINT | None | True | False | Once invoice may be composed of several rows if the customer is purchasing more than one type of item at a time. All rows which share an `id` are part of the same invoice
`price_id` | BIGINT | None | False | False | A foreign key for `price.id`. This is the price agreement for our price for a particular widget to a particular customer
`date_issued` | DATE | None | True | False | The date the invoice was issued to the customer
`date_due` | DATE | None | True | False | The date this incoice is due to be paid by the customer
`paid` | BIT(1) | 0 | True | False | Whether or not this invoice has been paid. 0 for no, 1 for yes.