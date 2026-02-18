"""Exercises: Functions and Scope"""\

import py

# ! 1. Write a function calculate_area(width, height) that takes two numbers and returns the area
# !    of a rectangle.


def calculate_area(width, height):
    """Multiplies width and height to calculate area."""
    area = width * height
    return area


print(calculate_area(3, 4))  # ? Output: 12
print(calculate_area(5, 6))  # ? Output: 30

# ! ------------------------------------------------------------------------------------------------

# ! 2. Write a function is_prime(number) that takes an integer and returns True if it's a prime
# ! number, and False.


def is_prime(number):
    """Checks if a number is prime and returns True or False."""
    if number < 2:  # Numbers less than 2 are not prime
        return False
    # Check divisibility up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:  # If number is divisible by any i, it's not prime
            return False
    return True  # If prime


print(is_prime(1))  # ? Output: False
print(is_prime(2))  # ? Output: True
print(is_prime(3))  # ? Output: True
print(is_prime(4))  # ? Output: False
print(is_prime(5))  # ? Output: True

# ! ------------------------------------------------------------------------------------------------

# ! 3. Create a module named py. Inside it, create a function reverse_string(s) and another
# ! function count_vowels(s). Create a separate main.py file that imports and uses these functions.

# ? The main.py file be this exercise file (imported at the top of this file).

# import py

print(py.reverse_string("Hello there!"))  # ? Output: !ereht olleH
print(py.count_vowels("Hello There Again!"))  # ? Output: 7

# ! ------------------------------------------------------------------------------------------------

# ! 4. Draw a diagram showing the scope of variables in the following code:
x = 10  # global


def my_func(y):  # y is local
    z = 5  # z is local
    return x + y + z

# ? Diagram:
# return x + y + z  ------> y function call (found locally) -----> z found locally -----> x found globally

# x is a global variable
# y is a local parameter
# z is a local variable
