"""Exercise 2: Report Generator module"""


def calculate_average(number_list):
    """Calculate the average of a list of numbers."""
    if not number_list:  # Check if the list is empty to avoid division by zero
        return 0
    total = sum(number_list)  # Sum all the numbers in the list
    count = len(number_list)  # Get the count of numbers in the list
    average = total / count  # Calculate the average
    return average


def generate_report(average, output_file):
    """Write a report containing the average to a text file."""
    with open(output_file, 'w', encoding='utf-8') as file:  # Open the file for writing
        file.write(f"The average of the numbers is: {average:.2f}\n")
