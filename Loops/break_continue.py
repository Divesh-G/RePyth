i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    else:
        print("finding....")
    i += 1


# continue
j = 0
while j <= 5:
    if(j == 3):
        j += 1
        continue
    else:
        print(j)
        j += 1


#Print all the even numbers using loop from 1 to 10
k = 1
while k <= 10:
    if(k%2 != 0):
        k += 1
        continue
    else:
        print(k)
        k += 1