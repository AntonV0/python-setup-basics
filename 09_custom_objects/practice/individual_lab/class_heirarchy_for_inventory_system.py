"""Individual Lab: Class Hierarchy for a Simple Inventory System"""


class Product():
    """Base class of a product in inventory."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def is_quantity_available(quantity):
        """Static method to check if a product is available."""
        return quantity > 0  # Check if quantity is a positive integer


class Book(Product):
    """Book class that inherits from Product and adds attributes."""

    def __init__(self, name, price, quantity, author, isbn):
        # Call the initialiser of the Product class
        super().__init__(name, price, quantity)
        self.author = author
        self.isbn = isbn

    @classmethod
    def create_book(cls, data):
        """Class method to create a Book instance from a dictionary."""
        return cls(  # Call the class method with a dictionary containing book details
            data["name"],
            data["price"],
            data["quantity"],
            data["author"],
            data["isbn"]
        )


class Electronics(Product):
    """Electronics class that inherits from Product and adds attributes."""

    def __init__(self, name, price, quantity, brand, warranty_months):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.warranty_months = warranty_months


if __name__ == "__main__":
    book_data = {  # Dictionary containing book details
        "name": "The Great Gatsby",
        "price": 10.99,
        "quantity": 5,
        "author": "F. Scott Fitzgerald",
        "isbn": "978-0743273565"
    }
    # Create a Book instance using the class method
    book1 = Book.create_book(book_data)
    # Create an Electronics instance
    electronics1 = Electronics("Smartphone", 299.99, 10, "Apple", 24)

    inventory = [book1, electronics1]  # List to hold inventory products

    for product in inventory:  # Loop through the inventory and print details of each product
        if isinstance(product, Book):  # Check if the product is an instance of the Book class
            print(
                f"Book: {product.name}, Author: {product.author}, ISBN: {product.isbn}")
        # Check if the product is an instance of the Electronics class
        elif isinstance(product, Electronics):
            print(
                # Parentheses to break the line for better readability
                f"Electronics: {product.name}, "
                f"Brand: {product.brand}, "
                f"Warranty: {product.warranty_months} months")

        # Check if the product is available using the static method and print the result
        print(f"Is '{product.name}' available? "
              f"{'Yes' if Product.is_quantity_available(product.quantity) else 'No'}\n")

# ? Output:
# ? Book: The Great Gatsby, Author: F. Scott Fitzgerald, ISBN: 978-0743273565
# ? Is 'The Great Gatsby' available? Yes

# ? Electronics: Smartphone, Brand: Apple, Warranty: 24 months
# ? Is 'Smartphone' available? Yes
