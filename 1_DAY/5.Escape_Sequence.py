print("hello\nworld")  # New line
print("Hello\tWorld")  # Tab space
print("Hello\\World")  # Backslash
print('He said, "Hello World!"')  # Double quotes inside single quotes
print("It's a beautiful day!")  # Single quote inside double quotes
print("Hello\bWorld")  # Backspace
print("Hello\rWorld")  # Carriage return
print("Hello\fWorld")  # Form feed
print("Hello\vWorld")  # Vertical tab
print("\a   Hello World")  # Alert (bell)


import time

for i in "|/-\\":
    print("\r" + i, end="")
    time.sleep(0.6)
