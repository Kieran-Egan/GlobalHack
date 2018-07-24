import random
print("Welcome to Rock Paper Scissors! Type the number that corresponds to the item you want to choose.")
player = input("1 = Rock, 2 = Paper, 3 = Scissors, Shoot! ")
print("Your choice is:")
if player == 1:
    print("Rock")
elif player == 2:
    print("Paper")
elif player == 3:
    print("Scissors")
else:
    print("You didn't type in a valid number. Try again!")

# break break break break break break break break break break break break break

print("The computer chose:")
diceThrow = random.randrange(1, 3)
computer = diceThrow
if computer == 1:
    print("Rock")
elif computer == 2:
    print("Paper")
elif computer == 3:
    print("Scissors")
else: 
    print("You didn't type in a valid number. Try again!")
    
# break break break break break break break break break break break break break

if player - computer == -1:
    print("You lost. Try again!")
elif player - computer == -2:
    print("You win!")
elif player - computer == 0:
    print("You tied")
elif player - computer == 1:
    print("You win!")
elif player - computer == 2:
    print("You lost. Try again!")
else:
    print("An error has occured!")
