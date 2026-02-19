"""Data storage subpackage for the company package."""


def save_order(order, filename):
    """Save the order to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Order ID: {order['id']}\n")  # Write order ID to file
        f.write("Items:\n")
        for item in order["items"]:  # Write each item in the order to the file
            f.write(
                f" - {item['name']}: {item['quantity']} x £{item['price']:.2f}\n")

        f.write(f"Subtotal: £{order['subtotal']:.2f}\n")
        f.write(f"Discount: £{order['discount']:.2f}\n")
        f.write(f"VAT: £{order['vat']:.2f}\n")
        f.write(f"Total: £{order['total']:.2f}\n")
