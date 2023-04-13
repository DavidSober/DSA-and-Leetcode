import random

player_hp = 100
enemy_hp = 50

print('You are stuck in a cave and need to find your way out.')
print('You notice two paths, one to the left and one to the right.')

while True:
    move = input('Enter direction to move (N/S/E/W): ')
    if move.upper() == 'N':
        print('You move North.')
    elif move.upper() == 'S':
        print('You move South.')
    elif move.upper() == 'E':
        print('You move East.')
    elif move.upper() == 'W':
        print('You move West.')
    else:
        print('Invalid direction. Try again.')
        continue

    # Random enemy encounter
    if random.random() < 0.25:
        print('You encounter an enemy!')
        while player_hp > 0 and enemy_hp > 0:
            action = input('Enter action (attack/defend): ')
            if action.lower() == 'attack':
                damage = random.randint(5, 15)
                enemy_hp -= damage
                print('You deal', damage, 'damage.')
            elif action.lower() == 'defend':
                print('You defend.')
            else:
                print('Invalid action. Try again.')
                continue

            # Enemy attacks
            if enemy_hp > 0:
                damage = random.randint(3, 10)
                player_hp -= damage
                print('Enemy deals', damage, 'damage.')

        if player_hp <= 0:
            print('You have been defeated.')
            break
        else:
            print('You have defeated the enemy!')

    # Check if player has reached the end
    if random.random() < 0.2:
        print('You have found the exit! Good job.')
        break

print('Game over!') 

