# starting index which is optional, stoping condition which is mandatory & step is optional (range function)
step = range(0, 10, 2)
print(step)

for el in step:
    print(el)

# for i in range(100):
#     print(i)


# negative indexing in range
for i in range(100, 0, -1):
    print(i)

# multiplication using range
n = int(input("Enter a number: "))
for ind in range(0, n*11, n):
    print(ind)


# alternative way for multiplication
m = int(input("Enter second number: "))
for fac in range(1, 11):
    print(m*fac)
