"""Exercise 1: Simple Object Creation"""


class Student:
    """Student class with attributes for name, age, and student ID."""

    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def study(self, subject):
        """Prints a message with student details and their study subject."""
        print(
            f"{self.name} (ID: {self.student_id}) is {self.age} years old and studying {subject}.")


if __name__ == "__main__":
    student1 = Student("Alice", 20, 1)  # Create a Student object
    student1.study("Mathematics")  # Call the study method

    student2 = Student("Bob", 22, 2)
    student2.study("Physics")

    student3 = Student("Charlie", 19, 3)
    student3.study("Chemistry")

# ? Output:
# Alice (ID: 1) is 20 years old and studying Mathematics.
# Bob (ID: 2) is 22 years old and studying Physics.
# Charlie (ID: 3) is 19 years old and studying Chemistry.
