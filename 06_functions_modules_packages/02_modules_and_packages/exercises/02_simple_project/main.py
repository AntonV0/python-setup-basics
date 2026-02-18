"""Exercise 2: Simple Project with Modules and Packages"""

from modules.data_processor import read_numbers_from_file
from modules.report_generator import calculate_average, generate_report


def simple_project(input_file, output_file):
    """Main function to run the simple project."""
    # ? Step 1: Read numbers from the input file
    numbers = read_numbers_from_file(input_file)

    # ? Step 2: Calculate the average of the numbers
    average = calculate_average(numbers)

    # ? Step 3: Generate a report with the average and write it to the output file
    generate_report(average, output_file)


if __name__ == "__main__":
    # Input file containing number list
    simple_project.input_file = "numbers.txt"

    # Output file for the generated report
    simple_project.output_file = "report.txt"

    # Run the simple project
    simple_project(simple_project.input_file, simple_project.output_file)

# ? Input file (numbers.txt):
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 1234

# 0.5
# 12.34

# Lorem ipsum

# ? Output in terminal:
# '' is not a valid number and will be skipped.
# '' is not a valid number and will be skipped.
# 'Lorem ipsum' is not a valid number and will be skipped.

# ? Output in report.txt:
# The average of the numbers is: 100.14
