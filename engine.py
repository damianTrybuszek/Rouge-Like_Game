import main
import msvcrt

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

def print_board(board):
    for element in board:
        print("".join(element))


def get_move():
    move = msvcrt.getch().decode('ASCII')
    return move

def put_player_on_board(board, player):
    height = 3
    width = 3
    board[height][width] = player
    while True:
        print_board(board)
        move = get_move()
        if move.lower() == "w":
            board[height][width] = " "
            board[height-1][width] = player
            height -=1
        elif move.lower() == "a":
            board[height][width] = " "
            board[height][width-1] = player
            width -= 1
        elif move.lower() == "s":
            board[height][width] = " "
            board[height+1][width] = player
            height += 1
        elif move.lower() == "d":
            board[height][width] = " "
            board[height][width+1] = player
            width += 1
        
        



        




        


    return board

put_player_on_board(create_board(30, 10), "@")

# print(get_move())
