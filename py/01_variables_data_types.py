## Variables and data types

name = "aishah"         #string
age = 40                #integer
weight = 60.1           #float
is_female = True        #bolean (only True or False)
randon_number = None    #NoneType

# Excersice 1. Create variables that consist String, Integer, Float, and Booleandata types. Print value for each key.
print(name)
print(type(age))
print(type(randon_number))

x = 11
y = 3

print("Addition: ", x + y)          #addition
print("Subtraction: ", x - y)       #subtraction
print("Multiple: ", x * y)          #multiple
print("Division: ", x / y)          #division
print("Floor division: ", x // y)   #floor division
print("Modulus: ", x % y)           #modulus
print("Exponentation: ", x ** y)    #exponentation


# Exercise 2. Convert Celsius to Fahrenheit. (F = C * 9/5 + 32)celcius = 25
celsius = 25
fahrenheit = celsius * 9/5 + 32
print("Fahrenheit:", fahrenheit)