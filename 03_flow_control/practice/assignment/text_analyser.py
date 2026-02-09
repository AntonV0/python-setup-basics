"""Assignment: Text Analyser"""

# Script that analyses a block of text
TEXT_BLOCK = "In publishing and graphic design, Lorem ipsum is a placeholder text " \
"commonly used to demonstrate the visual form of a document or a typeface " \
"without relying on meaningful content. Lorem ipsum may be used as a " \
"placeholder before the final copy is available. 29th of January, 2026."

# Count total number of uppercase letters, lowercase letters, digits, and spaces.
def analyse_text(text):
    """Analyse the given text and return counts of character types."""
    # Initialise counters
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    space_count = 0

    # Loop through each character in the text and update counters
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            space_count += 1

    # Print a report
    print("Text Analysis Report:")
    print(f"Uppercase letters: {uppercase_count}")
    print(f"Lowercase letters: {lowercase_count}")
    print(f"Digits: {digit_count}")
    print(f"Spaces: {space_count}")

analyse_text(TEXT_BLOCK)
# Output:
# Text Analysis Report:
# Uppercase letters: 4
# Lowercase letters: 218
# Digits: 6
# Spaces: 46
