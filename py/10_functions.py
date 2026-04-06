#Reusable block of code that do specific task

#Function call
def greet(name):
    return f"Hello, {name}!"
print(f"Function call: {greet('Alice')}") #Output: Hello, Alice!

#Function with multiple parameters
def add(a, b):
    return a + b
print(f"Multiple parameters: {add(5, 3)}") #Output: 8

#Function with default parameter
def power(base, exponent=2):
    return base ** exponent
print(f"Default parameter: {power(4)}")     #Output: 16 (default exponent is 2)
print(f"Modified parameter: {power(4, 3)}")  #Output: 64 (exponent is 3)

#Function with variable number of arguments
def sum_all(*args):
    return sum(args)
print(f"Variable number of arguments: {sum_all(1, 2, 3, 4)}") #Output: 10

#Function with keyword arguments
def introduce(name, age):
    return f"My name is {name} and I am {age} years old."
print(f"Keyword arguments: {introduce(name='Aishah', age=35)}")     #Output: My name is Aishah and I am 35 years old.

#Function with return value
print("\n--- Function with return value ---")
def square(x):
    return x * x
result = square(5)
print(f"Return value: {result}") #Output: 25

#Function with no return value (void function)
print("\n-----Void function output-----")
def print_greeting(name):
    print(f"Hello, {name}!")
#print_greeting(input("Enter your name: "))
print_greeting("Alisahh") 

#Key Value arguments
print("\n--- Key Value arguments ---")
def describe_pet(pet_name, animal_type='dog'):
    return f"I have a {animal_type} named {pet_name}."
print(f"Result: {describe_pet(pet_name='Buddy', animal_type='cat')}") #Output: I have a cat named Buddy.

#lambda function
print("\n--- Lambda function ---")
square_lambda = lambda x: x * x
print(f"Lambda function output: {square_lambda(6)}") #Output: 36
add_lambda = lambda x, y: x + y
print(f"Lambda function with multiple parameters: {add_lambda(10, 15)}")

# Exercises :
print("\n--- Exercises ---")
# 1.Write a function that checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
print(f"Is 7 a prime number? {is_prime(7)}") #Output: True
print(f"Is 10 a prime number? {is_prime(10)}") #Output

# 2.Build a temperature converter function. (Celsius to Fahrenheit)
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(f"25 degrees Celsius is {celsius_to_fahrenheit(25)} degrees Fahrenheit.") #Output: 77.0 degrees Fahrenheit