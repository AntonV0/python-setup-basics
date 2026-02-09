## Short Answer Test

### Q1.  
Why is it generally a bad idea to use a bare `except:` block?

**Answer:**  
A bare `except:` block is catches all exceptions, including unexpected ones. This can hide bugs, make debugging difficult, and prevent the program from failing in situations where it should stop. Catching specific exceptions leads to clearer error handling.

---

### Q2.  
Explain the flow of execution in a `try...except...finally` block when an exception is raised in the `try` block but is not caught by the `except` block.

**Answer:**  
When an exception is raised in the `try` block is not caught in the `except` block, the `finally` block still executes. After the `finally` block runs, the exception is re-raised and the program terminates unless it is caught somewhere else.

---

### Q3.  
Provide a scenario where an `else` clause in a `try` block would be useful and improve code readability.

**Answer:**  
An `else` clause is useful when code should only run if no exception occurs. For example, when converting user input to an integer, the `else` block nested inside the `try` block can contain code that runs only on successful conversion.
