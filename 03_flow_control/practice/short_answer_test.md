## Short Answer Test

### Q1.  
Explain the difference between a `while` loop and a `for` loop.  
Provide a scenario where a `while` loop is more appropriate.

**Answer:**  
A `for` loop is used when you already know how many times you want to iterate through the loop. A `while` loop continues running as long as the condition remains true. A `while` loop is more appropriate when validating user input, such as generating a password, where the number of attempts is not predetermined.

---

### Q2.  
What is an infinite loop, and how can you prevent it in a `while` loop?

**Answer:**  
An infinite loop occurs when the `while` loop condition never becomes false, so it continues iterating indefinitely. It can be prevented by using a `break` statement.

---

### Q3.  
How can you use a `for` loop with an `if` statement to find a specific item in a list and stop searching once it's found?

**Answer:**  
A `for` loop will iterate through the list, with a nested `if` statement inside it that checks if the item is in the list. If it's found, a `break` statement can be used to exit the loop.
