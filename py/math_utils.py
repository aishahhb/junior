#Libraries
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
PI = 3.14159

class Calculator:
    def __init__(self):
        pass

    def calculate(self, operation, x, y=None):
        if operation == 'add':
            return add(x, y)
        elif operation == 'subtract':
            return subtract(x, y)
        elif operation == 'multiply':
            return multiply(x, y)
        elif operation == 'divide':
            return divide(x, y)
        elif operation == 'factorial':
            return factorial(x)
        else:
            raise ValueError("Unsupported operation")

        self.history.append(f"{operation}({x}, {y}) = {result}")
        return result