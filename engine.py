import random
from board import Board


def create_board(width, height, level):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    gate = generate_gate(width, height, level+1)
    return Board(width, height, gate)
         
def generate_gate(board_width, board_height, level_to_go):
    x = board_width
    y = random.randint(2, board_height-1)
    return {"icon": "G", "width": x, "height": y, "level_to_go": level_to_go}   

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    return board.place_player(player)
   

