'''
What is Type Casting?
Type casting in Python is the process of converting a value from one data type to another.
Python supports both implicit and explicit type casting.
'''

# Type casting
num_str = "100"
num_int = int(num_str)  # Convert string to integer
print("Converted integer:", num_int)    
num_float = float(num_int)  # Convert integer to float
print("Converted float:", num_float)
num_str2 = str(num_float)  # Convert float back to string
print("Converted string:", num_str2)
print("Data type of num_str2:", type(num_str2))


# Demonstrating type casting with user input
# user_input = input("Enter a number: ")  # Input is always a string
# user_number = int(user_input)  # Convert input string to integer
# print("You entered the number:", user_number)
# Note: Uncomment the above three lines to test user input functionality.


'''
Types of Type Casting

Python supports two types:
1.Implicit Type Casting
2.Explicit Type Casting
'''



# Implicit Type Casting
a = 5       # Integer
b = 2.5     # Float
result = a + b  # Implicitly converts 'a' to float  
print("Result of implicit type casting (a + b):", result)
print("Data type of result:", type(result))



# Explicit Type Casting
x = 10.7
y = int(x)  # Explicitly converting float to integer
print("Explicitly converted integer:", y)
print("Data type of y:", type(y))


# Converting integer to string
z = str(y)
print("Explicitly converted string:", z)
print("Data type of z:", type(z))


# Converting string to float
s = "15.99"
f = float(s)
print("Explicitly converted float:", f)
print("Data type of f:", type(f))   
# Note: Type casting can lead to data loss, e.g., converting float to int truncates the decimal part.   


"""
            Explicit Type Casting

User manually converts data type using functions.

🔹 Common Casting Functions

Function	   Converts To
 int()	        Integer
 float()	    Float
 str()	        String
 bool()	        Boolean
 list()	        List
 tuple()	    Tuple
 set()	        Set
 dict()	        Dictionary
"""


# Common Errors in Type Casting
# 1. ValueError: Raised when the value is not compatible for conversion.
invalid_str = "Hello"
# invalid_int = int(invalid_str)  # Uncommenting this line will raise ValueError
# 2. TypeError: Raised when the type is not compatible for conversion.
invalid_list = [1, 2, 3]
# invalid_dict = dict(invalid_list)  # Uncommenting this line will raise TypeError
# Always ensure that the value and type are compatible before casting.


# Practical Example 
float_num = 9.78    
int_num = int(float_num)  # Convert float to integer
print("Original float number:", float_num)  
print("Converted integer number:", int_num)
str_num = "123"
int_from_str = int(str_num)  # Convert string to integer
print("String number:", str_num)
print("Converted integer from string:", int_from_str)
bool_from_int = bool(1)  # Convert integer to boolean
print("Boolean value from integer 1:", bool_from_int)   
list_from_tuple = list((1, 2, 3))  # Convert tuple to list
print("List converted from tuple:", list_from_tuple)
tuple_from_list = tuple([4, 5, 6])  # Convert list to tuple
print("Tuple converted from list:", tuple_from_list)
set_from_list = set([1, 2, 2, 3, 4])  # Convert list to set (removes duplicates)
print("Set converted from list:", set_from_list)
dict_from_tuples = dict([('a', 1), ('b', 2)])  # Convert list of tuples to dictionary
print("Dictionary converted from list of tuples:", dict_from_tuples)
# Note: Uncomment lines that raise errors to see the exceptions in action.
# Demonstrating 'is' vs '=='
a = [1, 2, 3]
b = a
print(a is b)  # True, both refer to the same object
print(a == b)  # True, values are the same
b = [1, 2, 3]
print(a is b)  # False, now they refer to different objects
print(a == b)  # True, values are the same