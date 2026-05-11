student = {
    "name" : "Balbhadra Kunwar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

print(student.keys())
print(len(student.keys()))
print(list(student["subjects"]))

print(student.values())
print(list(student.values()))

# .items method returns pairse in form of tupple
print(student.items())
 
 #can acces the output of items using indexing
pairs = list(student.items())
print(pairs[0])

# .get method to return value
print(student["name"]) # if we provide name2 which is not available. it gives error.
print(student.get("name")) # for the above condition it returns none.

# update method to add new data to the dictonary
student.update({"city" : "Kathmandu"})

# can update new dictonary to the existing dictonary as well
new_dict = {"munucipality" : "Nagarjun"}

student.update(new_dict)
print(student)