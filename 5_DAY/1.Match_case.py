# Write a program of Calculator using match case statement

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case '+':
        result = a + b
        print(f"{a} + {b} = {result}")
    case '-':
        result = a - b
        print(f"{a} - {b} = {result}")
    case '*':
        result = a * b
        print(f"{a} * {b} = {result}")
    case '/':
        if b != 0:
            result = a / b
            print(f"{a} / {b} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operator. Please use one of +, -, *, /.")