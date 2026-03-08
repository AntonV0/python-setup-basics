"""Exercise 6: Real World Interaction"""


class Player:
    """Player class with attributes for health and damage."""

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self, target_monster):
        """Simulate an attack on a Monster object."""
        print(f"Player attacks the monster for {self.damage} damage!")
        target_monster.take_damage(self.damage)

    def take_damage(self, damage):
        """Simulate the player taking damage."""
        self.health -= damage
        print(
            f"Player takes {damage} damage! Remaining health: {self.health}HP\n")
        if self.health <= 0:
            print("Player is defeated!")


class Monster:
    """Monster class with attributes for health and damage."""

    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def attack(self, target_player):
        """Simulate an attack on a Player object."""
        print(f"Monster attacks the player for {self.damage} damage!")
        target_player.take_damage(self.damage)

    def take_damage(self, damage):
        """Simulate the monster taking damage."""
        self.health -= damage
        print(
            f"Monster takes {damage} damage! Remaining health: {self.health}HP\n")
        if self.health <= 0:
            print("Monster is defeated!")


if __name__ == "__main__":
    def get_int(prompt):
        """Helper function to get integer input from the user."""
        while True:
            try:
                # prompt is the message shown to the user when asking for input
                return int(input(prompt))  # Convert the input to an integer
            except ValueError:
                print("Invalid input. Please enter numeric values for HP and damage.")

    player_hp = get_int("Enter player HP: ")
    player_damage = get_int("Enter player damage: ")
    monster_hp = get_int("Enter monster HP: ")
    monster_damage = get_int("Enter monster damage: ")

    player = Player(player_hp, player_damage)
    monster = Monster(monster_hp, monster_damage)

    print("\n--- Battle Start! ---\n")

    # Simulate the battle
    while player.health > 0 and monster.health > 0:  # Loop continues until someone is defeated

        player.attack(monster)  # Player attacks first
        if monster.health <= 0:
            print("Player wins the battle!")
            break

        monster.attack(player)  # Monster retaliates if still alive
        if player.health <= 0:
            print("Monster wins the battle!")
            break

# ? Example Output (Player wins):
# Enter player HP: 100
# Enter player damage: 20
# Enter monster HP: 60
# Enter monster damage: 10

# --- Battle Start! ---

# Player attacks the monster for 20 damage!
# Monster takes 20 damage! Remaining health: 40HP

# Monster attacks the player for 10 damage!
# Player takes 10 damage! Remaining health: 90HP

# Player attacks the monster for 20 damage!
# Monster takes 20 damage! Remaining health: 20HP

# Monster attacks the player for 10 damage!
# Player takes 10 damage! Remaining health: 80HP

# Player attacks the monster for 20 damage!
# Monster takes 20 damage! Remaining health: 0HP

# Monster is defeated!
# Player wins the battle!

# ? Example Output (Monster wins):
# --- Battle Start! ---

# Player attacks the monster for 25 damage!
# Monster takes 25 damage! Remaining health: 275HP

# Monster attacks the player for 60 damage!
# Player takes 60 damage! Remaining health: 140HP

# Player attacks the monster for 25 damage!
# Monster takes 25 damage! Remaining health: 250HP

# Monster attacks the player for 60 damage!
# Player takes 60 damage! Remaining health: 80HP

# Player attacks the monster for 25 damage!
# Monster takes 25 damage! Remaining health: 225HP

# Monster attacks the player for 60 damage!
# Player takes 60 damage! Remaining health: 20HP

# Player attacks the monster for 25 damage!
# Monster takes 25 damage! Remaining health: 200HP

# Monster attacks the player for 60 damage!
# Player takes 60 damage! Remaining health: -40HP

# Player is defeated!
# Monster wins the battle!
