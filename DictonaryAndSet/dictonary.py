info = {
    "name" : "Dibash",
    # "name" : "Hero",  will change dibash to hero
    "course" : "BCA",
    "age" : 23,
    "is_adult" : True,
    "subjects" : ["Python", "C", "Java"],
    "marks" : 95.5
}
print(info)
print(info["age"])
info["name"] = "Divesh"
print(info)

null_dict = {}
null_dict["name"] = "Null Dictonary"
print(null_dict)