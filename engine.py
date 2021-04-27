import main
def create_board(width, height):
    
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    game_board = []
    game_board.append(width * '#')
    for i in range(height -2):
        game_board.append("#" + (width-2) * " " + "#")
    
    game_board.append(width * "#")

    return game_board



def put_player_on_board(board, player):
    x = 0
    for row in board:
        y = 0
        for cell in row:
            if cell == player['player_icon']:
                board[x][y] = ' '
            y += 1
        x += 1

    height = player['position_y']
    width = player['position_x']
    board[height][width] = player['player_icon']

    return board
