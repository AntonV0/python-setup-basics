## Short Answer Test - Files and I/O

### Q1. Explain the purpose of the with statement when working with files and why it is considered a best practice.

**Answer:**  
The `with` statement automatically handles opening and closing the file, even if an error occurs. This is considered a best practice because it reduces the risk of resource leaks and makes the code cleaner and more readable.

---

### Q2. Describe the difference between the write() and writelines() methods for a file object.

**Answer:**  
The `write()` method writes a single string to a file, while the `writelines()` method writes a list of strings to a file. `writelines()` does not add newline characters automatically, so they must be included in the strings if needed.

---

### Q3. How would you handle a FileNotFoundError exception if a user provides a file path that doesn't exist? Provide a short code example.

**Answer:**  
You can handle a `FileNotFoundError` exception using a `try-except` block. For example:

```python
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
```
Output:
```
The file does not exist.
```

---

### Q4. When would you use the csv module instead of a basic text file for data storage, and why?

**Answer:**
You would use the `csv` module when you need to work with structured data in a table format, with rows and columns. The `csv` module provides functionality to read from and write to CSV files easily and handling formatting issues automatically. This is more convenient and less error-prone than manually parsing and formatting text files.

---

### Q5. What is the purpose of the os.path module in relation to file handling?

**Answer:**  
The `os.path` module provides functions for interacting with the file system in a platform-independent way. It allows you to check if a file or directory exists, join paths, get absolute paths, and extract file names or extensions, among other tasks. This is useful for writing code that works across different operating systems.