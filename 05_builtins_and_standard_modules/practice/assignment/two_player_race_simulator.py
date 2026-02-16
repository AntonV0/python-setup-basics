"""Two Player Race Simulator"""

import random  # To use randint() function


def race_simulator():
    """Simulate a two player race using dice rolls until one player reaches the finish line."""
    player1_position = 0
    player2_position = 0
    finish_line = 100
    dice_sides = 6

    while player1_position < finish_line and player2_position < finish_line:

        # ? Player 1 rolls the die and moves forward
        dice_score = random.randint(1, dice_sides)
        player1_position += dice_score
        print(
            f"Player 1 rolls a {dice_score} and moves to position {player1_position}")

        if player1_position >= finish_line:
            print("Player 1 wins")
            break  # Exit the loop if Player 1 wins

        # ? Player 2 rolls the die and moves forward
        dice_score = random.randint(1, dice_sides)
        player2_position += dice_score
        print(
            f"Player 2 rolls a {dice_score} and moves to position {player2_position}")

        if player2_position >= finish_line:
            print("Player 2 wins")
            break  # Exit the loop if Player 2 wins


# Run the race simulator
race_simulator()

# ? Example output:
# Player 1 rolls a 4 and moves to position 4
# Player 2 rolls a 3 and moves to position 3
# Player 1 rolls a 6 and moves to position 10
# Player 2 rolls a 3 and moves to position 6
# Player 1 rolls a 5 and moves to position 15
# Player 2 rolls a 6 and moves to position 12
# Player 1 rolls a 3 and moves to position 18
# Player 2 rolls a 5 and moves to position 17
# Player 1 rolls a 4 and moves to position 22
# Player 2 rolls a 3 and moves to position 20
# Player 1 rolls a 6 and moves to position 28
# Player 2 rolls a 5 and moves to position 25
# Player 1 rolls a 2 and moves to position 30
# Player 2 rolls a 3 and moves to position 28
# Player 1 rolls a 3 and moves to position 33
# Player 2 rolls a 1 and moves to position 29
# Player 1 rolls a 4 and moves to position 37
# Player 2 rolls a 5 and moves to position 34
# Player 1 rolls a 4 and moves to position 41
# Player 2 rolls a 3 and moves to position 37
# Player 1 rolls a 4 and moves to position 45
# Player 2 rolls a 4 and moves to position 41
# Player 1 rolls a 1 and moves to position 46
# Player 2 rolls a 1 and moves to position 42
# Player 1 rolls a 1 and moves to position 47
# Player 2 rolls a 6 and moves to position 48
# Player 1 rolls a 6 and moves to position 53
# Player 2 rolls a 3 and moves to position 51
# Player 1 rolls a 4 and moves to position 57
# Player 2 rolls a 6 and moves to position 57
# Player 1 rolls a 1 and moves to position 58
# Player 2 rolls a 5 and moves to position 62
# Player 1 rolls a 6 and moves to position 64
# Player 2 rolls a 1 and moves to position 63
# Player 1 rolls a 1 and moves to position 65
# Player 2 rolls a 2 and moves to position 65
# Player 1 rolls a 2 and moves to position 67
# Player 2 rolls a 2 and moves to position 67
# Player 1 rolls a 4 and moves to position 71
# Player 2 rolls a 2 and moves to position 69
# Player 1 rolls a 2 and moves to position 73
# Player 2 rolls a 4 and moves to position 73
# Player 1 rolls a 1 and moves to position 74
# Player 2 rolls a 3 and moves to position 76
# Player 1 rolls a 4 and moves to position 78
# Player 2 rolls a 4 and moves to position 80
# Player 1 rolls a 1 and moves to position 79
# Player 2 rolls a 3 and moves to position 83
# Player 1 rolls a 1 and moves to position 80
# Player 2 rolls a 5 and moves to position 88
# Player 1 rolls a 4 and moves to position 84
# Player 2 rolls a 6 and moves to position 94
# Player 1 rolls a 6 and moves to position 90
# Player 2 rolls a 5 and moves to position 99
# Player 1 rolls a 6 and moves to position 96
# Player 2 rolls a 6 and moves to position 105
# Player 2 wins
