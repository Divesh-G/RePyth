class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("Creating new student")

s1 = Student("Karan")
print(s1.name)

class Animal:
    # Default Constructor
    def __init__(self):
        pass

    # Parameterized Constructor
    def __init__(self, type, sound):
        self.type = type
        self.sound = sound
        print("I am a type")

a1 = Animal("Tiger", "Roar")
print(a1.type, a1.sound)

a2 = Animal("Lion","")
print(a2.type)