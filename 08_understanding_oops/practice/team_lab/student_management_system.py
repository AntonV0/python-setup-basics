"""Student Management System"""


class Person:
    """Base class representing a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    """Student subclass that inherits from Person."""

    def __init__(self, name, age, student_id, courses):
        super().__init__(name, age)
        self.__student_id = None  # Private attribute for encapsulation
        self.set_student_id(student_id)  # Validate and set student ID
        self.courses = courses

    def set_student_id(self, student_id):
        """Encapsulation setter with validation."""
        if Course.validate_student_id(student_id):
            self.__student_id = student_id

    def get_student_id(self):
        """Encapsulation getter."""
        return self.__student_id

    @classmethod  # Alternative constructor using a class method
    def from_dict(cls, data_dict):
        """Create a Student instance from a dictionary."""
        return cls(  # Unpacking dictionary values to initialise the Student object
            data_dict["name"],
            data_dict["age"],
            data_dict["student_id"],
            data_dict["courses"]
        )


class Teacher(Person):
    """Teacher subclass that inherits from Person."""

    def __init__(self, name, age, employee_id, subjects):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subjects = subjects


class Course:
    """Class representing a course."""

    def __init__(self, course_name, students=None, teachers=None):
        # None is used as the default value to avoid mutable default argument issues with lists
        # Use default empty lists if none provided to avoid mutable default argument issues
        self.course_name = course_name
        self.students = students if students else []
        self.teachers = teachers if teachers else []

    @staticmethod
    def validate_student_id(student_id):
        """Static method to validate student ID format."""
        if isinstance(student_id, int) and 100000 <= student_id <= 999999:
            return True
        raise ValueError("Student ID must be a 6-digit number.")


# ? Example usage:
# Creating instances of Student and Teacher, demonstrating encapsulation and class method usage:
student1 = Student("Alice", 20, 123456, ["Math", "Science"])
teacher1 = Teacher("Mr. Smith", 45, "T001", ["Math"])

# Creating a Student instance using the alternative constructor from a dictionary:
student_data = {
    "name": "Bob",
    "age": 22,
    "student_id": 654321,
    "courses": ["History"]
}

student2 = Student.from_dict(student_data)
print(student2.name)
# ? Output: Bob

# Demonstrating encapsulation by accessing the student ID through getter and setter methods:
print(student1.name)
print(student1.get_student_id())

# ? Output:
# ? Alice
# ? 123456

# Attempting to set an invalid student ID to demonstrate validation and error handling:
try:
    student1.set_student_id(12345)  # Invalid
except ValueError as e:
    print(e)

course1 = Course("Math", [student1], [teacher1])

# ? Output:
# ? Student ID must be a 6-digit number.
