#Error Handling

#if y not defined, it will raise a NameError, which we can catch and handle gracefully
try: print(y)
except NameError:
    print("Variable x is not defined")

#If we try to convert a non-numeric string to an integer, it will raise a ValueError, which we can catch and handle gracefully
try: x = int("abc")
except ValueError:
    print("Cannot convert 'abc' to an integer")

#multiple exceptions can be handled in a single except block by using a tuple of exception types
print("\n-----Multiple Exceptions:-----")
try: x = 1 / 0
except (ZeroDivisionError, ValueError):
    print("An error occurred: division by zero or invalid value")   
except Exception as e:
    print(f"An unexpected error occurred: {e}")

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero number.")

print(f"Result: {result}")

#using if else
print("\n-----Open File:-----")
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")  
else:
    # If the file is opened successfully, we can read its content
    content = file.read()
    print(content)
    print("File read successfully.")
finally:
    #always executes, regardless of whether an exception occurred or not. 
    # It is typically used for cleanup actions, such as closing files or releasing resources.
    if 'file' in locals() and not file.closed:
        file.close()
    print("This block will always execute, regardless of whether an exception occurred or not.")

#raising exceptions allows us to signal that an error has occurred and provide information about the error.
print("\n-----Raising Exceptions:-----")
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
try:    
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

print(f"Result: {result}")

#Custom Validation
print("\n-----Custom Validation:-----")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age cannot be greater than 120")
    return age

try:
    age = validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")


