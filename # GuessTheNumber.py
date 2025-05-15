# GuessTheNumber.py

import random
print("Name: Tejaswini M")
print("USN: 1AY24AI111")
print("Section: O")
number = random.randint(1, 10)
print("Guess a number between 1 and 10:")
guess = 0
while guess != number:
    guess = int(input("Your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it! Congratulations!")
        
