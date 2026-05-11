# sets is the collection of the unordered items. 
# Each element in the set must be unique and immutable

collection = {1, 2, 3, 2, 2, "Hello", "Hello"} #duplicates will be stored as only one item
print(collection)
print(type(collection))

empty_set = set()
dicto = {}
print(type(empty_set))
print(type(dicto))

collection.add(5) # add new value to the set
collection.add((10, 11, 12)) # can add tuples but not lists because of mutable
print(collection)

collection.remove(1) # removes given value
print(collection)

collection.pop() # removes random 1 value
print(collection)

collection.clear() # clear all values
print(collection)

