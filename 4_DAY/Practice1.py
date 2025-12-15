# Write a python program to Diaplay the multiplication table of a given number

num = int(input("Enter a Number to display its multiplication table: "))
print(f"Multiplication Table of {num} is:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
