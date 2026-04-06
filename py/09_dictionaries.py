# Exercises:
# 1.Create a dictionary called student_records with the following information:
# "student_001": name is "John", age is 19, major is "Computer Science", grades are [85, 92, 78]
# "student_002": name is "Sarah", age is 20, major is "Biology", grades are [90, 88, 95]  
# 2. Add a new student "student_003" with name "Mike", age 18, major "Math", grades [82,
# 3. Update John's age to 20  
# 4. Loop through the dictionary and print each student's information in this format:
# "Student ID:[id], Name:[name], Major:[major]"

student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

#Add new student to the dictionary - Q2
student_records["student_003"] = {
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 85, 98]
}

#Update John's age to 20 - Q3
student_records["student_001"]["age"] = 20

#Loop through the dictionary and print each student's information - Q4
for student_id, info in student_records.items():
    print(f"Student ID: {student_id}, Name: {info['name']}, Major: {info['major']}")


#additional code for exploration
print("\n--- Exploring dictionary operations ---")
#Get a list of all student IDs
student_ids = list(student_records.keys())
print("Student IDs:", student_ids) 

#Get all keys
print("Student Names:", student_records.keys())

#Get all values
print("Student Information:", student_records.values())

#Get key-value 
print("Student Items:", student_records.items())

#Check if a student ID exists
print("\n--- Check if a student ID exists ---")
is_student_002_present = "student_002" in student_records
print("Is student_002 present?", is_student_002_present) #boolean output: True

#Iterating thriught dictionary items
print("\n--- Iterating through dictionary items ---")
for student_id, info in student_records.items():
    print(f"Student ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Major: {info['major']}, Grades: {info['grades']}")
#accessing value using key
for key in student_records:
    print(f"Key: {key}, Value: {student_records[key]}")
    
#accessing key and value directly in the loop
for key, value in student_records.items():
    print(f"Key: {key}, Value: {value}")

#Nested dictionary access
print("\n--- Nested ---")
john_major = student_records["student_001"].items() #accessing John's major
print("John's Major:", john_major)
print("Student 003 Info:", student_records['student_003'])
print("Mike's Grades:", student_records['student_003']['grades'])

#delete a student
print("\n--- Delete ---")
del student_records["student_001"] #deletes student_001
print("Student Records after deletion:", student_records)

#Remove a student 
print("\n--- Remove ---")
removed_student = student_records.pop("student_003", None) #removes student_003 and returns its info, or None if not found
print("Removed Student Info:", removed_student)

#clear the dictionary
print("\n--- Clear Records ---")
student_records.clear() #removes all entries from the dictionary
print("Student Records after clearing:", student_records)
