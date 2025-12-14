"""
What is a Variable?
A variable is a name that refers to a value stored in memory.
"""


# Creating variables
age = 25               # Integer variable
name = "Alice"        # String variable
height = 5.7         # Float variable
is_student = True    # Boolean variable 



# Displaying variable values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)



# Variable naming rules 
# 1. Must start with a letter (a-z, A-Z) or underscore (_)  
# 2. Can contain letters, digits (0-9), and underscores
# 3. Cannot be a reserved keyword in Python
# 4. Variable names are case-sensitive


# Examples of valid variable names  
my_variable = 10
_variable2 = 20
var123 = 30


# Examples of invalid variable names (uncommenting these will cause errors)
# 1variable = 10      # Starts with a digit
# my-variable = 20    # Contains a hyphen
# class = 30          # 'class' is a reserved keyword



# Demonstrating data types
print("Data type of age:", type(age))
print("Data type of name:", type(name))
print("Data type of height:", type(height)) 
print("Data type of is_student:", type(is_student))



# Changing variable values
age = 26
print("Updated Age:", age)
# Multiple assignments
x, y, z = 1, 2.5, "Hello"   
print("x:", x, "y:", y, "z:", z)
# Swapping variable values
x, y = y, x
print("After swapping - x:", x, "y:", y)



# Constants (by convention, use uppercase variable names)
PI = 3.14159
GRAVITY = 9.81  
print("Value of PI:", PI)
print("Value of GRAVITY:", GRAVITY)
# Note: Python does not have built-in constant types,   
# but using uppercase names indicates that these values should not be changed.


a = b = c = 10 # Chained assignment
print("a:", a, "b:", b, "c:", c)

# Augmented assignment
a += 5  # Equivalent to a = a + 5



# Deleting a variable
x = 10
del x
# print(x)  # This will raise an error since x is deleted



a = 10
b = 10
print(id(a), id(b))
print(a is b)  # True, both refer to the same object in memory
b = 20
print(a is b)  # False, now they refer to different objects
print(a == b)  # False, values are different