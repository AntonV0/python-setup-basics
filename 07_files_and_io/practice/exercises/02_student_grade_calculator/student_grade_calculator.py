"""Exercise 2: Student Grade Calculator"""
from pathlib import Path


def read_grades_from_file(file_path):
    """Read grades from a grades.txt file and return a list of grades."""
    # each line has name then comma then grade
    grades = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # strip whitespace and split by comma
            parts = line.strip().split(',')
            # check if we have exactly 2 parts (name and grade)
            if len(parts) == 2:
                # unpack name and grade
                name, grade_str = parts
                try:
                    # convert grade to float and add to list
                    grade = float(grade_str)
                    grades.append(grade)
                except ValueError:
                    print(
                        f"Warning: '{grade_str}' is not a valid grade and will be skipped.")
    return grades


def calculate_average_grade(grades):
    """Calculate and return the average grade from a list of grades."""
    if not grades:
        return 0.0  # avoid division by zero
    total = sum(grades)
    average = total / len(grades)
    return average


def write_average_to_file(average, file_path):
    """Write the average grade to a file named average_grade.txt."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Average Grade: {average:.2f}\n")


def main():
    """Main function to read grades, calculate average, and write to file."""

    # Get folder where this script lives
    base_dir = Path(__file__).parent
    grades_file = base_dir / 'grades.txt'
    output_file = base_dir / 'average_grade.txt'

    # Read grades from file
    grades = read_grades_from_file(grades_file)

    # Calculate average grade
    average_grade = calculate_average_grade(grades)

    # Write average grade to file
    write_average_to_file(average_grade, output_file)

    print(f"Average grade calculated and written to {output_file}.")


if __name__ == "__main__":
    main()


# ? Output in average_grade.txt:
# ? Average Grade: 82.00
