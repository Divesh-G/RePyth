list = [2, 1, 3]

list.append(4)
print(list) #will add 4 to the exsisting list
list.sort() #sort the list in ascending order. If we try to print this then i will give none value
print(list)
list.sort(reverse = True) #to print the list in descending order
print(list)


list2 = ["Ram", "Shyam", "Hari", "Gita", "Sita"]
list2.sort()
print(list2)

list2.insert(2, "Dibash")
print(list2)

arry = [1, 2, 3, 4, 5]
arry.remove(2)
print(arry)
arry.pop(1)
print(arry)
