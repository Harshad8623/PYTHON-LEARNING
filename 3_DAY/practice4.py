# Write a python program to check the year is leap year or not

year = int(input("Enter year (e.g: 2025) : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
