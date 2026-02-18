"""Exercise 1: String utilities module"""


def reverse_string(s):
    """Return the reverse of the given string."""
    return s[::-1]  # Slicing to reverse the string


def is_palindrome(s):
    """Check if the given string is a palindrome (reads the same forwards and backwards)."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # ? Explanation:
    # 1. ''.join(...) is used to concatenate the characters into a single string.
    # 2. c.lower() converts each character to lowercase to ensure case insensitivity.
    # 3. c.isalnum() checks if the character is alphanumeric (ignoring spaces and punctuation).
    # Check if the cleaned string is the same as its reverse:
    return cleaned == cleaned[::-1]


def count_vowels(s):
    """Count the number of vowels in the given string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for c in s if c in vowels)
    # ? Explanation:
    # 1. sum(...) is used to count the total number of vowels.
    # 2. The generator expression (1 for c in s if c in vowels) iterates through each character in
    #    the string s and yields 1 for each vowel found, which sum() then adds up to get the total
    #    count of vowels.
