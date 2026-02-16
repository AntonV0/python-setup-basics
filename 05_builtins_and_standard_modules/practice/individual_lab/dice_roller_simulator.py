"""Text-Based Dice Roller Simulator using random module"""

import random  # To use randint() function

# Ask user to choose how many dice to roll and how many sides each die should have
num_dice = int(input("Enter the number of dice to roll: "))
num_sides = int(input("Enter the number of sides on each die: "))


def simulate_dice_roll(num_sides):
    """Simulate rolling a single die with a given number of sides."""
    return random.randint(1, num_sides)  # Generate a random integer between 1 and num_sides


# Simulate rolling the dice
for _ in range(num_dice):  # Loop to roll the specified number of dice
    # The underscore (_) is used as a throwaway variable (no need to keep track of the loop index)
    print("Rolled:", simulate_dice_roll(num_sides))

# ? Example output:
# Enter the number of dice to roll: 3
# Enter the number of sides on each die: 6
# Rolled: 4
# Rolled: 1
# Rolled: 6

# Enter the number of dice to roll: 5
# Enter the number of sides on each die: 20
# Rolled: 17
# Rolled: 3
# Rolled: 20
# Rolled: 8
# Rolled: 12
