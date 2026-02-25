## Short Answer Test - Modules and Packages

### Q1. Explain the concept of a namespace and how modules help in preventing naming conflicts.

**Answer:**  
A namespace is a container that holds a set of identifiers (such as variable names, function names, and class names) and ensures that all of them are unique within that container. Modules help in preventing naming conflicts by providing separate namespaces for different parts of a program. Importing uses the module's name as a prefix, which avoids clashes with identifiers in other modules or the main program.

---

### Q2. Describe the process of creating a simple Python package. What is the one key file required?

**Answer:**  
1. Create a directory for your package (e.g., `my_package`).
2. Inside this directory, create an `__init__.py` file.
3. You can then create modules within the package directory to define your functions, classes, or variables. E.g. `module1.py` and `module2.py` inside the `my_package` directory.
4. To use the package, you can import it in your main script using `import my_package` or import specific modules or functions using `from my_package import module1`. 

The key file required to create a package is the `__init__.py` file, which allows Python to recognise the directory as a package.

---

### Q3. What is the __name__ variable in a Python script, and how does it relate to modules and direct execution?

**Answer:**  
- The `__name__` variable in a Python script is a special built-in variable that indicates the name of the module. 
- When a script is run directly, `__name__` is set to `"__main__"`. 
- When a script is imported as a module in another script, `__name__` is set to the module's name. 
- This allows you to write code that only executes when the script is run directly, and not when it is imported as a module, using `if __name__ == "__main__":`.

---

### Q4. Why is it a good practice to use import module_name instead of from module_name import *?
**Answer:**

Using `import module_name` keeps the namespace clean and avoids potential naming conflicts. When you use `from module_name import *`, it imports all the names from the module into the current namespace, which can lead to overwriting existing names or make it more difficult to understand where certain functions or variables come from.

---

### Q5. What is the purpose of a requirements.txt file? How is it used in conjunction with virtual environments?

**Answer:**  

- A `requirements.txt` file is used to list all the dependencies (external libraries and packages) that a Python project requires. 
- It allows other developers to install these dependencies using a package manager like pip. 
- Together with virtual environments, the `requirements.txt` file helps ensure that the specific versions of the dependencies are installed in an isolated environment, preventing conflicts with other projects and ensuring consistency across different dependency versions. 
- You can use the command `pip install -r requirements.txt` to install the dependencies within the activated virtual environment.