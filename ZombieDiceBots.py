# ZombieDiceBots.py
import random
print("Name:Tejaswini M",
       "AUID:1AY24AI111",
       "Section:O")
def roll_dice():
    return [random.choice(['brain', 'shotgun', 'footsteps']) for _ in range(3)]

def simple_bot_turn():
    brains = 0
    shotguns = 0
    print("SimpleBot's turn:")
    while True:
        roll = roll_dice()
        brains += roll.count('brain')
        shotguns += roll.count('shotgun')
        print(f"Rolled: {roll} | Brains: {brains}, Shotguns: {shotguns}")
        
        if shotguns >= 3:
            print("BUSTED! Lost all brains.")
            return 0
        
        # Simple strategy: stop if 2 shotguns
        if shotguns >= 2:
            print(f"Stopping with {brains} brains.")
            return brains

# Run one turn
simple_bot_turn()
