f = open("D:\\python\\File_IO\\demo.txt", "r")

# if we read whole data before reading data line by line then py will return null
# data = f.read()
# print(data)
# print(type(data))

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()