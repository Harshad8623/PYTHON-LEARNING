# Write a python program to solve quadratic equation ax^2 + bx + c = 0
import cmath
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))   
c = float(input("Enter coefficient c: "))
d = (b**2) - (4*a*c)    # discriminant
sol1 = (-b + cmath.sqrt(d)) / (2*a)
sol2 = (-b - cmath.sqrt(d)) / (2*a)
print(f"The solutions are {sol1} and {sol2}")





# Alternative Method (Using math module)
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = (b**2) - (4*a*c)    # discriminant
if d >= 0:
    sol1 = (-b + math.sqrt(d)) / (2*a)
    sol2 = (-b - math.sqrt(d)) / (2*a)
    print(f"The solutions are {sol1} and {sol2}")
else:
    print("The equation has complex roots." )





# Another Alternative Method (Using numpy)
import numpy as np
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))   
coefficients = [a, b, c]
roots = np.roots(coefficients)
print(f"The solutions are {roots[0]} and {roots[1]}")





# Another Alternative Method (Using sympy)
from sympy import symbols, Eq, solve
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
x = symbols('x')
equation = Eq(a*x**2 + b*x + c, 0)
solutions = solve(equation, x)
print(f"The solutions are {solutions[0]} and {solutions[1]}")





# Another simple Alternative Method (Using f-strings)
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = (b**2) - (4*a*c)    # discriminant
sol1 = (-b + (d)**0.5) / (2*a)
sol2 = (-b - (d)**0.5) / (2*a)
print(f"The solutions are {sol1} and {sol2}")




# Another Alternative Method (Using complex numbers directly)
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = (b**2) - (4*a*c)    # discriminant
sol1 = (-b + complex(0, d**0.5)) / (2*a)
sol2 = (-b - complex(0, d**0.5)) / (2*a)
print(f"The solutions are {sol1} and {sol2}")