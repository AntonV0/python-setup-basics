# Practice — Installation and IDE

This folder contains exercises, lab work, assignments, and short answer questions
for the **Installation and IDE** module.

---

## Exercises

1. Write a Python script that imports the `sys` module and prints the version and
   `sys.executable` to the console. Run this script from your CLI.

2. Create a new project folder. Inside it, create a virtual environment named `.venv`.
   Activate it and install the `requests` package using `pip`. Run `pip freeze` to see
   the installed packages.

3. Configure VS Code to use `pylint`. Write a script with an unused variable
   (e.g., `x = 10`). Observe the warning that pylint provides in the **Problems**
   tab of VS Code.

4. Draw a UML sequence diagram illustrating the process of a developer writing code
   in VS Code, the formatter (`black`) running on save, and the developer then
   executing the script in the integrated terminal.

---

## Lab Work

### Individual Lab
Create a script `.py`. The script should check if it's running inside a virtual
environment. (Hint: check if `sys.prefix` is the same as `sys.base_prefix`).
The script should print a different message depending on the result.

### Team Lab
In breakout rooms, one student shares their screen. The team's goal is to create
a shared `.txt` file by running:
```bash
pip freeze > requirements.txt
```
Another team member then creates their own virtual environment and installs the
packages from this file using:
```bash
pip install -r requirements.txt
```
This simulates a real-world project setup.

---

## Assignment

Submit a single ZIP file containing:

- A Python script named `.py` that prints a welcome message.
- A `.txt` file listing the `pylint` and `black` packages.
- A screenshot of your VS Code window showing the script running successfully
  in an activated virtual environment within the integrated terminal.

---

## Short Answer Test

1. Explain why using virtual environments is a critical best practice in software development.
2. What is the difference between an interpreter and an IDE?
3. Describe the roles of a linter and a formatter. Can one replace the other?
   Why or why not?