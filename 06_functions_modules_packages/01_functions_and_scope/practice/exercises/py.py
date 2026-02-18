"""reverse_string and count_vowels functions in py module (exercise 3)"""


def reverse_string(s):
    """Reverses the input string s and returns it."""
    # First : is the start index (default is 0),
    # second : is the end index (default is end of string),
    # -1 is the step (negative for reverse)
    return s[::-1]  # Slicing to reverse the string


def count_vowels(s):
    """Counts the number of vowels in the input string s and returns the count."""
    vowels = 'aeiouAEIOU'  # Vowel string
    count = 0
    for char in s:
        if char in vowels:  # Check if the character is a vowel
            count += 1
    return count
