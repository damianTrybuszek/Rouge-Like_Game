def display_board(board, current_level):
    print("The Best Rouge Game in the World!\n")
    print(f"Current level: {current_level}.\n")
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()

def print_message(message = ''):
    print(message)

def print_table(inventory):
    

    elements = sorted(inventory, key = inventory.get, reverse=True)
    print('-' * 17)
    print ("{:>5} {:<2}".format('item name |', 'count'))
    print('-' * 17)

    for r in elements:
        results = (r, inventory[r])
        print ("{:>12} {:>4}".format(r +' | ', inventory[r]), end = '\n')
    print('-' * 17)

    return " "
