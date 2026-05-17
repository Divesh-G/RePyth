# Class definition
class Student:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
student1 = Student("Divesh", 20)
student2 = Student("Ram", 22)

# Calling methods
student1.display()

print()

student2.display()