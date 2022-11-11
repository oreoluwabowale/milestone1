from random import randint

print(" Rock, Paper, Scissors! Game".center(30))
print()
print("Rock is 1, Paper is 2, Scissors is 3. ")
print("Rock blunts scissors, (rock wins)")
print("Scissors cut paper (Scissors wins)")
print("Paper wraps rock (paper wins)")
print()
usersNumber = int(input("Please input a number from 1-3: "))
randomNumber = randint(1,3)


def game(choice):
    if choice == 1:
        playerChoosesRock(choice)
    elif choice == 2:
        playerChoosesPaper(choice)
    elif choice == 3:
        playerChoosesScissors(choice)
    else:
        print("Invalid Input")
        

def playerChoosesRock(UsersNumber):
    if usersNumber == 1 and randomNumber == 1:
        print("Computer chose: ", randomNumber)
        print("Draw")
    elif usersNumber == 1 and randomNumber == 2:
        print("Computer chose: ", randomNumber)
        print("You Lost")
    elif usersNumber == 1 and randomNumber == 3:
        print("Computer chose: ", randomNumber)
        print("You won")
        
def playerChoosesPaper(usersNumber):
    if usersNumber == 2 and randomNumber == 1:
        print("Computer chose: ", randomNumber)
        print("You won")
    elif usersNumber == 2 and randomNumber == 2:
        print("Computer chose: ", randomNumber)
        print("Draw")
    elif usersNumber == 2 and randomNumber == 3:
        print("Computer chose: ", randomNumber)
        print("You Lost")
        
def playerChoosesScissors(usersNumber):
    if usersNumber == 3 and randomNumber == 1:
        print("Computer chose: ", randomNumber)
        print("You Lost")
    elif usersNumber == 3 and randomNumber == 2:
        print("Computer chose: ", randomNumber)
        print("You Won")
    elif usersNumber == 3 and randomNumber == 3:
        print("Computer chose: ", randomNumber)
        print("Draw")
        
game(usersNumber)
        