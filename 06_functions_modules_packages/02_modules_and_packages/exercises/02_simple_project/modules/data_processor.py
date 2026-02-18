"""Exercise 2: Data Processor module"""


def read_numbers_from_file(file_path):
    """Reads a list of numbers from a text file and returns them as a list of floats."""
    number_list = []  # Initialise list
    with open(file_path, 'r', encoding="utf-8") as file:  # Open file for reading
        for line in file:  # Iterate through each line in the file
            try:
                number = float(line.strip())  # Convert each line to a float
                number_list.append(number)  # Add the number to the list
            except ValueError:  # If conversion fails, print a warning and skip the line
                print(
                    f"'{line.strip()}' is not a valid number and will be skipped.")
    return number_list
