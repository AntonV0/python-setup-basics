"""Exercise 7: Mixin Application"""


class DatabaseStorable():
    """Mixin class to add database storage capabilities."""

    def save_to_db(self):
        """Simulate saving the object to a database."""
        print(f"Saving {self} to the database...")

    def load_from_db(self):
        """Simulate loading the object from a database."""
        print(f"Loading {self} from the database...")


class User():
    """User class with no attributes."""
    pass  # Placeholder for the User class


class Product():
    """Product class with no attributes."""
    pass  # Placeholder for the Product class


class StorableUser(User, DatabaseStorable):
    """User class that inherits from both User and DatabaseStorable."""

    def __str__(self):  # Define the string representation of the object for better output
        return "User"


class StorableProduct(Product, DatabaseStorable):
    """Product class that inherits from both Product and DatabaseStorable."""

    def __str__(self):
        return "Product"


if __name__ == "__main__":
    user1 = StorableUser()
    product1 = StorableProduct()

    user1.save_to_db()
    user1.load_from_db()

    product1.save_to_db()
    product1.load_from_db()

# ? Output:
# Saving User to the database...
# Loading User from the database...
# Saving Product to the database...
# Loading Product from the database...
