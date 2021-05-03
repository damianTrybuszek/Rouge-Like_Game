from engine import create_board

def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    

    for y in range(1, board.height+1):
        #print(y)
        for x in range(1, board.width+1):
            #print(x)
            if x == board.gate["width"] and y == board.gate["height"]:
                print(board.gate["icon"])
            elif x == board.width:
                print(board.WALL_ICON)
            elif x == 1 or y == 1 or y == board.height: # or x == board.width:
                print(board.WALL_ICON, end="")
            elif x == board.player.x and y == board.player.y:
                print(board.player.ICON, end="")
            else:
                print(board.FLOOR_ICON, end="")


