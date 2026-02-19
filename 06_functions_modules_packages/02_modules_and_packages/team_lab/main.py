"""Simple company package"""

from company_package.interface.cli import run_checkout


def quickshop_company():
    run_checkout()


if __name__ == "__main__":
    quickshop_company()

# ? Example Output in CLI:
# Enter your name: Anton
# Item name (or 'done' to finish): Pen
# Price: 5
# Quantity: 1
# Item name (or 'done' to finish): Notebook
# Price: 15
# Quantity: 3
# Item name (or 'done' to finish): Laptop
# Price: 500
# Quantity: 1
# Item name (or 'done' to finish): Staples
# Price: 0.02
# Quantity: 500
# Item name (or 'done' to finish): done
# Discount % (0 for none): 10

# Order ID: anton
# Items:
#  - Pen: 1 x £5.00
#  - Notebook: 3 x £15.00
#  - Laptop: 1 x £500.00
#  - Staples: 500 x £0.02
# Subtotal: £560.00
# Discount: £56.00
# VAT: £100.80
# Total: £604.80

# ? Example content of order_anton.txt:
# Order ID: anton
# Items:
#  - Pen: 1 x £5.00
#  - Notebook: 3 x £15.00
#  - Laptop: 1 x £500.00
#  - Staples: 500 x £0.02
# Subtotal: £560.00
# Discount: £56.00
# VAT: £100.80
# Total: £604.80
