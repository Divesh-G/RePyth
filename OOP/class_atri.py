class Student:
    college_name = "ABC College"
    name = "anonymous" # Class Attribute

    def __init__(self, name, marks):
        self.name = name  # Object Attribute
        self.marks = marks
        print("I am a new student")

    def welcome(self):
        print("Welcome", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Karan", 97)
print(s1.name, s1.marks) # Karan

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)

print(s2.college_name)
print(Student.college_name)

print(s1.welcome())
print(s1.get_marks())


