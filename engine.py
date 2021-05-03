import main


def create_board_level_1(width, height):
    board = []
    for i in range(30):
        temp_table = []
        for j in range (60):
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

    for i in range(height+2):
        for j in range(width-4):
            if i == 5 and j == width- 4 -1:
                board[i][j+30]=main.GATE_ICON
            elif i == 4 and j == 0:
                board[i][j+30]=main.GATE_ICON
            elif j == 0 or j == width - 4 -1:
                board[i][j+30]="#"
            elif i == 0 or i == height +2 - 1:
                board[i][j+30]="#"

    for i in range(height-2):
        for j in range(width+2):
            if i == 2 and j == width+2 -1:
                board[i+18][j+34]=main.GATE_ICON
            elif i == 3 and j == 0:
                board[i+18][j+34]=main.GATE_ICON
            elif j == 0 or j == width +2 -1:
                board[i+18][j+34]="#"
            elif i == 0 or i == height - 2 - 1:
                board[i+18][j+34]="#"

    for i in range(height):
        for j in range(width-4):
            if i == 4 and j == width- 4 -1:
                board[i+20][j+10]=main.GATE_ICON
            elif i == height/2 and j == (width- 4)/2:
                board[i+20][j+10]=main.GATE_TO_UPPER_LEVEL
            elif j == 0 or j == width - 4 -1:
                board[i+20][j+10]="#"
            elif i == 0 or i == height - 1:
                board[i+20][j+10]="#"

    return board

def put_player_on_board(board, player, move):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                height = i
                width = j
                break
    
    gate_coords = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == main.GATE_ICON:
                gate_coords.append((i,j))
                

    if move.lower() == "w" and board[height-1][width] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        height -=1
    elif move.lower() == "a" and board[height][width-1] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        width -= 1
    elif move.lower() == "s" and board[height+1][width] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        height += 1
    elif move.lower() == "d" and board[height][width+1] not in ["#", main.GATE_ICON]:
        board[height][width] = " "
        width += 1
    
    board[height][width] = player

    if move.lower() == "w" and board[height-1][width] == main.GATE_ICON:
        board[height][width] = " " 
        height -=1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] - 1
            width = gate_coords[1][1]
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] + 1
            width = gate_coords[0][1]
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] - 1
            width = gate_coords[3][1]
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] + 1
            width = gate_coords[2][1]
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] + 1
            width = gate_coords[5][1]
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] + 1
            width = gate_coords[4][1]
        
        board[height][width] = player


    elif move.lower() == "a" and board[height][width-1] == main.GATE_ICON:
        board[height][width] = " "
        width -= 1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] 
            width = gate_coords[1][1] - 1
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] 
            width = gate_coords[0][1] - 1
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] 
            width = gate_coords[3][1] - 1
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] 
            width = gate_coords[2][1] - 1
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] 
            width = gate_coords[5][1] -1 
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] 
            width = gate_coords[4][1] - 1
        
        board[height][width] = player

    elif move.lower() == "s" and board[height+1][width] == main.GATE_ICON:
        board[height][width] = " "
        height += 1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] + 1
            width = gate_coords[1][1]
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] - 1
            width = gate_coords[0][1]
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] + 1
            width = gate_coords[3][1]
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] - 1
            width = gate_coords[2][1]
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] + 1
            width = gate_coords[5][1]
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] - 1
            width = gate_coords[4][1]
        
        board[height][width] = player
    elif move.lower() == "d" and board[height][width +1] == main.GATE_ICON:
        board[height][width] = " "
        width += 1
        if (height, width) == gate_coords[0]:
            height = gate_coords[1][0] 
            width = gate_coords[1][1] + 1
        elif (height, width) == gate_coords[1]:
            height = gate_coords[0][0] 
            width = gate_coords[0][1] - 1
        elif (height, width) == gate_coords[2]:
            height = gate_coords[3][0] 
            width = gate_coords[3][1] - 1
        elif (height, width) == gate_coords[3]:
            height = gate_coords[2][0] 
            width = gate_coords[2][1] - 1
        elif (height, width) == gate_coords[4]:
            height = gate_coords[5][0] 
            width = gate_coords[5][1] - 1 
        elif (height, width) == gate_coords[5]:
            height = gate_coords[4][0] 
            width = gate_coords[4][1] +1
        
        board[height][width] = player

    
    
