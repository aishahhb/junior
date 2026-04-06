#template creating a class
class Animal:
    #constructor
    def __init__(self, name, age): #initializer 
        self.name = name
        self.age = age

    #method
    def bark(self):
        return "Woof!"
#creating a subclass that inherits from Animal
class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)  # calling the constructor of the parent class

#creating an object of the class
my_tiger = Tiger("Simba", 5)
#accessing attributes and methods
print(my_tiger.name)  # Output: Simba
print(my_tiger.age)   # Output: 5


class Student:
    # class attribute (shared by all instances)
    species = "Nurul Amirah"  

    #constructor
    def __init__(self, name, age, tricky_courses, non_tricky):
        self.name = name
        self.age = age
        self.tricky_courses = tricky_courses["Courses"]
        self.non_tricky = non_tricky

    #method for tricky structure
    def list_tricky_courses(self):
        # Get subject names only from this student's tricky_courses
        subjects = {
            value
            for course in self.tricky_courses
            for key, value in course.items()
            if key.startswith("subject")
        }
        return list(subjects)
    
    def list_non_tricky_courses(self):
        #get subject used set()
        subjects = set()
        for course in self.non_tricky:
            subjects.add(course["subject"])

        return subjects
    
    #Get total score from non-tricky courses
    def total_score(self):
        return sum(course["score"] for course in self.non_tricky)
    
    #Get total score from tricky courses
    def total_score_tricky(self):
        return sum(course[key] for course in self.tricky_courses for key in course if key.startswith("score"))
    
#creating an object of the class
student1 = Student("Amir", 20, {
    #tricky structure :each course dictionary uses different keys
    "Courses": [
        {"subject1": "Math", "score1": 85}, 
        {"subject2": "Science", "score2": 90},
        {"subject3": "Art", "score3": 78}
    ]},[
        #not tricky structure : each course dictionary uses the same keys
        {"subject": "History", "score": 80},
        {"subject": "Literature", "score": 88},
        {"subject": "Math", "score": 85}
    ])
student2 = Student("Siti", 22, {
    "Courses": [
        {"subject1": "Math", "score1": 88},
        {"subject2": "Science", "score2": 92},
        {"subject3": "Art", "score3": 85}
    ]
    },[
        {"subject": "History", "score": 82},
        {"subject": "Literature", "score": 90},
        {"subject": "Math", "score": 88}
    ])

#accessing class attribute
print(Student.species)  # Output: Nurul Amirah
#accessing instance attributes
print(student1.name)  # Output: Amir
#get list of courses using the tricky method
print("Tricky Code:", student1.list_tricky_courses())
print("Non-Tricky Code:", student2.list_non_tricky_courses())
print("Total Score:", student1.total_score())
print("Total Score (Tricky):", student1.total_score_tricky()) 



# Exercise:
# 1.Create a simple game character class with attributes like name, health, and level. Include methods for attacking and taking damage.
print("\n-------Exercise-------")
class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def attack(self):
        return f"{self.name} attacks with power {self.level * 10}!"

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        else:
            return f"{self.name} takes {damage} damage and has {self.health} health left."
        
character1 = GameCharacter("Hazril", 100, 5)
print(character1.attack())  # Output: Hazril attacks with power 50!
print(character1.take_damage(30))  # Output: Hazril takes 30 damage and has 70 health left.