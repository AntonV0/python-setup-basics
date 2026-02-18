"""Exercise 1: String utilities using functions from module"""

from string_utils import reverse_string, is_palindrome, count_vowels


def string_utilities_demo():
    """Demonstrates the use of string utility functions."""
    user_input = input("Write a sentence: ")

    reversed_str = reverse_string(user_input)
    print(f"Reversed string: {reversed_str}")

    palindrome_check = is_palindrome(user_input)
    print(f"Is the string a palindrome? {'Yes' if palindrome_check else 'No'}")

    vowel_count = count_vowels(user_input)
    print(f"Number of vowels in the string: {vowel_count}")


# This ensures that the demo function runs only when this script is executed
# directly, not when imported as a module.
if __name__ == "__main__":
    string_utilities_demo()

# ? Example usage:
# Write a sentence: Lorem ipsum
# Reversed string: muspi meroL
# Is the string a palindrome? No
# Number of vowels in the string: 4

# Write a sentence: ABCDE EDCBA
# Reversed string: ABCDE EDCBA
# Is the string a palindrome? Yes
# Number of vowels in the string: 4
