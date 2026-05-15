import os

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

# append to end of a file 
with open("hello.txt", "a+") as fi:
    hello = fi.write("\nNew data")
    print(hello)

# deleting a data. import os for that
# os.remove("")

