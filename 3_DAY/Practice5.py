# Write a python program to find factorial of given number

num = int(input("Enter a Number (Positive number greater than 1) : "))
fact = 1
i = 1
if num<0:
    print("Factorial not exist for negative number")
elif num==0:
    print("Factorial of 0 is 0")
else:
    while i<=5:
        fact *= i
        i=i+1
    print(f"Factorial of {num} is {fact}")