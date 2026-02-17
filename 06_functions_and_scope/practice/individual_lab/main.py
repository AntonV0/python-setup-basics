"""User-facing Menu Using Imported Conversion Functions"""

from conversions.convert_temperature import celcius_to_fahrenheit, fahrenheit_to_celsius
from conversions.convert_distance import miles_to_kilometers, kilometers_to_miles


def validate_input(prompt, valid_options):  # prompt is the message shown to the user
    """Helper function to validate user input against a list of valid options"""
    while True:
        # Convert input to lowercase for case-insensitive comparison
        user_input = input(prompt).lower()
        if user_input in valid_options:  # If the input is valid, return it
            return user_input
        print(
            f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")


def user_menu():
    """User-facing menu for distance and temperature conversions"""

    conversion_type = validate_input(
        "What would you like to convert? (type distance or temperature): ",
        ["distance", "temperature"]
    )

    if conversion_type == "distance":  # distance conversion

        distance = validate_input(
            "Start with miles or kilometers? (type miles or kilometers): ",
            ["miles", "mile", "m", "kilometers", "kilometer", "km"]
        )

        while True:
            value = input("Enter the distance (numbers only): ")
            try:
                # Check if the input can be converted to a float (valid number)
                float(value)
                if distance in ("miles", "mile", "m"):
                    return miles_to_kilometers(value)
                else:
                    return kilometers_to_miles(value)
            except ValueError:
                print("Invalid number. Please enter digits only.")

    else:  # temperature conversion

        temperature = validate_input(
            "Start with celcius or fahrenheit? (type celcius or fahrenheit): ",
            ["celcius", "c", "fahrenheit", "f"]
        )

        while True:
            value = input("Enter the temperature (numbers only): ")
            try:
                # Check if the input can be converted to a float (valid number)
                float(value)
                if temperature in ("celcius", "c"):
                    return celcius_to_fahrenheit(value)
                else:
                    return fahrenheit_to_celsius(value)
            except ValueError:
                print("Invalid number. Please enter digits only.")


conversion_result = user_menu()
print("Conversion Result:", conversion_result)

# ! Example output:

# ? Miles to Kilometers:
# What would you like to convert? (type distance or temperature): distance
# Start with miles or kilometers? (type miles or kilometers): miles
# Enter the distance (numbers only): 5
# Conversion Result: 8.0467 km

# ? Fahrenheit to Celcius:
# What would you like to convert? (type distance or temperature): temperature
# Start with celcius or fahrenheit? (type celcius or fahrenheit): fahrenheit
# Enter the temperature (numbers only): 100
# Conversion Result: 37.7778 °C

# ? Invalid input examples:

# What would you like to convert? (type distance or temperature): temp
# Invalid input. Please enter one of the following: distance, temperature

# What would you like to convert? (type distance or temperature): distance
# Start with miles or kilometers? (type miles or kilometers): 123
# Invalid input. Please enter one of the following: miles, mile, m, kilometers, kilometer, km

# What would you like to convert? (type distance or temperature): temperature
# Start with celcius or fahrenheit? (type celcius or fahrenheit): c
# Enter the temperature (numbers only): abc
# Invalid number. Please enter digits only.
