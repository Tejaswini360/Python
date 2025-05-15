import random
print("Name:Tejaswini M",
       "AUID:1AY24AI111",
       "Section:O")
choices = ["rock", "paper", "scissors"]

print("Let's play Rock, Paper, Scissors!")
player = input("Enter your choice (rock, paper, or scissors): ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win!")
elif player in choices:
    print("You lose!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
