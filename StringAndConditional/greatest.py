a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))
d = int(input("enter third number:"))

if(a >= b and a >= c and a >= d):
    print("a is greater")
elif(b >= a and b >= c and b >= d):
    print("b is greater")
elif(c >= a and c >= b and c >= d):
    print("c is greater")
else:
    print("d is greater")