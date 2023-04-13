import random

# Define player attributes
player = {'name': 'Player', 'health': 100, 'attack': 10, 'defense': 5}

# Define enemy types and their attributes
enemies = {'goblin': {'health': 50, 'attack': 5, 'defense': 2},
           'troll': {'health': 100, 'attack': 10, 'defense': 5}}

# Define the cave map
cave = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '.', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '#', '.', '.', '#', '.', '#'],
        ['#', '.', '#', '.', '.', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

# Define helper functions
def print_cave():
    for row in cave:
        print(' '.join(row))
    print('')

def move_player(x, y):
    # Check if move is valid
    if cave[y][x] != '#':
        # Move player to new location
        cave[y][x] = 'P'
        player['x'] = x
        player['y'] = y
        return True
    else:
        return False

def attack(attacker, defender):
    damage = attacker['attack'] - defender['defense']
    if damage > 0:
        defender['health'] -= damage
        print(f'{attacker["name"]} attacks {defender["name"]} for {damage} damage.')
    else:
        print(f'{attacker["name"]} attacks {defender["name"]} but does no damage.')

def fight(enemy):
    print(f'A {enemy} appears!')
    while player['health'] > 0 and enemies[enemy]['health'] > 0:
        action = input('Attack (a) or Run (r)? ')
        if action == 'a':
            attack(player, enemies[enemy])
            if enemies[enemy]['health'] > 0:
                attack(enemies[enemy], player)
        elif action == 'r':
            if random.randint(1, 2) == 1:
                print('You successfully run away.')
                return True
            else:
                print('You fail to run away.')
                attack(enemies[enemy], player)
        else:
            print('Invalid input.')
        print(f'{player["name"]}: {player["health"]} HP')
        print(f'{enemy}: {enemies[enemy]["health"]} HP')
    if player['health'] > 0:
        print(f'You defeated the {enemy}.')
        return True
    else:
        print('You have been defeated.')
        return False

# Initialize player location
move_player(1, 1)

# Start game loop
while True:
    print_cave()
    # Check for win condition
    if player['x'] == 8 and player['y'] == 4:
        print('Congratulations, you have escaped the cave!')
        break
    # Check for encounter with enemy
    if random.randint(1, 5) == 1:
        if fight('goblin'):
            print('You continue on your way.')
        else:
            print('Game over.')
            break
    # Get player input for movement
    move = input('Enter direction to move (N, S, E, W): ').lower()
    if move == 'n':
        move_player
