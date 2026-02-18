"""Module for Converting Distance Between Miles and Kilometers"""


def miles_to_kilometers(miles):
    """Convert Miles to Kilometers"""
    m = float(miles)  # Convert input to float
    kilometers = m * 1.60934
    # Format to remove trailing zeros and decimal point if not needed
    return f"{kilometers:g} km"


def kilometers_to_miles(kilometers):
    """Convert Kilometers to Miles"""
    k = float(kilometers)
    miles = k / 1.60934
    return f"{miles:g} miles"
