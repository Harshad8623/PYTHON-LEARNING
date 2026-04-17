# Link : https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python


def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

a = 'Hello\nWorld'
print(a) # Output:
# Hello
# World
n = 5
print(f"The value of n is: {n}") # Output: The value of n is
a = r'Hello\nWorld'
print(a) # Output: Hello\nWorld
link = r"https//001f\\7/train/python"
print(link)