import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q) : ")
    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break

    if(userChoice < target):
        print("Your number is too small, take a bigger guess..")
    else:
        print("Your number is too big, take a small guess..")

print("-------GAME OVER-------")
