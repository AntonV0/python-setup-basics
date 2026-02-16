"""Exercises: Built-in functions and standard modules"""

import math  # Importing math module to use sqrt() function
import random  # Importing random module to use choice() function

# ! 1. Write a script that calculates the hypotenuse of a right-angled triangle given
# !    the other two sides. Use the sqrt() function.

# import math (top of the file)


def calculate_hypotenuse(side_a, side_b):
    """Calculate the hypotenuse of a right-angled triangle given the other two sides."""
    # Using Pythagorean theorem A^2 + B^2 = C^2
    hypotenuse = math.sqrt(side_a**2 + side_b ** 2)
    return hypotenuse


# Example usage:
side_a = 3
side_b = 4

side_c_hypotenuse = calculate_hypotenuse(side_a, side_b)
print("The hypotenuse of the triangle with sides",
      side_a, "and", side_b, "is:", side_c_hypotenuse)
# ? Output: The hypotenuse of the triangle with sides 3 and 4 is: 5.0

# ! ----------------------------------------------------------------------

# ! 2. Create a "Magic 8-Ball" program. Create a list of possible string answers and
# !    use choice() to select and print one each time the user asks a question.

# import random  (top of the file)


def magic_8_ball():
    """Simulate a Magic 8-Ball program that gives random answers to user questions."""
    possible_answers = [
        "It is certain.",
        "Most likely.",
        "Outlook good.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    user_question = input("Ask the Magic 8-Ball a question: ")
    answer = random.choice(possible_answers)
    print("Magic 8-Ball says:", answer)


# magic_8_ball()

# ! ----------------------------------------------------------------------

# ! 3. Write a script that generates a list of 6 unique random numbers between 1 and 49,
# !    simulating a lottery draw. Use sample().

# ! ----------------------------------------------------------------------

# ! 4. Use the sum() and len() built-in functions to calculate the average of a list of numbers.
