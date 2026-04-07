#Libraries
#Libraries are collections of pre-written code that can be used to perform specific tasks. 
# They provide a way to reuse code and save time when developing applications. 
# In Python, there are many built-in libraries as well as third-party libraries that can be installed using package managers like pip.

import os
import sys
import datetime
import random

print("--------------OS Library--------------")
print("Operating System:", os.name)
print("Current file path:", (__file__))
print("Current working directory:", os.getcwd())
print("Current file directory:", os.path.dirname(os.path.abspath(__file__)))

print("\n--------------Sys Library--------------")
print("Python executable path:", sys.executable)
print("Python version:", sys.version)
print("Search path:", sys.path.append("C:/PythonBootcamp/"))

print("\n--------------Datetime Library--------------")
now = datetime.datetime.now()
today = datetime.date.today()
formatatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time:", now)
print("Today's date:", today)
print("Formatted date and time:", formatatted_date)

print("\n--------------Random Library--------------")
random_number = random.randint(1, 100)
random_float = random.random()
random_choice = random.choice(['apple', 'banana', 'cherry'])
print("Random integer between 1 and 100:", random_number)
print("Random float between 0 and 1:", random_float)
print("Random choice from list:", random_choice)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)


