# Number Guessing Game

import random

computer = random.randint(1,10)
guess_no = int(input("guess no b/w 1 to 10 : "))
if guess_no == computer:
    print("You have guessed right")
elif guess_no > computer :
    print("you have guessed large")
elif guess_no < computer :
    print("you have guessed small")
else:
    print("Dfa ho")

print("computer guessed", computer)