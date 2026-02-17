# Practice — Built-in Functions & Standard Modules

This folder contains exercises, lab work, assignments, and short answer questions for the Built-in Functions & Standard Modules Python module.

---

## Exercises

1. Write a script that calculates the hypotenuse of a right-angled triangle given the other two sides. Use the `sqrt()` function.

2. Create a "Magic 8-Ball" program. Create a list of possible string answers and use `choice()` to select and print one each time the user asks a question.

3. Write a script that generates a list of 6 unique random numbers between 1 and 49, simulating a lottery draw. Use `sample()`.

4. Use the `sum()` and `len()` built-in functions to calculate the average of a list of numbers.

---

## Lab Work

**Individual Lab**: Create a simple text-based "Dice Roller" simulator. The user should be able to specify how many dice to roll and how many sides each die has. The program should then simulate the rolls using `randint()` and print the result of each roll and the total.

**Team Lab**: Build a simple password generator. The team should create lists of lowercase characters, uppercase characters, numbers, and symbols. The program should ask the user for the desired password length and then build a password by picking random characters from these lists, ensuring the final password is a mix of all character types. Use `choice` and `random.shuffle`.

---

## Assignment

Write a script that simulates a race between two players.

1. Both players start at position 0. The finish line is at position 100.

2. In each turn, use `randint(1, 6)` to simulate a dice roll for each player. Add the result to their current position.

3. The race continues in a `while loop` until one player reaches or exceeds position 100.

4. Print the winner.

---

## Short Answer Test

1. What is the difference between `random()` and `random.randint()`?

2. Name three built-in functions (from the `builtins` module) and briefly describe what they do.

3. How would you import and use the value of Pi from the `math` module?
