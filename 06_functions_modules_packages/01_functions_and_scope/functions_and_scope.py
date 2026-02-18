"""Functions and Scope in Python"""

# ! ------------------------------------------------------------------------------------------------

# ! FUNCTIONS

# ! ------------------------------------------------------------------------------------------------

# ! A function is a reusable block of code that performs a specific task.
# ! Instead of repeating the same code many times, we define it once and call it whenever we need it.

# ? Example 1: Repetition without a function

print("Greetings user!!!")
print("Greetings user!!!")
print("Greetings user!!!")

# This is repetitive and hard to maintain.

# Syntax:
# def function_name():
#     statements
#     statements

# ? Defining a function using 'def' keyword:


def greeting():
    print("Greetings user!!!")


# ? Calling the function
greeting()

# ? Using a loop to call the function multiple times
for _ in range(3):  # Using _ as a throwaway variable
    greeting()

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Function with internal variables


def profile():
    name = "Anton"
    age = 31
    print("My name is", name, "and my age is", age)


profile()  # Preferred way to call the function
# ? Output: My name is Anton and my age is 31

# Functions are also objects in Python
# You can assign them to variables
d1 = profile
d1()  # Calls the same function
# ? Output: My name is Anton and my age is 31

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Function with parameters (inputs)


def greet_user(user_name):
    print("Hello,", user_name)


greet_user("Anton")  # ? Output: Hello, Anton
greet_user("Alice")  # ? Output: Hello, Alice

# ? ------------------------------------------------------------------------------------------------

# ? Example 4: Function with parameters (placeholders)


def profile2(n1, a1):
    name = n1
    age = a1
    print("My name is", name, "and my age is", age)


profile2("Ben", 25)  # ? Output: My name is Ben and my age is 25
profile2("Catherine", 29)  # ? Output: My name is Catherine and my age is 29
profile2("David", 35)  # ? Output: My name is David and my age is 35

# ? ------------------------------------------------------------------------------------------------

# ? Example 5: Function with return value


def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)
print("Sum is:", result)  # ? Output: Sum is: 8

# ? ------------------------------------------------------------------------------------------------

# ? Example 6: Functions with local variables


def adding(a, b):
    ans = a + b
    print(ans + 5)  # ? Output: 12 if a=3, b=4
    c = 67  # ans is returned to the caller (c is the local variable)
    return ans


print(adding(3, 4))    # ? Output: 7
# print(ans + 5) # ? TypeError: can only concatenate list (not "int") to list
# print(c)  # ? Raises NameError since c is local to adding()

# ! ------------------------------------------------------------------------------------------------

# ! TYPES OF FUNCTION ARGUMENTS

# ! ------------------------------------------------------------------------------------------------

# ! 1. Positional arguments:

# ? Positional arguments are the most common type of arguments. They are passed to the function
# ? in the same order as they are defined in the function.


def profile3(name, age, place):  # Positional parameters
    print(f"My name is {name}. I am {age} years old and I live in {place}.")
    # f strings allow embedding expressions inside string literals


name1 = "Anton"
age1 = 31
place1 = "England"

profile3(name1, age1, place1)  # Calling with positional arguments

# ? Output: My name is Anton. I am 31 years old and I live in England.

# If the order of parameters is the same as the order of arguments, positional arguments work fine.
# However, if the order is different, it can lead to incorrect results.
# profile3(place1, name1, age1)  # Incorrect order of arguments

# ? ------------------------------------------------------------------------------------------------

# ! 2. Keyword arguments:

# ? To overcome the disadvantage of positional arguments, we can use keyword arguments.

profile3(age=age1, place=place1, name=name1)  # Calling with keyword arguments
# ? Output: My name is Anton. I am 31 years old and I live in England.
# Here, the order of arguments does not matter since we are using keywords.

# ? ------------------------------------------------------------------------------------------------

# ! 3. Default arguments:

# ? We can also provide default values for parameters. If the caller does not provide a value for
# ? that parameter, the default value will be used.


def profile4(name, age, place="Unknown"):  # Default parameter for place
    print(
        f"My name is {name}. I am {age} years old and I live in {place}.")


profile4("Anton", age1)
# ? Output: My name is Anton. I am 31 years old and I live in Unknown.
# If no default is set, this will raise TypeError since place argument is missing

# profile4(name=name1, age=age1, "UK") # Overriding default value
# ? SyntaxError: positional argument follows keyword argument

profile4(name=name1, age=age1, place="UK")
# ? Output: My name is Anton. I am 31 years old and I live in UK.

# ? ------------------------------------------------------------------------------------------------

# ! 4. Variable-length arguments:

# ? These allow passing a multiple number of arguments to a single parameter.

# ? Method 1:


def profile5(*names):  # Asterisk (*) indicates variable-length arguments
    print("My name is:", names)

    for i in names:
        print("Profile 5: My name is: ", i)


names = ["Anton", "Ben", "Catherine", "Diana"]
print(names)  # ['Anton', 'Ben', 'Catherine', 'Diana']

profile5(["Anton", "Ben", "Catherine"])
# ? Output: Profile 5: My name is:  ['Anton', 'Ben', 'Catherine']
# Note the comma, indicating it's a tuple with one element

# ? Method 2:


def profile6(age, *names):  # positional argument must come first

    for i in names:
        print("Profile 6: My name is ", i, age)


profile6(30, "Anton", "Ben", "Catherine")
# ? Output:
# ? Profile 6: My name is  Anton 30
# ? Profile 6: My name is  Ben 30
# ? Profile 6: My name is  Catherine 30

# ? Method 3


def profile7(*names, age=28):  # You can pass a default value also

    for i in names:
        print("Profile 7: My name is", i, "and my age is", age)


profile7("Anton", "Ben", "Catherine")  # age is assigned default value 28

# ? Output:
# ? Profile 7: My name is Anton and my age is 28
# ? Profile 7: My name is Ben and my age is 28
# ? Profile 7: My name is Catherine and my age is 28

# ? ------------------------------------------------------------------------------------------------

# ! 5. Keyword-variable length arguments:

# ? This allows to pass the argument in the form of key-value pairs.


# ? Method 1:


def about(**profile8):  # Double asterisk (**) indicates keyword-variable length arguments
    print(profile8)  # ? {'name': 'Anton', 'age': 31, 'place': 'England'}


about(name="Anton", age=31, place="England")

# ? Method 2:


def about2(place, phone="07123456789", **profile9):  # Positional argument must come first
    print(profile9, place, phone)


about2("France", name="John", age=50)
# ? Output: {'name': 'John', 'age': 50} France 07123456789

# ! ------------------------------------------------------------------------------------------------

# ! SCOPE OF VARIABLES

# ! ------------------------------------------------------------------------------------------------

# ! 1. Global scope:

# ? When a variable is defined outside any function, it has a global scope.

x = 10  # Global variable

# The global variable can be accessed everywhere in the module, below the line where it is defined.
# Global variables can also be accessed inside functions, but to modify them inside functions,
# we need to use the 'global' keyword.

# ? ------------------------------------------------------------------------------------------------

# ! 2. Local scope:

# ? When a variable is defined inside a function, it has a local scope.
# ? It can only be accessed within that function.


def local_scope():
    y = 5  # Local variable
    print(y)
    # x = 20 # Local variable, value reassigned to global variable 'x'
    # print(x)  # Error if 'x' is reassigned locally without 'global' keyword
    global x  # Declare 'x' as global to modify it
    x = x + 20  # Output: 30 if global x was 10
    print(x)
    global z
    z = 75  # 'z' is now a global variable


local_scope()  # Output: 5
# print(y)  # Raises NameError since y is local to local_scope()
print(z)  # ? Output: 75, z is global now
z = 5
print(z)  # ? Output: 5, z is reassigned globally

# ? ------------------------------------------------------------------------------------------------

# ! 3. Enclosed scope:

# ? A nested function can access variables from its enclosing function.


def outer_function():
    g = 99  # Enclosing variable
    h = 22  # Local variable to outer_function

    def inner_function():
        print(g)  # Accessing enclosing variable
        nonlocal h  # Declare 'h' as nonlocal to modify it, not global
        # 'h' is not defined globally, but in the enclosing function
        h = h + 10
        print(h)
    inner_function()  # Calling inner function from outer function


outer_function()  # ? Output: 99 (for g), 32 (for h)


# ? ------------------------------------------------------------------------------------------------

# ! 4. Built-in scope:

# ? Built-in scope contains names such as keywords, functions, exceptions that are built into Python.
# ? These names can be accessed from any part of the code.

print(len("Hello"))  # ? Output: 5, len() is a built-in function

# If a variable is defined with the same name as a built-in name,
# it will override the built-in name in the current scope.

len = 10  # Overriding built-in name 'len'
print(len)  # ? Output: 10
# print(len("Hello"))  # Raises TypeError since len is now an integer
del len  # Deleting the variable to restore built-in function

# ! ------------------------------------------------------------------------------------------------

# ! FUNCTIONS AS OBJECTS, NESTED FUNCTIONS, AND CLOSURES

# ! ------------------------------------------------------------------------------------------------

# ? Example 1: Functions can be assigned to objects


def hello():
    print("Hi!")


a1 = hello  # Assigning the function to an object (variable)
a1()  # Calling the function using the variable
# ? Output: Hi!
print(a1)
# ? Output: <function hello at 0x0000023512223950>

# ? Functions can be:
# - assigned to variables
# - passed as arguments to other functions
# - returned from other functions
# - nested inside other functions

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Nested functions


def outer():
    print("This is the outer function.")

    def inner():
        print("This is the inner function.")

    inner()  # Calling the inner function inside the outer function


outer()  # Calling the outer function
# ? Output:
# ? This is the outer function.
# ? This is the inner function.

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Functions can be returned


def outer2():
    def inner2():
        print("This is the inner function.")
    return inner2  # Returning the inner function


# Calling the outer function and getting the inner function
returned_function = outer2()
returned_function()
# ? Output: This is the inner function.

print(returned_function.__name__)
# ? Output: inner2
# (the name of the function that was returned)

# ? ------------------------------------------------------------------------------------------------

# ? Example 4: Closure concept
# This is a function that retains access to its enclosing scope even after the outer function
# has finished executing


def outer3(data):
    def inner3():
        # Accessing the data from the outer function
        print("This is the inner function. Data:", data)
    return inner3


# o3 now acts as an object that holds the inner function with access to the data passed to outer3
o3 = outer3("Hello all")
o3()  # Calling the returned inner function

# ? Output:
# ? This is the inner function. Data: Hello all

print(o3.__name__)
# ? Output: inner3

# ? ------------------------------------------------------------------------------------------------

# ? Example 5: Another example of closure with parameters


def outer4():
    def inner4(x):  # inner4 takes an argument 'x'
        print(x)
    return inner4  # Return the inner4 function without calling it


# outer4("hey")
# ? Output: TypeError: outer4() takes 0 positional arguments but 1 was given
# No output, because the inner function call fails before anything runs.

f = outer4()
# Prints inner4 because f is now referencing the inner4 function that was returned by outer4.
print(f.__name__)
# ? Output: inner4

f("hello")
# ? Output: hello
# The inner function is called with the argument "hello" and it prints it.

# ? What happens here:
# outer4() returns inner4(x)
# f = outer4() assigns the returned inner function to f
# f("hello") calls the inner function with "hello" as an argument

# ? ------------------------------------------------------------------------------------------------

# ? Example 6: Another example of closure with parameters


def multiply_by(n):
    def multiplier(x):
        return x * n
    return multiplier


m2 = multiply_by(2)  # m2 is now a function that multiplies its input by 2
m3 = multiply_by(3)  # m3 is now a function that multiplies its input by 3

print(m2(5))  # ? Output: 10
print(m3(5))  # ? Output: 15
# m2 and m3 are closures that retain access to the variable 'n' from their enclosing scope
# (multiply_by function)
