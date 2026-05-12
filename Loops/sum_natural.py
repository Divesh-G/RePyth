n = int(input("Enter a natural number: "))

boundary = range(1, n+1)
print(boundary)

sum = 0
for i in boundary:
    sum += i
    
print("Total sum: ", sum)

fact = 1
for j in boundary:
    fact *= j

print("Factorial of a number is: ", fact)

