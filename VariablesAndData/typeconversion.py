# type conversion is automatic 
a = 2 #python autmatically converts it to 2.0
b = 3.3
sum = a + b
print(sum)

#type casting is done by the user itself
c = "2"
d = float("5")
int(c)
print(c)
print(d)


pi = 3.14
print(str(pi))

# input in python
# input() keyword is used to take input from the users
# input will convert every value into string
name = input("enter your name: ")
print("welcome", name)
age = int(input("enter your age: "))
print("your age type is: ", type(age))

name1 = input("enter your name: ")
age1 = float(input("enter your age: "))
marks = int(input("enter your marks: "))

print(name1, age1, marks)

"""
hello this is multiline comment
"""