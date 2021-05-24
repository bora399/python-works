import random
import time
#Rock Paper Scissors Algorithm
# Rock > Scissors / Rock < Paper / Paper > Rock / Paper < Scissors / Scissors > Paper / Scissors < Rock 
#Rock Paper Scissors Algorithm

#Variables - Questions
name = input("What's your name ? ")
tour = int(input("How many tours do you want to play ?"))
i=0
playerPoint = 0
computerPoint = 0
remainingTour = 0
myList = ["Rock","Paper","Scissors"]
#Variables - Questions

#While Loop
while i < tour:
    choice = input("Your Choice /'Rock'/ /'Paper'/ /'Scissors'/ :  ")
    choice2 = choice.capitalize()#To capitalize the first letter
    computerChoice = random.choice(myList)
    if choice2 == computerChoice:
        print("Computer Choice : {}".format(computerChoice))
        time.sleep(1)
        print("Draw ! This tour won't count !")
        print("Remained Tour : {}".format(tour-i))
        print()
    elif choice2 == "Rock" or choice2 == "rock" and computerChoice == "Scissors":
        print("Computer Choice : {}".format(computerChoice))
        time.sleep(1)
        print("{} Won !".format(name))
        i+=1
        playerPoint += 1
        print("Remained Tour : {}".format(tour-i))
        print()
    elif choice2 == "Paper" or choice2 == "paper" and computerChoice == "Rock":
        print("Computer Choice : {}".format(computerChoice))
        time.sleep(1)
        print("{} Won !".format(name))
        i+=1
        playerPoint += 1
        print("Remained Tour : {}".format(tour-i))
        print()
    elif choice2 == "Scissors" or choice2 == "scissors" and computerChoice == "Paper":
        print("Computer Choice : {}".format(computerChoice))
        time.sleep(1)
        print("{} Won !".format(name))
        i+=1
        playerPoint += 1
        print("Remained Tour : {}".format(tour-i))
        print()
    elif computerChoice == "Rock" and choice2 == "Scissors" or choice2 == "scissors":
        print("Computer Choice : {}".format(computerChoice))
        time.sleep(1)
        print("Computer Won !")
        i+=1
        computerPoint += 1
        print("Remained Tour : {}".format(tour-i))
        print()
    elif computerChoice == "Paper" and choice2 == "Rock" or choice2 == "rock":
        print("Computer Choice : {}".format(computerChoice))
        time.sleep(1)
        print("Computer Won !")
        i+=1
        computerPoint += 1
        print("Remained Tour : {}".format(tour-i))
        print()
    elif computerChoice == "Scissors" and choice2 == "Paper" or choice2 == "paper":
        print("Computer Choice : {}".format(computerChoice))
        time.sleep(1)
        print("Computer Won !")
        i+=1
        computerPoint += 1
        print("Remained Tour : {}".format(tour-i))
        print()
#While Loop

#Finish
if playerPoint > computerPoint:
    print("Player Won !!! Player Score : {} /// Computer Score : {}".format(playerPoint,computerPoint))
elif computerPoint > playerPoint:
    print("Computer Won !!! Computer Score : {} /// Player Score : {}".format(computerPoint,playerPoint))
elif playerPoint == computerPoint:
    print("Draw !!! Player Score : {} /// Computer Score : {}".format(playerPoint,computerPoint))
#Finish

 
    
