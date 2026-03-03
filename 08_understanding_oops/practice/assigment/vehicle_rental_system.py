"""Assignment: Vehicle Rental System"""


class Vehicle:
    """Base class representing a vehicle."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Method to display information about the vehicle."""
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    """Car subclass that inherits from Vehicle."""

    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        """Override to include number of doors."""
        return f"{super().display_info()} with {self.num_doors} doors"
        # super() is used to call the display_info method of the parent Vehicle class
        # and then add additional information about the number of doors specific
        # to the Car subclass.


class Motorcycle(Vehicle):
    """Motorcycle subclass that inherits from Vehicle."""

    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type

    def display_info(self):
        """Override to include engine type."""
        return f"{super().display_info()} with {self.engine_type} engine"


class Truck(Vehicle):
    """Truck subclass that inherits from Vehicle."""

    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def display_info(self):
        """Override to include capacity."""
        return f"{super().display_info()} with {self.capacity} kg capacity"


class ElectricVehicle:
    """Mixin class for electric vehicle information."""

    def electric_info(self):
        """Method to provide electric vehicle information."""
        return "This is an electric vehicle."


class HybridCar(Car, ElectricVehicle):
    """HybridCar class that inherits from Car and ElectricVehicle mixin."""

    def __init__(self, make, model, year, num_doors, battery_capacity):
        super().__init__(make, model, year, num_doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()} and a battery capacity of {self.battery_capacity} kWh"

    def electric_info(self):
        return f"This is a hybrid car with a battery capacity of {self.battery_capacity} kWh"


# ? Example usage:
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Honda", "CBR600RR", 2019, "Inline-4")
truck = Truck("Ford", "F-150", 2021, 1000)
hybrid_car = HybridCar("Toyota", "Prius", 2022, 4, 8.8)
print(car.display_info())
print(motorcycle.display_info())
print(truck.display_info())
print(hybrid_car.display_info())
print(hybrid_car.electric_info())

# ? Output:
# ? 2020 Toyota Camry with 4 doors
# ? 2019 Honda CBR600RR with Inline-4 engine
# ? 2021 Ford F-150 with 1000 kg capacity
# ? 2022 Toyota Prius with 4 doors and a battery capacity of 8.8 kWh
# ? This is a hybrid car with a battery capacity of 8.8 kWh
