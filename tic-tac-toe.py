# This is actually a rock-paper-scissors game

#Write your solution below the starter code
# Follow the instructions in the tab to the right
from random import seed
from random import randint

seed(6)
#import random
import random

x = 1
# Welcome the user to the game
print("Welcome to rock, paper, scissors. Good luck!")

while x < 4:
    a = input("\nEnter your choice: Rock, Scissors, or Paper: ")
    a = a.lower()
    b = random.randint(1, 3)
    if b == 1:
        b = "rock"
        print("The computer chooses Rock")
    elif b == 2:
        b = "scissors"
        print("The computer chooses Scissors")
    elif b == 3:
        b = "paper"
        print("The computer chooses Paper")

    if a == b:
        print("It's a draw")
    elif (a == "rock" and b == "scissors"):
        print("Rock smashes Scissors. YOU WIN!")
    elif (a == "scissors" and b == "rock"):
        print("Rock smashes Scissors. YOU LOSE!")
    elif (a == "paper" and b == "rock"):
        print("Paper wraps rock. YOU WIN!")
    elif (a == "rock" and b == "paper"):
        print("Paper wraps rock. YOU LOSE!")
    elif (a == "scissors" and b == "paper"):
        print("Scissors cuts paper. YOU WIN!")
    elif (a == "paper" and b == "scissors"):
        print("Scissors cuts paper. YOU LOSE!")
    else:
        print(
            "Invalid input! You have to enter either Rock, Paper, or Scissors")
    x += 1
    # Make a choice for the computer player
    # Get a choice from the user
    # Compare the user and computer choice
    # Print the right message, based on the choices
