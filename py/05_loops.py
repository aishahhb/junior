#For loops
for i in range(5):
    print(f"Range 5: ", i)

#1 is start, 6 is stop
for i in range(1, 6): 
    print(f"Range 1-6: ", i)

#0 is start, 10 is stop, 3 is step (i increases by 3)
for i in range(0, 10, 3): 
    print(f"Range 0, 10, 3: ", i)


# Exercises:
# 1.Create a multiplication table generator.
# 2.Write a program that calculates the factorial of a given number.

# 1. Multiplication table generator
number = 5
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 2. Factorial calculation
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(f"Factorial of {number}: {factorial(number)}")
