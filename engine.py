import main
import msvcrt

# def create_board(width, height):
#     board = []

#     for i in range(height):
#         temp_table = []
#         for j in range(width):
#             if i == 3 and j == width-1:
#                 temp_table.append(main.GATE_ICON)
#             elif j == 0 or j == width -1:
#                 temp_table.append("#")
#             elif i == 0 or i == height -1:
#                 temp_table.append("#")
#             else:
#                 temp_table.append(" ")
#         board.append(temp_table)

#     return board


def create_board(width, height):
    board = []
    for i in range(30):
        temp_table = []
        for j in range (50):
            temp_table.append(" ")
        board.append(temp_table)


    for i in range(height):
        for j in range(width):
            if i == 3 and j == width-1:
                board[i][j]=main.GATE_ICON
            elif j == 0 or j == width -1:
                board[i][j]="#"
            elif i == 0 or i == height -1:
                board[i][j]="#"

    for i in range(height-5):
        for j in range(width-4):
            if i == 5 and j == width- 4 -1:
                board[i][j+30]=main.GATE_ICON
            elif i == 2 and j == 0:
                board[i][j+30]=main.GATE_ICON
            elif j == 0 or j == width - 4 -1:
                board[i][j+30]="#"
            elif i == 0 or i == height - 5 - 1:
                board[i][j+30]="#"

    for i in range(height-5):
        for j in range(width-4):
            if i == 5 and j == width- 4 -1:
                board[i+20][j+30]=main.GATE_ICON
            elif i == 2 and j == 0:
                board[i+20][j+30]=main.GATE_ICON
            elif j == 0 or j == width - 4 -1:
                board[i+20][j+30]="#"
            elif i == 0 or i == height - 5 - 1:
                board[i+20][j+30]="#"

    return board

def put_player_on_board(board, player, move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                height = i
                width = j
                break

    if move.lower() == "w" and board[height-1][width] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        height -=1
        board[height][width] = player
    elif move.lower() == "a" and board[height][width-1] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        width -= 1
        board[height][width] = player
    elif move.lower() == "s" and board[height+1][width] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        height += 1
        board[height][width] = player
    elif move.lower() == "d" and board[height][width+1] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        width += 1
        board[height][width] = player

    if move.lower() == "w" and board[height-1][width] == main.GATE_ICON:
        board[height][width] = " "
        height -=1
        # board[height][width] = player
    elif move.lower() == "a" and board[height][width-1] == main.GATE_ICON:
        board[height][width] = " "
        width -= 1
        # board[height][width] = player
    elif move.lower() == "s" and board[height+1][width] == main.GATE_ICON:
        board[height][width] = " "
        height += 1
        # board[height][width] = player
    elif move.lower() == "d" and board[height][width +1] == main.GATE_ICON:
        board[height][width] = " "
        width += 1
        # board[height][width] = player
    
    
