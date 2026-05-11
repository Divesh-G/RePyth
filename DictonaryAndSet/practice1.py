# add values to the dictonary
dicto = {
    "table" : ["a piece of furniture","list of facts and figures"],
    "cat" : "a small animal"
}
print(dicto)

# how many rooms are required if one subect takes one room
list1 = {"Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"}
print(type(list1))
print("Required number of classroom is:", len(list1))


# create a empty dictonary and input 3 marks
marks = {}
sub1 = int(input("Enter first marks: "))
marks.update({"phy":sub1})

sub2 = int(input("Enter second marks: "))
marks.update({"chem":sub2})

sub3 = int(input("Enter third marks: "))
marks.update({"math":sub3})

print(marks)

sett = {9, 9.0}
print(sett)