# 🟢 What are Comments in Python?
# Comments are notes written for humans, ignored by Python.

"""
They help explain  :
what code does
why something is written
logic, warnings, TODOs
They don’t affect execution.
"""
# Think of them like sticky notes in your code.

"""
    1. Single-line Comments
    Use the # symbol. 
"""
# Single line Comments


# Python has no official multi-line comment syntax
'''
This is a multi-line comment
which spans multiple lines.
It is often used to provide detailed explanations
or documentation for code sections.
'''

"""Another way to write multi-line comments
is by using triple double quotes.
This is also useful for documentation.
"""

name= "Harshad"  # This is an inline comment

print("Hello, World!")  # This prints a greeting message


# Docstrings (Not comments, but similar)
# Docstrings look like multi-line comments — BUT they are meant for documentation of functions, classes, modules.
def add(a, b):
    "Returns sum of two numbers hello"
    return a + b
# This is not ignored — Python stores this string as documentation.
# You can access it using:
print(add.__doc__)


"""
🟡 Why Comments Matter (Interview POV)

. improves readability
. helps debugging
. helps teamwork
. makes future updates easier
. required in production-grade code
"""
# Bad developers write code Great developers explain code.



# ❌ Bad Commenting
# loop
for i in range(10):
    print(i)


# ✅ Good Commenting
# Print numbers 0–9 using a simple range loop
for i in range(10):
    print(i)
