# Maz of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is greatest among {num1}, {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greatest among {num1}, {num2} and {num3}")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is greatest among {num1}, {num2} and {num3}")
# code does not handle equal numbers




# another way to find max of 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
maximum = max(num1, num2, num3)
print(f"{maximum} is the greatest among {num1}, {num2} and {num3}")




# another way to find max of 3 numbers
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greatest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")



# another way to find max of 3 numbers
if num1 >= num2:
    if num1 >= num3:
        print(f"{num1} is greatest")
    else:
        print(f"{num3} is greatest")
else:    
    if num2 >= num3:
        print(f"{num2} is greatest")
    else:
        print(f"{num3} is greatest")



# Another way to find max of 3 numbers'
if num1 == num2 == num3:
    print("All numbers are equal")
else:
    maximum = max(num1, num2, num3)
    print(f"{maximum} is the greatest")