def calcSum(): # parameter
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    c = a + b
    return c
# print(calcSum()) # argument

def calcMul(a, b):
    return a * b
print(calcMul(10.5, 6))

def calcAvg(a, b, c):
    return ((a+b+c)/3)
print(calcAvg(1,2,3))

print("hello", end=" ") # end will let the outpot to be printed in same line
print("By Divesh")
