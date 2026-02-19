"""Command-line interface (CLI) subpackage for the company package."""

from company_package.logic.orders import calculate_total, add_item, apply_discount, apply_vat
from company_package.data.storage import save_order


def display_order(order):
    """Display the order details in the CLI."""
    print(f"\nOrder ID: {order['id']}")
    print("Items:")
    for item in order["items"]:  # Display each item in the order with its quantity and price
        print(f" - {item['name']}: {item['quantity']} x £{item['price']:.2f}")

    print(f"Subtotal: £{order['subtotal']:.2f}")
    print(f"Discount: £{order['discount']:.2f}")
    print(f"VAT: £{order['vat']:.2f}")
    print(f"Total: £{order['total']:.2f}")


def run_checkout():
    """Run the checkout process in the CLI."""
    customer_name = input("Enter your name: ").strip() or "Customer"
    # Default to "Customer" if no name is entered
    order_id = customer_name.replace(" ", "_").lower()
    # Create order ID from customer name by replacing spaces with underscores and converting
    # to lowercase

    order = {
        "id": order_id,
        "items": [],  # Initialise an empty list to store items in the order
        "subtotal": 0.0,
        "discount": 0.0,
        "vat": 0.0,
        "total": 0.0,
    }

    while True:  # Loop to allow the user to enter multiple items until they type 'done'
        item_name = input("Item name (or 'done' to finish): ").strip()
        if item_name.lower() == "done":
            break

        price = input("Price: ").strip()
        quantity = input("Quantity: ").strip()

        try:
            price = float(price)  # Convert price to float
            quantity = int(quantity)  # Convert quantity to integer
        except ValueError:
            print("Invalid price or quantity. Try again.\n")
            continue

        # Add the item to the order using the add_item function from orders.py
        add_item(order, item_name, price, quantity)

    # Subtotal
    order["subtotal"] = calculate_total(order)

    # Discount
    discount_input = input("Discount % (0 for none): ").strip()
    try:
        # Convert discount input to float
        discount_percent = float(discount_input)
    except ValueError:
        discount_percent = 0.0  # Default to 0% if invalid input

    # Apply discount using the apply_discount function from orders.py
    after_discount, discount_amount = apply_discount(
        order["subtotal"], discount_percent / 100)
    order["discount"] = discount_amount

    # VAT + Final total
    final_total, vat_amount = apply_vat(after_discount)
    order["vat"] = vat_amount
    order["total"] = final_total

    display_order(order)  # Display the order details in the CLI

    filename = f"order_{order_id}.txt"
    # Save the order to a file using the save_order function from storage.py
    save_order(order, filename)
    print(f"\nSaved to: {filename}")

    return order
