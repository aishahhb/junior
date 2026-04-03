fruits = ('apple', 'banana', 'cherry')
temp_list = list(fruits)
temp_list[1] = 'orange'
fruits = tuple(temp_list)
print(fruits)   # ('apple', 'orange', 'cherry')

# Unpacking a tuple
person = ('John', 30, 'Engineer')
name, age, profession = person
print("Name:", name) 
print("Age:", age)   
print("Profession:", profession) 

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(f"Concatenated Tuple: {concatenated_tuple}")  

# Tuple repetition
repeated_tuple = tuple1 * 3
print(f"Repeated Tuple: {repeated_tuple}")

#checking if an item is in a tuple
if 2 in tuple1:
    print("2 is in tuple1.")


#counting occurrences of an item in a tuple
count_2 = repeated_tuple.count(2)
print(f"Number of occurrences of 2 in repeated_tuple: {count_2}")

# Tuple slicing
sliced_tuple = concatenated_tuple[2:5]
print(f"Sliced Tuple: {sliced_tuple}")

# Finding the largest and smallest number in a tuple
numbers_tuple = (5, 2, 9, 1, 5, 6)
largest = max(numbers_tuple)
smallest = min(numbers_tuple)
print("Largest number in tuple:", largest)
print("Smallest number in tuple:", smallest)

#Concatenate tuples
concatenated_tuple2 = repeated_tuple + numbers_tuple
print(f"Concatenated Tuple 2: {concatenated_tuple2}")


#Examples of tuples in real life:
# Coordinates of a point
point = (10, 20)

# Days of the week
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

print(point[0])
print(days[2])