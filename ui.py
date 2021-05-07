import time

def display_board(board, current_level, player):
    print("The Best Rouge Game in the World!\n")
    print(f"Current level: {current_level}.\n")
    print("These are your stats Prisoner:")
    print_player_stats(player)
    for row in board:
        for cell in row:
            print(cell, end=' ')
    
        print()
    print()

def print_message(message = ''):
    print(message)

def print_table(inventory):
    print("{:<8} {:<15} {:<10}".format('Item','Attack','Defense\n'))
    for item, properties in inventory.items():
        attack = properties.get("attack", 0)
        defense = properties.get("defense", 0)
        print("{:<8} {:<15} {:<10}".format(item, attack, defense))


# player = {"icon": "@", "hp":20, "attack": 4, "defense": 5, 'position_x': 5,'position_y': 3}

def print_player_stats(player):
    print("{:<8} {:<15} {:<10}".format('Health','Attack','Defense'))
    health = player["hp"]
    attack = player["attack"]
    defense = player["defense"]
    print("{:<8} {:<15} {:<10} \n".format(health, attack, defense))

def print_story():
    print("\tHello Dear Player....\n")
    time.sleep(2)

    print("Welcome to a Rouge-Like game...\n")
    time.sleep(2)
    print("\t...where you take the role of a nameless prisoner, abandoned and forgotten by the whole world...\n\n")

    time.sleep(2)
    print("You will be tortured, stalked, beaten and robbed. \n")
    time.sleep(2)
    print("But, try to find the way for freedom. Try to find the valuable items and kill all the enemies.\n\n")
    time.sleep(2)
    print("If you defeat the boss, you may be able to see the light of day.\n\n\n")
    time.sleep(2)
    print("  Good luck!\n")
    time.sleep(6)