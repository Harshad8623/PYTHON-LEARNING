# Write a python program to Diaplay the multiplication table of a given number

num = int(input("Enter a Number to display its multiplication table: "))
print(f"Multiplication Table of {num} is:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


# Alternative Method (Using while loop)
num = int(input("Enter a Number to display its multiplication table: "))
print(f"Multiplication Table of {num} is:")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num*i}")
    i += 1



# Another Alternative Method (Using list comprehension)
num = int(input("Enter a Number to display its multiplication table: "))
print(f"Multiplication Table of {num} is:")
table = [f"{num} x {i} = {num*i}" for i in
    range(1, 11)]
for line in table:  
    print(line)



# Another Alternative Method (Using lambda and map)
num = int(input("Enter a Number to display its multiplication table: "))
print(f"Multiplication Table of {num} is:")
table = list(map(lambda i: f"{num} x {i} = {num*i}", range(1, 11)))
for line in table:
    print(line)



# Another Alternative Method (Using numpy)
import numpy as np
num = int(input("Enter a Number to display its multiplication table: "))
print(f"Multiplication Table of {num} is:") 
i = np.arange(1, 11)
table = num * i
for val in table:
    print(f"{num} x {np.where(table == val)[0][0] + 1} = {val}")




# Another Alternative Method (Using f-strings and join)
num = int(input("Enter a Number to display its multiplication table: "))
print(f"Multiplication Table of {num} is:")
table = '\n'.join([f"{num} x {i} = {num*i}" for i in range(1, 11)])
print(table)