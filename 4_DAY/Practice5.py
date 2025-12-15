# Write a python program to reverse a given number
# Using while loop
num = int(input("Enter a Number: "))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print(f"The reverse of {num} is {rev}")


# Alternative Method (Using for loop and string conversion)
num = int(input("Enter a Number: "))
rev = ''
for digit in str(num):
    rev = digit + rev
print(f"The reverse of {num} is {rev}")



# Another Alternative Method (Using slicing)
num = int(input("Enter a Number: "))
rev = str(num)[::-1]
print(f"The reverse of {num} is {rev}")


# Another Alternative Method (Using recursion)
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return reverse_number(n // 10, rev)
    
num = int(input("Enter a Number: "))
rev = reverse_number(num)
print(f"The reverse of {num} is {rev}")