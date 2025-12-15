# Write a python program to find the sum of natural numbers up to a given number

num = int(input("Enter a positive integer: "))
if num < 1:
    print("Please enter a positive integer greater than 0.")
else:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(f"The sum of natural numbers up to {num} is: {sum}")