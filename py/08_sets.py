# Exercise:
# 1.Create a system that stores student grades as tuples (name, subject, grade) and uses sets to find unique subjects and students.

#list of tuples
#Each tuple has: (student_name, subject, grade)
grades = [
            ("Alice", "Math", 85),  
            ("Bob", "Science", 92),  
            ("Alice", "Science", 78),  
            ("Charlie", "Math", 90), 
            ("Bob", "Math", 88), 
            ("Alice", "English", 95),
            ("Aishah", "Bahasa Melayu", 95)
        ]

#Sets automatically remove duplicates.
unique_students = set() #set() -> collection of unique items (no duplicates)
unique_subjects = set()

for name, subject, grade in grades:
    unique_students.add(name)
    unique_subjects.add(subject)

print("Unique Students:", unique_students)
print("Unique Subjects:", unique_subjects)

#others code
print("\n--- Using index to access student names ---")
students = set()
for grade in grades:
    students.add(grade[0])  # grade[0] is the student name
print("Unique Students:", students)

subjects = set()
for grade in grades:
    subjects.add(grade[1])  # grade[1] is the subject
print("Unique Subjects:", subjects)

# Set comprehension to get unique student names -> call it Pythonic way to create sets in a concise manner.
print("\n--- Using set comprehension to get unique student names ---")
students = {grade[0] for grade in grades} #creates a set directly
print("Unique Students:", students)

#--------------just add on for exploration-----------------
print("\n--- Exploring set operations ---")
#sorted list of students
sorted_students = sorted(unique_students)
print("Sorted Unique Students:", sorted_students)

#remove a student from the set
unique_students.remove("Alice")
print("Unique Students after removing Alice:", unique_students)

#check if a student is in the set
is_aishah_in_set = "Aishah" in unique_students
print("Is Aishah in the set?", is_aishah_in_set) #boolean output: True

#clear the set of unique subjects
unique_subjects.clear()
print("Unique Subjects after clearing:", unique_subjects)

#difference between two sets (students who are not in the unique_students set)
other_students = {"David", "Alice", "Aishah"}  
students_not_in_unique = other_students.difference(unique_students)
print("Students not in unique_students set:", students_not_in_unique)
# output:
# Students not in unique_students set: {'David', 'Alice'}
# explanation:
# 'David' is not in the unique_students set, 
#  while 'Alice' was removed from the unique_students set, 
#  so both are considered as students not in the unique_students set.    

#if change (want to find students in unique_students set but not in other_students set)
students_not_in_unique = unique_students.difference(other_students)
print("Students in unique_students set but not in other_students set:", students_not_in_unique)
# output:
# Students in unique_students set but not in other_students set: {'Bob', 'Charlie'}
# explanation: 
# 'Bob' and 'Charlie' are in the unique_students set but not in the other_students set,
#  so they are considered as students in unique_students set but not in other_students set.

#union of two sets (all students from both sets)
all_students = unique_students.union(other_students)
print("All students from both sets:", all_students)
# output:
# All students from both sets: {'Bob', 'David', 'Charlie', 'Aishah'}
# explanation:
# The union of unique_students and other_students includes all unique students from both sets.  

#intersection of two sets (students who are in both sets)
common_students = unique_students.intersection(other_students)
print("Students in both sets:", common_students)
# output:
# Students in both sets: {'Aishah'}
# explanation: 
# The intersection of unique_students and other_students includes only the students that are present in both sets, which is 'Aishah' in this case.
# Alice not include because already removed at line 35, so Alice is not in both sets anymore.