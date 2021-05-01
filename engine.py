import main
import msvcrt
import PySimpleGUI as sg
import util

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

# def print_board(board):
#     for element in board:
#         print("".join(element))

# def get_move():
#     move = msvcrt.getch().decode('ASCII')
#     return move

def put_player_on_board(board, player, move):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == player:
                    height = i
                    width = j
                    break

        if move.lower() == "w":
            board[height][width] = " "
            height -=1
            board[height][width] = player
        elif move.lower() == "a":
            board[height][width] = " "
            width -= 1
            board[height][width] = player
        elif move.lower() == "s":
            board[height][width] = " "
            height += 1
            board[height][width] = player
        elif move.lower() == "d":
            board[height][width] = " "
            width += 1
            board[height][width] = player


