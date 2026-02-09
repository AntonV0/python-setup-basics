# Python Exception Handling – Bootcamp Assignments

This repository contains exercises, lab work, and an assignment completed as part of a Python bootcamp module on **exception handling**. The work focuses on writing robust programs that handle errors instead of crashing.

---

## Topics Covered
- Exception handling using `try`, `except`, `else`, and `finally`
- Handling built-in exceptions such as:
  - `ValueError`
  - `ZeroDivisionError`
  - `FileNotFoundError`
- Raising and catching custom exceptions
- Using loops for input validation
- Safe file handling
- User-friendly error reporting
- UML activity diagrams for exception flow

---

## Exercises

### 1. Age Input Validation
- Prompted the user for their age
- Used a `try...except ValueError` block to handle non-numeric input
- Repeatedly asked for input until a valid age was entered

### 2. Safe Division Function
- Created a function that divides two numbers
- Used `try...except ZeroDivisionError`
- Returned `None` when division by zero occurred

### 3. File Number Reader
- Read numbers from a text file line by line
- Handled:
  - `FileNotFoundError` when the file does not exist
  - `ValueError` when a line could not be converted to an integer
- Skipped invalid lines without crashing

### 4. UML Activity Diagram
- Drew a UML-style activity diagram to visualise:
  - Normal execution flow (no exception)
  - Exception raised and caught
  - Guaranteed execution of the `finally` block

---

## Lab Work

### Individual Lab – Contact Book with Custom Exceptions
- Extended a contact book application
- Raised a custom `KeyError` when attempting to add a duplicate contact
- Caught the exception in the main loop and displayed a user-friendly message

### Team Lab – Web Scraper with Error Handling
- Built a simple web scraper using the `requests` library  
- Prompted the user to enter a URL, automatically prepending `https://` when missing  
- Implemented a `while True loop` to allow multiple attempts without restarting the program  
- Added comprehensive exception handling to manage:
  - Invalid or malformed URLs  
  - Network and connection errors  
  - Request timeouts  
  - HTTP status errors (e.g. 404, 500)  
  - SSL-related errors  
- Ensured the program displays clear, user-friendly error messages rather than crashing the program
- Demonstrated correct ordering of exception handling to avoid overly broad catches  

---

## Assignment – Integer Input Utility
- Implemented `get_int_from_user(prompt)` function
- Used a `while` loop and `try...except ValueError` for validation
- Re-prompted the user until a valid integer was entered
- Returned the valid integer

---

## Short Answer Test
- Explained why bare `except:` blocks should be avoided
- Described execution flow of `try...except...finally` when exceptions are uncaught
- Provided a real-world scenario where `else` improves readability

---

## Tools and Technologies
- Python
- Virtual Environments (`venv`)
- VS Code
- Pylint
- autopep8
- Git & GitHub

---

## Notes
- Exception handling follows best practices by catching specific errors
- Resources are safely managed using `with` statements where applicable
- The virtual environment is excluded using `.gitignore`

---

This project demonstrates safe and structured error handling techniques commonly used in professional Python development.
