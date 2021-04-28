import tcod

def create_board(width, height):

    board = []

    for i in range(height):
        temp_table = []
        for j in range(width):
            if i == 3 and j == width-1:
                temp_table.append(" ")
            elif j == 0 or j == width -1:
                temp_table.append("#")
            elif i == 0 or i == height -1:
                temp_table.append("#")
            else:
                temp_table.append(" ")
        board.append(temp_table)

    return board



# print(create_board(10,5))

def print_board(board):
    for element in board:
        print("".join(element))

print_board(create_board(25,10))



def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
