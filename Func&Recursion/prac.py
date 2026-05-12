cities = ["Kathmandu", "Pokhara", "Chitwan", "Butwal"]
heroes = ["Tarzan","Ekku"]

def func(cities):
    print(len(cities))
    print(len(heroes))
 
    for hero in heroes:
        print(hero, end=" ")
    return 0
func(cities)

def fact(n):
    rng = range(1, n+1)
    fact = 1
    for num in  rng:
        fact *= num
    print(fact)
fact(7)


def converter(rate):
    usd = int(input("Enter USD Amount: "))
    npr = usd * rate
    print(usd, "USD is equal to NRs", npr)
converter(135)

def function():
    num = int(input("Enter a number: "))
    if(num%2 == 0):
        print("Even")
    else:
        print("Odd")
function()