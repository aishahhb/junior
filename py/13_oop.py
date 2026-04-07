#OOP - Inheritance
# It allows one class (child/subclass) to inherit properties and methods from another class (parent/superclass).
# This promotes code reusability and establishes a natural hierarchical relationship between classes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Parent display method:")
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person): #inheritance starts here - Student is a child class of Person
    def __init__(self, name, age, student_id): 
        super().__init__(name, age) #Using parent constructor → part of inheritance (reusing parent code)
        self.student_id = student_id

    def display(self): # This part is polymorphism - method overriding
        super().display() # Call the parent display method (supports reuse)
        print("\nChild display method:") 
        print(f"Student ID: {self.student_id}")

    def study(self): #Not polymorphism - No same method in parent 
        print(f"{self.name} is studying.")

# Create an instance of Student
student = Student("Alice", 20, "S12345")
student.display()
student.study()


#--------------Polymorphism---------------
# Polymorphism - Polymorphism allows methods to be used in different ways based on the object that is calling them.
# In this example, both Student and Teacher classes have a display method, but they behave differently based on the class they belong to.
# This is an example of method overriding, which is a key aspect of polymorphism in OOP. 

#------------------Conclusion------------------
# Inheritance = structure (parent → child)
# Polymorphism = behavior (same method, different result)