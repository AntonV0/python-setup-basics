"""Exercise 8: Complex Hierarchy"""


class Vehicle:
    """Base class representing a generic vehicle."""
    pass  # Placeholder for the Vehicle class


class Car(Vehicle):
    """Car class that inherits from Vehicle."""

    def drive(self):
        """Simulate driving the car."""
        print("Driving a car...")


class Boat(Vehicle):
    """Boat class that inherits from Vehicle."""

    def sail(self):
        """Simulate sailing the boat."""
        print("Sailing a boat...")


class AmphibiousVehicle(Car, Boat):
    """AmphibiousVehicle class that inherits from both Car and Boat."""

    def demonstrate_modes(self):
        """Demonstrate driving and sailing modes."""
        print("Demonstrating driving and sailing modes:")
        super().drive()  # Call the drive method from Car
        super().sail()   # Call the sail method from Boat


if __name__ == "__main__":
    amphibious_vehicle = AmphibiousVehicle()
    amphibious_vehicle.demonstrate_modes()

# ? Output:
# Demonstrating driving and sailing modes:
# Driving a car...
# Sailing a boat...
