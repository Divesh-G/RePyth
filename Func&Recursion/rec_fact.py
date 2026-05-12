def fact(n):
    # n = int(input("Enter a number: "))
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))


# recursive function to calculate sum of numbers using recursion
def sum(m):
    if(m == 0):
        return 0
    else:
        return sum(m-1) + m
print(sum(4))

# recursive function to print all the elements of list
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "apple", "banana", "litchi"]
print_list(fruits)