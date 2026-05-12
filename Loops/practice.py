list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1

x = 49
i = 0
for el in list:
    if(el == x):
        print("Element Found at idx", i )
        break
    i += 1
else:
    print("end")