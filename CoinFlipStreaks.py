print("Name:Tejaswini M",
       "AUID:1AY24AI111",
       "Section:O")
import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Create a list of 100 'heads' or 'tails' values.
    flips = []
    for i in range(100):
        flips.append('H' if random.randint(0, 1) == 0 else 'T')

    # Check for streaks of 6
    current_streak = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            current_streak += 1
            if current_streak == 6:
                numberOfStreaks += 1
                break  # Only count 1 streak per 100 flips
        else:
            current_streak = 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
