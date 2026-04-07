# Modules in Python
# A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix math_utils.py added.
# contains functions, classes, and variables that can be used in other Python programs.

# Importing functions and classes from a math_utils.py file
from math_utils import add, subtract, multiply, divide, factorial, PI, Calculator

# Using the imported functions and classes
print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("Division:", divide(5, 3))
print("Factorial:", factorial(5))
print("PI:", PI)
calc = Calculator()
print("Calculator Add:", calc.calculate('add', 5, 3))