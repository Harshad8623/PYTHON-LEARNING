# Printing horizontally i.e use of sep and end

num = [1,2,3,4,5,6]
for i in num:
    print(i, end=" ") # Print numbers on the same line with a space in between



# Using sep to change the separator between items
print("2025", "11", "18", sep="-")  # Output: 2025-11-18
print("2025", "11", "18", sep="/")  # Output: 2025/11/18
print("2025", "11", "18", sep=".")  # Output: 2025.11.18
print("Custom separators demonstrated.")


# using both sep and end together
print("Hello", "world", sep="-", end="***")  # Output: Hello-world***Welcome to Python!
print("Welcome to Python!")
print("Hello", "world", sep="-")  # Output: Hello-world
print("Welcome to Python!")
print("Hello", "world", end="-")  # Output: Hello world-Welcome to Python!
print("Welcome to Python!")

