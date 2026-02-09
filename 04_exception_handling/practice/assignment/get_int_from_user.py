"""Script to get an integer input from the user with error handling"""

def get_int_from_user(prompt="Please enter an integer: "):
    """Prompt the user for an integer input and handle invalid inputs."""
    while True:
        user_input = input(prompt) # Prompt user for input
        try:
            value = int(user_input) # Try to convert input to integer
            return value # Return the valid integer
        except ValueError:
            print(f"Invalid input '{user_input}'. Please enter a valid integer.")


user_integer = get_int_from_user()
print(f"You entered the integer: {user_integer}")

# Example output:
# Please enter an integer: abc
# Invalid input 'abc'. Please enter a valid integer.
# Please enter an integer: 3.14
# Invalid input '3.14'. Please enter a valid integer.
# Please enter an integer: 42
# You entered the integer: 42
