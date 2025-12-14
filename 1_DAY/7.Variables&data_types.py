"""
What is a Variable?
A variable in Python is a name that refers to a memory location where a value is stored.
Python variables are dynamically typed, meaning their data type is determined at runtime.
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

# Type casting
num_str = "100"
num_int = int(num_str)  # Convert string to integer
print("Converted integer:", num_int)
num_float = float(num_int)  # Convert integer to float
print("Converted float:", num_float)
num_str2 = str(num_float)  # Convert float to string    
print("Converted string:", num_str2)
print("Data type of num_str2:", type(num_str2)) 
# Input from user and type casting
# user_input = input("Enter a number: ")  # Input is always a string
# user_number = int(user_input)  # Convert input string to integer
# print("You entered the number:", user_number)
   


# Using f-strings for formatted output
name = "Bob"
age = 30
print(f"{name} is {age} years old.")
# Using format() method for formatted output    
print("{} is {} years old.".format(name, age))
# Using % operator for formatted output
print("%s is %d years old." % (name, age))
# Using concatenation for formatted output
print(name + " is " + str(age) + " years old.")
# Using commas in print for formatted output
print(name, "is", age, "years old.")
# Demonstrating global and local variables  
global_var = "I am a global variable"
def my_function():
    local_var = "I am a local variable"
    print(local_var)
    print(global_var)  # Accessing global variable inside function  
my_function()
print(global_var)
# print(local_var)  # This will raise an error since local_var is not accessible here   
# Using globals() and locals() to view variable scopes
print("Global variables:", globals())
def another_function(): 
    local_var2 = "Another local variable"
    print("Local variables:", locals())
another_function()
# Note: Uncomment the lines that raise errors to see the effects of variable scope. 
# Demonstrating mutable and immutable types
immutable_var = (1, 2, 3)  # Tuple (immutable)
mutable_var = [1, 2, 3]    # List (mutable) 
# immutable_var[0] = 10  # This will raise an error
mutable_var[0] = 10  # This works   
print("Mutable variable after modification:", mutable_var)  
# Note: Uncomment the line that raises an error to see the effect of immutability.  
# Using type() to check data types  
print("Type of immutable_var:", type(immutable_var))
print("Type of mutable_var:", type(mutable_var))
# Using isinstance() to check data types
print("Is immutable_var a tuple?", isinstance(immutable_var, tuple))
print("Is mutable_var a list?", isinstance(mutable_var, list))
# Using id() to check memory addresses
print("Memory address of immutable_var:", id(immutable_var))
print("Memory address of mutable_var:", id(mutable_var))
# Using dir() to list attributes and methods of a variable
print("Attributes and methods of mutable_var:", dir(mutable_var))
print("Attributes and methods of immutable_var:", dir(immutable_var))
# Using help() to get documentation of a variable's type    
print("Help on list type:") 
help(list)  
print("Help on tuple type:")
help(tuple)




# Demonstrating variable annotations (type hints)
name: str = "Charlie"
age: int = 28
height: float = 5.9
is_employed: bool = False   
print(f"Name: {name}, Age: {age}, Height: {height}, Employed: {is_employed}")
print("Data type of name:", type(name))
print("Data type of age:", type(age))
print("Data type of height:", type(height))
print("Data type of is_employed:", type(is_employed))   
# Note: Variable annotations do not enforce type checking at runtime, but they help with code readability and can be used by type checkers. 



# Using __annotations__ to view variable annotations
print("Variable annotations:", __annotations__)
# Demonstrating dynamic typing
var = 10
print("Value:", var, "Type:", type(var))
var = "Now I'm a string"
print("Value:", var, "Type:", type(var))
var = 3.14  
print("Value:", var, "Type:", type(var))
var = True
print("Value:", var, "Type:", type(var))
# Note: Python variables can change types dynamically, which is a key feature of the language.


# Using eval() to evaluate expressions stored in strings
expr = "5 + 10 * 2"
result = eval(expr)
print("Result of expression '{}': {}".format(expr, result)) 




# Using globals() and locals() to demonstrate variable scopes   
global_var = "I am global"
def scope_function():
    local_var = "I am local"
    print("Inside function - Local variable:", local_var)
    print("Inside function - Global variable:", global_var) 
scope_function()
print("Outside function - Global variable:", global_var)
# print("Outside function - Local variable:", local_var)  # This will raise an error
# Note: Uncomment the line that raises an error to see the effect of variable scope. 




# Using nonlocal keyword to modify a variable in the enclosing scope    
def outer_function():
    outer_var = "Outer variable"
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified outer variable"
        print("Inside inner function:", outer_var)
    inner_function()
    print("Inside outer function:", outer_var)
outer_function()
# Note: The nonlocal keyword allows modification of variables in the nearest enclosing scope that is not global.
