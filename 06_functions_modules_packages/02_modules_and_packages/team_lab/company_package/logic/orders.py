"""Orders subpackage for the company package."""


def calculate_total(order):
    """Calculate the total price of an order."""
    total = 0.0
    for item in order['items']:
        total += item['price'] * item['quantity']
    return total


def add_item(order, item_name, price, quantity):
    """Add an item to the order."""
    order['items'].append(
        {'name': item_name, 'price': price, 'quantity': quantity})

    return order


def apply_discount(total, discount_rate):
    """Apply a discount to the total price."""
    discount = total * discount_rate
    return total - discount, discount


def apply_vat(total, vat_rate=0.20):
    """Apply VAT to the total price."""
    vat = total * vat_rate
    return total + vat, vat
