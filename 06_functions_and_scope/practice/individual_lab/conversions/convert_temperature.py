"""Module for Converting Temperature Between Celsius and Fahrenheit"""


def celcius_to_fahrenheit(celcius):
    """Convert Celcius to Fahrenheit"""
    c = float(celcius)  # Convert input to float
    fahrenheit = (c * 9/5) + 32
    # Format to remove trailing zeros and decimal point if not needed
    return f"{fahrenheit:g} F"


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celcius"""
    f = float(fahrenheit)
    celcius = (f - 32) * 5/9
    return f"{celcius:g} °C"
