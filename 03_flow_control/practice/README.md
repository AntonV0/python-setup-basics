# Flow Control in Python

This repository contains exercises, lab work, and an assignment completed as part of a Python bootcamp module on **flow control**. The focus is on using loops, conditionals, and basic program logic to solve common problems.

---

## Topics Covered
- `for` loops
- `while` loops
- Conditional statements (`if / elif / else`)
- Loop control (`break`)
- Boolean flags
- Basic input validation
- Nested logic
- Program flow visualisation (UML)

---

## Exercises

### 1. FizzBuzz
- Printed numbers from 1 to 100
- Replaced multiples of:
  - 3 with `"Fizz"`
  - 5 with `"Buzz"`
  - Both 3 and 5 with `"FizzBuzz"`
- Used conditional logic inside a `for` loop

### 2. Number Guessing Game
- Generated a random number between 1 and 100
- Used a `while` loop to repeatedly prompt the user
- Provided `"Too high"` / `"Too low"` hints
- Terminated when the correct number was guessed

### 3. Highest Score Finder
- Iterated through a list of dictionaries representing student records
- Used a `for` loop and `if` statement to find the student with the highest score

### 4. UML Activity Diagram
- Created a UML-style activity diagram (ASCII/Markdown)
- Visualised the loop, decision points, and outputs of the FizzBuzz program

---

## Lab Work

### Individual Lab – Password Validator
- Validated passwords based on:
  - Minimum length of 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one number
- Used:
  - A `for` loop to iterate through characters
  - Boolean flags
  - `if` statements for validation logic

### Team Lab – Shopping Cart Checkout
- Represented a shopping cart as a list of prices
- Calculated:
  - Subtotal using a loop
  - 10% discount if subtotal exceeded £50
  - VAT (tax)
- Printed a formatted receipt with totals
- Used nested conditional logic

---

## Assignment – Text Analyser
- Analysed a block of text character by character
- Counted:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Spaces
- Used:
  - A `for` loop
  - `if / elif / else` statements
- Printed a final analysis report

---

## Short Answer Test
- Explained differences between `for` and `while` loops
- Described infinite loops and how to prevent them
- Explained how to search a list using a loop and stop early with `break`

---

## Tools & Technologies
- Python
- Virtual Environments (`venv`)
- VS Code
- Pylint
- autopep8
- Git & GitHub

---

## Notes
- Code follows PEP 8 naming and formatting conventions
- Linter warnings were addressed where appropriate
- The virtual environment is excluded via `.gitignore`

---

This repository demonstrates practical use of Python flow control constructs and structured problem-solving using loops and conditionals.
