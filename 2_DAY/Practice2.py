            # Write a program to swap two numbers

# Method 1: Using Temporary Variable
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)




# Method 2: Without Using Temporary Variable
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

a, b = b, a

print("a =", a)
print("b =", b)




# Method 3: Using Addition and Subtraction
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

a = a + b
b = a - b
a = a - b

print("a =", a)
print("b =", b)




# Method 4: Using Multiplication and Division
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
a = a * b
b = a // b
a = a // b
print("a =", a)
print("b =", b)




# Method 5: Using Bitwise XOR Operator
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
a = a ^ b
b = a ^ b
a = a ^ b   
print("a =", a)
print("b =", b)


# Method 6: Using Python's Tuple Unpacking
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
a, b = b, a
print("a =", a)
print("b =", b)




# Method 7: Using List  
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
lst = [a, b]
lst[0], lst[1] = lst[1], lst[0]
a, b = lst
print("a =", a)
print("b =", b)




# Method 8: Using Arithmetic Mean
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
mean = (a + b) / 2
a = 2 * mean - a
b = 2 * mean - b
print("a =", a)
print("b =", b)




# Method 9: Using a Function
def swap(x, y):
    return y, x
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
a, b = swap(a, b)
print("a =", a)
print("b =", b)



# Method 10: Using List Comprehension
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
a, b = [b, a]
print("a =", a)
print("b =", b)



# Method 11: Using Dictionary
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
d = {'a': a, 'b': b}
d['a'], d['b'] = d['b'], d['a']
a, b = d['a'], d['b']
print("a =", a)
print("b =", b)


# Method 12: Using Stack
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
stack = []
stack.append(a)
stack.append(b)
b = stack.pop()
a = stack.pop()
print("a =", a)
print("b =", b)



# Method 13: Using Recursion
def recursive_swap(x, y):
    if x == 0:
        return y, x
    else:
        return recursive_swap(x - 1, y + 1)
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
a, b = recursive_swap(a, b)
print("a =", a)
print("b =", b)




# Method 14: Using Lambda Function
swap = lambda x, y: (y, x)
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
a, b = swap(a, b)
print("a =", a) 
print("b =", b)




# Method 15: Using NumPy Library
import numpy as np
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
arr = np.array([a, b])
arr = arr[::-1]
a, b = arr
print("a =", a)
print("b =", b)




# Method 16: Using Pandas Library
import pandas as pd 
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): ")) 
df = pd.DataFrame({'Values': [a, b]})
df = df.iloc[::-1].reset_index(drop=True)
a, b = df['Values']
print("a =", a)
print("b =", b)