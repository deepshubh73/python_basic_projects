import random

score = comp = 0

while True:
    choice = input("rock/paper/scissors (exit to quit): ")
    if choice == "exit": break
    
    com = random.choice(["rock", "paper", "scissors"])
    print(f"Computer: {com}")
    
    if choice == com:
        print("Tie!")
    elif (choice == "rock" and com == "scissors") or \
         (choice == "paper" and com == "rock") or \
         (choice == "scissors" and com == "paper"):
        score += 1
        print("You win!")
    else:
        comp += 1
        print("Computer wins!")
    
    print(f"Score: You {score} - {comp} Computer\n")

print(f"Final: You {score} - {comp} Computer")
print("You win!" if score > comp else "Computer wins!" if comp > score else "Tie!")
